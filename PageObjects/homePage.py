from selenium.webdriver.common.by import By

class HomePage:

    __signup_login_nav_button = "//li/a[contains(@href, 'login')]"
    __logout_nav_button = "//li/a[contains(@href, 'logout')]"
    __delete_account_nav_button = "//li/a[contains(@href, 'delete_account')]"
    __logged_in_username = "//*[contains(@class, 'nav')]//li//b"

    def __init__(self, driver):
        self.__driver = driver

    def clickSignupLogin(self):
        self.__driver.find_element(By.XPATH, self.__signup_login_nav_button).click()

    def getLoggedInUsername(self):
        return self.__driver.find_element(By.XPATH, self.__logged_in_username).text
    
    def clickDeleteAccount(self):
        self.__driver.find_element(By.XPATH, self.__delete_account_nav_button).click()

    def clickLogout(self):
        self.__driver.find_element(By.XPATH, self.__logout_nav_button).click()