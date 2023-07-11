from selenium import webdriver
import requests
from bs4 import BeautifulSoup


def getSource():
    url = "https://articulo.mercadolibre.com.ar/MLA-721448642-raspberry-pi-3-b-plus-kit-64gb-a1-fuente-gab-disipa-e14-rs-_JM#reco_item_pos=0&reco_backend=machinalis-homes-pdp-boos&reco_backend_type=function&reco_client=home_navigation-recommendations&reco_id=6ac7c9a8-b64e-4cc2-a57f-5bc61c9ba317"
    req = requests.get(url)
    if req.status_code == 200:
        print("Existing web page!")
    else:
        print("Web page doesn't exist!")
    return req

def getPrice(response):
    text_parsed = BeautifulSoup(response.text, "html.parser")
    #search_results = text_parsed.find()
    print(text_parsed)


if __name__ == "__main__":
    html_req = getSource()
    getPrice(html_req)
