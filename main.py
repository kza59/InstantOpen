import pyautogui
import time
import subprocess
import psutil
import os
import subprocess #we need this to open subprocesses
import logging
#"C:\Microsoft VS Code\Code.exe"
FILE_PATH1 = FILE_PATH1 = "/mnt/c/Microsoft VS Code/Code.exe"
FILE_PATH3 = FILE_PATH3 = "/mnt/c/Program Files (x86)/Foxit Software/Foxit PDF Reader/FoxitPDFReader.exe"
def openThing(filePath): #opens a file on the computer. For example, if your filePath is: "C:\Users\16043\Desktop\Desmos _ Scientific Calculator.html" it will open that
    try:
        subprocess.Popen(filePath)
        print(f"Opened {filePath}")
    except Exception as e:
        print(f"Failed to open {filePath}: {e}")

    
def closeThing(filePath):  #closes a file on the computer
    process_name = os.path.basename(filePath)
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            process.terminate()
            print(f"Terminated {process_name}")
            break
    else:
        print(f"No process found for {filePath}")
    

EXECUTABLES = {FILE_PATH1, FILE_PATH3}
for EXE in EXECUTABLES:
    openThing(EXE)


    
