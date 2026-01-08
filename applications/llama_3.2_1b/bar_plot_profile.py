#!/usr/bin/env python3
"""
Generate a bar plot showing the top 15 most expensive functions by cumulative time.
"""
import json
import argparse
import matplotlib.pyplot as plt
from collections import defaultdict

def load_profile_data(json_file):
    """Load profile data from JSON file."""
    with open(json_file, 'r') as f:
        return json.load(f)

def extract_function_name(full_identifier):
    """Extract just the function name from the full identifier."""
    # Remove parameters if present
    if '(' in full_identifier:
        full_identifier = full_identifier.split('(')[0]
    
    # Split by '/' to get path components
    path_parts = full_identifier.split('/')
    
    # Get the last part which contains filename:line:function
    last_part = path_parts[-1]
    parts = last_part.split(':')
    
    if len(parts) >= 3:
        # Format: filename:line:function
        return parts[-1].strip()
    elif len(parts) >= 2:
        # Format: filename:function or similar
        return parts[-1].strip()
    else:
        return full_identifier.strip()

def aggregate_time_by_function(profile_data):
    """
    Aggregate cumulative time for each function across all call sites.
    
    Args:
        profile_data: Dict {func: [time, {children}]}
        
    Returns:
        Dict mapping function name to total cumulative time
    """
    time_by_function = defaultdict(float)
    
    def process_node(func_id, node_data):
        """Recursively process nodes and accumulate time."""
        if not isinstance(node_data, list) or len(node_data) != 2:
            return
        
        time, children = node_data
        
        # Extract function name and add time
        func_name = extract_function_name(func_id)
        time_by_function[func_name] += time
        
        # Recurse to children
        for child_id, child_data in children.items():
            process_node(child_id, child_data)
    
    # Process all root functions
    for func_id, func_data in profile_data.items():
        process_node(func_id, func_data)
    
    return time_by_function

def create_bar_plot(time_by_function, output_file, top_n=15):
    """
    Create a bar plot showing the top N most expensive functions.
    
    Args:
        time_by_function: Dict mapping function name to cumulative time
        output_file: Path to save the plot
        top_n: Number of top functions to display
    """
    # Sort by time and get top N
    sorted_functions = sorted(time_by_function.items(), key=lambda x: x[1], reverse=True)
    top_functions = sorted_functions[:top_n]
    
    # Prepare data for plotting
    function_names = [func for func, _ in top_functions]
    times = [time for _, time in top_functions]
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create horizontal bars (easier to read function names)
    bars = ax.barh(range(len(function_names)), times, color='steelblue')
    
    # Customize the plot
    ax.set_yticks(range(len(function_names)))
    ax.set_yticklabels(function_names)
    ax.set_xlabel('Cumulative Time (seconds)', fontsize=12)
    ax.set_ylabel('Function Name', fontsize=12)
    ax.set_title(f'Top {top_n} Most Expensive Functions by Cumulative Time', fontsize=14, fontweight='bold')
    
    # Add value labels on the bars
    for i, (bar, time) in enumerate(zip(bars, times)):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2, 
                f' {time:.3f}s', 
                ha='left', va='center', fontsize=10)
    
    # Invert y-axis so the highest time is at the top
    ax.invert_yaxis()
    
    # Add grid for better readability
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    
    # Tight layout
    plt.tight_layout()
    
    # Save the plot
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"Bar plot saved to {output_file}")
    
    # Print summary statistics
    total_time = sum(times)
    print(f"\nTop {top_n} Functions Summary:")
    print(f"Total cumulative time (top {top_n}): {total_time:.3f}s")
    for i, (func_name, time) in enumerate(top_functions, 1):
        print(f"{i:2d}. {func_name:40s} {time:8.3f}s")

def main():
    parser = argparse.ArgumentParser(
        description='Generate a bar plot of the top N most expensive functions by cumulative time'
    )
    parser.add_argument('input', help='Input profile JSON file')
    parser.add_argument('-o', '--output', default='bar_plot.png',
                        help='Output image file (default: bar_plot.png)')
    parser.add_argument('-n', '--top-n', type=int, default=15,
                        help='Number of top functions to display (default: 15)')
    
    args = parser.parse_args()
    
    # Load profile data
    profile_data = load_profile_data(args.input)
    
    # Aggregate time by function name
    time_by_function = aggregate_time_by_function(profile_data)
    
    # Create the bar plot
    create_bar_plot(time_by_function, args.output, args.top_n)

if __name__ == '__main__':
    main()
