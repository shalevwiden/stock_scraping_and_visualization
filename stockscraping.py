import requests
import bs4
from bs4 import BeautifulSoup


import sys
import os

import csv

import requests

# top companies scraping
stocks_page_to_scrape=requests.get('https://companiesmarketcap.com/')

stocksoup=BeautifulSoup(stocks_page_to_scrape.text,'html.parser')
# findAll(tag name ,attrs={tag attributes})
# getting that good good data mf
companynames=stocksoup.find_all('div',attrs={"class":"company-name"})

company_marketcaps_raw=stocksoup.find_all('td', attrs={"class":"td-right"})

company_countries=stocksoup.find_all('span', attrs={"class":"responsive-hidden"})

company_countries=[country.get_text().strip() for country in company_countries]

company_marketcaps=[]

tenbillion=int(("10,000,000,000").replace(',',''))
# or can write 10_000_000_000
for rawdata in company_marketcaps_raw:
        # data-sort is a custom HTML attribute used to help javascript sort data
        # .get BeautifulSoup method
        datasortattr = rawdata.get('data-sort')
        # if all of this is met PER rawdata, since we're iterating over that
        if datasortattr and datasortattr.isdigit() and int(datasortattr)>tenbillion:
              company_marketcaps.append(rawdata.get('data-sort'))


# can also go back and filter based on the datasortattr. For example get companies above 1 tril, between 500 bil and 1 tril, and below 500 bil
# then create matplotlib graphs for all of those

# create a dictionary for it because why not
name_mktcap_dict={}

for company, marketcap,country in zip(companynames, company_marketcaps, company_countries):
    name_mktcap_dict[company.text]=[marketcap, country]
# now the data is nicely in that dict.

listof_datalists=[]


# car companies market cap scraping
cmc_cars_page_to_scrape=requests.get('https://companiesmarketcap.com/automakers/largest-automakers-by-market-cap/')

# scrape this car shit too ngl

if __name__=="__main__":


    # good to check everythings working with the venv:
    print(f'the version of beautiful soup is\n {(bs4.__version__)}')
    print(f'the version of requests is\n {(requests.__version__)}')

    print(f'\nthe python version being used is:{sys.executable}\n')

    for company in companynames:
        print(company.text)
    print('\n\n')
    print('Company Market Caps:\n')
    print(company_marketcaps)

    print(f'\nname_mktcap_dict:\n{name_mktcap_dict}')
    print(f'Company Countries\n{company_countries}')


'''
to do:

I need to functionize this
'''