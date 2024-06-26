from Dashboard import dashboard
from seleniumwire import webdriver
from rateSuggestions import suggestionCalendar
from HI import hotelIntelligence
from rates_Inventory import Inventory
from compsetOverview import compsetInventory
from reservations import reservations
from reports import reportsData
from ratePulseDashboard import ratePulseDashboard
from RateMonitor import rateMonitor
from Fluctuation import fluctuation
from reputation import reputation
from visibility import visibility
from quickReport import quickReportResponse
from openpyxl import load_workbook

username = 'amarkothi@hotmail.com'
password = 'Retvens@9feb'
hId = 340007
chId = 340008
userId = '1Cr067'
roomId = 2248
# excel_filename = "C:\\Projects\\Retvens\\RateX Automate\\RateX_Report.xlsx"

driver = webdriver.Chrome()

# wb = load_workbook(excel_filename)
# ws = wb.active

dashboard(username, password, userId, hId, driver)
# quickReportResponse(driver, userId, hId)
suggestionCalendar(userId, hId, driver)
# hotelIntelligence(userId, hId, driver)
# Inventory(userId, hId, driver)
# compsetInventory(userId, hId, chId, driver)
# reservations(userId, hId, chId, driver)
# reportsData(userId, hId, driver)
# ratePulseDashboard(userId, hId, driver)
# rateMonitor(userId, hId, driver)
# fluctuation(userId, hId, driver, roomId)
# reputation(userId, hId, driver)
# visibility(userId, hId, driver)

# wb.save(excel_filename)
# print(f"Excel file saved as {excel_filename}")

driver.quit()
