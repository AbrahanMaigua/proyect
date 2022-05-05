from flask import Flask, flash, render_template, request, flash

import os

path = os.getcwd() 

app = Flask(__name__, template_folder='tamplate')

print(app.template_folder)

@app.route('/')
def leson():
  title='Abecedario'
  return render_template('leson.html', title=title)



if __name__ == "__main__":
  app.run(
    debug=True

  )