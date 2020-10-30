def Run():
  text = input()
  resul = checkio(text,'[')
  print(resul)

#составить список скобок
#беру первую скобку и смотрю, где есть ее закрывающая пара, если закрывающая не содержит в себе пары скообок

def checkio(text,bracket):
  list_brackets = []
  print(text)
  for i in text:
    if i in "[](){}":
      list_brackets.append(i) 
  if len(list_brackets) == 0: 
    return True
  elif all(list_brackets.count(opening) == list_brackets.count(closing)
    for opening, closing in zip("[({", "])}")):
    print(list_brackets)
    try:
      for j in len(list_brackets):
        print(j) 
        if list_brackets[j] == "(" and list_brackets[j+1] == ")":
          list_brackets.pop(j)
          list_brackets.pop(j)
          
        elif list_brackets[j] == "{" and list_brackets[j+1] == "}":
          list_brackets.pop(j)
          list_brackets.pop(j)
          
        elif list_brackets[j] == "[" and list_brackets[j+1] == "]":
          list_brackets.pop(j)
          list_brackets.pop(j)
    except:
      if len(list_brackets)==0:
        return True
      else: return (not list_brackets)
  else:
    return False