from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import random
import wikipedia
import webbrowser

print("Hello, and welcome to Random Good Article by Subject (RGAS)! Please input a random subject below:\n")
print("Input 0 for 'Agriculture, food, and drink'\nInput 1 for 'Art and architecture'\nInput 2 for 'Engineering and technology'\nInput 3 for 'Geography and places'\nInput 4 for 'History'\nInput 5 for 'Language and literature'\nInput 6 for 'Mathematics'\nInput 7 for 'Media and drama'\nInput 8 for 'Music'\nInput 9 for 'Natural sciences'\nInput A for 'Philosophy and religion'\nInput B for 'Social sciences and society'\nInput C for 'Sports and recreation'\nInput D for 'Video games'\nInput E for 'Warfare'")

category = input("> ")

link = "https://en.wikipedia.org/wiki/Wikipedia:Good_articles"

if category == "0":
    link += "/Agriculture,_food_and_drink"
elif category == "1":
    link += "/Art_and_architecture"
elif category == "2":
    link += "/Engineering_and_technology"
elif category == "3":
    link += "/Geography_and_places"
elif category == "4":
    link += "/History"
elif category == "5":
    link += "/Language_and_literature"
elif category == "6":
    link += "/Mathematics"
elif category == "7":
    link += "/Media_and_drama"
elif category == "8":
    link += "/Music"
elif category == "9":
    link += "/Natural_sciences"
elif category == "A":
    link += "/Philosophy_and_religion"
elif category == "B":
    link += "/Social_sciences_and_society"
elif category == "C":
    link += "/Sports_and_recreation"
elif category == "D":
    link += "/Video_games"
elif category == "E":
    link += "/Warfare"
else:
    print("Oops!")

req = Request(link)
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

links = links[:links.index('/wiki/Help:Category')]
links = links[169:]

while True:
    while True:
        randlink = random.randint(0, len(links))
        if 'action=edit' in links[randlink]:
            links.remove(links[randlink])
            continue
        else:
            break

    links[randlink] = links[randlink][6:]

    try:
        print(f'Would you like to view {wikipedia.page(links[randlink]).title}? (y/n)')
        doView = input()
        if doView == 'y' or doView == 'Y':
            break
        else:
            continue
    except:
        continue

webbrowser.open('https://en.wikipedia.org/wiki/' + links[randlink])