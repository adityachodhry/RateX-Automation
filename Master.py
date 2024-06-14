from Dashboard import dashboard
from seleniumwire import webdriver
from rateSuggestions import suggestionCalendar
from HI import hotelIntelligence
from rates_Inventory import Inventory
from compsetOverview import compsetInventory
from reservations import reservations
from reports import reportsData
from ratePulseDashboard import ratePulseDashboard

username = 'amarkothi@hotmail.com'
password = 'Retvens@9feb'
hId = 340007
chId = 340008
userId = '1Cr067'

driver = webdriver.Chrome()

dashboard(username, password, userId, hId, driver)
suggestionCalendar(userId, hId, driver)
hotelIntelligence(userId, hId, driver)
Inventory(userId, hId, driver)
compsetInventory(userId, hId, chId, driver)
reservations(userId, hId, chId, driver)
reportsData(userId, hId, driver)
ratePulseDashboard(userId, hId, driver)

driver.quit()