from selenium.webdriver.common.by import By

class ContactPage:

    def __init__(self, driver):
        self.__driver = driver

    def getContactTitle(self):
        return self.__driver.find_element(By.XPATH, self.__contact_title).text