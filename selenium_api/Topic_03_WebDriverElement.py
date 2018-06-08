import unittest
from selenium import webdriver

class Topic_03_WebDriverElement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie(executable_path=".\\driver\\chromedriver.exe")

    def test_03_VerifyEnableDisable(self):
        driver = self.driver
        driver.implicitly_wait(30)
        driver.get("http://daominhdam.890m.com/")
        # driver.maximize_window()
        elementEmail = driver.find_element_by_xpath("//input[@type='email']")
        self.assertTrue(elementEmail.is_enabled())
        elementUnder18 = driver.find_element_by_xpath("//input[@id='under_18']")
        self.assertTrue(elementUnder18.is_enabled())
        elementEduText = driver.find_element_by_xpath("//textarea[@id='edu']")
        self.assertTrue(elementEduText.is_enabled())
        elementJob = driver.find_element_by_xpath("//select[@id='job1']")
        self.assertTrue(elementJob.is_enabled())
 
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

