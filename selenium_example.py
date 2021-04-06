'''
Created on 2021/03/31

@author: Masaya Misaizu
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from locators import locator
from csv import reader
import random
from selenium.webdriver.support.ui import Select
from idlelib.idle_test.test_textview import ButtonClickTest

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("http://automationpractice.com/")
driver.maximize_window()

with open('testdata.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=';')
    for row in csvreader:
        
        assert driver.find_element(*locator["contact_us"]).is_displayed()
        driver.find_element(*locator["contact_us"]).click()
        
        select = Select(driver.find_element(*locator["subject_head"]))
        print(row[12])
        select.select_by_value(row[12])
        
        driver.find_element(*locator["email"]).send_keys(row[0])
    
        driver.find_element(*locator["message"]).send_keys(row[13])

        assert driver.find_element(*locator["check_success"]).is_displayed()
                
        assert driver.find_element(*locator["sign_in"]).is_displayed()
        driver.find_element(*locator["sign_in"]).click()

        driver.find_element(*locator["create_acc_field"]).send_keys(str(random.randint(0,1000000))+row[0])

        driver.find_element(*locator["create_acc_button"]).click()

        assert driver.title == "Login - My Store"

        driver.find_element(*locator["first_name"]).send_keys(row[1])

        driver.find_element(*locator["last_name"]).send_keys(row[2])

        driver.find_element(*locator["password"]).send_keys(row[3])

        select = Select(driver.find_element(*locator["days"]))
        select.select_by_value(row[4])

        select = Select(driver.find_element(*locator["months"]))
        select.select_by_value(row[5])

        select = Select(driver.find_element(*locator["years"]))
        select.select_by_value(row[6])

        driver.find_element(*locator["newsletter_checkbox"]).click()
        driver.find_element(*locator["optin_checkbox"]).click()

        driver.find_element(*locator["address"]).send_keys(row[7])

        driver.find_element(*locator["city"]).send_keys(row[8])
    
        select = Select(driver.find_element(*locator["state"]))
        select.select_by_visible_text(row[9])

        driver.find_element(*locator["postcode"]).send_keys(row[10])

        driver.find_element(*locator["mobile"]).send_keys(row[11])

        driver.find_element(*locator["register_button"]).click()

        assert driver.title == "My account - My Store"
    
        driver.find_element(*locator["logout"]).click()

driver.quit()
