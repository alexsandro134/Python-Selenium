import unittest
import time
from selenium import webdriver

class Topic_07_IFrameWindowPopup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=".\\driver\\chromedriver.exe")
        self.driver.maximize_window()

    def test_01_IFrameHandle(self):
        driver = self.driver
        driver.get("https://www.hdfcbank.com/")
        iframeFlipBanner = driver.find_element_by_xpath("//div[@class='flipBannerWrap']//iframe")
        driver.switch_to.frame(iframeFlipBanner)

        self.assertEqual(driver.find_element_by_xpath("//span[@id='messageText']").text, "What are you looking for?")
        driver.switch_to.default_content()

        iframeSlideBanner = driver.find_element_by_xpath("//div[@class='slidingbanners']//iframe")
        driver.switch_to.frame(iframeSlideBanner)

        itemList = driver.find_elements_by_xpath("//div[@id='productcontainer']/div")
        self.assertEqual(len(itemList), 6)

    def test_02_HandleMutipleWindows(self):
        driver = self.driver
        driver.get("http://www.hdfcbank.com/")
        original_handle = driver.current_window_handle
        driver.find_element_by_xpath("//a[text()='Agri']").click()
        
        allWindows = driver.window_handles
        for window_items in allWindows:
            if window_items != original_handle:
                driver.switch_to.window(window_items)
                break

        driver.find_element_by_xpath("//p[text()='Account Details']").click()

        allWindows = driver.window_handles
        for window in allWindows:
            driver.switch_to.window(window)
            if driver.title == "Welcome to HDFC Bank NetBanking":
                break
        
        footerFrame = driver.find_element_by_xpath("//frame[@name='footer']")
        driver.switch_to.frame(footerFrame)

        driver.find_element_by_xpath("//a[text()='Privacy Policy']").click()

        allWindows = driver.window_handles
        for window in allWindows:
            driver.switch_to.window(window)
            if driver.title == "HDFC Bank - Leading Bank in India, Banking Services, Private Banking, Personal Loan, Car Loan":
                break
        
        driver.find_element_by_xpath("//a[text()='CSR']").click()

        driver.switch_to.window(original_handle)

        allWindows = driver.window_handles
        for window_items in allWindows:
            if window_items != original_handle:
                driver.switch_to.window(window_items)
                driver.close()
        driver.switch_to.window(original_handle)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

