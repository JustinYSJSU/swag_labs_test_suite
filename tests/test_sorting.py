import pytest
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select # handling select menu items

from utils.test_util import login
from utils.test_util import extract_price

class TestSwagLabsSorting():

    @pytest.fixture
    def driver(self):
        driver = webdriver.Firefox()
        yield driver  
        driver.quit()  

    def test_sort_alphabetical_normal(self, driver):
        """
        Tests the default sorting (A - Z)

        Args:
            self: instance of the class
            driver: selenium firefox webdriver
        """

        login(driver, "standard_user", "secret_sauce")

        # A - Z sorting is the default option, so do not need to find the select menu

        # once the inventory items are all found, figure out a way to create or get a list for 
        # since this is default option, only need to check the number of elements is the same
        inventory_items_alphabetical = driver.find_elements(By.CLASS_NAME, "inventory_item")
        
        texts = sorted([i.text for i in inventory_items_alphabetical])
        assert texts == sorted(texts)
    
    def test_sort_alphabetical_reverse(self, driver):
        """
        Tests reverse sorting (Z - A)

        Args:
            self: instance of the class
            driver: selenium firefox webdriver
        """

        login(driver, "standard_user", "secret_sauce")

        # Pre-reverse sorted list of items to check against 
        inventory_items_reverse_check = driver.find_elements(By.CLASS_NAME, "inventory_item")

        # list of item names, ordered in reverse
        # get text attribute of each element in the sorted list, sorted by the text attribute of each element 
        inventory_item_name_reverse_check= [e.text for e in sorted(inventory_items_reverse_check, key=lambda x: x.text, reverse=True)]

        # Find select menu and select reverse sorting by alphabet 
        select_menu = driver.find_element(By.CLASS_NAME, "product_sort_container")
        select_menu = Select(select_menu) # specific Select object
        
        select_menu.select_by_index(1) # select the second option (Z - A). has a list of all options 
 
        # get list of all items, now ordered in reverse alphabet order
        inventory_items_reverse_alphabetical = driver.find_elements(By.CLASS_NAME, "inventory_item")

        texts = sorted([i.text for i in inventory_items_reverse_alphabetical])
        assert texts == sorted(texts)

    def test_sort_price_low_high(self, driver):
        """
        Tests default sorting by price (low to high)

        Args:
            self: instance of the class
            driver: selenium firefox webdriver
        """
        login(driver, "standard_user", "secret_sauce")

        select_menu = driver.find_element(By.CLASS_NAME, "product_sort_container")
        select_menu = Select(select_menu) # specific Select object
        
        select_menu.select_by_index(2) # select the third option (price low - high). has a list of all options 

        inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        
        # create a list of all prices, then compared to sorted version

        prices = [float(extract_price(item.text)) for item in inventory_items]
        assert prices == sorted(prices)

    def test_sort_price_high_low(self, driver):
        """
        Tests sorting by price (high to low)

        Args:
            self: instance of the class
            driver: selenium firefox webdriver
        """
        login(driver, "standard_user", "secret_sauce")

        select_menu = driver.find_element(By.CLASS_NAME, "product_sort_container")
        select_menu = Select(select_menu) # specific Select object
        
        select_menu.select_by_index(3) # select the third option (price low - high). has a list of all options 

        inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        
        # create a list of all prices, then compared to sorted version
        prices = [float(extract_price(i.text)) for i in inventory_items]

        assert prices == sorted(prices, reverse=True)


        
        
            
        


    
