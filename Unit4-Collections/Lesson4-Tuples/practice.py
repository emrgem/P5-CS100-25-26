def create_rgb_color(red, green, blue):
    """Example:
        create_rgb_color(88, 101, 242)
        Returns: ((88, 101, 242), "#5865f2")
    """
    # TODO: Create RGB tuple
    rgb_tuple = (red, green, blue)
    # TODO: Create hex string "#RRGGBB"
    hex_string = f"#{red:02x}{green:02x}{blue:02x}"
    # TODO: Return both as tuple
    return rgb_tuple, hex_string

result = create_rgb_color(88,101,242)
print(result)


def calculate_player_stats(scores):
    """
    Calculate stats for player scores.
    
    Returns: (total, average, best, worst)
             Returns (0, 0, 0, 0) if empty
    
    Example:
        calculate_player_stats([100, 85, 92, 78, 95])
        Returns: (450, 90.0, 100, 78)
    """
    # TODO: Handle empty list
    if not scores:
        return 0,0,0,0
    # TODO: Calculate total, average, best, worst
    total = sum(scores)
    average = total/len(scores)
    best = max(scores)
    worst = min(scores)
    
    # TODO: Return all four as tuple
    return total, average, best, worst

result2 = calculate_player_stats([100, 85, 92, 78, 95])
print(result2)