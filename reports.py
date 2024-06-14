import time
import requests, json
from datetime import datetime, timedelta
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def reportsData(userId, hId, driver):

    try:
        ratePulse_TemplateReport = 'https://ratex.retvenslabs.com/Report/TemplateReport'
        driver.get(ratePulse_TemplateReport)
        print('Template Report Page Open Sucessfully')
    except TimeoutException:
        print("Template Report Page not Open")

    time.sleep(10)

    today = datetime.now()
    fromDate = today.strftime("%Y-%m-%d")

    TemplateReports = f'https://rxserver.retvenslabs.com/api/reports/getTemplateReports?userId={userId}&hId={hId}'

    response = requests.request("GET", TemplateReports)

    if response.status_code == 200:
        result = response.json()
        data_slot = result.get('data', {})
        
        if data_slot:
            print("Template Reports Data is Available")
        else:
            print("Template Reports Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    try:
        reportTable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.p-4.border-2.rounded-lg.cursor-pointer.bg-white.hover\\:pl-5'))
        )
        reportTable.click()
        print('Template Reports Table Opened Successfully')
    except TimeoutException:
        print("Template Reports Table not found")
    
    time.sleep(10)