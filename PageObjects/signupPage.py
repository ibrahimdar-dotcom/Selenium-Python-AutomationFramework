from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SignUpPage:

    __signup_title = "//div[@class='signup-form']/h2"
    __name_textbox = "//*[@data-qa='signup-name']"
    __email_textbox = "//*[@data-qa='signup-email']"
    __signup_button = "//*[@data-qa='signup-button']"
    __form_title = "//div[@class='login-form']/h2/b"
    __title_male_radio = "//input[@id='id_gender1']"
    __title_female_radio = "//input[@id='id_gender2']"
    __form_name_textbox = "//*[@data-qa='name']"
    __form_email_textbox = "//*[@data-qa='email']"
    __day_selector = "//*[@data-qa='days']"
    __month_selector = "//*[@data-qa='months']"
    __year_selector = "//*[@data-qa='years']"
    __newsletter_checkbox = "//*[@id='newsletter']"
    __offers_checkbox = "//*[@id='optin']"
    __first_name_textbox = "//*[@data-qa='first_name']"
    __last_name_textbox = "//*[@data-qa='last_name']"
    __company_textbox = "//*[@data-qa='company']"
    __address1_textbox = "//*[@data-qa='address']"
    __address2_textbox = "//*[@data-qa='address2']"
    __country_selector = "//*[@data-qa='country']"
    __state_textbox = "//*[@data-qa='state']"
    __city_textbox = "//*[@data-qa='city']"
    __zipcode_textbox = "//*[@data-qa='zipcode']"
    __mobile_textbox = "//*[@data-qa='mobile_number']"
    __acct_creation_button = "//*[@data-qa='create-account']"
    __acct_creation_text = "//*[@data-qa='account-created']/b"
    __cont_button = "//*[@data-qa='continue-button']"
    __acct_delete_text = "//*[@data-qa='account-deleted']/b"
    __duplicate_signup_validation = "//form[contains(@action, 'signup')]//p"

    def __init__(self, driver):
        self.__driver = driver

    def getSignupTitle(self):
        return self.__driver.find_element(By.XPATH, self.__signup_title).text
    
    def setName(self,username):
        self.__driver.find_element(By.XPATH, self.__name_textbox).clear()
        self.__driver.find_element(By.XPATH, self.__name_textbox).send_keys(username)

    def setEmail(self,email):
        self.__driver.find_element(By.XPATH, self.__email_textbox).clear()
        self.__driver.find_element(By.XPATH, self.__email_textbox).send_keys(email)

    def clickSignup(self):
        self.__driver.find_element(By.XPATH, self.__signup_button).click()

    def getFormTitle(self):
        return self.__driver.find_element(By.XPATH, self.__form_title).text
    
    def setTitlegender(self,title_gender):
        if title_gender.contains("Mr"):
            self.__driver.find_element(By.XPATH, self.__title_male_radio).click()
        else:
            self.__driver.find_element(By.XPATH, self.__title_female_radio).click()

    def getName(self):
        return self.__driver.find_element(By.XPATH, self.__form_name_textbox).text

    def getEmail(self):
        return self.__driver.find_element(By.XPATH, self.__form_email_textbox).text
    
    def setDay(self,day):
        day_selector = Select(self.__driver.find_element(By.XPATH, self.__day_selector))
        day_selector.select_by_visible_text(day)
    
    def setMonth(self,month):
        month_selector = Select(self.__driver.find_element(By.XPATH, self.__month_selector))
        month_selector.select_by_visible_text(month)

    def setYear(self,year):
        year_selector = Select(self.__driver.find_element(By.XPATH, self.__year_selector))
        year_selector.select_by_visible_text(year)

    def setNewsletter(self):
        self.__driver.find_element(By.XPATH, self.__newsletter_checkbox).click()

    def setOffers(self):
        self.__driver.find_element(By.XPATH, self.__offers_checkbox).click()

    def setFirstName(self,first_name):
        self.__driver.find_element(By.XPATH, self.__first_name_textbox).clear()
        self.__driver.find_element(By.XPATH, self.__first_name_textbox).send_keys(first_name)

    def setLastName(self,last_name):
        self.__driver.find_element(By.XPATH, self.__last_name_textbox).clear()
        self.__driver.find_element(By.XPATH, self.__last_name_textbox).send_keys(last_name)

    def setCompany(self,company):
        self.__driver.find_element(By.XPATH, self.__company_textbox).clear()
        self.__driver.find_element(By.XPATH, self.__company_textbox).send_keys(company)

    def setAddress1(self,address1):
        self.__driver.find_element(By.XPATH, self.__address1_textbox).clear()
        self.__driver.find_element(By.XPATH, self.__address1_textbox).send_keys(address1)

    def setAddress2(self,address2):
        self.__driver.find_element(By.XPATH, self.__address2_textbox).clear()
        self.__driver.find_element(By.XPATH, self.__address2_textbox).send_keys(address2)

    def setCountry(self,country):
        country_selector = Select(self.__driver.find_element(By.XPATH, self.__country_selector))
        country_selector.select_by_visible_text(country)

    def setState(self,state):
        self.__driver.find_element(By.XPATH, self.__state_textbox).clear()
        self.__driver.find_element(By.XPATH, self.__state_textbox).send_keys(state)

    def setCity(self,city):
        self.__driver.find_element(By.XPATH, self.__city_textbox).clear()
        self.__driver.find_element(By.XPATH, self.__city_textbox).send_keys(city)

    def setZipcode(self,zipcode):
        self.__driver.find_element(By.XPATH, self.__zipcode_textbox).clear()
        self.__driver.find_element(By.XPATH, self.__zipcode_textbox).send_keys(zipcode)

    def setMobile(self,mobile):
        self.__driver.find_element(By.XPATH, self.__mobile_textbox).clear()
        self.__driver.find_element(By.XPATH, self.__mobile_textbox).send_keys(mobile)

    def clickCreateAcct(self):
        self.__driver.find_element(By.XPATH, self.__acct_creation_button).click()
    
    def getAcctCreationText(self):
        return self.__driver.find_element(By.XPATH, self.__acct_creation_text).text
    
    def clickContinue(self):
        self.__driver.find_element(By.XPATH, self.__cont_button).click()
    
    def getLoggedInUsername(self):
        return self.__driver.find_element(By.XPATH, self.__logged_in_username).text
    
    def clickDeleteAccount(self):
        self.__driver.find_element(By.XPATH, self.__delete_account_button).click()

    def getAcctDeleteText(self):
        return self.__driver.find_element(By.XPATH, self.__acct_delete_text).text

    def clickLogout(self):
        self.__driver.find_element(By.XPATH, self.__logout_button).click()

    def getDuplicateSignupValidationMsg(self):
        return self.__driver.find_element(By.XPATH, self.__duplicate_signup_validation).text