import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_backpack_purchase_flow():
    """
    Test Case: Verify a user can login and add a backpack to the cart.
    """
    # Browser Setup
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10) # Added a standard implicit wait for stability
    driver.get("https://www.saucedemo.com/")

    # Page Initializations
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # 1. Login Flow
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # 2. Inventory Actions
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    # 3. Verification
    # Check if the URL updated to the cart page
    expected_url = "https://www.saucedemo.com/cart.html"
    assert driver.current_url == expected_url, f"Expected {expected_url} but got {driver.current_url}"
    
    print("Test Status: Success - Item added to cart.")

    # Teardown
    driver.quit()

if __name__ == "__main__":
    test_backpack_purchase_flow()