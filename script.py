#pip install requests_html  
# pip install pyfiglet
# Import the pyfiglet module  
from requests_html import HTMLSession
import pyfiglet as pyg 

# Taking the input text for the default format  
res= pyg.figlet_format("Welcome to \nCheck Travel App")   
# Printing the result in the output  
print(' Web Scraping With Python ')  
print(res)  
# print(result)

# print("""         $$\                           $$\               $$\                                            $$\                                     
#           $$ |                          $$ |              $$ |                                           $$ |                                    
#  $$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\       $$$$$$\    $$$$$$\  $$$$$$\ $$\    $$\  $$$$$$\  $$ |       $$$$$$\   $$$$$$\   $$$$$$\  
# $$  _____|$$  __$$\ $$  __$$\ $$  _____|$$ | $$  |      \_$$  _|  $$  __$$\ \____$$\\$$\  $$  |$$  __$$\ $$ |       \____$$\ $$  __$$\ $$  __$$\ 
# $$ /      $$ |  $$ |$$$$$$$$ |$$ /      $$$$$$  /         $$ |    $$ |  \__|$$$$$$$ |\$$\$$  / $$$$$$$$ |$$ |       $$$$$$$ |$$ /  $$ |$$ /  $$ |
# $$ |      $$ |  $$ |$$   ____|$$ |      $$  _$$<          $$ |$$\ $$ |     $$  __$$ | \$$$  /  $$   ____|$$ |      $$  __$$ |$$ |  $$ |$$ |  $$ |
# \$$$$$$$\ $$ |  $$ |\$$$$$$$\ \$$$$$$$\ $$ | \$$\         \$$$$  |$$ |     \$$$$$$$ |  \$  /   \$$$$$$$\ $$ |      \$$$$$$$ |$$$$$$$  |$$$$$$$  |
#  \_______|\__|  \__| \_______| \_______|\__|  \__|         \____/ \__|      \_______|   \_/     \_______|\__|       \_______|$$  ____/ $$  ____/ 
#                                                                                                                              $$ |      $$ |      
#                                                                                                                              $$ |      $$ |      
#                                                                                                                              \__|      \__|      """)


#create session 
s=HTMLSession()

city=str(input("enter city name = "))
#url for weater and time of each city and favourite places
url=f'https://www.google.com/search?q=weather+{city}'
urlTime=f'https://www.google.com/search?q=time+in+{city}'
urlFav=f'https://www.google.com/search?q=google+travel+{city}'
#get the data and add ur user-agent
r=s.get(url,headers={'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'})
rT=s.get(urlTime,headers={'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'})
rF=s.get(urlFav,headers={'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'})
#target some data to extract it
temp=r.html.find('span#wob_tm',first=True).text #return list 
unit=r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text #u can search more than one element and 
desc=r.html.find('div#wob_dcp.wob_dcp',first=True).find('span#wob_dc',first=True).text 
Precipitation=r.html.find('span#wob_pp',first=True ).text
Humidity=r.html.find('span#wob_hm',first=True ).text
Wind=r.html.find('span#wob_ws.wob_t',first=True ).text
localTime=rT.html.find('div.gsrt.vk_bk.FzvWSb.YwPhnf',first=True ).text
if city=="now":  
    city=r.html.find('div.wob_loc.q8U8x',first=True ).text
    urlFav=f'https://www.google.com/search?q=google+travel+{city}'
    rF=s.get(urlFav,headers={'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'})
    try:
        fav1=rF.html.find('div.c1UYF span.aVSTQd.tNxQIb.OSrXXb',first=True ).text
        print("location:", city ,"\n","temperature:", temp ,unit,"\n","description:",desc,"\n","Precipitation:",Precipitation ,"\n","Humidity:",Humidity ,"\n","Wind:",Wind ,"\n",f"time in {city} is ",localTime ,"\n","favourite places is",fav1)
    except:
        print("favourit places : cant find favourite places")
        print("location:", city ,"\n","temperature:", temp ,unit,"\n","description:",desc,"\n","Precipitation:",Precipitation ,"\n","Humidity:",Humidity ,"\n","Wind:",Wind ,"\n",f"time in {city} is ",localTime,"\n")
else:
    try:
        fav1=rF.html.find('div.c1UYF span.aVSTQd.tNxQIb.OSrXXb',first=True ).text
        print("location:", city ,"\n","temperature:", temp ,unit,"\n","description:",desc,"\n","Precipitation:",Precipitation ,"\n","Humidity:",Humidity ,"\n","Wind:",Wind ,"\n",f"time in {city} is ",localTime ,"\n","favourite places is",fav1)
    except:
        print("favourit places : cant find favourite places")
        print("location:", city ,"\n","temperature:", temp ,unit,"\n","description:",desc,"\n","Precipitation:",Precipitation ,"\n","Humidity:",Humidity ,"\n","Wind:",Wind ,"\n",f"time in {city} is ",localTime ,"\n")



raw=input("Press Enter to continue...")

