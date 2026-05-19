from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

# ─────────────────────────────────────────────────────────────────
#  DashboardPage  –  the landing page after successful login
# ─────────────────────────────────────────────────────────────────

class DashboardPage(BasePage):

    # ── Locators ─────────────────────────────────────────────────
    DASHBOARD_HEADER  = (By.XPATH, "//h6[text()='Dashboard']")
    USER_MENU         = (By.XPATH, "//li[@class='oxd-userdropdown']")
    LOGOUT_OPTION     = (By.XPATH, "//a[text()='Logout']")
    SEARCH_MENU_INPUT = (By.XPATH, "//input[@placeholder='Search']")

    # ── Actions ──────────────────────────────────────────────────

    def is_loaded(self):
        """Confirm Dashboard page is fully loaded."""
        return self.is_visible(self.DASHBOARD_HEADER) # check for unique element on dashboard to confirm page is loaded

    def get_page_heading(self):
        return self.get_text(self.DASHBOARD_HEADER)

    def logout(self):
        """Click user menu → Logout."""
        self.click(self.USER_MENU)
        self.click(self.LOGOUT_OPTION)
        self.log.info("Logged out successfully")

    def navigate_to(self, menu_name):
        """Type in sidebar search to jump to any module (e.g. 'PIM', 'Leave')."""
        self.enter_text(self.SEARCH_MENU_INPUT, menu_name)
        self.log.info(f"Navigating to menu: {menu_name}")
