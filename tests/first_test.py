from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


def test_eight_components():
    # 1. Start the session
    driver = webdriver.Edge()

    # 2. Take action on browser
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    
    # 3. Request browser information
    title = driver.title
    assert title == "Web form"

    # 4. Establish Waiting Strategy
    driver.implicitly_wait(0.5)

    # 5. Find an element
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # 6. Take action on element
    text_box.send_keys("Selenium")
    submit_button.click()

    # 7. Request element information
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    # 8. End the session
    driver.quit()





