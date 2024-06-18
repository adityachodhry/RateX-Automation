import time
import requests
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from openpyxl import Workbook
from openpyxl.styles import Font

def dashboard(username, password, userId, hId, driver):

    login_url = 'https://ratex.retvenslabs.com/login'
    excel_filename = 'dashboard_checks.xlsx'

    driver.get(login_url)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))

    driver.find_element(By.NAME, 'email').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)

    driver.find_element(By.XPATH, '//button[text()="Log-in"]').click()

    WebDriverWait(driver, 10).until(EC.url_changes(login_url))

    def take_screenshot_and_save_as(filename):
        driver.save_screenshot(filename + '.png')
        print(f"Screenshot saved as {filename}.png")

    wb = Workbook()
    ws = wb.active

    bold_font = Font(bold=True)
    ws.append(["Check", "Status"])
    ws["A1"].font = bold_font
    ws["B1"].font = bold_font

    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.absolute.right-2.top-4.bg-red-50.text-red-600.text-sm.py-1.px-2.rounded-lg.hover\\:bg-red-500.hover\\:text-white.cursor-pointer'))
        )
        close_button.click()
        ws.append(["Popup", "Closed successfully"])
        print("Closed popup successfully")
    except TimeoutException:
        ws.append(["Popup", "Popup not found"])
        print("No popup found")

    if "Invalid username or password" in driver.page_source:
        ws.append(["Login", "Login unsuccessful due to invalid credentials"])
        print("Login Unsuccessful")
        driver.quit()
    else:
        ws.append(["Login", "Login successful"])
        print("Login Successful")

    try:
        dashboard_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.p-5.flex.flex-col.gap-4'))
        )
        dashboard_element.click()
        ws.append(["Dashboard", "Dashboard is open and working properly"])
        print("Dashboard is open and working properly")
    except TimeoutException:
        take_screenshot_and_save_as("dashboard_issue")
        ws.append(["Dashboard", "Dashboard element not found; something is wrong on this page"])
        print("Something is wrong in this dashboard page")

    time.sleep(10)

    api_checks = [
        ("7 Days Pricing", f'https://rxserver.retvenslabs.com/api/dashboard/next7DaysPricing?hId={hId}&userId={userId}'),
        ("Performance Matrix", f'https://rxserver.retvenslabs.com/api/dashboard/performaceMatrix?hId={hId}&userId={userId}&timePeriod=past30Days&chartData=revenue'),
        ("Forecasted Data", f'https://rxserver.retvenslabs.com/api/dashboard/getForecastedData?userId={userId}&hId={hId}&rangeType=7D'),
        ("Sentiment Analysis", f'https://rxserver.retvenslabs.com/api/dashboard/getSentimentAnalysisData?userId={userId}&hId={hId}'),
        ("Notifications", f'https://rxserver.retvenslabs.com/api/notifications/getNotifications?hId={hId}'),
        ("Take Actions", f'https://rxserver.retvenslabs.com/api/dashboard/getActionsToTake?hId={hId}&userId={userId}'),
        ("Reputation", f'https://rxserver.retvenslabs.com/api/dashboard/getReputationWidgetData?hId={hId}&userId={userId}'),
        ("Cancellation", f'https://rxserver.retvenslabs.com/api/dashboard/getCancellationWidgetData?userId={userId}&hId={hId}')
    ]

    for check_name, url in api_checks:
        response = requests.request("GET", url)
        if response.status_code == 200:
            result = response.json()
            data_slot = result.get('data', {})
            status = f"Available; Data retrieved successfully" if data_slot else "Not Available; No data found in the response"
        else:
            status = f"Request failed with status code: {response.status_code}; Unable to retrieve data"
        ws.append([check_name, status])

    wb.save(excel_filename)
    print(f"Excel file saved as {excel_filename}")