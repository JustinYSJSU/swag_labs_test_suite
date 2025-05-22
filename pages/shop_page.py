from selenium.webdriver.common.by import By

from login_page import LoginPage

class ShopPage():

    def __init__(self, driver):
        self.view_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    
    # def get_items(self, driver):

    def view_cart(self):
        self.view_cart_link.click()
    