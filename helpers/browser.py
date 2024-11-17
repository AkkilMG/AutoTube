# (c) 2022-2023, Akkil MG
# License: GNU General Public License v3.0
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

async def browser():
    try:
        chrome_options = Options()
        chrome_options.add_argument(r"--user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data")
        chrome_options.add_argument(r"--profile-directory=Profile 4")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return {'driver': driver, 'success': True}
    except Exception as e:
        print(f"Exception occurred (browser): {e}")
        return {'success': False}
