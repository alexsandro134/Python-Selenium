import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from random import randint

firstName = "taile"
fileName = "test-photo.png"
folderName = "taile" + str(randint(0, 9999))
emailAddress = "taile" + str(randint(0, 9999)) + "@gmail.com"

class Topic_09_UploadFile(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=".\\driver\\chromedriver.exe")

    def test_01_UploadFile(self):

        driver = self.driver
        driver.get("https://encodable.com/uploaddemo/")
        driver.maximize_window()
        driver.find_element_by_xpath("//input[@type='file']").send_keys("E:\\Python\\Selenium Python\\WebDriver_API_Python\\test-data\\" + fileName + "")

        select = Select(driver.find_element_by_xpath("//select[@name='subdir1']"))
        select.select_by_visible_text("/uploaddemo/files/")

        driver.find_element_by_xpath("//input[@id='newsubdir1']").send_keys(folderName)
        driver.find_element_by_xpath("//input[@id='formfield-email_address']").send_keys(emailAddress)
        driver.find_element_by_xpath("//input[@id='formfield-first_name']").send_keys(firstName)
        driver.find_element_by_xpath("//input[@id='uploadbutton']").click()

        time.sleep(10)
        driver.find_element_by_xpath("//dd[contains(text(),'Email Address: " + emailAddress + "')]").is_displayed()
        driver.find_element_by_xpath("//dd[contains(text(),'First Name: " + firstName + "')]").is_displayed()
        driver.find_element_by_xpath("//dt[a[contains(text()," + fileName + ")]]").is_displayed()

        driver.find_element_by_xpath("//a[text()='View Uploaded Files']").click()
        driver.find_element_by_xpath("//td[a[text()='" + folderName + "']]").click()
        driver.find_element_by_xpath("//a[text()='" + fileName + "']").is_displayed()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

