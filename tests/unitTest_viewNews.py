# Selenium test script
# test script to verify a valid user is logged in successfully
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import warnings


class ll_ATS(unittest.TestCase):
    # set up the test class - assign the driver to Chrome - if using a different
    # browser, change the browser name below
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/akarnati@unomaha.edu/Documents/stock_management_ClassEmailCC_noMsgBroker/djangoProject1/tests/chromedriver")
        warnings.simplefilter('ignore', ResourceWarning)  # ignore resource warning if occurs

    # If login is successful, 'Logout' will be displayed as the text in the Navbar
    def test_ll(self):
        user = "group3sprint"  # must be a valid username for the application
        pwd = "group3@wad"  # must be the password for a valid user

        # open the browser and go to the admin page
        driver = self.driver
        driver.maximize_window()
        driver.get("https://group3sprint.pythonanywhere.com/")
        time.sleep(3)
        driver.find_element(By.XPATH, '/ html / body / div / nav / ul / li[2] / a[2]').click()
        time.sleep(3)
        elem = driver.find_element(By.ID, "username")
        elem.send_keys(user)
        time.sleep(3)
        elem = driver.find_element(By.ID, "password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        try:
            time.sleep(3)
            elem = driver.find_element(By.XPATH, '/html/body/div/div[1]/nav/ul[1]/li[3]/a/i').click()
            time.sleep(3)
            print("Test passed - Watchlist is successfully displayed")
            assert True

        except NoSuchElementException:
            self.fail("Edit Service does not appear when User Clicked it - test failed")

    def tearDown(self):
        self.driver.close()

