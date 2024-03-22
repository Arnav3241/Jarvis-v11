import eel

eel.init("Interface")

o = 0

eel.start("index.html", block=False)

while True:
    eel.sleep(1)
    print(o)
    o += 10