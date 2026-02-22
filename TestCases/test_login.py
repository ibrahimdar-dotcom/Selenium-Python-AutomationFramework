from selenium import webdriver
import pytest
from PageObjects.loginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import Log_Generation

class TestLogin:

    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logging = Log_Generation
    logger = logging.log_setup()

    def test_login_valid(self, setup):
        self.logger.info("----------- TEST_LOGIN ---------")
        self.logger.info("-------- Verifying login with valid creds --------")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = Login(self.driver)
        self.login.setUsername(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()

        appTitle = self.login.getAppTitle()

        if appTitle == "Swag Labs":
            self.logger.info("-------- TEST_PASSED_Login_valid_creds --------")
            assert True
        else:
            self.logger.info("-------- TEST_FALIED_login_valid_creds ----------")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_valid_login.png")
            assert False

        self.driver.close()
        