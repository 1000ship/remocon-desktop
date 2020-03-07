import asyncio;
import websockets;
import pyautogui as gui
import threading
import time
import socket
import qrcode

stackIn = []
stackOut = []

SOCKET_IP = socket.gethostbyname_ex( socket.gethostname() )[-1][-1]
SOCKET_PORT = 2362
webClientURL = "http://1000sh.iptime.org:8000/list/HDD1/1000sh-disk/_page/remocon?ip={}&port={}".format( SOCKET_IP, SOCKET_PORT );
img = qrcode.make(webClientURL)
img.save("qrcode.png")

print( "IP : {}".format( SOCKET_IP ) )
print( "Port : {}".format( SOCKET_PORT ) )

def guiProcess ():
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
threading.Thread(target=guiProcess).start()

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

print("Client: ", webClientURL)
print("Try connect")
start_server = websockets.serve(accept, "0.0.0.0", SOCKET_PORT);
asyncio.get_event_loop().run_until_complete(start_server);
asyncio.get_event_loop().run_forever();