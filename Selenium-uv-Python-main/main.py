from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://seleniumbase.io/simple/login")
    username = driver.find_element(
        By.ID,
        "username",
    )
    password = driver.find_element(
        By.ID,
        "password",
    )
    username.send_keys("demo_user")
    password.send_keys("secret_pass")
    driver.find_element(
        By.LINK_TEXT,
        "Sign in",
    ).click()
    assert "Welcome!" in driver.page_source
    print("Login Test Passed")
finally:
    driver.quit()