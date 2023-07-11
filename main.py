from selenium import webdriver
import requests
from bs4 import BeautifulSoup

# 
def getSource(product_url):
    req = requests.get(product_url)
    if req.status_code == 200:
        print("Existing web page!\n")
    else:
        print("Web page doesn't exist!")
    return req

def getPrice(response):
    text_parsed = BeautifulSoup(response.content, "html.parser")
    price= text_parsed.find('span',class_ = "andes-money-amount__fraction").text
    print("Price is: ", price)
    return price
    
if __name__ == "__main__":
    url = "https://articulo.mercadolibre.com.ar/MLA-721448642-raspberry-pi-3-b-plus-kit-64gb-a1-fuente-gab-disipa-e14-rs-_JM#reco_item_pos=0&reco_backend=machinalis-homes-pdp-boos&reco_backend_type=function&reco_client=home_navigation-recommendations&reco_id=2eae1ea7-ea50-4c98-89bd-5504f54a934a"
    html_req = getSource(url)
    getPrice(html_req)
