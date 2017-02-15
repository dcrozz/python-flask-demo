#  from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


#  display = Display(visible=0, size=(1024, 768))
#  display.start()

browser = webdriver.Firefox()

home_url = 'http://localhost:5000'

browser.get(home_url)

username = browser.find_element_by_id('username')
passwd = browser.find_element_by_id('password')
signin = browser.find_element_by_id('submit')

username.send_keys('admin')
passwd.send_keys('admin')
signin.send_keys(Keys.RETURN)

assert browser.title == 'Home - microblog'

post1 = browser.find_element_by_id('post')
post1.send_keys('hello world1' + Keys.RETURN)
sleep(1)
post2 = browser.find_element_by_id('post')
post2.send_keys('hello world2' + Keys.RETURN)
browser.get( home_url + '/user/admin' )
newest_post = browser.find_element_by_xpath("/html/body/div[@class='container']/table[@class='table table-hover'][1]/tbody/tr/td[2]/p[2]/strong/span")
assert 'hello world2' == newest_post.text

delete = browser.find_element_by_xpath("/html/body/div[@class='container']/table[@class='table table-hover'][1]/tbody/tr/td[2]/p[1]/span/a")
delete.click()

assert browser.title == 'Home - microblog'
