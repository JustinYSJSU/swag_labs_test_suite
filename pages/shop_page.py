from selenium.webdriver.common.by import By

class ShopPage():

    def __init__(self, driver):
        self.view_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    
    def add_to_cart(self, driver):
        print()
        
    def get_items(self, driver):
        return driver.find_elements(By.CLASS_NAME, "cart_item")

    def view_cart(self):
        self.view_cart_link.click()
    