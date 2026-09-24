import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://seleniumbase.io/simple/login"


# 1. เคส Login สำเร็จ แล้วกด Logout (Positive Flow)
def test_login_and_logout(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)

    wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    ).send_keys("demo_user")

    driver.find_element(By.ID, "password").send_keys("secret_pass")

    wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
    ).click()

    heading = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )
    assert heading.text == "Welcome!"

    wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign out"))
    ).click()

    message = wait.until(
        EC.visibility_of_element_located((By.ID, "top_message"))
    )
    assert "signed out" in message.text.lower()

    time.sleep(5)


# 2. เคส Username ถูก แต่ไม่ใส่ Password (Negative Case)
def test_login_correct_user_empty_password(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)

    wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    ).send_keys("demo_user")

    driver.find_element(By.ID, "password").send_keys("")

    wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
    ).click()

    assert "Welcome!" not in driver.page_source

    time.sleep(5)


# 3. เคส Username ผิด (invalid_user) แต่ Password ถูก (Negative Case)
def test_login_wrong_user_correct_password(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)

    wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    ).send_keys("invalid_user")

    driver.find_element(By.ID, "password").send_keys("secret_pass")

    wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
    ).click()

    assert "Welcome!" not in driver.page_source

    time.sleep(5)


# 4. เคสกด Enter บน คีย์บอร์ด แทนการคลิกปุ่ม Sign in (Keyboard Interaction)
def test_login_submit_via_enter_key(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)

    wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    ).send_keys("demo_user")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_pass")
    password_field.send_keys(Keys.ENTER)

    heading = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )
    assert heading.text == "Welcome!"

    time.sleep(5)


# 5. เคสพิมพ์ข้อมูลแล้วล้างออกด้วย .clear() ก่อนพิมพ์ใหม่ (Input Management)
def test_input_clear_and_retype(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)

    username_input = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )

    # พิมพ์ผิดก่อน แล้วลบออก
    username_input.send_keys("wrong_user_123")
    time.sleep(1)
    username_input.clear()

    # พิมพ์ค่าที่ถูกต้อง
    username_input.send_keys("demo_user")
    driver.find_element(By.ID, "password").send_keys("secret_pass")

    wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
    ).click()

    heading = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )
    assert heading.text == "Welcome!"

    time.sleep(5)


# 6. เคสตรวจสอบองค์ประกอบ UI เบื้องต้น (UI Verification)
def test_login_page_ui_elements(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)

    assert "Login" in driver.title

    username_input = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    password_input = driver.find_element(By.ID, "password")
    sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")

    assert username_input.is_enabled()
    assert password_input.is_enabled()
    assert sign_in_button.is_displayed()

    time.sleep(5)