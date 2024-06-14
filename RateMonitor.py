import time
import requests, json
from datetime import datetime, timedelta
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def rateMonitor(userId, hId, driver):

    try:
        ratePulse_rate_monitor = 'https://ratex.retvenslabs.com/rate-pulse/rate_monitor'
        driver.get(ratePulse_rate_monitor)
        print('Rate Monitor Page Open Sucessfully')
    except TimeoutException:
        print('Rate Monitor not Open')

    time.sleep(10)

    today = datetime.now()
    fromDate = today.strftime("%Y-%m-%d")

    todayRate = f'https://rxserver.retvenslabs.com/api/dashboard/todayRate?hId={hId}&userId={userId}'

    response = requests.request("GET", todayRate)

    if response.status_code == 200:
        result = response.json()
        data_slot = result.get('data', {})
        
        if data_slot:
            print("Rate Monitor Today Rate Data is Available")
        else:
            print("Rate Monitor Today Rate Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    rateTendencies = f'https://rxserver.retvenslabs.com/api/dashboard/rateTendencies?hId={hId}&userId={userId}&startDate={fromDate}&otaId=1'

    response_1 = requests.request("GET", rateTendencies)

    if response.status_code == 200:
        result_1 = response_1.json()
        data_slot_1 = result_1.get('data', {})
        
        if data_slot_1:
            print("Rate Monitor Rate Tendencies Data is Available")
        else:
            print("Rate Monitor Rate Tendencies Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    

    ratesMonitor = f'https://rxserver.retvenslabs.com/api/dashboard/ratesMonitor?otaId=1&hId={hId}&userId={userId}&startDate={fromDate}'

    response_2 = requests.request("GET", ratesMonitor)

    if response.status_code == 200:
        result_2 = response_2.json()
        data_slot_2 = result_2.get('data', {})
        
        if data_slot_2:
            print("Rate Monitor Overview Data is Available")
        else:
            print("Rate Monitor Overview Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    DropDownList = f'https://rxserver.retvenslabs.com/api/userDashboardSetting/getDropDownList?hId={hId}&userId={userId}'

    response_3 = requests.request("GET", DropDownList)

    if response.status_code == 200:
        result_3 = response_3.json()
        data_slot_3 = result_3.get('data', {})
        
        if data_slot_3:
            print("Rate Monitor DropDown List Data is Available")
        else:
            print("Rate Monitor DropDown List Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    priceTrend = f'https://rxserver.retvenslabs.com/api/dashboard/priceTrend?hId={hId}&userId={userId}&startDate={fromDate}&otaId=7'

    response_4 = requests.request("GET", priceTrend)

    if response.status_code == 200:
        result_4 = response_4.json()
        data_slot_4 = result_4.get('data', {})
        
        if data_slot_4:
            print("Rate Monitor Price Trend Data is Available")
        else:
            print("Rate Monitor Price Trend Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")