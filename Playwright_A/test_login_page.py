'''
We are going to automate this webpage using python playwright. https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
First we will try to login using the correct credentials and then we will try to login using incorrect credentials. We will also check if the error message is displayed when we use incorrect credentials.
dependencies:
- playwright
- pytest
- faker (optional)
- xdist (optional)

'''

from playwright.sync_api import expect,sync_playwright
import pytest

def test_login_page():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        expect(page).to_have_title("OrangeHRM")

        page.wait_for_timeout(6000)
        browser.close()

