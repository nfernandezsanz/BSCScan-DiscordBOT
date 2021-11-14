import cloudscraper
from bs4 import BeautifulSoup

def token_info(contract):
    link = "https://www.bscscan.com/token/" + contract
    
    scraper = cloudscraper.create_scraper()
    scrap = scraper.get(link).text
    soupa = BeautifulSoup(scrap, 'html.parser')

    #print holders
    tokenholders = soupa.find(id='ContentPlaceHolder1_tr_tokenHolders').get_text()
    tokenholdersa = "Holders: " + ((((tokenholders.strip()).strip("Holders:")).strip()).strip(" a ")).strip()
    #print(tokenholdersa)

    #print name
    website = soupa.find('span', class_='text-secondary small').get_text()
    tokename = "Name: " + website
    #print(tokename)

    return (tokename, tokenholdersa)

