import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from Utilities.config_reader import ConfigReader
from Pages.login_page import LoginPage
from Pages.dashboard_page import DashboardPage

# ─────────────────────────────────────────────────────────────────
#  conftest.py  –  shared fixtures used by every test file.
#
#  Fixtures available:
#    config        → dict from config/config.yaml
#    driver        → Selenium WebDriver (Chrome or Firefox)
#    login_page    → LoginPage object (driver already inside)
#    dashboard     → DashboardPage object
#    logged_in     → opens browser + logs in, ready for dashboard tests
# ─────────────────────────────────────────────────────────────────


@pytest.fixture(scope="session")
def config():
    """Load config once for the whole test session."""
    return ConfigReader().get()  # return the config dict to any test that needs it


@pytest.fixture(scope="function")
def driver(config):
    """
    Start a fresh browser for each test, quit when done.
    Change scope to 'class' or 'module' if you want to share a browser.
    """
    browser   = config.get("browser", "chrome").lower()    # default to Chrome if not specified
    headless  = config.get("headless", False) # default to False if not specified

    if browser == "firefox":
        opts = FirefoxOptions()
        if headless:
            opts.add_argument("--headless")
        drv = webdriver.Firefox(options=opts)
    else:                                   # default → Chrome
        opts = ChromeOptions()
        if headless:
            opts.add_argument("--headless")
            opts.add_argument("--no-sandbox")
            opts.add_argument("--disable-dev-shm-usage")
        drv = webdriver.Chrome(options=opts)

    drv.maximize_window()
    drv.implicitly_wait(config["timeouts"]["implicit"])
    drv.set_page_load_timeout(config["timeouts"]["page_load"])

    yield drv          # hand the browser to the test

    drv.quit()         # always close browser after test finishes


@pytest.fixture(scope="function", autouse=True)
def open_login_page(driver, config):
    """Start every test from the Login page so tests don't repeat page navigation."""
    driver.get(f"{config['base_url']}/web/index.php/auth/login")
    yield


@pytest.fixture(scope="function")
def login_page(driver):
    """Return a LoginPage object already on the login screen."""
    return LoginPage(driver)


@pytest.fixture(scope="function")
def dashboard(driver):
    """Return a DashboardPage object."""
    return DashboardPage(driver)


@pytest.fixture(scope="function")
def logged_in(login_page, config):
    """
    Use the open login page, perform login, and return DashboardPage.
    This fixture keeps dashboard tests concise and DRY.
    """
    login_page.login(
        config["credentials"]["username"],
        config["credentials"]["password"]
    )
    return DashboardPage(login_page.driver)
