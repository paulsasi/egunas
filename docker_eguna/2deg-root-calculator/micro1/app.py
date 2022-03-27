from flask import Flask, render_template, request
import sqlite3
from os.path import dirname, abspath
from dataclasses import dataclass
import json
import random
import string
import time
import os

app = Flask(__name__)

DATABASE_FILE = str(dirname(abspath(__file__))) + '/db/test.db'
SAVE_PATH = str(dirname(abspath(__file__))) + '/data/'
TABLE_NAME= 'coordinates'

@dataclass
class Coordinates:
    A: float
    B: float
    C: float

    def push_to_database(self, db_path = DATABASE_FILE, table= TABLE_NAME):
        print('DB PATH: {}'.format(db_path))

        con = sqlite3.connect(db_path)

        cur = con.cursor()

        cur.execute('''INSERT INTO {} (a, b, c) VALUES ({}, {}, {});'''.format(table, self.A, self.B, self.C))

        con.commit()

        con.close()

    def dump(self):
        return json.dumps([self.A , self.B, self.C])


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        #Coeficients
        req = request.form

        # y = Ax² + Bx + C
        try:
            A:float = float(req.get("A"))
        except:
            print('A not a number!')

        try:
            B: float = float(req.get("B"))
        except:
            print('B not a number!')

        try:
            C:float = float(req.get("C"))
        except:
            print('C not a number!')


        #Init Coordiantes object
        cords = Coordinates(A, B, C)

        #Push into the database
        cords.push_to_database()

        #Write content in txt file

        file_content = cords.dump()
        name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        f = open(SAVE_PATH + name + '.txt', "w")
        f.write(file_content)
        f.close()

        #Read file (if it s not present, wait)
        limit_time = 0
        while not os.path.exists(SAVE_PATH + name + '_results.txt'):
            time.sleep(1)
            limit_time += 1
            if limit_time == 5:
                break

        if os.path.isfile(SAVE_PATH + name + '_results.txt'):
            g = open(SAVE_PATH + name + '_results.txt', "r")

            content = g.read()
            content = json.loads(content)
            x = content['x']
            y = content['y']
            g.close()
            os.remove(SAVE_PATH + name + '_results.txt')
        else:
            print('Result file not found!')
            x = [0]
            y = [0]

        data = zip(x, y)
        return render_template('result.html', data=data)

    return render_template('home.html')

app.run(debug=True, host='0.0.0.0')