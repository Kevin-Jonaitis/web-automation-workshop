from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('http://rocky-brook-8124.herokuapp.com/signup.html')
username_element = browser.find_element_by_name("username");
username_element.send_keys("testUser");

time.sleep(1);
password_element = browser.find_element_by_name("password");
password_element.send_keys("12345");

time.sleep(1);
submitButton = browser.find_element_by_xpath("//input[@value='Signup!']");
time.sleep(1);
submitButton.click();
