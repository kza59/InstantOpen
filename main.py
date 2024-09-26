import pyautogui
import time
import subprocess
import psutil
import os
import subprocess #we need this to open subprocesses
import logging
import webbrowser
import pyvda
#"C:\Microsoft VS Code\Code.exe"



import os
import subprocess

def openThing(filePath):
    try:
        if filePath.endswith(".new"):
            new_desktop = pyvda.VirtualDesktop.create()
            new_desktop.go()
        if filePath.startswith("\\wsl.localhost"):
            filePath = filePath.replace("\\\\wsl.localhost\\Ubuntu", "/home/kza59")
            filePath = filePath.replace("\\", "/")
            win_file_path = subprocess.run(['wslpath', '-w', filePath], capture_output=True, text=True).stdout.strip()
        else:
            win_file_path = filePath

        if win_file_path.endswith(".html"):
            chromePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            if os.path.exists(chromePath):
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
                webbrowser.get('chrome').open(f'file://{os.path.abspath(win_file_path).replace("\\", "/")}')
                print(f"Opened {win_file_path} in Chrome")
            else:
                print("Chrome is not installed in the default path.")
            return

        if win_file_path.endswith(".pdf"):
            foxit_path = r"C:\Program Files (x86)\Foxit Software\Foxit PDF Reader\FoxitPDFReader.exe"
            if os.path.exists(foxit_path):
                subprocess.Popen([foxit_path, win_file_path], shell=True)
                print(f"Opened {win_file_path} in Foxit PDF Reader")
            else:
                print("Foxit PDF Reader not found.")
            return

        if win_file_path == "/mnt/c/Windows/System32/wsl.exe" or win_file_path == r"C:\Windows\System32\wsl.exe":
            subprocess.Popen(['cmd.exe', '/c', 'start', 'wsl'])
            print("Opened WSL")
            return

        if os.path.exists(win_file_path):
            subprocess.Popen([win_file_path], shell=True)
            print(f"Opened {win_file_path}")
        else:
            print(f"File does not exist: {win_file_path}")

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
    


def readConfig(file_name):
    executablePaths = [] #array of executables as paths
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                path = line.strip()
                executablePaths.append(path)
    except FileNotFoundError:
        print("Config File not found")
    return executablePaths



#main function
if __name__ == "__main__":
    configFile = "configs\\config5.txt"
    EXECUTABLES = readConfig(configFile)
    for EXE in EXECUTABLES:
        openThing(EXE)
