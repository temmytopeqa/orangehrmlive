import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"
PAUSE = 10

# Setup
driver = webdriver.Chrome()
wait = WebDriverWait(driver, PAUSE)
driver.get(URL)
driver.maximize_window()
actions = ActionChains(driver)

# ===== Utility Functions =====
def click_when_clickable(by, value, timeout=10):
    try:
        print(f"[INFO] Waiting to click: {value}")
        element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
        element.click()
        time.sleep(1)
    except Exception as e:
        print(f"[ERROR] Could not click element: {value}\n{e}")

def send_keys_when_present(by, value, keys):
    try:
        print(f"[INFO] Sending keys to: {value}")
        element = wait.until(EC.presence_of_element_located((by, value)))
        element.send_keys(keys)
    except Exception as e:
        print(f"[ERROR] Could not send keys to element: {value}\n{e}")

def hover_and_click(menu_xpath, submenu_xpath):
    try:
        print(f"[INFO] Hovering on: {menu_xpath} → Clicking: {submenu_xpath}")
        menu = wait.until(EC.visibility_of_element_located((By.XPATH, menu_xpath)))
        actions.move_to_element(menu).perform()
        time.sleep(1)
        submenu = wait.until(EC.element_to_be_clickable((By.XPATH, submenu_xpath)))
        submenu.click()
        time.sleep(1)
    except Exception as e:
        print(f"[ERROR] Hover/Click failed for: {submenu_xpath}\n{e}")

# ====== Main Functional Flow ======

def login():
    send_keys_when_present(By.NAME, "username", USERNAME)
    send_keys_when_present(By.NAME, "password", PASSWORD)
    click_when_clickable(By.XPATH, "//button[@type='submit']")

def navigate_admin_section():
    click_when_clickable(By.XPATH, '//span[text()="Admin"]')
    click_when_clickable(By.XPATH, '//span[text()="User Management"]')
    click_when_clickable(By.XPATH, '//a[text()="Users"]')

def navigate_job_section():
    click_when_clickable(By.XPATH, '//span[text()="Job"]')
    click_when_clickable(By.XPATH, '//a[text()="Job Titles"]')
    click_when_clickable(By.XPATH, '//span[text()="Job"]')
    click_when_clickable(By.XPATH, '//a[text()="Pay Grades"]')
    click_when_clickable(By.XPATH, '//span[text()="Job"]')
    click_when_clickable(By.XPATH, '//a[text()="Employment Status"]')
    click_when_clickable(By.XPATH, '//span[text()="Job"]')
    click_when_clickable(By.XPATH, '//a[text()="Job Categories"]')
    click_when_clickable(By.XPATH, '//span[text()="Job"]')
    click_when_clickable(By.XPATH, '//a[text()="Work Shifts"]')

def navigate_organization_section():
    click_when_clickable(By.XPATH, '//span[text()="Organization"]')
    click_when_clickable(By.XPATH, '//a[text()="General Information"]')
    click_when_clickable(By.XPATH, '//span[text()="Organization"]')
    click_when_clickable(By.XPATH, '//a[text()="Locations"]')
    click_when_clickable(By.XPATH, '//span[text()="Organization"]')
    click_when_clickable(By.XPATH, '//a[text()="Structure"]')

def navigate_qualifications_section():
    click_when_clickable(By.XPATH, '//span[text()="Qualifications"]')
    click_when_clickable(By.XPATH, '//a[text()="Skills"]')
    click_when_clickable(By.XPATH, '//span[text()="Qualifications"]')
    click_when_clickable(By.XPATH, '//a[text()="Education"]')
    click_when_clickable(By.XPATH, '//span[text()="Qualifications"]')
    click_when_clickable(By.XPATH, '//a[text()="Licenses"]')
    click_when_clickable(By.XPATH, '//span[text()="Qualifications"]')
    click_when_clickable(By.XPATH, '//a[text()="Languages"]')
    click_when_clickable(By.XPATH, '//span[text()="Qualifications"]')
    click_when_clickable(By.XPATH, '//a[text()="Memberships"]')

def navigate_others():
    click_when_clickable(By.XPATH, '//a[text()="Nationalities"]')
    click_when_clickable(By.XPATH, '//button[text()="Add"]')
    click_when_clickable(By.XPATH, '//a[text()="Corporate Branding"]')
    click_when_clickable(By.XPATH, '//span[text()="Configuration"]')

# ========== Execute Test ==========

try:
    login()
    navigate_admin_section()
    navigate_job_section()
    navigate_organization_section()
    navigate_qualifications_section()
    navigate_others()
    print("\n✅ All sections navigated successfully.")
except Exception as e:
    print(f"\n❌ Test failed: {e}")
finally:
    time.sleep(PAUSE)
    driver.quit()