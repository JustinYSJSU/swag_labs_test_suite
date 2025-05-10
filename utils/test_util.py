import re

from selenium.webdriver.common.by import By

def login(driver, username, password):
        """
        Utility function for testing login

        Args:
            self: current instance of the class
            driver: selenium firefox webdriver
            username: username to try
            password: password to try
        """
        driver.get("https://www.saucedemo.com/")

        username_field = driver.find_element(By.ID, "user-name")
        username_field.send_keys(username)
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

def add_single_item(driver):
       login(driver, "standard_user", "secret_sauce")
       add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
       add_to_cart_button.click()

def add_double_item(driver):
       login(driver, "standard_user", "secret_sauce")
       add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
       add_to_cart_button.click()

       add_to_cart_button_two = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
       add_to_cart_button_two.click()

def extract_price(text):
       # regex search the item text descriptionfor the price of the item
       # match with a $, then [0-9] for dollar amount, [0-9]{2} for cent
       price = re.search(r"\$([0-9]+\.[0-9]{2})", text)
       return price.group(1) # the part of the text that matches for the price
