from selenium.webdriver.common.by import By

class DiscoverPageLocator:
    """Locators for elements on the Bandcamp discover page."""
    DISCOVER_PLAYLIST = (By.CLASS_NAME, "results-grid")
    COOKIE_CONSENT_BUTTON = (By.CSS_SELECTOR, "#cookie-control-dialog button.g-button.outline",)

class TrackListLocator:
    """Locators for elements in a track list."""
    ITEM = (By.CLASS_NAME, "results-grid-item")
    PAGINATION_BUTTON = (By.ID, "view-more")

class TrackLocator:
    """Locators for elements in a track."""
    PLAY_BUTTON = (By.CSS_SELECTOR, "button.play-pause-button")
    ARTIST = (By.CSS_SELECTOR, "div.meta p a span")
    ALBUM = (By.CSS_SELECTOR, "div.meta p a strong")
    GENRE = (By.CSS_SELECTOR, "div.meta p.genre")
    URL = (By.CSS_SELECTOR, "div.meta p a")