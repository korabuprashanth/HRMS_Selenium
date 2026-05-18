from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.logger import get_logger

# ─────────────────────────────────────────────────────────────────
#  BasePage  –  every page class inherits from here.
#  All raw Selenium calls live here so page classes stay clean.
# ─────────────────────────────────────────────────────────────────

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver  = driver
        self.timeout = timeout
        self.log     = get_logger()

    # ── internal helper ──────────────────────────────────────────
    def _wait(self):
        return WebDriverWait(self.driver, self.timeout)

    # ── core actions ─────────────────────────────────────────────

    def click(self, locator):
        """Wait for element to be clickable, then click it."""
        self.log.info(f"Click → {locator}")
        self._wait().until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        """Clear the field and type text."""
        self.log.info(f"Type '{text}' → {locator}")
        element = self._wait().until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Return the visible text of an element."""
        element = self._wait().until(EC.visibility_of_element_located(locator))
        return element.text

    def is_visible(self, locator):
        """Return True if element is visible, False otherwise."""
        try:
            self._wait().until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def get_title(self):
        """Return current page title."""
        return self.driver.title

    def get_url(self):
        """Return current URL."""
        return self.driver.current_url
