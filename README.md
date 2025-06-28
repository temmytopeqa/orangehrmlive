# orangehrmlive
Automating the web flow

OrangeHRM Automation Script
This Python script uses Selenium WebDriver to automate interactions with the OrangeHRM (Open Source) demo site. It performs a sequence of navigation steps through the Admin section after logging into the dashboard.

🧰 Requirements
Python 3.x

Google Chrome

ChromeDriver (Ensure it's compatible with your Chrome version and in your system PATH)

Selenium package

Install Selenium via pip:

bash
Copy
Edit
pip install selenium
🚀 What the Script Does
Launches Chrome and opens the OrangeHRM login page.

Logs in using the default demo credentials:

Username: Admin

Password: admin123

Navigates through the Admin module, visiting various pages like:

User Management

Job Titles, Pay Grades, Employment Status, Job Categories, Work Shifts

Organization info (General Info, Locations, Structure)

Qualifications (Skills, Education, Licenses, Languages, Memberships)

🗂️ Script Structure
python
Copy
Edit
# Setup and Configuration
username = "Admin"
password = "admin123"
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
pause = 5  # Pause between actions for page loading

# Login steps using CSS selectors

# Menu navigation using class names and XPath
# Each section is accessed by expanding menu tabs and clicking on links
⚠️ Notes
time.sleep() is used to pause between steps; this can be replaced with Selenium's WebDriverWait for better reliability.

Script assumes stable internet and consistent UI structure on the OrangeHRM demo site.

The script uses XPath and class-based selectors, which may break if the UI changes.

📌 Optional Features (Commented Out)
The script includes commented-out sections for:

Navigating to Nationalities

Accessing Corporate Branding

Opening Configuration settings

You can uncomment and run those parts as needed.

🧪 Usage
Run the script using:

bash
Copy
Edit
python script_name.py
Make sure Chrome and ChromeDriver are correctly installed and compatible.

📞 Support
If you encounter issues, ensure:

ChromeDriver matches your browser version.

Network access to the OrangeHRM demo site is available.

All required packages are installed.