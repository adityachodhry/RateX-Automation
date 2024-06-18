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
    endDate = (today + timedelta(days=1)).strftime("%Y-%m-%d")

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
        quarterlyReportTable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div#quarep.p-4.border-2.rounded-lg.cursor-pointer.bg-white.hover\\:pl-5'))
        )
        quarterlyReportTable.click()
        print('Quarterly Reports Table Opened Successfully')
    except TimeoutException:
        print("Quarterly Reports Table not found")
    
    time.sleep(10)

    reportsData = f'https://rxserver.retvenslabs.com/api/reports/getQuarterlyReport?userId={userId}&hId={hId}&startDate={fromDate}&endDate={endDate}&whatsAppNotify=false'

    response_1 = requests.request("GET", reportsData)

    if response.status_code == 200:
        result_1 = response_1.json()
        data_slot_1 = result_1.get('data', {})
        
        if data_slot_1:
            print("Quarterly Reports Data is Available")
        else:
            print("Quarterly Reports Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    # try:
    #     backButton = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.bg-[#3361FF].w-fit.flex.items-center.justify-center.cursor-pointer.rounded-lg.h-[36px].py-1.px-3'))
    #     )
    #     backButton.click()
    #     print("Back Successfully")
    # except TimeoutException:
    #     print("No Back Button found")

    # time.sleep(3)

    # try:
    #     monthReportTable = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, 'div#moenrep.p-4.border-2.rounded-lg.cursor-pointer.bg-white.hover\\:pl-5'))
    #     )
    #     monthReportTable.click()
    #     print('Month End Report Table Opened Successfully')
    # except TimeoutException:
    #     print("Month End Report Table not found")
    
    # time.sleep(10)

    # try:
    #     yearReportTable = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, 'div#yeenrep.p-4.border-2.rounded-lg.cursor-pointer.bg-white.hover\\:pl-5'))
    #     )
    #     yearReportTable.click()
    #     print('Year End Report Table Opened Successfully')
    # except TimeoutException:
    #     print("Year End Report Table not found")
    
    # time.sleep(10)

    # try:
    #     parityReportTable = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, 'div#parrep.p-4.border-2.rounded-lg.cursor-pointer.bg-white.hover\\:pl-5'))
    #     )
    #     parityReportTable.click()
    #     print('Parity Report Table Opened Successfully')
    # except TimeoutException:
    #     print("Parity Report Table not found")
    
    # time.sleep(10)

    # try:
    #     paceReportTable = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, 'div#parep.p-4.border-2.rounded-lg.cursor-pointer.bg-white.hover\\:pl-5'))
    #     )
    #     paceReportTable.click()
    #     print('Pace Report Table Opened Successfully')
    # except TimeoutException:
    #     print("Pace Report Table not found")
    
    # time.sleep(10)

    # try:
    #     sourceReportTable = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, 'div#sourep.p-4.border-2.rounded-lg.cursor-pointer.bg-white.hover\\:pl-5'))
    #     )
    #     sourceReportTable.click()
    #     print('Source Report Table Opened Successfully')
    # except TimeoutException:
    #     print("Source Report Table not found")
    
    # time.sleep(10)

    # try:
    #     revenueReportTable = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, 'div#revrep.p-4.border-2.rounded-lg.cursor-pointer.bg-white.hover\\:pl-5'))
    #     )
    #     revenueReportTable.click()
    #     print('Revenue Report Table Opened Successfully')
    # except TimeoutException:
    #     print("Revenue Report Table not found")
    
    # time.sleep(10)