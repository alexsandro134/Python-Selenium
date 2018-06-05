import unittest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Topic_04_DropDownList(unittest.TestCase):
    # name = "Tai Le"
    # dob = "11/05/1991"
    # address = "Xuan Thuy"
    # city = "Ha Noi"
    # state = "Cau Giay"
    # pin = "123457"
    # telephone = "0123456789"
    # password = "98764311"
    
    def setUp(self):
        self.driver = webdriver.Ie(executable_path=".\\driver\\chromedriver.exe")
        
    def test_01_HandleDropDownList(self):
        driver = self.driver
        driver.get("http://daominhdam.890m.com/")
        driver.maximize_window()
        jobRole01 = Select(driver.find_element_by_xpath("//select[@id='job1']"))
        self.assertFalse(jobRole01.is_multiple)
        
        jobRole01.select_by_visible_text("Automation Tester")
        self.assertEqual(jobRole01.first_selected_option.text, "Automation Tester")
        time.sleep(2)

        jobRole01.select_by_value("manual")
        self.assertEqual(jobRole01.first_selected_option.text, "Manual Tester")
        time.sleep(2)

        jobRole01.select_by_index(3)
        self.assertEqual(jobRole01.first_selected_option.text, "Mobile Tester")
        time.sleep(2)
        
        self.assertEqual(len(jobRole01.options), 5) 

    def test_02_HandleTextboxArea(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/v4/")
        driver.maximize_window()

        driver.find_element_by_xpath("//input[@name='uid']").send_keys("mngr134897")
        driver.find_element_by_xpath("//input[@name='password']").send_keys("mAvYpYn")

        driver.find_element_by_xpath("//input[@name='btnLogin']").click()
        self.assertTrue(driver.find_element_by_xpath("//marquee").is_displayed())

        driver.find_element_by_xpath("//a[text()='New Customer']").click()
        driver.find_element_by_xpath("//input[@name='name']").send_keys("Tai Le")
        driver.find_element_by_xpath("//input[@value='m']").click()

        driver.execute_script("arguments[0].removeAttribute('type')", driver.find_element_by_xpath("//input[@id='dob']"))

        driver.find_element_by_xpath("//input[@id='dob']").send_keys("11/05/1991")
        driver.find_element_by_xpath("//textarea[@name='addr']").send_keys("Xuan Thuy")
        driver.find_element_by_xpath("//input[@name='city']").send_keys("Ha Noi")
        driver.find_element_by_xpath("//input[@name='state']").send_keys("Cau Giay")
        driver.find_element_by_xpath("//input[@name='pinno']").send_keys("1234567")
        driver.find_element_by_xpath("//input[@name='telephoneno']").send_keys("0123456789")
        driver.find_element_by_xpath("//input[@name='emailid']").send_keys(email_generator())
        driver.find_element_by_xpath("//input[@name='password']").send_keys("98764311")

        driver.find_element_by_xpath("//input[@name='sub']").click()

        self.assertTrue(driver.find_element_by_xpath("//p[@class='heading3']").is_displayed())

        customerId = driver.find_element_by_xpath("//td[text()='Customer ID']/following-sibling::td").text

        driver.find_element_by_xpath("//a[text()='Edit Customer']").click()
        driver.find_element_by_xpath("//input[@name='cusid']").send_keys(customerId)
        driver.find_element_by_xpath("//input[@type='submit']").click()

        self.assertEqual(driver.find_element_by_xpath("//input[@name='name']").get_attribute("value"), "Tai Le")
        self.assertEqual(driver.find_element_by_xpath("//textarea[@name='addr']").text, "Xuan Thuy")

    def tearDown(self):
        self.driver.close()

def email_generator(size=5, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size)) + '@' + random.choice(chars) + '.com'

if __name__ == "__main__":
    unittest.main()

