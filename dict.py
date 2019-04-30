import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
  w=w.lower()
  if (w in data):
    return data[w]
  elif w.title() in data: 
        return data[w.title()]  

  elif w.upper() in data: 
        return data[w.upper()]      

  elif len(get_close_matches(w,data.keys()))>0:
    print( "Did you mean %s instead ?" % get_close_matches(w,data.keys())[0] )
    inp = input("y/n  \n")
    if (inp == "Y" or inp =="y"):
      return data[get_close_matches(w,data.keys())[0]]

    elif (inp == "N" or inp=="n"):
       return "Sorry ,the word doesn't exist"
    else:
     
      return "We didnt understand your query"

  else:
    return "The word doesn't exist in our database"


word=input("Enter word : ")

out = (translate(word))

i=1
if type(out)==list:
  for item in out:
    print("%d . "  %i, end="") 
    i=i+1
    print(item)

else:
 
  print(out)

