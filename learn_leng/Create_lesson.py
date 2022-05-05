import sys
import os
from datetime import datetime, date, time, timezone
path = os.getcwd() + r'\bin\utili'
sys.path.insert(0, path )

from db import *
class content():
  def __init__(self) -> None:
      self.leng_primary  = 'es'
      self.leng_secudary = 'pt'
      self.leng =  self.leng_primary + '-' + self.leng_secudary
      self.db   = database()

    
  def config(self):
    print(
      'leng: ', self.leng,
      '1) change leng.'
    )
    option = input('select number option: ')
    if option -- 1:
      leng = ('es', 'pt', 'en')
      print(leng)
      self.leng = input('lengues: ', 5)
      self.leng_primary, self.leng_secudary = self.leng.split('-')
      
  def create_date(self):
    print(
      'leng: ', self.leng,
      '1) change leng.'
    )
    option = input('select number option: ')
    
  def save(self, table, leng1, leng2):
    self.db.insert(table, [leng1, leng2])



if __name__ == "__main__":
  print('cli')
  db = database()
  db.create_table('es', {
    'text':'TEXT NOT NULL',
  })
  db.create_table('pt', {
    'text':'TEXT NOT NULL',
  })
  word1 = list()
  word2 = list()

  while True:
    print(
    '-i insert\n',
   # '-u Update\n', 
   # '-d delete\n'
   )
    option = input('\nselct option: ')
    if option[:2] == '-i':
      leng1 = input('es: ')
      leng2 = input('pt: ')
      db.insert('es', (leng1))
      db.insert('pt', (leng2))


