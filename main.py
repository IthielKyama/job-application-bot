from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3997498524&f_AL=true&keywords=python%20developer"
           "&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

time.sleep(2)
sign_in = driver.find_element(By.LINK_TEXT, 'Sign in')
sign_in.click()

time.sleep(2)
email = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
email.send_keys(EMAIL)
password.send_keys(PASSWORD)

time.sleep(2)
submit_btn = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
submit_btn.click()

input("Press ENTER when you have completed the captcha")
time.sleep(5)
job_list = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')

for job in job_list:
    job.click()
    time.sleep(2)
    try:
        save_btn = driver.find_element(By.CSS_SELECTOR, '.jobs-save-button')
        save_btn.click()
    except NoSuchElementException:
        continue
