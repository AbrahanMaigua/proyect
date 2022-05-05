import sys
import os
from datetime import datetime, date, time, timezone
path = os.getcwd() + r'\bin\utili'
sys.path.insert(0, path )

from db import *

memoria = list()

def save(word):
  time = datetime.now()
  for i in memoria:
      
    if word != memoria:
      print(memoria)

    if word == memoria :
      print(memoria)
      
      memoria.append( (word, time.strftime('%c')))

def sepword(text: str):
  """ descomponemos el text
  esto vendiars valiedo O(n2)   """
  text = text.split(' ')  
  for value in text:
    aux = list()
    for i in value:
      aux.append(i)
      
    
  return tuple(aux)

def validate(word, text):
  pos, hits = list(), 0
  a, b= sepword(word.lower()), sepword(text.lower())

  for index in range(len(a)):
    hits += 1
    if a[index] != b[index]:
      pos.append(hits-1)
      print(hits-1, end=' ')
      print(a[index], b[index], a[index] != b[index] )

  return pos, text, word
        
def leam():
  global db
  db    = database()
  words = db.select('word')
  for word in words:
    print(word[0], word[1])  
    text = input(f'que sinifica {word[1]}: ')
    validate(word[0], text)
        
if __name__ == '__main__':
  leam()