import pyperclip
import names
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
'chrome' or 'tor'
"""
browser = "chrome"

if browser == "chrome":
    from selenium.webdriver.chrome.options import Options
    options = webdriver.ChromeOptions() 
    options.add_argument(r"user-data-dir=C:\Users\loan nguyen\AppData\Local\Google\Chrome\User Data\Default") #Path to your chrome profile
##    w = webdriver.Chrome(executable_path="C:\\Users\\chromedriver.exe", chrome_options=options)
##    userProfile= "C:\Users\loan nguyen\AppData\Local\Google\Chrome\User Data\Default"
    driver = webdriver.Chrome(executable_path=r"D:\01_software\chromedriver_win32\chromedriver.exe", chrome_options=options)
elif browser == "tor":
    from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
    binary = FirefoxBinary(r'D:\01_software\Tor Browser\Browser\firefox.exe')
    profile = FirefoxProfile(r'D:\01_software\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default')
    driver = webdriver.Firefox(firefox_profile= profile, firefox_binary= binary)
     
def random_username(sex='female', no_of_digits=3):
    import random
    digits = random.randrange(100,1000) # interger from 100 to 999
    #first_name = names.get_first_name(gender=sex)
    fullname = names.get_full_name(gender=sex)
    return fullname.replace(" ","") + str(digits)
    

def get_new_email_online():
    driver.get("http://getairmail.com")
    try:
        driver.find_element_by_id("start_here").click() # new email
    except:
        driver.find_element_by_link_text('Change Email Address').click() # change to another email
    wait = WebDriverWait(driver, 10)
##    ### click 'Copy ToClipboard' button
##    element = wait.until(EC.presence_of_element_located((By.ID,"clipbtn")))
##    driver.find_element_by_id("clipbtn").click()
    ### copy directly from textbox
    element = wait.until(EC.presence_of_element_located((By.ID,"tempemail")))
    element.click()
    element.send_keys(Keys.CONTROL, 'a')
    element.send_keys(Keys.CONTROL, 'c')
##    import time
##    time.sleep(0.5)
    email = pyperclip.paste()
    return email
    
def signup_new_account(username, email, password):
##    driver.get("http://community.myfitnesspal.com/")
##    driver.find_element_by_link_text("Sign Up").click()
    # Step 1 of 3
    driver.get("https://www.myfitnesspal.com/account/create")
    try:
        driver.find_element_by_id("user_username").send_keys(username)
    except:
        pass
    driver.find_element_by_id("user_email").send_keys(email)
    driver.find_element_by_id("user_password").send_keys(password)
    driver.find_element_by_id("submit").click()

    # Step 2 of 3
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID,'weight_value_display_value')))
    driver.find_element_by_id("weight_value_display_value").send_keys("79")
    driver.find_element_by_id("profile_goal_weight_display_value").send_keys("63")
    from selenium.webdriver.support.ui import Select
    select = Select(driver.find_element_by_id('profile_dob_2i'))
    select.select_by_value("2")
    select = Select(driver.find_element_by_id('profile_dob_3i'))
    select.select_by_value("28")
    select = Select(driver.find_element_by_id('profile_dob_1i'))
    select.select_by_value("1988")
    driver.find_element_by_id("profile_zipcode").send_keys("700000")
    
    select = Select(driver.find_element_by_id('exercise_goal_times_per_week'))
    select.select_by_value("3")
    driver.find_element_by_id("exercise_goal_minutes_per_day").send_keys("30")
    try:
        driver.find_element_by_id("pp-consent-checkbox").click()
    except:
        pass
    driver.find_element_by_id("account-profile-submit").click()

    # Step 3 of 3
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.title_contains("Invite Your Friends"))
    driver.find_element_by_id("friends-invite-skip").click()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID,'get-started-now')))
    driver.find_element_by_id("get-started-now").click()

    # store created account to file
    with open("./emails.txt", "r+") as f:
        content = f.read()
        f.seek(0, 0)
        f.write(email + "\n" + content)
    

    driver.get("http://www.myfitnesspal.com/forums")
    driver.find_element_by_id("Form_Connect").click()

    # verify welcome email sent to mailbox
    
    

def autopost():
    with open("./postcontent.txt",'r',-1,encoding='utf-8') as rf:
        lines = rf.readlines()
        print(lines)

    
if __name__== '__main__':
##    email = get_new_email_online() ## 1
##    username = email.split('@')[0]
    username = random_username()
    email = username+("@gmail.com")
    password = "admin987"
    print(email)
    signup_new_account(username, email, password)  ## 2
##    autopost()
    
##    driver.quit()

#workflow
##1. register email
##2. sign up with new mail
##3. 
