from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        # Finding the backpack and the cart icon
        # Using 'selectors' so we only have to change them here if the site updates
        self.backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    #  What the user actually does on this page
    def add_backpack_to_cart(self):
        """Clicks the 'Add to Cart' button for the Sauce Labs Backpack"""
        self.driver.find_element(*self.backpack_add_button).click()

    def go_to_cart(self):
        """Clicks the shopping cart icon to view selected items"""
        self.driver.find_element(*self.cart_icon).click()