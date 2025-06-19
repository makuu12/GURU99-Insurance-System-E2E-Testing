import time
from testcases.modules import ClickModule
from testcases.setup import init
from testcases.manageAccount import manage
from testcases.quotationModule import quotation
 
if __name__ == "__main__":
    base = init()
    base.setup("https://demo.guru99.com/insurance/v1/index.php")
    # manage(base.driver).createAccount() 
    manage(base.driver).login()
    time.sleep(3)

    ClickModule(base.driver).reqQuotation() # Next feature: scroll to module
    q = quotation(base.driver)
    [q.fillRequest(), q.calculateRequest(), q.SaveQuotation()] 
    # Quotation(base.driver).resetForm()
    code = quotation(base.driver).getNumber() 

    ClickModule(base.driver).retQuotation()
    quotation(base.driver).retrieveQuotation(code) # NF: verify data from json
    time.sleep(5)
    ClickModule(base.driver).editProfile()
    manage(base.driver).editProfile() 
    ClickModule(base.driver).profile()
    manage(base.driver).verifyProfile() 

    manage(base.driver).logout() 
    