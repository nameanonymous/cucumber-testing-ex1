'''
Created on 2021/03/31

@author: Masaya Misaizu
'''
from selenium.webdriver.common.by import By

locator = {
    "sign_in": (By.CLASS_NAME, "login"),
    "contact_us": (By.ID,"contact-link"),
    "subject_head":(By.ID,"id_contact"),
    "email":(By.ID,"email"),
    "message":(By.ID,"message"),
    "check_success":(By.CLASS_NAME,"alert alert-success"),
    "create_acc_field": (By.ID, "email_create"),
    "create_acc_button": (By.ID, "SubmitCreate"),
    "gender": (By.ID, "id_gender1"),
    "first_name": (By.ID, "customer_firstname"),
    "last_name": (By.ID, "customer_lastname"),
    "password": (By.ID, "passwd"),
    "days": (By.ID, "days"),
    "months": (By.ID, "months"),
    "years": (By.ID, "years"),
    "newsletter_checkbox": (By.ID, "newsletter"),
    "optin_checkbox": (By.ID, "optin"),
    "address": (By.ID, "address1"),
    "city": (By.ID, "city"),
    "state": (By.ID, "id_state"),
    "postcode": (By.ID, "postcode"),
    "mobile": (By.ID, "phone_mobile"),
    "register_button": (By.ID, "submitAccount"),
    "logout": (By.XPATH, "//*[@id='header']/div[2]/div/div/nav/div[2]/a")
}
