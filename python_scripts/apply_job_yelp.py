from selenium import webdriver
import time
import os

def automate_job_application(link, browser):
	browser.implicitly_wait(10)
	browser.get(link);
	browser.switch_to_frame("jobviteframe");
	browser.find_element_by_xpath("//div[@class='apply-button']//a").click()
	browser.find_element_by_name("jvfirstname").send_keys("Kevin");
	browser.find_element_by_name("jvlastname").send_keys("Jonaitis");
	browser.find_element_by_name("jvfld-x-sV9Vfwb").send_keys("Irvine"); # City
	browser.find_element_by_xpath("//select[@name='jvfld-x-XV9VfwG']/option[@value='California']").click()
	browser.find_element_by_xpath("//select[@name='jvfld-x-uV9Vfwd']/option[@value='United States']").click()
	browser.find_element_by_name("jvemail").send_keys("kevitis117@gmail.com");
	browser.find_element_by_name("jvphone").send_keys("17145558294");
	browser.find_element_by_xpath("//select[@name='jvworkstatus']/option[@value='I have the unrestricted right to work in the U.S.']").click()
	browser.find_element_by_name("ImportResume").click()
	browser.switch_to_frame("File1");
	browser.find_element_by_name("File").send_keys(os.getcwd() + "/resume.txt");
	browser.switch_to_default_content();
	browser.switch_to_frame("jobviteframe");
	browser.find_element_by_xpath("//input[@value='Upload']").click()
	time.sleep(2)



fp = webdriver.FirefoxProfile()
fp.add_extension(extension='/Users/appjam/Documents/adblock_plus.xpi')
profile = webdriver.FirefoxProfile('/Users/appjam/Library/Application Support/Firefox/Profiles/9hr6jd2y.OkCupid')
browser = webdriver.Firefox(firefox_profile=profile)
browser.implicitly_wait(10)
browser.set_page_load_timeout(20)
#browser = webdriver.Firefox();
browser.get("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=q6X9VfwR&cs=924aVfwV&nl=0&jvresize=http://www.yelp.com/html/jobvite.html")
#browser.switch_to_frame("jobviteframe");
links = browser.find_elements_by_xpath("//table[1]//tbody//tr//td//a");
text_links = []
for link in links:
        job_link = link.get_attribute("href")
	text_links.append(job_link)
print text_links
for link in text_links:       
	automate_job_application(link,browser)
