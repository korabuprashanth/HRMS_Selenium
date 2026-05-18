import pytest

# ─────────────────────────────────────────────────────────────────
#  test_dashboard.py  –  Dashboard module test cases
#
#  Uses the 'logged_in' fixture → browser is already on Dashboard.
# ─────────────────────────────────────────────────────────────────

class TestDashboard:

    def test_dashboard_loads(self, logged_in):
        """After login, Dashboard page should be visible."""
        assert logged_in.is_loaded(), "Dashboard did not load after login"

    def test_dashboard_heading(self, logged_in):
        """Dashboard heading text should be exactly 'Dashboard'."""
        heading = logged_in.get_page_heading()
        assert heading == "Dashboard", f"Unexpected heading: '{heading}'"

    def test_logout(self, logged_in, login_page, config):
        """Logout should redirect back to Login page."""
        logged_in.logout()
        # After logout the login page should appear
        assert "login" in login_page.get_url().lower(), \
            "Not redirected to login page after logout"
