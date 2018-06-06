import unittest
from selenium import webdriver

class Topic_08_JSExecutor(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=".\\driver\\chromedriver.exe")
        self.driver.maximize_window()

    def test_01_UsingJE(self):
        driver = self.driver
        driver.get("http://live.guru99.com/")
        domainName = driver.execute_script("return document.domain")
        self.assertEqual(domainName, "live.guru99.com")
        
        urlPage = driver.execute_script("return document.URL")
        self.assertEqual(urlPage, "http://live.guru99.com/")

        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//a[text()='Mobile']"))
        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//h2[a[contains(text(),'Samsung Galaxy')]]/following-sibling::div[@class='actions']//button"))

        innerText = str(driver.execute_script("return document.documentElement.innerText;").encode("utf-8"))
        self.assertTrue(innerText.__contains__("Samsung Galaxy was added to your shopping cart."))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

