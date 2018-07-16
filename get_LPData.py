# importing Libraries
import requests
from bs4 import BeautifulSoup

#Main loop 1 to 10

for pageNum in range(2900, 3000):
    page_link = "https://www.lonelyplanet.com/thorntree/forums/asia-indian-subcontinent/india?page="+str(pageNum)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    page_response = requests.get(page_link, headers = headers, timeout=5)

    page_content = BeautifulSoup(page_response.content, "html.parser")
    data_title = []
    data_content = []
    data_extracted = {"titles":data_title, "content": data_content}

    # data = page_content.find_all('div', attrs={"class":"media"})
    titles = page_content.find_all('div', attrs={"class": "topic__title"})
    contents = page_content.find_all('div', attrs={"class": "js-post__content"})

    # run a loop and get all the data with findnext
    for title in titles:
        data_title.append(title.a.string)

    for content in contents:
        content_bits = content.find_all('p')
        content_text = ''
        for bit in content_bits:
            if bit.string is not None:
                content_text = content_text + bit.string
        data_content.append(content_text)

        data_out = []
    for i in range(len(data_extracted["titles"])):
        review = {"title": data_extracted["titles"][i], "content":data_extracted["content"][i]}
        data_out.append(review)

    
    f = open('datalp.txt', "a+")
    for item in data_out:
        f.write("%s," % str(item))
    f.close()
    print("current page %s" % str(pageNum))
    



   



