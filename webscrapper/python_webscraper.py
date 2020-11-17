from bs4 import BeautifulSoup
import lxml
import requests
url="https://pokemondb.net/pokedex/stats/gen3"
data=requests.get(url)
soup=BeautifulSoup(data.text,"lxml")
number=soup.find_all("tr")
del number[0]
pokemn_list={}
# print(number[0].prettify())
for i in number:
    name=i.find("td",class_="cell-name")
    name2=name.find("a",class_="ent-name").text
    stats_numbers=i.find_all("td",class_="cell-num")
    hp=stats_numbers[1].text
    at=stats_numbers[2].text
    df=stats_numbers[3].text
    sp=stats_numbers[4].text
    spd=stats_numbers[5].text
    spe=stats_numbers[6].text
    # pokemn_list.append(stats)
    pokemn_list[name2]={
        "secondary_form":None,
        "hp":hp,
        "attack":at,
        "defense":df,
        "speed":spe,
        "special":sp,
        "sp.defense":spd,
    }
print(pokemn_list['Jirachi'])
  