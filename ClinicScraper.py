import requests
from bs4 import BeautifulSoup
import pandas as pd
from colorama import Fore

def get_clinic_name(clinic_id):
    url         =  f'https://{clinic_id}.portal.athenahealth.com/'
    response    =   requests.get(url)
    html        =   response.text
    soup        =   BeautifulSoup(html,'html.parser')
    clinic_name =   soup.find_all('h1')[-1].text.strip()
    return clinic_name

list = []



def cieo_id_scrape(start,end):
    for clinic_id in range(start,end+1):

       date_dict = {}
       date_dict['clinic_id'] = clinic_id
       date_dict['clinic_name'] = get_clinic_name(clinic_id)
       print(f" Scraping  in Portal \t id  ==> {clinic_id} \n")
       print(f'--------------------------------------------- \n')
       if date_dict['clinic_name'] != 'Payment Confirmation' and date_dict['clinic_name'] != "Sorry, we can't find that practice. Make sure you typed the right address.":
            list.append(date_dict)
    df = pd.DataFrame(list)
    df.to_csv(f'clinics{start}.csv',index=False)
start =int(input(f'Enter start Id:\n'))
end = int(input(f'Enter end Id:\n'))
cieo_id_scrape(start,end)
