import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:

        return data[word]
    elif len(get_close_matches(word,data.keys())) >0:
        key=input( "did you mean %s instead?\npress Y for YES OR N for NO " % get_close_matches(word,data.keys()) [0])
        if key.upper()=="Y"  :
            return data[get_close_matches(word,data.keys()) [0]]
        elif key.upper()=="N":
            return "the word does not exist"
        else:
            return "invalid response"       





    else:

            print("the word does not exist.Please check the word again ")

  
  
  
txt=input("enter your word: ") 
output=(translate(txt)) 
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)        