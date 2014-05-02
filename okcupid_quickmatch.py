from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def click_5_stars():
        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        base_url = "http://www.okcupid.com/"
        verificationErrors = []
        accept_next_alert = True

        driver.get(base_url)
        driver.find_element_by_id("open_sign_in_button").click()
        driver.find_element_by_id("login_username").clear()
        driver.find_element_by_id("login_username").send_keys("Kevin117007")
        driver.find_element_by_id("login_password").clear()
        driver.find_element_by_id("login_password").send_keys("123456")
        driver.find_element_by_id("sign_in_button").click()
        driver.find_element_by_link_text("Quickmatch").click()
        clicked = 0
        while(clicked < 10000):
            #driver.find_element_by_xpath("(//ul[@id='stars']//li)[4]").click()
            driver.find_element_by_xpath('//*[@id="stars"]/li[4]/a').click()
            clicked = clicked + 1
            time.sleep(1)

        driver.quit()

click_5_stars()
