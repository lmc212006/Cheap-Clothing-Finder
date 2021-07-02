from selenium import webdriver
from time import sleep

def getCheapestMyntra(drvr, link, elToSearch):

    drvr.get(link)

    out = {}
    sleep(2)

    for i in range(elToSearch):
        out[drvr.find_element_by_xpath(f"//*[@id='desktopSearchResults']/div[2]/section/ul/li[{i + 1}]/a/div[2]/div/span").text] = drvr.find_element_by_xpath("//*[@id='desktopSearchResults']/div[2]/section/ul/li[1]/a/div[2]/h4[1]").text
    return out 

def getCheapestAjio(drvr, link, elToSearch):
    drvr.get(link)

    out = {}
    sleep(2)

    for i in range(elToSearch):
        out[drvr.find_element_by_xpath(f"//*[@id='products']/div[3]/div[1]/div/div[{i + 1}]/a/div/div[2]/div[3]/span").text] = drvr.find_element_by_xpath(f"//*[@id='products']/div[3]/div[1]/div/div[{i + 1}]/a/div/div[2]/div[2]").text                                                                                                                                                           
                                                                                                                                                           

    return out

PATH = "chromedriver.exe"

rsearchQuery = input("Enter the item you want to buy:")
searchQuery = rsearchQuery.replace(" ", "-")

searchNum = int(input("Enter the amount of elements you want to search"))

driver = webdriver.Chrome(PATH, 1)

linkMyntra = f"https://www.myntra.com/{searchQuery}"
searchQuery = searchQuery.replace("-", "%20")
linkAjio = f"https://www.ajio.com/search/?text={searchQuery}"

myntraVals = getCheapestMyntra(driver, linkMyntra, searchNum)
ajioVals = getCheapestAjio(driver, linkAjio, searchNum)

myntraPrices = list(myntraVals.keys())
ajioPrices = list(ajioVals.keys())

currentCheapest = 10000000

cheapShop = ""
cheapIndex = 0

for i in range(len(myntraPrices)):
    
    if int(myntraPrices[i].strip("Rs. ").split("R")[0]) < currentCheapest:
        currentCheapest = int(myntraPrices[i].strip("Rs .").split("R")[0])
        cheapShop = "Myntra"
        cheapIndex = i

    if int(ajioPrices[i].strip("Rs .").split("R")[0]) < currentCheapest:
        currentCheapest = int(ajioPrices[i].strip("Rs .").split("R")[0])
        cheapShop = "Ajio"
        cheapIndex = i

if cheapShop == "Ajio":
    print("The cheapest", rsearchQuery, "was at the price", currentCheapest, "from", cheapShop, ", and is called", list(myntraVals.values())[cheapIndex])
else:
    print("The cheapest", rsearchQuery, "was at the price", currentCheapest, "from", cheapShop, ", and is called", list(myntraVals.values())[cheapIndex])

driver.close()

sleep(30)