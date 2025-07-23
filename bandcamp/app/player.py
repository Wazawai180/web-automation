from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bandcamp.web.pages import DiscoverPage

BANDCAMP_DISCOVER_URL = "https://bandcamp.com/discover"

class Player:
    """A simple player class to interact with Bandcamp's discover page."""
    
    def __init__(self) -> None:
        self._driver = self._setup_driver()
        self.page = DiscoverPage(self._driver)
        self.tracklist = self.page.discover_tracklist
        self.current_track = self.tracklist.available_tracks[0]

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Close the headless browser."""
        self._driver.quit()

    def play(self, track_number=None):
        """Play the first, or the next available numbered track."""
        if track_number:
            self.current_track = self.tracklist.available_tracks[track_number - 1]
        self._current_track.play()

    def pause(self):
        """Pause the current track."""
        self.current_track.pause()

    def _setup_driver(self):
        """Create a headless browser pointing to Bandcamp."""
        options = Options()
        options.add_argument("--headless")
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        browser.get(BANDCAMP_DISCOVER_URL)
        return browser