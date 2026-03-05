from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

try:
    print("Opening SauceDemo...")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    print("Logging in...")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    print("Adding Backpack to cart...")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    print("Starting checkout...")
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Freddy")
    driver.find_element(By.ID, "last-name").send_keys("Tester")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    print("Verifying Order Overview...")
    item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    total_price = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    
    assert item_name == "Sauce Labs Backpack"
    assert "$32.39" in total_price
    print(f"Verified: {item_name} for {total_price}")

    driver.find_element(By.ID, "finish").click()
    print("Test Passed: Order placed successfully!")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    time.sleep(5)
    print("Closing browser...")
    driver.quit()