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
        json.dump(grounding,fp,indent=1)


def clean_distraction(body):
    effort_list = []
    for i in body.children:
        if i.text.strip()[:-2].isdecimal():
            new_tag = BeautifulSoup("").new_tag("p")
            effort_list += [new_tag]
        elif i.text == "":
            pass
        else:
            effort_list[-1].contents.append(i)
    return effort_list

def scrape_distraction():
    url = "https://www.beautyafterbruises.org/blog/distraction101"

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    low_effort_header = soup.find("h3")
    med_effort_header = low_effort_header.find_next_sibling("h3")
    high_effort_header = med_effort_header.find_next_sibling("h3")

    low_effort_body = low_effort_header.find_next_sibling("ol")
    med_effort_body  = med_effort_header.find_next_sibling("p")
    high_effort_body  = high_effort_header.find_next_sibling("p")

    low_effort_list = [i.find("p")for i in low_effort_body.find_all("li")]

    med_effort_list =  clean_distraction(med_effort_body)

    high_effort_list = clean_distraction(high_effort_body)

    d = {
        "low": [str(i) for i in low_effort_list],
        "med": [str(i) for i in med_effort_list],
        "high": [str(i) for i in high_effort_list]
        }

    path = "../help_gen/src/data/distraction.json"

    with open(path,"w") as fp:
        json.dump(d,fp,indent=1)

def scrape_selfcare():
    url = "https://www.beautyafterbruises.org/blog/selfcare"
    path =  "../help_gen/src/data/selfcare.json"

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    care = soup.find("ol").find_all("li")


    low = []
    med = []
    high = []

    arr = [low,med,high]
    ind = 0
    for i in care:
        if i.find("h3"):
            # print(i)
            for j in i:
                if j.text == "":
                    continue
                if j.name == "h3":
                    ind+=1
        
        arr[ind].append(str(i.find("p")))

    d = {
        "low":low,
        "med":med,
        "high":high
        }

    with open(path,"w") as fp:
        json.dump(d,fp,indent=1)


# scrape_grounding()
# scrape_distraction()
scrape_selfcare()