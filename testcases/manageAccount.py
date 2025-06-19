from selenium.webdriver.common.by import By
import time, os
from library.components import find_element_and_select, load_file, save_json

class manage:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("aaa@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='submit']").click()
    
    def createAccount(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        data = load_file("account.json")
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//input[@id='user_firstname']").send_keys(data["firstname"])
        self.driver.find_element(By.XPATH, "//input[@id='user_surname']").send_keys(data["surname"])
        self.driver.find_element(By.XPATH, "//input[@id='user_phone']").send_keys(data["contact"])
        time.sleep(3)

        find_element_and_select(self.driver, By.ID, "user_dateofbirth_1i", data["birthdate"]["year"])
        find_element_and_select(self.driver, By.XPATH, "//select[@id='user_dateofbirth_2i']", data["birthdate"]["month"])
        find_element_and_select(self.driver, By.XPATH, "//select[@id='user_dateofbirth_3i']", data["birthdate"]["day"])
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//label[normalize-space()='Provisional']").click()
        find_element_and_select(self.driver, By.XPATH, "//select[@id='user_licenceperiod']", data["licenceperiod"])
        find_element_and_select(self.driver, By.XPATH, "//select[@id='user_occupation_id']", data["occupation"])
        time.sleep(3)

        # Address
        self.driver.find_element(By.XPATH, "//input[@id='user_address_attributes_street']").send_keys(data["Address"]["street"])
        self.driver.find_element(By.XPATH, "//input[@id='user_address_attributes_city']").send_keys(data["Address"]["city"])
        self.driver.find_element(By.XPATH, "//input[@id='user_address_attributes_county']").send_keys(data["Address"]["county"])
        self.driver.find_element(By.XPATH, "//input[@id='user_address_attributes_postcode']").send_keys(data["Address"]["postcode"])
        time.sleep(3)

        # Account
        self.driver.find_element(By.XPATH, "//input[@id='user_user_detail_attributes_email']").send_keys(data["email"])
        self.driver.find_element(By.XPATH, "//input[@id='user_user_detail_attributes_password']").send_keys(data["password"])
        self.driver.find_element(By.XPATH, "//input[@id='user_user_detail_attributes_password_confirmation']").send_keys(data["password"])
        time.sleep(3)
        
        self.driver.find_element(By.XPATH, "//input[@name='submit']").click()
    

    def editProfile(self):
        newData = "Jane"
        data = load_file("account.json")
        data["firstname"] = newData
        firstName = self.driver.find_element(By.XPATH, "//input[@id='user_firstname']")
        firstName.send_keys(newData)

        newdata = firstName.get_attribute("value")
        data["firstname"] = newdata
        save_json(data, "account.json")
        # print("should be jane", fn)

        self.driver.find_element(By.XPATH, "//input[@name='commit']").click()

        


    def verifyProfile(self):
        data = load_file("account.json")
        title = self.driver.find_element(By.XPATH, "//div[@id='tabs-4']//p[1]")
        firstname = self.driver.find_element(By.XPATH, "//div[@id='tabs-4']//p[3]")
        surname = self.driver.find_element(By.XPATH, "//div[@id='tabs-4']//p[5]")
        contact = self.driver.find_element(By.XPATH, "//div[@id='tabs-4']//p[7]")
        birthdate = self.driver.find_element(By.XPATH, "//div[@id='tabs-4']//p[9]")
        status = self.driver.find_element(By.XPATH, "//div[@id='tabs-4']//p[11]") # licence type
        licenceperiod = self.driver.find_element(By.XPATH, "//div[@id='tabs-4']//p[13]")
        occupation = self.driver.find_element(By.XPATH, "//div[@id='tabs-4']//p[15]")
        driverHistory = self.driver.find_element(By.XPATH, "//div[@id='tabs-4']//p[17]")
        Address = self.driver.find_element(By.XPATH, "//div[@id='tabs-4']//p[19]")

        birthdate = data["birthdate"]
        year = birthdate["year"]
        month = birthdate["month"]
        day = birthdate["day"]
        expected_birthdate = f"{month} {day}, {year}"

        Address = data["Address"]
        street = Address["street"]
        city = Address["city"]
        county = Address["county"]
        postcode = Address["postcode"]
        expected_address = f"{street}, {city}, {county}, {postcode}"

        assert data["title"] in title, f"Title mismatch: '{data['title']}' not in '{title}'"
        assert data["firstName"] in firstname, f"Firstname mismatch: '{data['firstname']}' not in '{firstname}'"
        assert data["lastname"] in surname, f"Surname mismatch: '{data['lastname']}' not in '{surname}'"
        assert data["phone"] in contact, f"Contact mismatch: '{data['phone']}' not in '{contact}'"
        assert expected_birthdate in birthdate, f"Expected '{expected_birthdate}' in '{birthdate}'"
        assert data["licencetype"] in status, f"Licence type mismatch: '{data['licencetype']}' not in '{status}'"
        assert data["licenceperiod"] in licenceperiod, f"Licence period mismatch: '{data['licenceperiod']}' not in '{licenceperiod}'"
        assert data["occupation"] in occupation, f"Occupation mismatch: '{data['occupation']}' not in '{occupation}'"
        assert data["driverHistory"] in driverHistory, f"Driver history mismatch: '{data['driverHistory']}' not in '{driverHistory}'"
        assert expected_address in Address, f"Address mismatch: '{data['Address']}' not in '{Address}'"

        
        def logout(self):
            self.driver.find_element(By.XPATH, "//input[@value='Log out']").click()

