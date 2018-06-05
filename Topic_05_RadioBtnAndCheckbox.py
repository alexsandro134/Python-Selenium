import unittest
import time
from selenium import webdriver

class Topic_05_RadioBtnCheckbox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=".\\driver\\chromedriver.exe")

    def test_01_VerifyButtonEnabled(self):
        driver = self.driver
        driver.get("http://daominhdam.890m.com/")
        driver.maximize_window()
        driver.find_element_by_xpath("//button[@id='button-enabled']").click()
        self.assertEqual(driver.current_url, "http://daominhdam.890m.com/#")
        driver.back()
    
    def test_02_VerifyCheckbox(self):
        driver = self.driver
        dualZoneXpath = "//label[contains(text(),'Dual-zone')]/preceding-sibling::input"
        driver.get("https://demos.telerik.com/kendo-ui/styling/checkboxes")
        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(dualZoneXpath))
        self.assertTrue(driver.find_element_by_xpath(dualZoneXpath).is_selected())
        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(dualZoneXpath))
        self.assertFalse(driver.find_element_by_xpath(dualZoneXpath).is_selected())

    def test_03_VerifyRadioButton(self):
        driver = self.driver
        petrolRadioBtn = "//label[contains(text(),'2.0 Petrol')]/preceding-sibling::input"
        driver.get("http://demos.telerik.com/kendo-ui/styling/radios")
        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(petrolRadioBtn))
        if(not driver.find_element_by_xpath(petrolRadioBtn).is_selected()):
            driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(petrolRadioBtn))

    def test_04_ActionWithJSAlert(self):
        driver = self.driver
        buttonJsAlert = "//button[text()='Click for JS Alert']"
        driver.get("http://daominhdam.890m.com/")
        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(buttonJsAlert))
        alert = driver.switch_to_alert()
        self.assertEqual(alert.text, "I am a JS Alert")
        alert.accept()
        self.assertEqual(driver.find_element_by_xpath("//p[@id='result']").text, "You clicked an alert successfully")

    def test_05_ActionWithJSPrompt(self):
        driver = self.driver
        text = "lethientai"
        buttonJSPrompt = "//button[text()='Click for JS Prompt']"
        driver.get("http://daominhdam.890m.com/")
        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(buttonJSPrompt))
        alert = driver.switch_to_alert()
        alert.send_keys(text)
        alert.accept()
        self.assertEqual(driver.find_element_by_xpath("//p[@id='result']").text, "You entered: " + text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

