# A automate software for all the students who didn't get up early in the morning for the classes

# @author: "vidit"

from selenium import webdriver
from getpass import getpass
import time

username = 'viditvarshney222@gmail.com'
# username = input("Enter your email id")

password = 'Vidit@#1234'
# password = getpass("Enter your password")

driver = webdriver.Chrome("/home/vidit/WebDriver/chromedriver")

driver.get("https://zoom.us/signin")
time.sleep(3)

username_textbox = driver.find_element_by_id("email")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(password)

login_button = driver.find_element_by_css_selector('#login-form > div:nth-child(3) > div > div.signin > a')
login_button.submit()



# Now joining a meeting 

join_meeting = driver.find_element_by_id("btnJoinMeeting")
join_meeting.click()


# meeting_number = ''
meeting_number = input("Enter your Meeting Id: ")

meeting_id = driver.find_element_by_id("join-confno")
meeting_id.send_keys(meeting_number)

join_button = driver.find_element_by_id("btnSubmit")
join_button.click()
