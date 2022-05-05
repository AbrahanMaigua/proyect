import sqlite3

class database():
  def __init__(self, name='palabras.sql'):
    self.name = name
    self.table = ''

  def open_db(self):
    self.database = sqlite3.connect(self.name, timeout=20)
      
    return self.database

  def create_table(self,name: str, row:dict):
    '''
    name: str: is name of table in database
    row: dict: content of table
    return 200 if surcce
    return 404 if error

    '''
    print(row.keys())
    self.database = self.open_db()
    cur  = self.database.cursor()
    cont = ''
    for value in row.keys():
      cont += '\n' + value + ' ' + row.get(value) + ','
      
    sql = f'''CREATE TABLE IF NOT EXISTS {name} ({cont[:-1]});'''
    print(sql)

    cur.execute(sql)
    self.database.close()
    return 200 
  
  def add_columna(self, table, row):
    self.database = self.open_db()
    cur = self.database.cursor()
    cont = ''
    for value in row.keys():
      cont += '\n' + value + ' ' + row.get(value) + ','
    sql = f'''ALTER TABLE {table} ADD {cont[:-1]};'''

    cur.execute(sql)
    # validasmo y cerramos la base de datos 
    self.database,commit()
    self.database.close()

  def insert(self, table: str, value: tuple):
    '''
    table: str: is name table insert value
    value: tuple: content examplo [
      (word, palabra),
      (code, codigo),

    ]
    '''
    self.database = self.open_db()
    cur  = self.database.cursor()
    cont = '?,' * (len(value[0]))
    print(cont)
    if len(value) == 1:
      sql = f'''INSERT INTO {table} VALUES ({cont[:-1]});'''
      cur.execute(sql, value[0])

    if len(value) >= 2:
      sql = f'''INSERT INTO {table} VALUES ({cont[:-1]});'''
      cur.executemany(sql, value)
    
    print(sql)
    self.database.commit()
    self.database.close()

    
    return 200 
  
  def delete(self, table, ID=int , action='ID'):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :param action: ALL, ID
    :return:
    """
    self.database = self.open_db()
    cur =  cur  = self.database.cursor()

    if action == 'ID':
      sql = f'''DELETE FROM {table} WHERE id=?'''
      cur.execute(sql, (ID,))

    if action == "ALL":
      sql = f'''DELETE FROM {table}'''
      cur.execute(sql)

    self.database.commit()
    self.database.close()


  
  def update(self, table: str , value: tuple):
    """
    :param :
    :return:
    """
    cont = '?, ' * (len(value) + 1)
    sql = f'''UPDATE {table} set ({cont[:-1]})'''
    self.database = self.open_db()
    cur  = self.database.cursor()
    cur.execute(sql, value)
    self.database.commit()
    self.database.close()

  def select(self, table):
    
    sql = f'''SELECT * FROM {table}'''
    self.database = self.open_db()
    cur  = self.database.cursor()
    cur.execute(sql)
    date = cur.fetchall()
    self.database.close()

    return date