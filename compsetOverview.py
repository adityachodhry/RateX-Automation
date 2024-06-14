import time
import requests, json
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def compsetInventory(userId, hId, chId, driver):

    try:
        compset_overview_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.flex.items-center.w-full.gap-3.ml-3[href="/compset_overview"]'))
        )
        compset_overview_link.click()
        print('Compset Overview Page Opened Successfully')
    except TimeoutException:
        print("Compset Overview Page not found")

    time.sleep(10)

    userDashboardSetting = f'https://rxserver.retvenslabs.com/api/userDashboardSetting/getCompset?hId={hId}'

    response = requests.request("GET", userDashboardSetting)

    if response.status_code == 200:
        result = response.json()
        data_slot = result.get('data', {})
        
        if data_slot:
            print("Compset Dashboard Data is Available")
        else:
            print("Compset Dashboard Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    compsetrateRecord = f'https://rxserver.retvenslabs.com/api/dashboard/getCompsetRateRecords?userId={userId}&hId={hId}&today=2024-06-12&asOn=2024-06-12&compHId={chId}'

    response_1 = requests.request("GET", compsetrateRecord)

    if response.status_code == 200:
        result_1 = response_1.json()
        data_slot_1 = result_1.get('data', {})
        
        if data_slot_1:
            print("Compset Rate Record Data is Available")
        else:
            print("Compset Rate Record Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    compsetMealPlanDetail = f'https://rxserver.retvenslabs.com/api/userDashboardSetting/getMealPlanDetail?hId={hId}&userId={userId}'

    response_2 = requests.request("GET", compsetMealPlanDetail)

    if response.status_code == 200:
        result_2 = response_2.json()
        data_slot_2 = result_2.get('data', {})
        
        if data_slot_2:
            print("Compset MealPlan Detail Data is Available")
        else:
            print("Compset MealPlan Detail Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")