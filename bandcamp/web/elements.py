from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bandcamp.web.base import WebComponent, Track
from bandcamp.web.locators import TrackListLocator, TrackLocator

class TrackListElement(WebComponent):
    """Represents the track list element on the Bandcamp discover page."""
    def __init__(self, parent: WebElement, driver: WebDriver = None) -> None:
        super().__init__(parent, driver)
        self.available_tracks = self._get_available_tracks()

    def load_more(self) -> None:
        """Loads more tracks"""
        view_more_button = self._driver.find_element(
            *TrackListLocator.PAGINATION_BUTTON
        )
        view_more_button.click()
        self.wait.until(
            EC.element_to_be_clickable(TrackListLocator.PAGINATION_BUTTON),
        )
        self.available_tracks = self._get_available_tracks()

    def _get_available_tracks(self) -> list:
        """Fetches the list of available tracks in the playlist."""
        self._wait.until(
            self._track_text_loaded,
            message="Timeout waiting for track text to load",
        )
        all_tracks = self._driver.find_elements(*TrackListLocator.ITEM)

        # Filter tracks that are available and have text
        return [
            TrackElement(track, self._driver)
            for track in all_tracks
            if track.is_displayed() and track.text.strip()
        ]
    
    def _track_text_loaded(self, driver):
        """Checks if the track text is loaded."""
        return any(
            e.is_displayed() and e.text.strip()
            for e in driver.find_elements(*TrackListLocator.ITEM)
        )
    
class TrackElement(WebComponent):
    """Represents a track element within a playlist."""
    def play(self) -> None:
        """Plays the track."""
        if not self.is_playing:
            self._get_play_button().click()

    def pause(self) -> None:
        """Pauses the track."""
        if self.is_playing:
            self._get_play_button().click()

    @property
    def is_playing(self) -> bool:
        """Checks if the track is currently playing."""
        return "Pause" in self._get_play_button().get_attribute("aria-label")
    
    def _get_play_button(self):
        """Returns the play button element for the track."""
        return self._parent.find_element(*TrackLocator.PLAY_BUTTON)
    
    def _get_track_info(self):
        """Returns the track information element."""
        full_url = self._parent.find_element(*TrackLocator.URL).get_attribute("href")

        # Extracts the clean url from the query parameter
        clean_url = full_url.split("?")[0] if full_url else ""

        # In case no genre exists, return empty string
        try:
            genre = self._parent.find_element(*TrackLocator.GENRE).text
        except NoSuchElementException:
            genre = ""
        return Track(
            album = self._parent.find_element(*TrackLocator.ALBUM).text,
            artist = self._parent.find_element(*TrackLocator.ARTIST).text,
            genre = genre,
            url = clean_url,
        )