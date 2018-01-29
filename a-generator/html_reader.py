from bs4 import BeautifulSoup
import json

html = open('./input/JAVA-250.html', 'rb', buffering=1).read(1000000)
# print(html)
soup = BeautifulSoup(html, 'html.parser')
#
div = soup.find_all('p')
# div = soup.select("div[class='entry-content'], p")

# div = soup.select("p > strong")
# strong =
#, style=True            {"class": "entry-content"}

# print(div)

for strong_tag in soup.find_all('p'):
    question = strong_tag.text

    if '?' in question:
        print('*****************************************************************')
        print(question)
        anserbr = strong_tag.next_sibling
        answerp = strong_tag.find_all_next("p")
        if '?' not in answerp[0]:
            if (anserbr):
                print(anserbr)
            if (answerp):
                print(answerp[0].text)



    # print(strong_tag.find_next("ul").text)
        # , strong_tag.next_sibling
qa_list = {}