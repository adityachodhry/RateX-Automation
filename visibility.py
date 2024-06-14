import time
import requests, json
from datetime import datetime, timedelta
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def visibility(userId, hId, driver):

    try:
        ratePulse_visibility = 'https://ratex.retvenslabs.com/rate-pulse/visibility'
        driver.get(ratePulse_visibility)
        print('Rate Visibility Page Open Sucessfully')
    except TimeoutException:
        print('Rate Visibility Page not Open')

    time.sleep(10)

    today = datetime.now()
    fromDate = today.strftime("%Y-%m-%d")

    visibilityOverView = f'https://rxserver.retvenslabs.com/api/dashboard/visibilityOverView?hId={hId}&userId={userId}'

    response = requests.request("GET", visibilityOverView)

    if response.status_code == 200:
        result = response.json()
        data_slot = result.get('data', {})
        
        if data_slot:
            print("Visibility OverView Data is Available")
        else:
            print("Visibility OverView Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    DropDownList = f'https://rxserver.retvenslabs.com/api/userDashboardSetting/getDropDownList?hId={hId}&userId={userId}'

    response_1 = requests.request("GET", DropDownList)

    if response.status_code == 200:
        result_1 = response_1.json()
        data_slot_1 = result_1.get('data', {})
        
        if data_slot_1:
            print("DropDown List Data is Available")
        else:
            print("DropDown List Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    

    visibilityLeaderBoard = f'https://rxserver.retvenslabs.com/api/dashboard/visibilityLeaderBoard?hId={hId}&userId={userId}&startDate={fromDate}'

    response_2 = requests.request("GET", visibilityLeaderBoard)

    if response.status_code == 200:
        result_2 = response_2.json()
        data_slot_2 = result_2.get('data', {})
        
        if data_slot_2:
            print("Visibility Leader Board Data is Available")
        else:
            print("Visibility Leader Board Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    visibilityCalender = f'https://rxserver.retvenslabs.com/api/dashboard/visibilityCalender?hId={hId}&userId={userId}&startDate={fromDate}'

    response_3 = requests.request("GET", visibilityCalender)

    if response.status_code == 200:
        result_3 = response_3.json()
        data_slot_3 = result_3.get('data', {})
        
        if data_slot_3:
            print("Visibility Calender Data is Available")
        else:
            print("Visibility Calender Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    visibilityTrends = f'https://rxserver.retvenslabs.com/api/dashboard/visibilityTrends?hId={hId}&userId={userId}&startDate={fromDate}'

    response_4 = requests.request("GET", visibilityTrends)

    if response.status_code == 200:
        result_4 = response_4.json()
        data_slot_4 = result_4.get('data', {})
        
        if data_slot_4:
            print("Visibility Trends Data is Available")
        else:
            print("Visibility Trends Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")