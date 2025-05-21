import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage

class TestSwagLabsLoginLogout:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Firefox()
        yield driver  
        driver.quit()  

    def test_login_success(self, driver):
        """
        Test for the login function on Sauce Demo. 
        Uses the provided username and password with a correct combination

        Args:  
            self: current instance of class
            driver: the firefox selenium webdriver
        """
        login_page = LoginPage(driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.submit_login()

        # assert driver.find_element(By.ID, "logout_sidebar_link").is_displayed()

    def test_login_failure_incorrect_username(self, driver):
        """
        Test for the login function on Sauce Demon. 
        Uses the provided username and password with an incorrect combination 
            - wrong username, right password

        Args:  
            self: current instance of class
            driver: the firefox selenium webdriver
        """

        login_page = LoginPage(driver)
        login_page.enter_username("wrong_name")
        login_page.enter_password("secret_sauce")
        login_page.submit_login()

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

        login_page = LoginPage(driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("wrong_password")
        login_page.submit_login()

        assert driver.find_element(By.CLASS_NAME, "error-button").is_displayed()

    def test_login_failure_no_username(self, driver):
        """
        Test for the login function on Sauce Demo. 
        Uses the provided username and password with an incorrect combination 
            - no username provided, right password
        Args:  
            self: current instance of class
            driver: the firefox selenium webdriver
        """

        login_page = LoginPage(driver)
        login_page.enter_username("")
        login_page.enter_password("secret_sauce")
        login_page.submit_login()

        assert driver.find_element(By.CLASS_NAME, "error-button").is_displayed()

    def test_login_failure_no_password(self, driver):
        """
        Test for the login function on Sauce Demo. 
        Uses the provided username and password with an incorrect combination 
            - right username, no password provided
        Args:  
            self: current instance of class
            driver: the firefox selenium webdriver
        """

        login_page = LoginPage(driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("")
        login_page.submit_login()

        assert driver.find_element(By.CLASS_NAME, "error-button").is_displayed()


    
    def test_logout(self, driver):
        """
        Test for logout feature
        Login, then check for logout button / link and click

        Args:
            self: instance of class
            driver: firefox selenium webdriver
        """

        login_page = LoginPage(driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.submit_login()
        
        react_burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
        react_burger_menu.click()

        logout_link = driver.find_element(By.ID, "logout_sidebar_link")
        logout_link.click()

        assert driver.find_element(By.ID, "login-button").is_displayed()
    