import csv
import json
with open('example.csv', mode = 'r') as file:
    csv = csv.reader(file)
    for lines in csv:
        print(lines)
# 2
contact = {'name': 'Stan', 'phone': '010-0000-0000'}
with open("output.json" , "w") as out:
    json.dump(contact,out,indent=6)
print("Save succeed")
# 3
with open('/content/file.txt', 'r') as t:
    for e in t:
        print(e)
# 4
try:
    with open('/content/data.json', 'r') as j:
        try:
            data = json.load(j)
            print(json.dumps(data, indent=4, ensure_ascii=False))
        except TypeError:
            print('Type error')
        except Exception as e:
            print(e)
except OSError:
    print('Couldnmt open the file')
except Exception as e:
    print(e)