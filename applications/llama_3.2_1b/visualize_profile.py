import json
import argparse
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import defaultdict

# Try to import seaborn, fall back to matplotlib if not available
try:
    import seaborn as sns
    HAS_SEABORN = True
except ImportError:
    HAS_SEABORN = False

def load_profile_data(json_file):
    """Load profile data from JSON file."""
    with open(json_file, 'r') as f:
        return json.load(f)

def extract_function_info(full_name):
    """Extract function name, filename, path components, and full path from the identifier."""
    # Remove parameters if present
    if '(' in full_name:
        full_name = full_name.split('(')[0]
    
    # Split by '/' to get path components
    path_parts = full_name.split('/')
    
    # Get the last part which contains filename:line:function
    last_part = path_parts[-1]
    parts = last_part.split(':')
    
    if len(parts) >= 3:
        # Format: filename:line:function
        filename = parts[0].strip()
        func_name = parts[-1].strip()
    elif len(parts) >= 2:
        # Format: filename:function or similar
        filename = parts[0].strip()
        func_name = parts[-1].strip()
    else:
        filename = ""
        func_name = full_name.strip()
    
    # Store directory components (excluding the last part which is filename:line:func)
    dir_parts = path_parts[:-1] if len(path_parts) > 1 else []
    
    return {
        'func_name': func_name,
        'filename': filename,
        'dir_parts': dir_parts,
        'full_path': full_name
    }

def collect_unique_identifiers(profile_data, time_threshold_pct=1.0):
    """
    Collect all unique function identifiers from the profile data.
    
    Args:
        profile_data: Dict {func: [time, {children}]}
        time_threshold_pct: Minimum percentage to consider
        
    Returns:
        Set of unique function identifiers
    """
    # Calculate total time
    total_time = sum(child[0] for child in profile_data.values() if isinstance(child, list))
    if total_time == 0:
        return set()
    
    threshold = (time_threshold_pct / 100.0) * total_time
    identifiers = set()
    
    def collect_from_node(func_id, node_data):
        """Recursively collect identifiers."""
        if not isinstance(node_data, list) or len(node_data) != 2:
            return
        
        time, children = node_data
        
        # Add this identifier (regardless of threshold, we want all unique functions)
        identifiers.add(func_id)
        
        # Recurse to children
        for child_id, child_data in children.items():
            collect_from_node(child_id, child_data)
    
    # Process all root functions
    for func_id, func_data in profile_data.items():
        collect_from_node(func_id, func_data)
    
    return identifiers

def build_disambiguation_map(identifiers):
    """
    Build a map from full identifier to minimal disambiguated name.
    
    Args:
        identifiers: Set of unique function identifiers
        
    Returns:
        Dict mapping full_identifier -> disambiguated_name
    """
    from collections import Counter, defaultdict
    
    # Extract info for all identifiers
    full_info = {}
    func_name_groups = defaultdict(list)
    
    for full_id in identifiers:
        info = extract_function_info(full_id)
        full_info[full_id] = info
        func_name_groups[info['func_name']].append(full_id)
    
    result = {}
    
    # Process each group of same-named functions
    for func_name, id_list in func_name_groups.items():
        if len(id_list) == 1:
            # Unique function name, use as-is
            result[id_list[0]] = func_name
        else:
            # Multiple functions with same name, need disambiguation
            # Try progressively longer path suffixes until we find something unique
            max_dirs = max(len(full_info[full_id]['dir_parts']) for full_id in id_list)
            
            disambiguated = False
            for num_dirs in range(0, max_dirs + 1):
                # Build candidates with this many directory components
                candidates = {}
                for full_id in id_list:
                    info = full_info[full_id]
                    dir_parts = info['dir_parts']
                    filename = info['filename']
                    
                    if num_dirs == 0:
                        # Just filename
                        candidate = f"{filename}:{func_name}" if filename else func_name
                    else:
                        # Take last num_dirs directories + filename
                        path_suffix = dir_parts[-num_dirs:] if len(dir_parts) >= num_dirs else dir_parts
                        if path_suffix and filename:
                            candidate = "/".join(path_suffix) + f"/{filename}:{func_name}"
                        elif filename:
                            candidate = f"{filename}:{func_name}"
                        else:
                            candidate = func_name
                    
                    candidates[full_id] = candidate
                
                # Check if all candidates are unique
                if len(set(candidates.values())) == len(candidates):
                    # Apply the disambiguation to all functions in this group
                    result.update(candidates)
                    disambiguated = True
                    break
            
            # Fallback to full path if still not unique (shouldn't happen)
            if not disambiguated:
                for full_id in id_list:
                    result[full_id] = full_info[full_id]['full_path']
    
    return result

def build_hierarchical_layout(profile_data, time_threshold_pct=1.0, zoom_path=None):
    """
    Build hierarchical layout for flame graph with proper parent-child positioning.
    
    Args:
        profile_data: Either dict {func: [time, {children}]} or [time, {child_calls}]
        time_threshold_pct: Minimum percentage of total time to display
        zoom_path: Optional list of disambiguated function names to zoom into (e.g., ['inference', 'generate'])
        
    Returns:
        List of rectangles with (depth, x_start, width, func_name, time, pct)
    """
    # Handle both formats: dict or [time, {children}]
    if isinstance(profile_data, dict):
        root_children = profile_data
    elif isinstance(profile_data, list) and len(profile_data) == 2:
        _, root_children = profile_data
    else:
        return [], 0.0
    
    if root_children:
        # Calculate total time from root level
        total_time = sum(child[0] for child in root_children.values() if isinstance(child, list))
        if total_time == 0:
            return [], 0.0
        
        # Build disambiguation map for all unique functions
        unique_identifiers = collect_unique_identifiers(root_children, time_threshold_pct)
        disambig_map = build_disambiguation_map(unique_identifiers)
        
        # If zoom_path is specified, find the subtree to zoom into
        if zoom_path:
            # Build reverse map: disambiguated_name -> [full_identifiers]
            reverse_map = defaultdict(list)
            for full_id, disambig_name in disambig_map.items():
                reverse_map[disambig_name].append(full_id)
            
            # Navigate to the zoomed node
            current_data = root_children
            current_depth = 0
            
            for target_name in zoom_path:
                # Find matching function in current level
                found = False
                for func_id, func_data in current_data.items():
                    disambig_name = disambig_map.get(func_id, func_id)
                    if disambig_name == target_name:
                        if isinstance(func_data, list) and len(func_data) == 2:
                            _, current_data = func_data
                            current_depth += 1
                            found = True
                            break
                
                if not found:
                    print(f"Warning: Could not find '{target_name}' in zoom path. Available at this level:")
                    for func_id in list(current_data.keys())[:10]:
                        print(f"  - {disambig_map.get(func_id, func_id)}")
                    return [], 0.0
            
            # Use the zoomed subtree as root
            root_children = current_data
            # Recalculate total time for the zoomed view
            total_time = sum(child[0] for child in root_children.values() if isinstance(child, list))
            if total_time == 0:
                return [], 0.0
        
        threshold = (time_threshold_pct / 100.0) * total_time
        rectangles = []
        
        def process_node(func_name, node_data, depth, x_start, parent_time=None):
            """Recursively process nodes and position them."""
            if not isinstance(node_data, list) or len(node_data) != 2:
                return
            
            time, children = node_data
            
            # Calculate width as proportion of total time
            width = time / total_time
            pct_total = (time / total_time) * 100
            
            # Calculate percentage relative to parent (if parent exists)
            if parent_time is not None and parent_time > 0:
                pct_parent = (time / parent_time) * 100
            else:
                pct_parent = 100.0  # Root nodes are 100% of themselves
            
            # Get disambiguated name from the map
            display_name = disambig_map.get(func_name, func_name)
            
            # Add rectangle for this function
            # Mark whether it should be labeled based on threshold
            rectangles.append({
                'depth': depth,
                'x_start': x_start,
                'width': width,
                'func_name': display_name,
                'full_identifier': func_name,
                'time': time,
                'pct': pct_parent,  # Use parent-relative percentage
                'pct_total': pct_total,  # Keep total percentage for reference
                'show_label': time >= threshold
            })
            
            # Process children with proper positioning
            # Children should be positioned within this function's span
            child_x = x_start
            for child_name, child_data in children.items():
                if isinstance(child_data, list) and len(child_data) == 2:
                    child_time = child_data[0]
                    process_node(child_name, child_data, depth + 1, child_x, parent_time=time)
                    # Move position for next child
                    child_x += child_time / total_time
        
        # Process all root-level functions
        x_pos = 0.0
        for func_name, func_data in root_children.items():
            if isinstance(func_data, list) and len(func_data) == 2:
                func_time = func_data[0]
                process_node(func_name, func_data, 0, x_pos)
                x_pos += func_time / total_time
        
        return rectangles, total_time
    
    return [], 0.0

def draw_flame_graph(rectangles, total_time, output_file='flame_graph.png'):
    """Draw flame graph visualization."""
    if not rectangles:
        print("No data to visualize")
        return
    
    # Calculate layout
    max_depth = max(rect['depth'] for rect in rectangles)
    fig, ax = plt.subplots(figsize=(20, max_depth + 2))
    
    # Color palette - rocket colormap
    if HAS_SEABORN:
        colors = sns.color_palette("pastel")
    else:
        # Use matplotlib's tab20 colormap
        cmap = plt.cm.get_cmap('tab20')
        colors = [cmap(i) for i in range(20)]
    
    for rect in rectangles:
        depth = rect['depth']
        x_start = rect['x_start']
        width = rect['width']
        func_name = rect['func_name']
        pct = rect['pct']
        time_abs = rect['time']
        
        # Convert to absolute time coordinates
        x_start_abs = x_start * total_time
        width_abs = width * total_time
        
        # Choose color based on function name hash
        color_idx = hash(func_name) % len(colors)
        
        patch = mpatches.Rectangle(
            (x_start_abs, depth), width_abs, 0.8,
            facecolor=colors[color_idx],
            edgecolor='black',
            linewidth=1
        )
        ax.add_patch(patch)
        
        # Add text label if above threshold AND width is sufficient
        # Use absolute width for threshold check
        if rect.get('show_label', True) and width_abs > 0.015 * total_time:  # Threshold in absolute time
            # Create wrapped text that fits within the rectangle
            import textwrap
            
            # Calculate approximate character width based on rectangle width
            # Rough estimate: each character is about 0.06 inches at fontsize 7
            fig_width_inches = 20  # From figsize
            chars_per_inch = 14  # Approximate at fontsize 7
            rect_width_inches = (width_abs / total_time) * fig_width_inches
            max_chars = int(rect_width_inches * chars_per_inch)
            max_chars = max(max_chars, 3)  # At least 3 characters
            
            # Wrap the function name
            wrapped_name = '\n'.join(textwrap.wrap(func_name, width=max_chars, break_long_words=True, break_on_hyphens=False))
            
            # Build label with wrapped name
            label = f"{wrapped_name}\n{pct:.1f}%\n{time_abs:.3f}s"
            
            # Limit number of lines to fit in rectangle height (0.8 units)
            max_lines = 3  # Approximately 3 lines fit in 0.8 height
            label_lines = label.split('\n')
            if len(label_lines) > max_lines:
                label = '\n'.join(label_lines[:max_lines])
            
            ax.text(
                x_start_abs + width_abs/2, depth + 0.4,
                label,
                ha='center', va='center',
                fontsize=7,
                clip_on=True
            )
    
    ax.set_xlim(0, total_time)
    ax.set_ylim(-0.5, max_depth + 0.5)
    ax.set_xlabel('Cumulative Time (seconds)', fontsize=12)
    ax.set_ylabel('Call Stack Depth', fontsize=12)
    ax.set_title('Flame Graph - Profile Visualization', fontsize=14, weight='bold')
    ax.set_yticks(range(max_depth + 1))
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"Flame graph saved to {output_file}")
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Generate flame graph from profile JSON data')
    parser.add_argument('input', nargs='?', default='profile.json',
                        help='Input JSON profile file (default: profile.json)')
    parser.add_argument('-o', '--output', default='flame_graph.png',
                        help='Output flame graph image file (default: flame_graph.png)')
    parser.add_argument('-t', '--threshold', type=float, default=1.0,
                        help='Time threshold percentage for displaying functions (default: 1.0)')
    parser.add_argument('-z', '--zoom', type=str, default=None,
                        help='Zoom into a specific call path using disambiguated names separated by ">" (e.g., "inference>generate")')
    
    args = parser.parse_args()
    
    # Parse zoom path if provided
    zoom_path = None
    if args.zoom:
        zoom_path = [name.strip() for name in args.zoom.split('>')]
        print(f"Zooming into path: {' > '.join(zoom_path)}")
    
    # Load profile JSON
    profile_data = load_profile_data(args.input)
    
    # Build hierarchical layout with specified threshold and zoom
    rectangles, total_time = build_hierarchical_layout(profile_data, time_threshold_pct=args.threshold, zoom_path=zoom_path)
    
    if not rectangles:
        print("No data to visualize")
        return
    
    print(f"Total profiled time: {total_time:.2f}s")
    print(f"Displaying {len(rectangles)} function calls above {args.threshold}% threshold")
    
    # Draw flame graph
    draw_flame_graph(rectangles, total_time, output_file=args.output)

if __name__ == '__main__':
    main()
