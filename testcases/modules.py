from selenium.webdriver.common.by import By
from library.components import scroll_to_element
import time

class ClickModule:
    def __init__(self, driver):
        self.driver = driver

    def home(self):
        self.driver.find_element(By.XPATH, "//a[@id='ui-id-1']").click()

    def reqQuotation(self):
        self.driver.find_element(By.XPATH, "//a[@id='ui-id-2']").click()

    def retQuotation(self):
        link = "https://demo.guru99.com/insurance/v1/new_quotation.php"
        if self.driver.current_url == link:
            self.driver.back()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@id='ui-id-3']").click()

    def profile(self):
        link = "https://demo.guru99.com/insurance/v1/retrieve_quotation.php"
        if self.driver.current_url == link:
            self.driver.back()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@id='ui-id-4']").click()

    def editProfile(self):
        link = "https://demo.guru99.com/insurance/v1/retrieve_quotation.php"
        if self.driver.current_url == link:
            self.driver.back()
        time.sleep(5)
        # scroll_to_element(self.driver, By.XPATH, "//input[@value='Log out']")
        self.driver.find_element(By.XPATH, "//a[@id='ui-id-5']").click()

