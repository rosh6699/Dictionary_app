import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
  #convert to lower case
  w=w.lower()

  #find matches
  matches = get_close_matches(w,data.keys())
  
  if (w in data):
    return data[w]
    
  elif w.title() in data: 
        return data[w.title()]  

  elif w.upper() in data: 
        return data[w.upper()]      

  elif len(matches)>0:
    print( "Did you mean {} instead ?".format(matches[0]) )
    inp = input("y/n  \n")
    if (inp == "Y" or inp =="y"):
      return data[matches[0]]

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
    print("{} . {}".format(i, item))
    i = i+1
else:
  print(out)

