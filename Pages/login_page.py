from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

# ─────────────────────────────────────────────────────────────────
#  LoginPage  –  covers the OrangeHRM login screen
#  URL: /web/index.php/auth/login
# ─────────────────────────────────────────────────────────────────

class LoginPage(BasePage):

    # ── Locators ─────────────────────────────────────────────────
    USERNAME_FIELD  = (By.NAME, "username")
    PASSWORD_FIELD  = (By.NAME, "password")
    LOGIN_BUTTON    = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE   = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
    DASHBOARD_TITLE = (By.XPATH, "//h6[text()='Dashboard']")

    # ── Actions ──────────────────────────────────────────────────

    def open(self, base_url):
        """Navigate to the login page. This can be used from calling it otherpages & when want to navigte"""
        self.driver.get(f"{base_url}/web/index.php/auth/login")
        self.log.info("Opened Login Page")

    def login(self, username, password):
        """Enter credentials and submit the form."""
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        self.log.info(f"Login attempted with user: {username}")

    def is_dashboard_visible(self):
        """Return True when Dashboard heading appears (login success)."""
        return self.is_visible(self.DASHBOARD_TITLE)

    def get_error_message(self):
        """Return the error text shown on failed login."""
        return self.get_text(self.ERROR_MESSAGE)
