def find_song_position(playlist, song):
    """Find song position safely using defensive check."""
    if song in playlist:
        position = playlist.index(song)
        return position
    return -1  # Not found indicator

def find_song_position_v2(playlist, song):
    """Find song position safely using try/except."""
    try:
        position = playlist.index(song)
        return position
    except ValueError:
        return -1  # Not found indicator

playlist = ["Flowers", "Anti-Hero", "Unholy", "As It Was"]

# Test 1: Find existing song
result1 = find_song_position(playlist, "Unholy")

# Test 2: Find non-existing song
result2 = find_song_position(playlist, "Despacito")

def count_votes(votes, option):
    """Return how many times option was voted for."""
    return votes.count(option)

# Test
poll = ["Yes", "No", "Yes", "Yes", "Maybe", "No", "Yes"]
yes_votes = count_votes(poll, "Yes")
print(yes_votes)  # 4