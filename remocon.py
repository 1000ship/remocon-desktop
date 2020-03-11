import asyncio;
import websockets;
import pyautogui as gui
import threading
import time

stackIn = []
stackOut = []

def guiThread ():
    global stackIn, stackOut
    while True:
        try:
            if not stackOut:
                while stackIn:
                    stackOut.append( stackIn.pop() )
            # read
            mouseBias = [0, 0]
            mouseClick = False
            str = None
            while stackOut:
                query = stackOut.pop()
                args = query.split()
                if args[0] == "m":
                    dx, dy = map( int, args[1:] )
                    mouseBias[0] += dx
                    mouseBias[1] += dy
                elif args[0] == "c":
                    mouseClick = True
                elif args[0] == "t":
                    str = " ".join(args[1:])
                elif args[0] == "h":
                    gui.hotkey(*tuple(args[1:]))
                elif args[0] == "ss":
                    gui.screenshot("screenshot.png")
                else:
                    print("What is '{}'".format(query))
            # excute
            gui.move( mouseBias[0], mouseBias[1] )
            if mouseClick:
                gui.mouseDown()
                time.sleep(0.01)
                gui.mouseUp()
                mouseClick = False
            if str != None:
                gui.typewrite(str)
        except Exception as e:
            print(e)
            continue

async def accept(websocket, path):
    global stackIn
    print("Connected")
    while True:
        try:
            data = await websocket.recv();
            stackIn += [data]
        except:
            print("Diconnected... Find another connection")
            break

def socketThread (port, event_loop):
    asyncio.set_event_loop( event_loop )
    wsServer = websockets.serve(accept, "0.0.0.0", port);
    event_loop.run_until_complete(wsServer);
    event_loop.run_forever();

def run ( port ):
    event_loop = asyncio.get_event_loop()
    threading.Thread(target=guiThread).start()
    threading.Thread(target=socketThread, args=[port, event_loop]).start()
    print("Try connect")

if __name__ == "__main__":
    run( port=2362 )