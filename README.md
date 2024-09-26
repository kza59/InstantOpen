# InstantOpen
A way to instantly open the workspace that you desire, works on windows system. WIP

Have you ever wanted to open vscode, the terminal, and your favorite coding website, and configure them, side by side, just the way you want, but it's kinda annoying? Now you can simply press a single button to open your workspace of choice.

# Features
-Can create new desktop and open all programs there simply by adding x.new to the start of your config.txt file
-Opens files even if they are in wsl file system
-Can open links to the internet in chrome, pdfs in foxit pdf reader
-Compiles to executables you can easily run in windows start menu

# Dependencies:
Please check the requirements.txt. Note: It may not include all dependencies.`

# How to use:
1. Make sure you have all the dependencies installed.
2. There is a config directory in both the dist directory and the actual project folder itself. These need to match, for example if you have a config1.txt file you need it in both config folders.
3. Once you have all these things set up, make sure you are on windows. Open up powershell, navigate to the project, and run the instantOpen script, by doing .\InstantOpen.bat
4. This will compile all the exe files based on your config.txts. You will see the exe files show up in the dist folder.



