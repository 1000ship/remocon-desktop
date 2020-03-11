
# Remocon for Desktop
you should use with 'https://github.com/1000ship/remocon-web'
Python and Javascript use websocket

## file set
- remocon.py : now, testing

## info
- Need Lib : asyncio, websockets, pyautogui, opencv-python, qrcode
- 'opencv-python' is optional, but it will enhance program speed

## PyInstaller Build
- folder 단위로 빌드
> sudo pyinstaller --icon appicon.ico -y --onedir --osx-bundle-identifier me.1000ship.remocon --hidden-import=tkinter --hidden-import=pyautogui --hidden-import=websockets --hidden-import=qrcode --hidden-import=asyncio --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' main.py
- app 파일 빌드
> sudo pyinstaller -N 'Remocon' --windowed --icon appicon.ico -y --onefile --osx-bundle-identifier me.1000ship.remocon --hidden-import=tkinter --hidden-import=pyautogui --hidden-import=websockets --hidden-import=qrcode --hidden-import=asyncio --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' main.py