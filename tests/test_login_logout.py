import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from utils.test_util import login

class TestSwagLabsLoginLogout:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Firefox()
        yield driver  
        driver.quit()  

    def test_site(self, driver):
        """
        Test to ensure the correct site is being navigated to

        Args:
            self: current instance of class
            driver: the firefox selenium webdriver

        Return: 
            None
        """

        driver.get("https://www.saucedemo.com/")
        assert driver.title == "Swag Labs"
    
    def test_login_success(self, driver):
        """
        Test for the login function on Sauce Demo. 
        Uses the provided username and password with a correct combination

        Args:  
            self: current instance of class
            driver: the firefox selenium webdriver
        """
        login(driver, "standard_user", "secret_sauce")

        react_burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
        react_burger_menu.click()

        assert driver.find_element(By.ID, "logout_sidebar_link").is_displayed()

    def test_login_failure_incorrect_username(self, driver):
        """
        Test for the login function on Sauce Demon. 
        Uses the provided username and password with an incorrect combination 
            - wrong username, right password

        Args:  
            self: current instance of class
            driver: the firefox selenium webdriver
        """

        login(driver, "no_user_here", "secret_sauce")

        assert driver.find_element(By.CLASS_NAME, "error-button").is_displayed()

    def test_login_failure_incorrect_password(self, driver):
        """
        Test for the login function on Sauce Demo. 
        Uses the provided username and password with an incorrect combination 
            - right username, wrong password
        Args:  
            self: current instance of class
            driver: the firefox selenium webdriver
        """

        login(driver, "standard_user", "this_is_wrong")

        assert driver.find_element(By.CLASS_NAME, "error-button").is_displayed()

    def test_login_failure_no_username(self, driver):
        """
        Test for the login function on Sauce Demo. 
        Uses the provided username and password with an incorrect combination 
            - right username, wrong password
        Args:  
            self: current instance of class
            driver: the firefox selenium webdriver
        """

        login(driver, "", "secret_sauce")

        assert driver.find_element(By.CLASS_NAME, "error-button").is_displayed()

    def test_login_failure_no_password(self, driver):
        """
        Test for the login function on Sauce Demo. 
        Uses the provided username and password with an incorrect combination 
            - right username, wrong password
        Args:  
            self: current instance of class
            driver: the firefox selenium webdriver
        """

        login(driver, "standard_user", "")

        assert driver.find_element(By.CLASS_NAME, "error-button").is_displayed()

    def test_logout(self, driver):
        """
        Test for logout feature
        Login, then check for logout button / link and click

        Args:
            self: instance of class
            driver: firefox selenium webdriver
        """

        login(driver, "standard_user", "secret_sauce")
        react_burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
        react_burger_menu.click()

        logout_link = driver.find_element(By.ID, "logout_sidebar_link")
        logout_link.click()

        assert driver.find_element(By.ID, "login-button").is_displayed()