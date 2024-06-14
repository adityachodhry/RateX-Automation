import time
import requests, json
from datetime import datetime, timedelta
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def reputation(userId, hId, driver):

    try:
        ratePulse_reputation = 'https://ratex.retvenslabs.com/rate-pulse/reputation'
        driver.get(ratePulse_reputation)
        print('Rate Reputation Page Open Sucessfully')
    except TimeoutException:
        print('Rate Reputation Page not Open')

    time.sleep(10)

    today = datetime.now()
    fromDate = today.strftime("%Y-%m-%d")

    reputationOverview = f'https://rxserver.retvenslabs.com/api/dashboard/reputationOverview?hId={hId}&userId={userId}'

    response = requests.request("GET", reputationOverview)

    if response.status_code == 200:
        result = response.json()
        data_slot = result.get('data', {})
        
        if data_slot:
            print("Reputation OverView Data is Available")
        else:
            print("Reputation OverView Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    rattingOverview = f'https://rxserver.retvenslabs.com/api/dashboard/rattingOverview?hId={hId}&userId={userId}'

    response_1 = requests.request("GET", rattingOverview)

    if response.status_code == 200:
        result_1 = response_1.json()
        data_slot_1 = result_1.get('data', {})
        
        if data_slot_1:
            print("Ratting Data is Available")
        else:
            print("Ratting Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    

    recentReview = f'https://rxserver.retvenslabs.com/api/dashboard/recentReview?hId={hId}&userId={userId}'

    response_2 = requests.request("GET", recentReview)

    if response.status_code == 200:
        result_2 = response_2.json()
        data_slot_2 = result_2.get('data', {})
        
        if data_slot_2:
            print("Recent Review Data is Available")
        else:
            print("Recent Review Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    rattingLeaderboard = f'https://rxserver.retvenslabs.com/api/dashboard/rattingLeaderboard?hId={hId}&userId={userId}'

    response_3 = requests.request("GET", rattingLeaderboard)

    if response.status_code == 200:
        result_3 = response_3.json()
        data_slot_3 = result_3.get('data', {})
        
        if data_slot_3:
            print("Ratting Leaderboard Data is Available")
        else:
            print("Ratting Leaderboard Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    rattingTrend = f'https://rxserver.retvenslabs.com/api/dashboard/rattingTrend?hId={hId}&userId={userId}&startDate={fromDate}'

    response_4 = requests.request("GET", rattingTrend)

    if response.status_code == 200:
        result_4 = response_4.json()
        data_slot_4 = result_4.get('data', {})
        
        if data_slot_4:
            print("Ratting Trend Data is Available")
        else:
            print("Ratting Trend Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")