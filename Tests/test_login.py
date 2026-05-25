import pytest

# ─────────────────────────────────────────────────────────────────
#  test_login.py  –  Login module test cases
#
#  Fixtures used (all from conftest.py):
#    config      → YAML config dict
#    login_page  → LoginPage (browser not yet on the site)
#    logged_in   → DashboardPage (browser already logged in)
# ─────────────────────────────────────────────────────────────────

class TestLogin:

    def test_valid_login(self, login_page, config):
        """Valid credentials should land on Dashboard."""
        login_page.login(
            config["credentials"]["username"],
            config["credentials"]["password"]
        )
        assert login_page.is_dashboard_visible(), \
            "Dashboard not visible after valid login"

    def test_invalid_password(self, login_page, config):
        """Wrong password should show an error message."""
        login_page.login(config["credentials"]["username"], "wrongpassword")

        error = login_page.get_error_message()
        assert "Invalid credentials" in error, \
            f"Expected error message, got: '{error}'"

    def test_empty_username(self, login_page, config):
        """Submitting blank username should show a validation error."""
        login_page.login("", config["credentials"]["password"])

        # OrangeHRM shows "Required" on blank fields
        assert not login_page.is_dashboard_visible(), \
            "Should NOT reach Dashboard with empty username"

    def test_page_title(self, login_page, config):
        """Page title must contain 'OrangeHRM'."""
        title = login_page.get_title()
        assert "OrangeHRM" in title, f"Unexpected title: '{title}'"
