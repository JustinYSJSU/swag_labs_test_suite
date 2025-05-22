import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from utils.test_util import login, add_single_item, add_double_item

from pages.shop_page import ShopPage

class TestSwagLabsCart:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Firefox()
        yield driver  
        driver.quit()  


    def test_add_to_cart_empty(self, driver):
       """
       Testing adding a shop item to an empty cart

       Args:    
            self: instance of the class
            driver: selenium firefox webdriver
       """
       '''
       login(driver, "standard_user", "secret_sauce")
       add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
       add_to_cart_button.click()

       view_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
       view_cart_link.click()

       assert driver.find_element(By.CLASS_NAME, "cart_list").is_displayed()
       '''
       shop_page = ShopPage(driver)

    def test_add_to_cart_existing(self, driver):
        """
        Test adding a shop item to a non - empty cart

        Args:
            self: instance of the class
            driver: selenium firefox webdriver
        """
        total_items = 2
        add_single_item(driver)
        add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_to_cart_button.click()

        view_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        view_cart_link.click()

        item_count = driver.find_elements(By.CLASS_NAME, "cart_item")
        
        assert len(item_count) == total_items

    def test_remove_from_cart_single(self, driver):
        """
        Test removing a single item from the cart, when it is the only item present

        Args:
            self: instance of the class
            driver: selenium firefox webdriver
        """

        add_single_item(driver)
        view_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        view_cart_link.click()

        remove_item_button = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        remove_item_button.click()

        item_count = driver.find_elements(By.CLASS_NAME, "cart_item")

        assert len(item_count) == 0
        
    def test_remove_from_cart_multiple(self, driver):
        """
        Test removing a single item from the cart, when there are multiple items
        """

        add_double_item(driver)

        view_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        view_cart_link.click()

        remove_item_buttons = driver.find_elements(By.CLASS_NAME, "btn btn_secondary btn_small cart_button")

        for b in remove_item_buttons:
            b.click()
        
        assert len(remove_item_buttons) == 0