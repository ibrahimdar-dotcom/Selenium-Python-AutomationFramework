from selenium import webdriver
import pytest
import time
from PageObjects.loginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import Log_Generation
from Utilities import XLUtil

class TestLogin:

    baseURL = ReadConfig.getAppURL()
    path = ".\\TestData\\loginData.xlsx"

    logging = Log_Generation
    logger = logging.log_setup()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_valid(self, setup):
        self.logger.info("----------- TEST_LOGIN ---------")
        self.logger.info("-------- Verifying login with valid credentials --------")
        self.driver = setup    
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.login = Login(self.driver)
        
        self.rows = XLUtil.getRowCount(self.path, 'Sheet1')
        
        for row in range(2, self.rows+1):
            self.login.setUsername(XLUtil.readCellData(self.path,'Sheet1',row,1))
            self.login.setPassword(XLUtil.readCellData(self.path,'Sheet1',row,2))
            self.login.clickLogin()
            expected = XLUtil.readCellData(self.path,'Sheet1',row,3) 

            appTitle = self.login.getAppTitle()

            if appTitle == expected:
                self.logger.info("-------- Test Case: " + str(int(row - 1)) + " PASSED --------")
                assert True
            else:
                self.logger.info("-------- Test Case: " + str(int(row - 1)) + " FAILED --------")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_" + str(int(row + 1)) + "valid_login.png")
                assert False

        self.driver.close()


    @pytest.mark.regression
    def test_login_invalid(self, setup):
        self.logger.info("-------- Verifying login with invalid credetials --------")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.login = Login(self.driver)

        self.rows = XLUtil.getRowCount(self.path, 'Sheet2')
        
        for row in range(2, self.rows+1):
            self.driver.refresh()
            try:
                self.login.setUsername(XLUtil.readCellData(self.path, 'Sheet2', row, 1))
            except TypeError:
                print("Username field is empty")
            
            try:
                self.login.setPassword(XLUtil.readCellData(self.path, 'Sheet2', row, 2))
            except TypeError:
                print("Password field is empty")
            finally:
                self.login.clickLogin()

            expected_msg = XLUtil.readCellData(self.path, 'Sheet2', row, 3)
            actual_msg = self.login.getValidationMsg()
            
            if actual_msg == expected_msg:
                self.logger.info("-------- Test Case: " + str(int(row - 1)) + " PASSED --------")
                assert True
            else:
                self.logger.info("-------- Test Case: " + str(int(row - 1)) + " FAILED --------")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_" + str(int(row + 1)) + "invalid_login.png")
                assert False

        self.driver.close()
