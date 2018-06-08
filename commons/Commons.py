from selenium import webdriver

class CommonsVerify(object):
    def __init__(self, browser):
        if (browser == "chrome"):
            self.driver = webdriver.Chrome()

    def isElementDisplayed(self, xpathName):
        driver = self.driver
        element = driver.find_element_by_xpath(xpathName)
        if(element.is_displayed()):
            return True
        else:
            return False

    def isElementEnabled(self, xpathName):
        driver = self.driver
        element = driver.find_element_by_xpath(xpathName)
        if(element.is_enabled()):
            return True
        else:
            return False

    def isElementSelected(self, xpathName):
        driver = self.driver
        element = driver.find_element_by_xpath(xpathName)
        if(element.is_selected()):
            return True
        else:
            return False
    
    # ================================
    #  Working with Element

    def sendTextToElement(self, xpathName, text):
        driver = self.driver
        element = driver.find_element_by_xpath(xpathName)
        element.clear()
        element.send_keys(text)

    def clickToElement(self, xpathName):
        driver = self.driver
        element = driver.find_element_by_xpath(xpathName)
        if (element.is_enabled()):
            element.click()
    
    def getTextElement(self, xpathName):
        driver = self.driver
        element = driver.find_element_by_xpath(xpathName)
        return element.text

    # ================================
    #  Working with Window Handles

    def switchToChildWindow(self, parent):
        driver = self.driver
        allWindows = driver.window_handles
        for window in allWindows:
            if window != parent:
                driver.switch_to.window(window)
                break

    
    def switchToMultipleWindow(self, expectedTitle):
        driver = self.driver
        allWindows = driver.window_handles
        for window in allWindows:
            driver.switch_to.window(window)
            if driver.title == expectedTitle:
                break

    
    def closeOtherWindow(self, parent):
        driver = self.driver
        allWindows = driver.window_handles
        for window in allWindows:
            if window != parent:
                driver.switch_to.window(parent)
                driver.close()

        driver.switch_to.window(parent)
    
    # ================================
    #  Working with Js
    def workingWithBrowserByJS(self, js):
        driver = self.driver
        try:
            return driver.execute_script(js)
        except Exception as e:
            print(e.message)
            return None

    def clickToElementByJs(self, xpath):
        driver = self.driver
        try:
            return driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(xpath))
        except Exception as e:
            print(e.message)
            return None
    
    def removeAttributeInDOM(self, xpath, attributeName):
        driver = self.driver
        try:
            return driver.execute_script("arguments[0].removeAttribute('" + attributeName + "');", driver.find_element_by_xpath(xpath))
        except Exception as e:
            print(e.message)
            return None
    
    def scrollToBottomPage(self):
        driver = self.driver
        try:
            return driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        except Exception as e:
            print(e.message)
            return None
    
    def scrollToElement(self, xpath):
        driver = self.driver
        try:
            return driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element_by_xpath(xpath))
        except Exception as e:
            print(e.message)
            return None
            