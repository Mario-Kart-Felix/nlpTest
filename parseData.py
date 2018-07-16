# parsing the saved data from LonelyPlanet forum
import ast
import json
import demjson
# testing eval for single quotes




cleanList = []
forumData = open("datalp_RawNL.txt", 'r').read()
rawData = forumData.split("XspltX")


csvFile = open("dataContent.csv", "w+")
for item in rawData:
    try:
        itemDict = demjson.decode(item)
        textOut = itemDict['content'] + "'\r\n'"
        csvFile.write(textOut)
    except:
        pass
    
csvFile.close()