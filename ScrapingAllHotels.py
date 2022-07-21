from email import header
import bs4
from bs4 import BeautifulSoup
import requests
import time

url = "https://www.booking.com/searchresults.de.html?label=gen173nr-1FCAEoggI46AdIB1gEaDuIAQGYAQe4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvDb25YGwAIB0gIkOWQ5ODZmOGMtMWNlOS00NzMwLTkxMzktNTAyNGE5NzI3Yjky2AIF4AIB&sid=cdd06566a7f2f57bfc3b78bc746b75d7&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.de.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIB1gEaDuIAQGYAQe4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvDb25YGwAIB0gIkOWQ5ODZmOGMtMWNlOS00NzMwLTkxMzktNTAyNGE5NzI3Yjky2AIF4AIB%26sid%3Dcdd06566a7f2f57bfc3b78bc746b75d7%26sb_price_type%3Dtotal%3Bsrpvid%3Dbb267d3b7fe30135%26%26&ss=Stuttgart&is_ski_area=0&ssne=Stuttgart&ssne_untouched=Stuttgart&dest_id=-1871728&dest_type=city&checkin_year=2022&checkin_month=7&checkin_monthday=22&checkout_year=2022&checkout_month=7&checkout_monthday=24&extended_dates_check=0&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')
                        
#alle hotel felder durchlaufen
hotels = soup.select('.da89aeb942')

#getting all hotels with prices
while True:

    for item in hotels:
        print(item.select('.a23c043802')[0].get_text() + " -- Price: " + item.select('.bd73d13072')[0].get_text())
        

        print("-------------")
        time.sleep(1)
    time.sleep(6)





    
   