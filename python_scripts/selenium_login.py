from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://rocky-brook-8124.herokuapp.com/signup.html')
username_element = browser.find_element_by_name("username");
username_element.send_keys("testUser");

password_element = browser.find_element_by_name("password");
password_element.send_keys("12345");

submitButton = browser.find_element_by_xpath("//input[@value='Signup!']");
submitButton.click();