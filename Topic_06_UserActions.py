import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

class Topic_06_UserActions(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=".\\driver\\chromedriver.exe")

    def test_01_HoverMouse(self):
        driver = self.driver
        driver.get("http://daominhdam.890m.com")
        driver.maximize_window()

        hoverElement = driver.find_element_by_xpath("//a[text()='Hover over me']")
        action = ActionChains(driver)
        action.move_to_element(hoverElement).perform()

        self.assertTrue(driver.find_element_by_xpath("//div[@class='tooltip-inner']").is_displayed())

    def test_02_ClickAndHold(self):
        driver = self.driver
        driver.get("http://jqueryui.com/resources/demos/selectable/display-grid.html")
        elements = driver.find_elements_by_xpath("//ol[@id='selectable']/li")

        action = ActionChains(driver)
        action.click_and_hold(on_element=elements[0]).click_and_hold(on_element=elements[3]).click().perform()
        elements = driver.find_elements_by_xpath("//ol[@id='selectable']/li[contains(@class,'ui-selected')]")
        self.assertEqual(len(elements), 4)

    def test_03_DoubleClick(self):
        driver = self.driver
        driver.get("http://www.seleniumlearn.com/double-click")
        element = driver.find_element_by_xpath("//button[contains(text(),'Double')]")

        action = ActionChains(driver)
        action.double_click(element).perform()

        alert = driver.switch_to_alert()
        self.assertEqual(alert.text,"The Button was double-clicked.")
        alert.accept()

    def test_04_RightClick(self):
        driver = self.driver
        driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
        rightClickElement = driver.find_element_by_xpath("//span[text()='right click me']")

        action = ActionChains(driver)
        action.context_click(rightClickElement).perform()

        quitElement = driver.find_element_by_xpath("//li[contains(@class,'context-menu-icon-quit')]")
        action.move_to_element(quitElement).perform()

        self.assertTrue(driver.find_element_by_xpath("//li[contains(@class,'context-menu-hover') and contains(.,'Quit')]").is_displayed())

        quitElement.click()
        alert = driver.switch_to_alert()
        alert.accept()

    def test_05_DragAndDrop(self):
        driver = self.driver
        driver.get("http://demos.telerik.com/kendo-ui/dragdrop/angular")

        draggableElement = driver.find_element_by_xpath("//div[@id='draggable']")
        droptargetElement = driver.find_element_by_xpath("//div[@id='droptarget']")

        action = ActionChains(driver)
        action.drag_and_drop(draggableElement, droptargetElement).perform()

        self.assertEqual(droptargetElement.text,"You did great!")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

