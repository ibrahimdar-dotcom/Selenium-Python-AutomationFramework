from selenium.webdriver.common.by import By

class LoginPage:

    __login_title = "//div[@class='login-form']/h2"
    __email_textbox = "//*[@data-qa='login-email']"
    __password_textbox = "//*[@data-qa='login-password']"
    __login_button = "//*[@data-qa='login-button']"

    def __init__(self, driver):
        self.__driver = driver

    def getLoginTitle(self):
        return self.__driver.find_element(By.XPATH, self.__login_title).text

    def setEmail(self, email):
        self.__driver.find_element(By.XPATH, self.__email_textbox).clear()
        self.__driver.find_element(By.XPATH, self.__email_textbox).send_keys(email)

    def setPassword(self, password):
        self.__driver.find_element(By.XPATH, self.__password_textbox).clear()
        self.__driver.find_element(By.XPATH, self.__password_textbox).send_keys(password)

    def clickLoginButton(self):
        self.__driver.find_element(By.XPATH, self.__login_button).click()