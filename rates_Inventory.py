import time
import requests, json
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def Inventory(userId, hId, driver):

    try:
        rates_inventory_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.flex.items-center.w-full.gap-3.ml-3[href="/rates_&_inventory"]'))
        )
        rates_inventory_link.click()
        print('Rates & Inventory Page Opened Successfully')
    except TimeoutException:
        print("Rates & Inventory Page not found")

    time.sleep(10)

    RoomDetail = f'https://rxserver.retvenslabs.com/api/userDashboardSetting/getRoomDetail?hId={hId}&userId={userId}'

    response = requests.request("GET", RoomDetail)

    if response.status_code == 200:
        result = response.json()
        data_slot = result.get('data', {})
        
        if data_slot:
            print("Room Detail Data is Available")
        else:
            print("Room Detail Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    rateRecord = f'https://rxserver.retvenslabs.com/api/dashboard/rateRecord?userId={userId}&hId={hId}&today=2024-06-12&asOn=2024-06-12'

    response_1 = requests.request("GET", rateRecord)

    if response.status_code == 200:
        result_1 = response_1.json()
        data_slot_1 = result_1.get('data', {})
        
        if data_slot_1:
            print("Rate Record Data is Available")
        else:
            print("Rate Record Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    MealPlanDetail = f'https://rxserver.retvenslabs.com/api/userDashboardSetting/getMealPlanDetail?hId={hId}&userId={userId}'

    response_2 = requests.request("GET", MealPlanDetail)

    if response.status_code == 200:
        result_2 = response_2.json()
        data_slot_2 = result_2.get('data', {})
        
        if data_slot_2:
            print("MealPlan Detail Data is Available")
        else:
            print("MealPlan Detail Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")