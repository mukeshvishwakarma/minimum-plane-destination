def min_planes_to_destination(fuel):
    """
    Calculate the minimum number of planes needed to reach the last airport.
    
    Args:
    fuel (list): List of integers representing fuel units at each airport.
    
    Returns:
    int: Minimum number of planes needed, or -1 if impossible.
    """
    n = len(fuel)
    if n <= 1:
        return 0  # Already at the destination or only one airport

    planes_hired = 0
    current_max_reach = 0
    next_max_reach = 0

    for i in range(n):
        # Check if we need to hire a new plane
        if i > current_max_reach:
            if next_max_reach <= current_max_reach:
                return -1  # Impossible to proceed
            planes_hired += 1
            current_max_reach = next_max_reach
        
        # Update the farthest reachable airport if we hire another plane
        next_max_reach = max(next_max_reach, i + fuel[i])
        
        # Check if we've reached or passed the last airport
        if current_max_reach >= n - 1:
            return planes_hired

    return -1  # If we exit the loop, we couldn't reach the last airport

# Test cases
print(min_planes_to_destination([2, 1, 2, 3, 1]))  
print(min_planes_to_destination([1, 6, 3, 4, 5, 0, 0, 0, 6])) 
print(min_planes_to_destination([1, 0, 0]))  