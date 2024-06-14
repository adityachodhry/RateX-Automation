import time
import requests, json
from datetime import datetime, timedelta
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def ratePulseDashboard(userId, hId, driver):

    try:
        ratePulse_dashboard_url = 'https://ratex.retvenslabs.com/rate-pulse/dashboard'
        driver.get(ratePulse_dashboard_url)
        print('Rate Pulse Dashboard Page Open Sucessfully')
    except TimeoutException:
        print("Rate Pulse Dashboard Page not Open")

    time.sleep(10)

    today = datetime.now()
    fromDate = today.strftime("%Y-%m-%d")

    todayRate = f'https://rxserver.retvenslabs.com/api/dashboard/todayRate?hId={hId}&userId={userId}'

    response = requests.request("GET", todayRate)

    if response.status_code == 200:
        result = response.json()
        data_slot = result.get('data', {})
        
        if data_slot:
            print("Rate Pulse Today Rate Data is Available")
        else:
            print("Rate Pulse Today Rate Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    

    rateParityOverview = f'https://rxserver.retvenslabs.com/api/dashboard/rateParityOverview?hId={hId}&userId={userId}'

    response_1 = requests.request("GET", rateParityOverview)

    if response.status_code == 200:
        result_1 = response_1.json()
        data_slot_1 = result_1.get('data', {})
        
        if data_slot_1:
            print("Rate Pulse Rate Parity Overview Data is Available")
        else:
            print("Rate Pulse Rate Parity Overview Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    visibilityOverView = f'https://rxserver.retvenslabs.com/api/dashboard/visibilityOverView?hId={hId}&userId={userId}&startDate={fromDate}'

    response_2 = requests.request("GET", visibilityOverView)

    if response.status_code == 200:
        result_2 = response_2.json()
        data_slot_2 = result_2.get('data', {})
        
        if data_slot_2:
            print("Rate Pulse Visibility OverView Data is Available")
        else:
            print("Rate Pulse Visibility OverView Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    ReputationWidgetData = f'https://rxserver.retvenslabs.com/api/dashboard/getReputationWidgetData?hId={hId}&userId={userId}'

    response_3 = requests.request("GET", ReputationWidgetData)

    if response.status_code == 200:
        result_3 = response_3.json()
        data_slot_3 = result_3.get('data', {})
        
        if data_slot_3:
            print("Rate Pulse Reputation Data is Available")
        else:
            print("Rate Pulse Reputation Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    last7DaysRates = f'https://rxserver.retvenslabs.com/api/dashboard/last7DaysRates?hId={hId}&userId={userId}'

    response_4 = requests.request("GET", last7DaysRates)

    if response.status_code == 200:
        result_4 = response_4.json()
        data_slot_4 = result_4.get('data', {})
        
        if data_slot_4:
            print("Rate Pulse last7DaysRates Data is Available")
        else:
            print("Rate Pulse last7DaysRates Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    parityCalander = f'https://rxserver.retvenslabs.com/api/dashboard/parityCalander?hId={hId}&userId={userId}&type=amongCompset'

    response_5 = requests.request("GET", parityCalander)

    if response.status_code == 200:
        result_5 = response_5.json()
        data_slot_5 = result_5.get('data', {})
        
        if data_slot_5:
            print("Rate Pulse Parity Calander Data is Available")
        else:
            print("Rate Pulse Parity Calander Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")