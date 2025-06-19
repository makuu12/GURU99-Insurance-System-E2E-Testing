from library.components import find_element_and_select, load_file
from selenium.webdriver.common.by import By
import json, re, os, time

class quotation:
    
    def __init__(self, driver):
        self.driver = driver

    def fillRequest(self):
        data = load_file("qoute.json")
        time.sleep(3)

        find_element_and_select(self.driver, By.XPATH, "//select[@id='quotation_breakdowncover']", data["breakdown_cover"])
        # self.driver.find_element(By.XPATH, "//label[normalize-space()='YES']").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//input[@id='quotation_incidents']").send_keys(data["incident_description"])
        self.driver.find_element(By.XPATH, "//input[@id='quotation_vehicle_attributes_registration']").send_keys(data["registration"])
        self.driver.find_element(By.XPATH, "//input[@id='quotation_vehicle_attributes_mileage']").send_keys(data["mileage"])
        self.driver.find_element(By.XPATH, "//input[@id='quotation_vehicle_attributes_value']").send_keys(data["value"])
        time.sleep(3)

        find_element_and_select(self.driver, By.XPATH, "//select[@id='quotation_vehicle_attributes_parkinglocation']", data["parking_location"])
        time.sleep(3)

        # Start Policy
        find_element_and_select(self.driver, By.XPATH, "//select[@id='quotation_vehicle_attributes_policystart_1i']", data["policy_start"]["year"])
        find_element_and_select(self.driver, By.XPATH, "//select[@id='quotation_vehicle_attributes_policystart_2i']", data["policy_start"]["month"])
        find_element_and_select(self.driver, By.XPATH, "//select[@id='quotation_vehicle_attributes_policystart_3i']", data["policy_start"]["day"])
        time.sleep(3)

    def calculateRequest(self):
        self.driver.find_element(By.XPATH, "//input[@value='Calculate Premium']").click()

    def SaveQuotation(self):
        self.driver.find_element(By.XPATH, "//input[@name='submit']").click()
    
    def resetForm(self):
        self.driver.find_element(By.XPATH, "//input[@id='resetquote']").click()

    # This shit will get a code from the generated request and post to the retrieve Quotation
    def getNumber(self):
        a = self.driver.find_element(By.XPATH, "//body")
        text = a.text
        match = re.search(r'\b\d{5,6}\b', text)
        time.sleep(4)
        if match:
            return match.group(0)
        return None
    
    def retrieveQuotation(self, code):
        self.driver.find_element(By.XPATH, "//input[@placeholder='identification number']").send_keys(code)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='getquote']").click()