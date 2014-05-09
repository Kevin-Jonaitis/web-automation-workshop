from selenium import webdriver
import time
from selenium.webdriver.common.proxy import *

def click_5_stars():

	fp = webdriver.FirefoxProfile()
	fp.add_extension(extension='/Users/appjam/Documents/adblock_plus.xpi')
	profile = webdriver.FirefoxProfile('/Users/appjam/Library/Application Support/Firefox/Profiles/9hr6jd2y.OkCupid')
	driver = webdriver.Firefox(firefox_profile=profile)
	driver.delete_all_cookies()
	#driver = webdriver.Chrome()
        base_url = "http://www.okcupid.com/"	
	driver.implicitly_wait(10)
        
	driver.get(base_url + "logout")
#        driver.delete_all_cookies()
	driver.get(base_url)
	driver.find_element_by_id("open_sign_in_button").click()
        driver.find_element_by_id("login_username").clear()
        driver.find_element_by_id("login_username").send_keys("TDogSchmosby")
        driver.find_element_by_id("login_password").clear()
        driver.find_element_by_id("login_password").send_keys("1qaz2wsx3edc")
        driver.find_element_by_id("sign_in_button").click()
#	driver.refresh()
#	driver.execute_script("window.stop()")	
	time.sleep(2)
	driver.get(base_url + "quickmatch")
       
	clicked = 0
        while(clicked < 10000):
			driver.find_element_by_xpath('//button[@id="quickmatch-like"]').click()
	    		print "clicked star"
			clicked = clicked + 1
			time.sleep(1)			
        driver.quit()

click_5_stars()
