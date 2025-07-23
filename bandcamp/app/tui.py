from bandcamp.app.player import Player

MAX_TRACKS = 100
COLUMN_WIDTH = CW = 30

def interact():
    """Control the player through user interactions"""
    with Player() as player:
        while True:
            print("\nType: play <track_number>, pause, tracks, more, or exit to control the player.")
            match input("> ").strip().lower().split():
                case ["play"]:
                    play(player)
                case ["play", track]:
                    try:
                        track_number = int(track)
                        play(player, track_number)
                    except ValueError:
                        print("Invalid track number. Please enter a valid number.")
                case ["pause"]:
                    pause(player)
                case ["tracks"]:
                    dispay_tracks(player)
                case ["more"] if len(player.tracklist.available_tracks) >= MAX_TRACKS:
                    print("You have reached the maximum number of tracks available.")
                case ["more"]:
                    player.tracklist.load_more_tracks()
                    dispay_tracks(player)
                case ["exit"]:
                    print("Exiting the player.")
                    break
                case _:
                    print("Unknown command. Please try again.")

def play(player, track_number=None):
    """Play a specific track or the first available track."""
    if track_number is None:
        track_number = 1
    try:
        player.play(track_number)
        print(f"Playing track {track_number}: {player.current_track.title}")
    except IndexError:
        print(f"Track number {track_number} is not available.")

def pause(player):
    """Pause the currently playing track."""
    player.pause()
    
def dispay_tracks(player):
    """Display the available tracks"""
    header = f"{'Track #':<5}{'Album':<{CW}}{'Artist':<{CW}}{'Genre':<{CW}}"
    print(header)
    print("-" * len(header))
    for track_number, track_element in enumerate(
        player.tracklist.available_tracks, start=1
    ):
        track = track_element._get_track_info()
        album = _truncate(track.album, CW)
        artist = _truncate(track.artist, CW)
        genre = _truncate(track.genre, CW)
        print(f"{track_number:<5}{album:<{CW}}{artist:<{CW}}{genre:<{CW}}")

def _truncate(text, width):
    """Truncate text to fit within the specified width."""
    return text[:width - 3] + "..." if len(text) > width else text