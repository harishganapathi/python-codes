from selenium  import webdriver
browser = webdriver.Firefox()
web_page = input("enter the page to fill in the form")
browser.get(web_page)

if len(sys.argv) <= 1
    web_page = input("enter the page to fill in the form")
    browser.get(web_page)
	username = browser.find_element_by_id('usernameId')
	email = input('enter the username')
	username.send_keys(email)
#password
	password = browser.find_element_by_name('j_password')
	passkey = input('enter you password')
	password.send_keys(passkey)
#captcha
	captcha = browser.find_element_by_name('nlpAnswer')
	captcha_inp = input('enter the captcha')
	captcha.send_keys(captcha_inp)
#login
	login = browser.find_element_by_id('loginbutton')
	login.click()
elif:
    web_page = input("enter the page to fill in the form")
    browser.get(sys.argv[1])
    username = browser.find_element_by_id('usernameId')
	email = input('enter the username')
	username.send_keys(sys.argv[2])
#password
	password = browser.find_element_by_name('j_password')
	passkey = input('enter you password')
	password.send_keys(sys.argv[3])
#captcha
	captcha = browser.find_element_by_name('nlpAnswer')
	captcha_inp = input('enter the captcha')
	captcha.send_keys(sys.argv[4])
#login
	login = browser.find_element_by_id('loginbutton')
	login.click()
