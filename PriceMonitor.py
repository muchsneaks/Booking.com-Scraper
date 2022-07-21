from email import header
from unittest import expectedFailure
import bs4
from bs4 import BeautifulSoup
import requests
import time
import re
from discord_webhook import DiscordWebhook, DiscordEmbed
from os import system

system("title " + "Booking.com Price Checker")

url = "https://www.booking.com/hotel/de/the-niu-mesh.de.html?aid=304142&label=gen173nr-1DCAEoggI46AdIB1gEaDuIAQGYAQe4ARfIAQzYAQPoAQH4AQKIAgGoAgO4Aryb4ZYGwAIB0gIkYWQ2YTAzNzktZmQ3Ny00NDE5LWIyNGYtMzg1ODE1YWVkNmNm2AIE4AIB&sid=cdd06566a7f2f57bfc3b78bc746b75d7&all_sr_blocks=505835201_265190761_0_2_0;checkin=2022-07-22;checkout=2022-07-24;dest_id=-1871728;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=505835201_265190761_0_2_0;hpos=1;matching_block_id=505835201_265190761_0_2_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=505835201_265190761_0_2_0__16280;srepoch=1658346369;srpvid=382a8b0058010fd6;type=total;ucfs=1&#hotelTmpl"
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/940377611220160602/39stKrdCKcygp7X_8GYiZ5GnLy8lABC0I74Nvc68khUsy95v9oh0oJrIsOXB9HTQdFHq')

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')

#checking for price and send update when it changes
while True:
    try:   
        price = soup.select('.prco-valign-middle-helper')[0].get_text()
        price2 = re.sub('[^0-9]', '', price)
        hotelname = soup.select('.pp-header__title')[0].get_text()
        picture = soup.select(".hide")
        Zimmerart = soup.select(".hprt-roomtype-icon-link")[0].get_text()
      
    


        print(hotelname + price)
        for img in picture:
            if img.has_attr('src'):
                discordpic = img['src']
                break
        
        
        try:
            if int(oldprice) > int(price2):
                print("Room got cheaper old price was: " + oldprice + "€ and new price is: " + price2 + "€")
                embed = DiscordEmbed(title="Booking.com Price Checker", description="Informing you about all price changes", color='03b2f8')
                embed.set_thumbnail(url=discordpic)
                embed.add_embed_field(name='**Hotelname :hotel: **', value=hotelname)
                embed.add_embed_field(name='**Old Price **', value=oldprice)
                embed.add_embed_field(name='**New Price :money_with_wings:  **', value=price2)
                embed.add_embed_field(name='**Room**', value=Zimmerart, inline=False)
                
                webhook.add_embed(embed)
                webhook.execute()
            else:
                print("Room is the same price")
                
        except:
            pass


      
        oldprice = re.sub('[^0-9]', '', price)
       
        print("-------------------------------------------------")
        time.sleep(120)
    
    except:
        print("Error......Reytrying......")
        time.sleep(20)
    

 
