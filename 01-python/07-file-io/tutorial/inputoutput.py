import json
# Dosya okuma
with open("/home/orgoloth/Desktop/boru_last/test.txt", "r", encoding="utf-8") as file:
    myList = file.readlines()
    print(myList)

# JSON'a yazma
with open("/home/orgoloth/Desktop/boru_last/test.json", "w", encoding="utf-8") as j:
    json.dump(myList, j, ensure_ascii=False)


# JSON'dan okuma
with open("/home/orgoloth/Desktop/boru_last/test.json", "r", encoding="utf-8") as j2:
    myList_last = json.load(j2)
    print(myList_last)