"""
LoginPage Object page

Abstracts behavior of the login page

Page Actions
- entering username
- entering password
- submitting login information
"""

from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        driver.get("https://www.saucedemo.com/")
        self.username_field = driver.find_element(By.ID, "user-name")
        self.password_field = driver.find_element(By.ID, "password")
        self.login_button = driver.find_element(By.ID, "login-button")
    
    def enter_username(self, username):
        self.username_field.clear()
        self.username_field.send_keys(username)

    def enter_password(self, password):
        self.password_field.clear()
        self.password_field.send_keys(password)
    
    def submit_login(self):
        self.login_button.click()