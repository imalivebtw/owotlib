from websocket import create_connection
import json
import time
from datetime import datetime

tilewidth = 16
tileheight = 8
color = "#ffffff"
timestamp = time.time()
global editid
editid = 1

owot = 'wss://ourworldoftext.com/ws/'
ws = create_connection(owot)

def write(tx, ty, cx, cy, text):
    time.sleep(1/25)#make it faster if you want but you could get ratelimited
    global editid
    editid += 1
    ws.send(json.dumps(
        {
  "kind": "write",
  "edits": [
    [tx, ty, cx, cy, timestamp, text, editid, color]
  ]
}
))

def writestr(tx, ty, cx, cy, string):
    for chars in list(string):
        cx += 1
        if cx >= 16:
            tx += 1
            cx = 0
        write(ty, tx, cy, cx, chars)

def batch_write(batch):
    ws.send(json.dumps(
        {
  "kind": "write",
  "edits": batch
}
))

def fill(txmin, tymin, txmax, tymax, char):
   for a in range(txmin, txmax+1):
      for b in range(tymin, tymax+1):
         print(f'x:{a}, y:{b}')
         for c in range(tilewidth):
            for d in range(tileheight):
               write(a, b, c, d, char)
               time.sleep(1/100)




wipe_batch = []

editid = 0

def gen_batch(char, tx, ty):
    for x in range(8):#this works (somehow)
        for y in range(16):#dont touch it
            timestamp = int(time.time())
            row = [tx, ty, x, y, timestamp, char, editid, color]
            wipe_batch.append(row)

"""#uncomment this to get a clock at the owot spawn
while True:
    try:
        now = datetime.now()
        timestr = now.strftime('%H:%M:%S')
        timestr = timestr.replace("0", "🯰")
        timestr = timestr.replace("1", "🯱")
        timestr = timestr.replace("2", "🯲")
        timestr = timestr.replace("3", "🯳")
        timestr = timestr.replace("4", "🯴")
        timestr = timestr.replace("5", "🯵")
        timestr = timestr.replace("6", "🯶")
        timestr = timestr.replace("7", "🯷")
        timestr = timestr.replace("8", "🯸")
        timestr = timestr.replace("9", "🯹")
        writestr(-1, 1, 11, 0, timestr)
        print(timestr)
    except ConnectionResetError:
        time.sleep(5)
        print('ConnectionResetError')
    except:
        time.sleep(5)
        print('error')
"""
bunny = [
    [-2, -1, 7, 13, timestamp, '(', editid, color],
    [-2, -1, 7, 14, timestamp, '_', editid, color],
    [-2, -1, 7, 15, timestamp, '_', editid, color],
    [-2, 0, 7, 0, timestamp, '_', editid, color],
    [-2, 0, 7, 1, timestamp, ')', editid, color],
    [-2, -1, 6, 13, timestamp, '(', editid, color],
    [-2, -1, 6, 14, timestamp, '0', editid, color],
    [-2, -1, 6, 15, timestamp, '-', editid, color],
    [-2, 0, 6, 0, timestamp, '0', editid, color],
    [-2, 0, 6, 1, timestamp, ')', editid, color],
    [-2, -1, 5, 13, timestamp, '(', editid, color],
    [-2, -1, 5, 14, timestamp, '\\', editid, color],
    [-2, -1, 5, 15, timestamp, '(', editid, color],
    [-2, 0, 5, 0, timestamp, '\\', editid, color]
]

n1 = [
    [0, 0, 0, 0, timestamp, '█', editid, color],
    [0, 0, 0, 1, timestamp, '█', editid, color],
    [0, 0, 0, 2, timestamp, '█', editid, color],
    [0, 0, 0, 3, timestamp, '█', editid, color],
    [0, 0, 1, 0, timestamp, '█', editid, color],
    [0, 0, 1, 1, timestamp, '█', editid, color],
    [0, 0, 1, 2, timestamp, '█', editid, color],
    [0, 0, 1, 3, timestamp, '█', editid, color],
    [0, 0, 2, 0, timestamp, '█', editid, color],
    [0, 0, 2, 1, timestamp, '█', editid, color],
    [0, 0, 2, 2, timestamp, '█', editid, color],
    [0, 0, 2, 3, timestamp, '█', editid, color]
]

n2 = [
    [0, 0, 0, 0, timestamp, '▀', editid, color],
    [0, 0, 0, 1, timestamp, '▀', editid, color],
    [0, 0, 0, 2, timestamp, '▀', editid, color],
    [0, 0, 0, 3, timestamp, '▀', editid, color],
    [0, 0, 1, 0, timestamp, '▀', editid, color],
    [0, 0, 1, 1, timestamp, '▀', editid, color],
    [0, 0, 1, 2, timestamp, '▀', editid, color],
    [0, 0, 1, 3, timestamp, '▀', editid, color],
    [0, 0, 2, 0, timestamp, '▀', editid, color],
    [0, 0, 2, 1, timestamp, '▀', editid, color],
    [0, 0, 2, 2, timestamp, '▀', editid, color],
    [0, 0, 2, 3, timestamp, '▀', editid, color]
]

"""
while True:#animation
  time.sleep(3/5)
  batch_write(n1)
  time.sleep(3/5)
  batch_write(n2)
"""

"""
while True:#this code is now obsolete
    write(0,0,0,0,'▚')
    time.sleep(1/20)
    write(0,0,1,0,'▚')
    time.sleep(1/20)
    write(0,0,2,0,'▚')
    time.sleep(1/20)
    write(0,0,3,0,'▚')
    time.sleep(1/20)
    write(0,0,4,0,'▚')
    time.sleep(1/20)
    write(0,0,5,0,'▚')
    time.sleep(1/20)

    write(0,0,0,0,'▞')
    time.sleep(1/20)
    write(0,0,1,0,'▞')
    time.sleep(1/20)
    write(0,0,2,0,'▞')
    time.sleep(1/20)
    write(0,0,3,0,'▞')
    time.sleep(1/20)
    write(0,0,4,0,'▞')
    time.sleep(1/20)
    write(0,0,5,0,'▞')
    time.sleep(1/20)
"""
