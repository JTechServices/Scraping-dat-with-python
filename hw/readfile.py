# 1) kolik je tam produktů +
# 2) názvy produktů vypíše (prostě jeden za druhým pod sebou, nemusíte řešit žádné složité formátování apod...)
# 3) Vypíšete k jednotlivým produktům náhradní díly (jsou jen u některých)

from bs4 import BeautifulSoup as bs


content = []
nd = []
count = 0

# Read XML file and save content
file = open("export_full.xml", "rb")
content = file.read()
soup = bs(content, "xml")
items = soup.find_all("item")

# looping through all items in XML
# Print products, ID & total count
for item in items:
    count += 1;
    print(item["name"])

    try:
        print(item["code"])
        print(nd[count])   

    except Exception as e:
        print("Nemá ND")
    
   

print(count)

