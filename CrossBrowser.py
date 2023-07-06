import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

class CrossBrowser:
    def __init__(self, driver):
        self.driver = driver

    def cross_browser(self):
        # Open the website and maximize the window
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.maximize_window()

        print("Test case started")

        # Name field
        first_name = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.ID, 'firstName')))
        first_name.send_keys("SQA")

        last_name = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.ID, 'lastName')))
        last_name.send_keys("testing")

        user_email = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.ID, 'userEmail')))
        user_email.send_keys("sqa@yopmail.com")

        gender_radio = self.driver.find_element(By.XPATH, "//label[contains(text(),'Male')]")
        self.driver.execute_script('arguments[0].click()', gender_radio)

        user_number = self.driver.find_element(By.ID, 'userNumber')
        user_number.send_keys("1234567890")

        dob = self.driver.find_element(By.ID, 'dateOfBirthInput')
        self.driver.execute_script('arguments[0].click()', dob)

        # Calendar popup
        select_month = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
        select_month.select_by_index(1)
        time.sleep(1)

        select_year = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
        select_year.select_by_value('1996')
        time.sleep(1)

        select_day = self.driver.find_element(By.CLASS_NAME, "react-datepicker__day--007")
        self.driver.execute_script('arguments[0].click()', select_day)

        subject = self.driver.find_element(By.ID, 'subjectsInput')
        subject.send_keys('Computer Science')
        subject.send_keys(Keys.RETURN)

        hobbies = self.driver.find_element(By.XPATH, "//label[contains(text(),'Sports')]")
        self.driver.execute_script('arguments[0].click()', hobbies)

        upload_pic = self.driver.find_element(By.ID, 'uploadPicture')
        upload_pic.send_keys("//Users//mac//Downloads//sale.png")

        current_address = self.driver.find_element(By.ID, 'currentAddress')
        current_address.send_keys('Rawalpindi, Isb')

        #self.driver.execute_script("document.body.style.zoom='50%'")

        submit_btn = self.driver.find_element(By.XPATH, "//button[@id='submit']")
        self.driver.execute_script('arguments[0].click()', submit_btn)

        time.sleep(2)

        close_btn = self.driver.find_element(By.ID, 'closeLargeModal')
        self.driver.execute_script('arguments[0].click()', close_btn)

        time.sleep(2)

        print("Test case completed")


# Instantiate Chrome WebDriver
chrome_service = ChromeService(ChromeDriverManager().install())
# Add any desired Chrome options if needed
chrome_driver = webdriver.Chrome(service=chrome_service)
submit_form = CrossBrowser(chrome_driver)
submit_form.cross_browser()
chrome_driver.quit()

# Instantiate Firefox WebDriver
firefox_driver = webdriver.Firefox()
submit_form = CrossBrowser(firefox_driver)
submit_form.cross_browser()
firefox_driver.quit()

safari= webdriver.Safari()
submit_form = CrossBrowser(safari)
submit_form.cross_browser()
safari.quit()