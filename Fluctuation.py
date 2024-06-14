import time
import requests, json
from datetime import datetime, timedelta
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def fluctuation(userId, hId, driver, roomId):

    try:
        ratePulse_rate_fluctuation = 'https://ratex.retvenslabs.com/rate-pulse/rate_fluctuation'
        driver.get(ratePulse_rate_fluctuation)
        print('Rate Fluctuation Page Open Sucessfully')
    except TimeoutException:
        print('Rate Fluctuation Page not Open')

    time.sleep(10)

    today = datetime.now()
    fromDate = today.strftime("%Y-%m-%d")

    fluctuationOverView = f'https://rxserver.retvenslabs.com/api/dashboard/fluctuationOverView?hId={hId}&userId={userId}'

    response = requests.request("GET", fluctuationOverView)

    if response.status_code == 200:
        result = response.json()
        data_slot = result.get('data', {})
        
        if data_slot:
            print("Fluctuation OverView Data is Available")
        else:
            print("Fluctuation OverView Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    fluctuationCalendar = f'https://rxserver.retvenslabs.com/api/dashboard/fluctuationCalendar?hId={hId}&userId={userId}&otaId=1&roomID={roomId}'

    response_1 = requests.request("GET", fluctuationCalendar)

    if response.status_code == 200:
        result_1 = response_1.json()
        data_slot_1 = result_1.get('data', {})
        
        if data_slot_1:
            print("Fluctuation Calendar Data is Available")
        else:
            print("Fluctuation Calendar Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    

    fluctuationTrend = f'https://rxserver.retvenslabs.com/api/dashboard/fluctuationTrend?hId={hId}&userId={userId}&roomID={roomId}'

    response_2 = requests.request("GET", fluctuationTrend)

    if response.status_code == 200:
        result_2 = response_2.json()
        data_slot_2 = result_2.get('data', {})
        
        if data_slot_2:
            print("Fluctuation Trend Data is Available")
        else:
            print("Fluctuation Trend Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    DropDownList = f'https://rxserver.retvenslabs.com/api/userDashboardSetting/getDropDownList?hId={hId}&userId={userId}'

    response_3 = requests.request("GET", DropDownList)

    if response.status_code == 200:
        result_3 = response_3.json()
        data_slot_3 = result_3.get('data', {})
        
        if data_slot_3:
            print("Fluctuation DropDown List Data is Available")
        else:
            print("Fluctuation DropDown List Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")