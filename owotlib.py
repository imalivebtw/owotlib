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
    time.sleep(1/100)#make it faster if you want but you could get ratelimited
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
    basecx = cx
    for chars in list(string):
        cx += 1
        if chars == '@':
            cy += 1
            cx = basecx
            chars = ''
        if cx >= 16:
            tx += 1
            cx = 0
        if cy >= 8:
            ty += 1
            cy = 0
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
