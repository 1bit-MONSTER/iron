#!/usr/bin/env python3
"""
Profile Path Analyzer

Analyzes profile.json to aggregate time spent in selected functions across call paths.
Supports fuzzy matching and "zooming into" specific call paths.
"""

import json
import argparse
import sys
from typing import Dict, List, Tuple, Set
import matplotlib.pyplot as plt
import matplotlib


def parse_function_name(full_name: str) -> Tuple[str, str, str]:
    parts = full_name.rsplit(':', 2)
    if len(parts) == 3:
        return parts[0], parts[1], parts[2]
    return full_name, '', ''


def fuzzy_match(pattern: str, full_name: str) -> bool:
    return pattern.lower() in full_name.lower()


def get_all_paths(profile: Dict, current_path: List[str] = None) -> List[Tuple[List[str], float]]:
    """
    Extract all call paths from the profile with their total times.
    
    Args:
        profile: Profile dictionary
        current_path: Current call path being explored
    
    Returns:
        List of (call_path, total_time) tuples
    """
    if current_path is None:
        current_path = []
    
    paths = []
    
    for func_name, data in profile.items():
        time_spent = data[0]
        children = data[1] if len(data) > 1 else {}
        
        new_path = current_path + [func_name]
        paths.append((new_path, time_spent))
        
        if children:
            child_paths = get_all_paths(children, new_path)
            paths.extend(child_paths)
    
    return paths


def is_subpath(path: List[str], zoom_path: List[str]) -> bool:
    """
    Check if path is a subpath of zoom_path.
    
    Args:
        path: The path to check
        zoom_path: The zoom-in path
    
    Returns:
        True if path starts with zoom_path
    """
    if len(path) < len(zoom_path):
        return False
    
    for i, func in enumerate(zoom_path):
        if not fuzzy_match(func, path[i]):
            return False
    
    return True


def find_matching_functions(profile: Dict, patterns: List[str]) -> Dict:
    """
    Find all function names in the profile that match any of the patterns.
    If multiple patterns match, uses the most specific (longest) pattern.
    
    Args:
        profile: Profile dictionary
        patterns: List of search patterns
    
    Returns:
        Dict mapping function names to their matched pattern
    """
    matching = {}
    
    def traverse(data: Dict):
        for func_name, value in data.items():
            # Find all matching patterns and use the longest (most specific)
            matched_patterns = [p for p in patterns if fuzzy_match(p, func_name)]
            if matched_patterns:
                # Use the longest pattern as it's the most specific
                most_specific = max(matched_patterns, key=len)
                matching[func_name] = most_specific
            
            if len(value) > 1 and value[1]:
                traverse(value[1])
    
    traverse(profile)
    return matching


def aggregate_times(profile: Dict, selected_funcs: Dict, zoom_path: List[str]) -> Dict[str, float]:
    aggregated = {func: 0.0 for func in selected_funcs.values()}
    
    def traverse(data: Dict, current_path: List[str], counted_parent: str | None):
        for func_name, (time_spent, subprofile) in data.items():
            new_path = current_path + [func_name]
            # Start with parent's pattern, will be overridden if this function is selected
            counted_this_iter = counted_parent
            
            # Check if this path is within the zoom scope
            if not zoom_path or is_subpath(new_path, zoom_path):
                # If this function is selected, add its time
                if func_name in selected_funcs:
                    pattern = selected_funcs[func_name]
                    if counted_parent is None:
                        aggregated[pattern] += time_spent
                    elif counted_parent != pattern:
                        raise RuntimeError(f"Double-counting detected: pattern '{counted_parent}' calls '{pattern}', which would lead to double-counting '{pattern}'.")
                    counted_this_iter = pattern
            
            # Recurse into children
            if subprofile:
                traverse(subprofile, new_path, counted_this_iter)
    
    traverse(profile, [], None)
    return aggregated


def calculate_total_time(profile: Dict, zoom_path: List[str]) -> float:
    """
    Calculate total time for the zoomed-in path.
    
    Args:
        profile: Profile dictionary
        zoom_path: Zoom-in path (empty list for entire profile)
    
    Returns:
        Total time in seconds
    """
    if not zoom_path:
        # No zoom - return total of all top-level functions
        return sum(value[0] for value in profile.values())
    
    # Find the zoomed function and return its time
    def find_zoom_time(data: Dict, path_remaining: List[str]) -> float:
        if not path_remaining:
            return 0.0
        
        pattern = path_remaining[0]
        
        for func_name, value in data.items():
            if fuzzy_match(pattern, func_name):
                if len(path_remaining) == 1:
                    # Found the zoom target
                    return value[0]
                else:
                    # Continue searching deeper
                    if len(value) > 1 and value[1]:
                        result = find_zoom_time(value[1], path_remaining[1:])
                        if result > 0:
                            return result
        
        return 0.0
    
    return find_zoom_time(profile, zoom_path)


def print_results(total_time: float, aggregated: Dict[str, float], plot_file: str = None):
    """
    Print the analysis results.
    
    Args:
        total_time: Total time in the zoomed scope
        aggregated: Dictionary of function times
        plot_file: Optional path to save a matplotlib bar plot
    """
    print("\n" + "="*80)
    print("PROFILE ANALYSIS RESULTS")
    print("="*80)
    
    print(f"\nTotal time (zoomed scope): {total_time:.6f} seconds")
    print("-"*80)
    
    # Sort by time (descending)
    sorted_funcs = sorted(aggregated.items(), key=lambda x: x[1], reverse=True)
    
    selected_total = 0.0
    for func_name, time in sorted_funcs:
        selected_total += time
        percentage = (time / total_time * 100) if total_time > 0 else 0
        print(f"{func_name}")
        print(f"  Time: {time:.6f}s ({percentage:.2f}%)")
        print()
    
    # Calculate "other" time
    other_time = total_time - selected_total
    other_percentage = (other_time / total_time * 100) if total_time > 0 else 0
    
    print("-"*80)
    print(f"Selected functions total: {selected_total:.6f}s ({selected_total/total_time*100:.2f}%)")
    print(f"Other (unselected): {other_time:.6f}s ({other_percentage:.2f}%)")
    print("="*80)
    
    # Create plot if requested
    if plot_file:
        create_bar_plot(total_time, sorted_funcs, other_time, plot_file)


def create_bar_plot(total_time: float, sorted_funcs: List[Tuple[str, float]], other_time: float, output_file: str):
    """
    Create a bar plot showing time spent in each selected pattern and "other".
    
    Args:
        total_time: Total time in the zoomed scope
        sorted_funcs: List of (pattern, time) tuples sorted by time
        other_time: Time spent in unselected functions
        output_file: Path to save the plot
    """
    # Prepare data
    labels = [func for func, _ in sorted_funcs] + ["Other"]
    times = [time for _, time in sorted_funcs] + [other_time]
    percentages = [(time / total_time * 100) if total_time > 0 else 0 for time in times]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create bars
    bars = ax.bar(range(len(labels)), times, color='steelblue', alpha=0.8)
    
    # Color the "Other" bar differently
    bars[-1].set_color('lightgray')
    
    # Customize plot
    ax.set_xlabel('Pattern', fontsize=12, fontweight='bold')
    ax.set_ylabel('Time (seconds)', fontsize=12, fontweight='bold')
    ax.set_title(f'Profile Analysis - Total Time: {total_time:.3f}s', fontsize=14, fontweight='bold')
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha='right')
    
    # Add value labels on bars
    for i, (bar, time, pct) in enumerate(zip(bars, times, percentages)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{time:.3f}s\n({pct:.1f}%)',
                ha='center', va='bottom', fontsize=9)
    
    # Add grid for readability
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save plot
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"\nPlot saved to: {output_file}")
    plt.close()


def main():
    parser = argparse.ArgumentParser(
        description='Analyze profile.json to aggregate time spent in selected functions.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze all torch calls
  %(prog)s logs/profile.json --select torch
  
  # Analyze multiple patterns
  %(prog)s logs/profile.json --select torch numpy inference
  
  # Zoom into a specific call path
  %(prog)s logs/profile.json --select torch --zoom inference forward
  
  # List all unique functions
  %(prog)s logs/profile.json --list-functions
        """
    )
    
    parser.add_argument('profile', help='Path to profile.json file')
    parser.add_argument('--select', '-s', nargs='+', metavar='PATTERN',
                        help='Function patterns to select (fuzzy match)')
    parser.add_argument('--zoom', '-z', nargs='+', metavar='PATTERN',
                        help='Call path to zoom into (fuzzy match sequence)')
    parser.add_argument('--list-functions', '-l', action='store_true',
                        help='List all unique function names in the profile')
    parser.add_argument('--plot', '-p', metavar='FILE',
                        help='Save a bar plot to the specified file (e.g., plot.png)')
    
    args = parser.parse_args()
    
    # Load profile
    try:
        with open(args.profile, 'r') as f:
            profile = json.load(f)
    except FileNotFoundError:
        print(f"Error: Profile file '{args.profile}' not found.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in profile file: {e}", file=sys.stderr)
        sys.exit(1)
    
    
    # Require --select for analysis
    if not args.select:
        print("Error: --select is required for analysis", file=sys.stderr)
        parser.print_help()
        sys.exit(1)
    
    # Find matching functions
    selected_funcs = find_matching_functions(profile, args.select)
    
    if not selected_funcs:
        print(f"Error: No functions matched the patterns: {args.select}", file=sys.stderr)
        sys.exit(1)
    
    print(f"\nMatched {len(selected_funcs)} function(s) from patterns: {args.select}")
    
    # Prepare zoom path
    zoom_path = args.zoom if args.zoom else []
    
    if zoom_path:
        print(f"Zooming into path: {' -> '.join(zoom_path)}")
    
    # Calculate total time
    total_time = calculate_total_time(profile, zoom_path)
    
    if total_time == 0:
        print(f"Error: Could not find zoom path or it has zero time.", file=sys.stderr)
        sys.exit(1)
    
    # Aggregate times
    aggregated = aggregate_times(profile, selected_funcs, zoom_path)
    
    # Print results
    print_results(total_time, aggregated, args.plot)


if __name__ == '__main__':
    main()
