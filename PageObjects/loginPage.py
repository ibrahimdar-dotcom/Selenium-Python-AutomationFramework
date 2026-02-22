from selenium.webdriver.common.by import By

class Login:

    __username_textbox = "//input[@id='user-name']"
    __password_textbox = "//input[@id='password']"
    __login_button = "//input[@id='login-button']"
    __app_logo_title = "//div[@class='primary_header']//div[@class='app_logo']"
    __validation_msg = "//div[contains(@class, 'error-message-container')]/h3"
    
    def __init__(self, driver):
        self.__driver = driver

    def setUsername(self,username):
        self.__driver.find_element(By.XPATH, self.__username_textbox).clear()
        self.__driver.find_element(By.XPATH, self.__username_textbox).send_keys(username)

    def setPassword(self,password):
        self.__driver.find_element(By.XPATH, self.__password_textbox).clear()
        self.__driver.find_element(By.XPATH, self.__password_textbox).send_keys(password)

    def clickLogin(self):
        self.__driver.find_element(By.XPATH, self.__login_button).click()

    def getAppTitle(self):
        return self.__driver.find_element(By.XPATH, self.__app_logo_title).text

    def getValidationMsg(self):
        return self.__driver.find_element(By.XPATH, self.__validation_msg).text