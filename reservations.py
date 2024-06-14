import time
import requests, json
from datetime import datetime, timedelta
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def reservations(userId, hId, chId, driver):

    try:
        reservations_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.flex.items-center.w-full.gap-3.ml-3[href="/reservations"]'))
        )
        reservations_link.click()
        print('Reservations Page Opened Successfully')
    except TimeoutException:
        print("Reservations link not found")

    time.sleep(10)

    today = datetime.now()
    fromDate = today.strftime("%Y-%m-%d")

    getDropDownList = f'https://rxserver.retvenslabs.com/api/userDashboardSetting/getDropDownList?hId={hId}&userId={userId}'

    response = requests.request("GET", getDropDownList)

    if response.status_code == 200:
        result = response.json()
        data_slot = result.get('data', {})
        
        if data_slot:
            print("Reservations DropDown Data is Available")
        else:
            print("Reservations DropDown Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    reservations = f'https://rxserver.retvenslabs.com/api/dashboard/getReservations?hId={hId}&forDate={fromDate}&type=next7'

    response_1 = requests.request("GET", reservations)

    if response.status_code == 200:
        result_1 = response_1.json()
        data_slot_1 = result_1.get('data', {})
        
        if data_slot_1:
            print("Reservations Data is Available")
        else:
            print("Reservations Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")