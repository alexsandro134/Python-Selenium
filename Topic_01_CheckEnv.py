import unittest
from selenium import webdriver

class Topic_01_CheckEnv(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie(executable_path=".\\driver\\chromedriver.exe")

    def test_01_VerifyTitle(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/v4/")
        # driver.maximize_window()
        self.assertEqual("Guru99 Bank Home Page", driver.title)
 
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

