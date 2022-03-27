import time
import calculator
from os.path import dirname, abspath
import os
import json
from dataclasses import dataclass

@dataclass
class Coordinates:
    A: float
    B: float
    C: float

    def dump(self):
        return json.dumps([self.A , self.B, self.C])

    def compute(self):
        x = [i for i in range(len(range(1000)))]
        y = list(map(lambda x0: self.A * x0 * x0 + self.B * x0 + self.C, x))
        return  json.dumps({'x': x, 'y': y})

WATCH_PATH = str(dirname(abspath(__file__))) + '/data'

def watcher():


    while True:
        files = os.listdir(WATCH_PATH)

        if len(files) != 0:

            for file in files:
                if file[-12:] != '_results.txt' and file[-4:] == '.txt':

                    f = open(WATCH_PATH + '/' + file, 'r')
                    content = f.read()
                    f.close()
                    os.remove(WATCH_PATH + '/' + file)

                    content = json.loads(content)
                    cords = Coordinates(content[0], content[1], content[2])

                    results = cords.compute()

                    new_name = file[:-4] + '_results.txt'
                    g = open(WATCH_PATH + '/' + new_name, 'w')
                    g.write(results)
                    g.close()

            if len(files) > 10:
                break

if __name__ == '__main__':

    watcher()