from flask import Flask, redirect, render_template
import sqlite3

app = Flask(__name__)

#function to remap list
def dictDish(args):
    return {
       'id': args[0],
       'dish_name': args[1],
       'description': args[2]
    }
  
db = sqlite3.connect('dishes.db');
cursor = db.cursor()
cursor.execute("SELECT * FROM dishes")
dishes = cursor.fetchall()
dishesList = list(map(dictDish, dishes))

#get all dishes
@app.route('/')
def index():
  dish_name = [i['dish_name'] for i in dishesList]
  return render_template('./index.html', dish_name=dish_name)

#get a dish with name and description
@app.route('/dish/<index>')
def showDish(index):
  return render_template('./dish.html', dish=dishesList[int(index)])
  
if __name__ == "__main__":
  app.run(debug=True)