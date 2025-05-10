# Swag Labs Test Suite 

An automated test suite for the e-commerce site [Swag Labs](https://www.saucedemo.com/) created with Python, Selenium, and Pytest

## Overview
- Comprehensive test suite written using Python, Selenium, Pytest
- Unit tests for the following site functionalities
  - Authentication 
  - Shopping Cart
  - Item Sorting

## Test Suite Coverage
- Authentication
  - Login pass (correct username / password)
  - Login fail (incorrect username, correct password)
  - Login fail (correct username, incorrect password)
  - Login fail (no username, correct password)
  - Login fail (correct username, no password)
  - Logout pass

- Shopping Cart
  - Add item to empty cart
  - Add item to a non-empty cart
  - Remove single item from cart with a single item
  - Remove single item from cart with multiple items

- Item Sorting
  - Sort by name A - Z
  - Sort by name Z - A
  - Sort by price low - high
  - Sort by price high - low
    

