from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time

def test_buy_backpack():
    # 1. Setup: Start the Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # 2. Initialize Page Objects (Our "Maps")
    # This connects the 'Brain' to the 'Finger'
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    # 3. Execution: Perform the steps
    # Notice how easy this is to read!
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    # Add the item to the cart
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    # 4. Verification: Did we reach the cart?
    time.sleep(2)  # Small pause just so we can see it happen
    assert "cart.html" in driver.current_url
    
    print("\n✅ Test Passed: Backpack successfully added to cart!")

    # 5. Cleanup: Close the browser
    driver.quit()

# The "Magic Password" for Python to run this specific file
if __name__ == "__main__":
    test_buy_backpack()