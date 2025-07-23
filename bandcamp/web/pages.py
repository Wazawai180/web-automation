from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from bandcamp.web.base import WebPage
from bandcamp.web.elements import TrackListElement
from bandcamp.web.locators import DiscoverPageLocator

class DiscoverPage(WebPage):
        def __init__(self, driver: WebDriver) -> None:
                super().__init__(driver)
                self._accept_cookie_consent()
                self.discover_tracklist() = TrackListElement(
                        self._driver.find_element(*DiscoverPageLocator.DiscoverPlaylist),
                        self._driver,
                )

        def _accept_cookie_consent(self) -> None:
                try:
                        self._driver.find_element(*DiscoverPageLocator.CookieConsentButton).click()
                except NoSuchElementException:
                        pass