
# 🎮 Remocon for Desktop
 You should use with 'https://github.com/1000ship/remocon-web'

 Python and Javascript use websocket

![](_readme/testing.gif)

My blog post(Korean)

=> https://blog.naver.com/cjstjdgur123/221843365322  

## 📂 File set
- main.py : this is main program, managing gui
- remocon.py : about web-socket server and use pyautogui

## 📦 You should install these librarys before using
- Need Lib : asyncio, websockets, pyautogui, opencv-python, qrcode, pyinstaller
- 'opencv-python' is optional, but it will enhance program speed
- 'pyinstaller' is for build

## 🏗 PyInstaller Build
- folder 단위로 빌드 (Build to folder with pyInstaller)
```bash
sudo pyinstaller --clean -n 'Remocon' --icon appicon.ico -y --onedir --osx-bundle-identifier me.1000ship.remocon --hidden-import=tkinter --hidden-import=pyautogui --hidden-import=websockets --hidden-import=qrcode --hidden-import=asyncio --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' main.py
```



- app 파일 빌드 (Build to app file with pyInstaller)
```bash
sudo pyinstaller --clean -n 'Remocon' --windowed --icon appicon.ico -y --onefile --osx-bundle-identifier me.1000ship.remocon --hidden-import=tkinter --hidden-import=pyautogui --hidden-import=websockets --hidden-import=qrcode --hidden-import=asyncio --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' main.py
```

