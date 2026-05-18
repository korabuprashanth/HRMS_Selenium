# OrangeHRM Selenium Framework
### Simple • Clean • Page Object Model

Built for: https://opensource-demo.orangehrmlive.com

---

## 📁 Folder Structure

```
orangehrm_framework/
│
├── config/
│   └── config.yaml          ← browser, URL, credentials, timeouts
│
├── Pages/
│   ├── base_page.py         ← ALL selenium actions (click, type, etc.)
│   ├── login_page.py        ← Login screen locators + actions
│   └── dashboard_page.py    ← Dashboard locators + actions
│
├── Tests/
│   ├── test_login.py        ← Login test cases
│   └── test_dashboard.py    ← Dashboard test cases
│
├── Utilities/
│   ├── config_reader.py     ← Reads config.yaml
│   └── logger.py            ← Console + file logging
│
├── reports/                 ← Auto-generated HTML report + test.log
├── conftest.py              ← Fixtures (driver, login_page, logged_in)
├── pytest.ini               ← Pytest settings
└── requirements.txt
```

---

## ⚡ Setup (One Time)

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Tests

```bash
# Run all tests
pytest

# Run only login tests
pytest Tests/test_login.py

# Run a single test by name
pytest Tests/test_login.py::TestLogin::test_valid_login

# Run headless (no browser window)
# → set headless: true in config/config.yaml
```

---

## 🔧 How to Add a New Page

1. Create `Pages/employee_page.py`
2. Inherit from `BasePage`
3. Add locators + actions
4. Add a fixture in `conftest.py` if needed
5. Write tests in `Tests/test_employee.py`

### Example

```python
# Pages/employee_page.py
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class EmployeePage(BasePage):

    ADD_BUTTON     = (By.XPATH, "//button[normalize-space()='Add']")
    FIRST_NAME     = (By.XPATH, "//input[@name='firstName']")
    SAVE_BUTTON    = (By.XPATH, "//button[@type='submit']")
    SUCCESS_TOAST  = (By.XPATH, "//div[@class='oxd-toast-content']")

    def click_add(self):
        self.click(self.ADD_BUTTON)

    def fill_first_name(self, name):
        self.enter_text(self.FIRST_NAME, name)

    def save(self):
        self.click(self.SAVE_BUTTON)

    def is_saved(self):
        return self.is_visible(self.SUCCESS_TOAST)
```

---

## 📊 HTML Report

After each run, open:
```
reports/report.html
```

---

## 🔑 Key Concepts

| Thing | What it does |
|---|---|
| `BasePage` | Wraps all Selenium calls. You never write `driver.find_element` in test code. |
| `LoginPage` | Knows where username/password fields are and how to log in. |
| `conftest.py` | Creates the browser and page objects — tests just receive them as arguments. |
| `logged_in` fixture | Logs in for you before the test starts. Use for any test that needs the dashboard. |
| `config.yaml` | Change browser/URL/credentials here. No code edits needed. |
