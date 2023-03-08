from bs4 import BeautifulSoup
from bs4 import element
import requests
import json




def scrape_grounding():
    url = "https://www.beautyafterbruises.org/blog/grounding101"
    path = "../help_gen/src/data/grounding.json"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    grounding = soup.find("ol").find_all("li")
    grounding = [str(g.find("p")) for g in grounding]
    with open(path,"w") as fp:
        json.dump(grounding,fp)


# scrape_grounding()





url = "https://www.beautyafterbruises.org/blog/distraction101"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# body = soup.find("div",id="yui_3_17_2_1_1678264151102_350")
low_effort_header = soup.find("h3")
med_effort_header = low_effort_header.find_next_sibling("h3")
high_effort_header = med_effort_header.find_next_sibling("h3")

# print(low_effort_header,med_effort_header,high_effort_header)

low_effort_body = low_effort_header.find_next_sibling("ol")
med_effort_body  = med_effort_header.find_next_sibling("p")
high_effort_body  = high_effort_header.find_next_sibling("p")

low_effort_list = [i.find("p")for i in low_effort_body.find_all("li")]

med_effort_list = []
for i in med_effort_body.children:
    if i.text.strip()[:-2].isdecimal():
        # use 61. as entry header
        new_tag = soup.new_tag("p")
        med_effort_list += [new_tag]
    elif i.text == "":
        # skip newlines
        pass
    else:
        med_effort_list[-1].contents.append(i)

high_effort_list = []
for i in high_effort_body.children:
    if i.text.strip()[:-2].isdecimal():
        # use 61. as entry header
        new_tag = soup.new_tag("p")
        high_effort_list += [new_tag]
    elif i.text == "":
        # skip newlines
        pass
    else:
        high_effort_list[-1].contents.append(i)


d = {
    "low": [str(i) for i in low_effort_list],
    "med": [str(i) for i in med_effort_list],
    "high": [str(i) for i in high_effort_list]
    }


with open("./distraction.json","w") as fp:
    json.dump(d,fp,indent=1)

url = "https://www.beautyafterbruises.org/blog/selfcare"


# h3 low impact header
# medium and high are part of the list
