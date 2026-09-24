from websocket import create_connection
import json
import random as rnd
import time
from datetime import datetime

cache = []
tilewidth = 16
tileheight = 8
color = "00ff00"
timestamp = time.time()
global editid
editid = 2

owot = "wss://ourworldoftext.com/test/ws/"
ws = create_connection(owot)

def write(tx, ty, cx, cy, text):
    global cache
    global editid
    editid += 1
    cache += [[tx, ty, cx, cy, timestamp, text, editid, color]]

def send_cache():
    global cache
    time.sleep(1)
    ws.send(json.dumps(
    {
        "kind": "write",
        "edits": cache
    }
    )
    )
    cache = []

def writestr(tx, ty, cx, cy, string):
    basecx = cx
    basetx = tx
    for chars in list(string):
        cx += 1
        if chars == '\n':
            cy += 1
            cx = basecx
            tx = basetx
            chars = ''
        if cx >= 16:
            tx += 1
            cx = 0
        if cy < 0:
            ty -= 1
            cy = 7
        if cy >= 8:
            ty += 1
            cy = 0
        write(ty, tx, cy, cx, chars)
    send_cache()


"""#templates
                {
  "kind": "write",
  "edits": [
    [tx, ty, cx, cy, timestamp, text, editid, color]
  ]
}
{
    "kind": "link", 
    "type": "url", 
    "data": {
		"tileY": ty, "tileX": tx,
		"charY": cy, "charX": cx,
		"url": url
    }
}
"""

"""
while True:
    try:
        now = datetime.utcnow()
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
        writestr(-1, -2, 0, 6, timestr)
        print(timestr)
    except ConnectionResetError:
        time.sleep(5)
        print('ConnectionResetError')
"""

