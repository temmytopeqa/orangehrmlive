import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

 #Variables
username = "Admin"
password = "admin123"
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
pause = 5  # Pause time in seconds


driver.get(url) # Test URL
time.sleep(5)

#Log in page
driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(username)# UserName text field
time.sleep(pause)
driver.find_element(By.CSS_SELECTOR, "Input[name='password']").send_keys(password)# Password text field
time.sleep(pause)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()# Click Log in Button
time.sleep(pause)



#Landing Page - Select Admin
driver.find_element(By.CLASS_NAME, "oxd-main-menu-item").click()# Click Admin Button
time.sleep(pause)

#Admin - user management
driver.find_element(By.CLASS_NAME, "oxd-topbar-body-nav-tab").click()# Click User Management
time.sleep(pause)
#Admin>User management>Users
driver.find_element(By.CSS_SELECTOR, "ul.oxd-dropdown-menu").click()# Click users
time.sleep(pause)

#Admin - Job
driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab')]/span[contains(@class, 'oxd-topbar-body-nav-tab-item') and contains(text(), 'Job')]/i[contains(@class, 'bi-chevron-down')]").click()# Click Job
time.sleep(pause)
#Admin>Job>Job Titles
driver.find_element(By.XPATH,  "//li/a[contains(@class, 'oxd-topbar-body-nav-tab-link')]").click()# Click Job Titles
time.sleep(pause)

#Admin>Job>pay grades
driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab')]/span[contains(@class, 'oxd-topbar-body-nav-tab-item') and contains(text(), 'Job')]/i[contains(@class, 'bi-chevron-down')]").click()# Click Admin Button
time.sleep(pause)
driver.find_element(By.XPATH,  "//a[contains(@class, 'oxd-topbar-body-nav-tab-link') and text()='Pay Grades']").click()
time.sleep(pause)

#Admin>Job>Employment Status
driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab')]/span[contains(@class, 'oxd-topbar-body-nav-tab-item') and contains(text(), 'Job')]/i[contains(@class, 'bi-chevron-down')]").click()# Click Admin Button
time.sleep(pause)
driver.find_element(By.XPATH,  "//li/a[@role='menuitem' and contains(@class, 'oxd-topbar-body-nav-tab-link') and text()='Employment Status']").click()
time.sleep(pause)

#Admin>Job>Job categories
driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab')]/span[contains(@class, 'oxd-topbar-body-nav-tab-item') and contains(text(), 'Job')]/i[contains(@class, 'bi-chevron-down')]").click()# Click Admin Button
time.sleep(pause)
driver.find_element(By.XPATH,  "//a[contains(@class, 'oxd-topbar-body-nav-tab-link') and text()='Job Categories']").click()
time.sleep(pause)

##Admin>Job>Work shifts
driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab')]/span[contains(@class, 'oxd-topbar-body-nav-tab-item') and contains(text(), 'Job')]/i[contains(@class, 'bi-chevron-down')]").click()# Click Admin Button
time.sleep(pause)
driver.find_element(By.XPATH,  "//a[text()='Work Shifts']").click()
time.sleep(pause)

##Admin>Organisation
driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab') and span[contains(text(), 'Organization')]]").click()# Click Organisation
time.sleep(pause)
driver.find_element(By.XPATH, "//a[text()='General Information']").click()# Click General Information
time.sleep(pause)
driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab') and span[contains(text(), 'Organization')]]").click()# Click Organisation
time.sleep(pause)
driver.find_element(By.XPATH, "//li/a[contains(text(), 'Locations')]").click()# Click Locations
time.sleep(pause)
driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab') and span[contains(text(), 'Organization')]]").click()# Click Organisation
time.sleep(pause)
driver.find_element(By.XPATH, "//li/a[text()='Structure']").click()# Click structure
time.sleep(pause)

#Admin - Qualification
driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab') and span[contains(text(), 'Qualifications')]]").click()# Click Qualification
time.sleep(pause)
driver.find_element(By.XPATH, "//li/a[text()='Skills']").click()# Click Skill
time.sleep(pause)
driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab') and span[contains(text(), 'Qualifications')]]").click()# Click Qualification
time.sleep(pause)
driver.find_element(By.XPATH, "//a[text()='Education']").click()# Click Qualification
time.sleep(pause)
driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab') and span[contains(text(), 'Qualifications')]]").click()# Click Qualification
time.sleep(pause)
driver.find_element(By.XPATH, "//a[text()='Licenses']").click()# Click Qualification
time.sleep(pause)
driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab') and span[contains(text(), 'Qualifications')]]").click()# Click Qualification
time.sleep(pause)
driver.find_element(By.XPATH, "//a[text()='Licenses']").click()# Click Licenses
time.sleep(pause)
driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab') and span[contains(text(), 'Qualifications')]]").click()# Click Qualification
time.sleep(pause)
driver.find_element(By.XPATH, "//a[text()='Languages']").click()# Click Languages
time.sleep(pause)
driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab') and span[contains(text(), 'Qualifications')]]").click()# Click Qualification
time.sleep(pause)
driver.find_element(By.XPATH, "//a[text()='Memberships']").click()# Click Memberships
time.sleep(pause)
driver.find_element(By.XPATH, "//li[contains(@class, 'oxd-topbar-body-nav-tab') and span[contains(text(), 'Qualifications')]]").click()# Click Qualification
time.sleep(pause)

#Admin - Nationalities
#driver.find_element(By.XPATH, "//li[@class='oxd-topbar-body-nav-tab --visited']//a[contains(@class, 'oxd-topbar-body-nav-tab-item') and text()='Nationalities']").click()
#time.sleep(pause)

#Admin - Corporate Branding
#driver.find_element(By.XPATH,  "//li[@class='oxd-topbar-body-nav-tab']/a[text()='Corporate Branding']").click()# Click Nationalities
#time.sleep(pause)

##Admin - Configuration
#driver.find_element(By.XPATH,  "//ul[@class='oxd-dropdown-menu']//a[contains(text(), 'Configuration')]").click()# Click Configuration
#time.sleep(pause)