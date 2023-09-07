import re
from playwright.sync_api import Page, expect, sync_playwright
import pytest


def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

    # create a locator
    get_started = page.get_by_role("link", name="Get started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*intro"))


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_login_and_navigate_to_credit_calculator(page):
    # Open the application
    page.goto("https://online.mobibanka.rs/DEMO/")  # Replace with your application's URL

    # Choose Product Catalogue from Main Menu
    page.get_by_role("link", name="Katalog ponuda").click()

    # Wait for 5 seconds (adjust the duration as needed)
    page.wait_for_timeout(5000)

    # Execute JavaScript to count the elements
    products_count = page.evaluate('document.querySelectorAll(".product-list li").length')

    # Assert the count (modify as needed)
    assert products_count > 0, "No product list items found"

    # Locate and click the element with the text "Krediti"
    krediti_element = page.get_by_role("link", name="Krediti", exact=True)
    krediti_element.click()

    # Wait for 5 seconds (adjust the duration as needed)
    page.wait_for_timeout(5000)

    # Execute JavaScript to count the elements
    products_count = page.evaluate('document.querySelectorAll(".product-list li").length')

    # Assert the count (modify as needed)
    assert products_count > 0, "No product list items found"

    # Define the text you want to find within the <p> element
    product_name_text = "Keš kredit sa fiksnom kamatnom stopom"

    # Create a locator for the <a> element containing the specific <p> element text
    link_locator = page.locator(f'a:has(.product-info:has(.product-name:has-text("{product_name_text}")))')

    # Check if the link with the specified text is present
    assert link_locator.count() > 0, f"Link with text '{product_name_text}' not found on the page."

    # Click on the link
    link_locator.first.click()

    # Wait for 5 seconds (adjust the duration as needed)
    page.wait_for_timeout(5000)

    # Locate and click the element with the text "Krediti"
    # krediti_element = page.get_by_role("link", name="Keš kredit sa fiksnom kamatnom stopom", exact=True)
    # krediti_element.click()

    # Locate the button with the text "Prijavi se za ovaj proizvod"
    button_text = "Prijavi se za ovaj proizvod"
    button_selector = f"button:has-text('{button_text}')"
    is_button_present = page.locator(button_selector).first.is_visible()

    # Check if the button is present
    assert is_button_present, f"The button '{button_text}' is not present on the page."