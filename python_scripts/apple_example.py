from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://jobs.apple.com/us/search')
count = 0;

while(count < 10):
	browser.execute_script("pageNext()")

