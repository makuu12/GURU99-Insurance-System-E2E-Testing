from selenium import webdriver

class init:
    def __init__(self):
            self.driver = None

    def setup(self, link):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        # self.driver.get("https://demo.guru99.com/insurance/v1/index.php")
        self.driver.get(link)
        return self.driver
        