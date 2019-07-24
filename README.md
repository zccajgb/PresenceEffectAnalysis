# PresenceEffectAnalysis
## Setup Instructions
1. create a github account
2. Install git for windows https://git-for-windows.github.io/
3. install VS code https://code.visualstudio.com/download
4. Install Python https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe
5. Install Pip https://bitbucket.org/pcarbonn/pipwin/downloads/pip-Win_1.9.exe
6. Control Panel > System and Security > System > Advanced System Settings
    1. double click User Variables for Olja > Path
    2. Add "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python37"
7. open VS code
    1. click the papers in the top right corner and set the folder you want to use
    2. terminal > new terminal
    3. run command 
        1. got config --global user.name "Olja Sutskova"
        2. git config --global user.email "email@example.com"
        3. git clone https://github.com/zccajgb/PresenceEffectAnalysis.git
        4. click the squre with on the left hand side (extensions)
        5. install python extensions
        6. install pylint
    4. press ctrl + shift + p 
        - python: select interpreter, enter, enter
8. Control Panel > System and Security > System > Advanced System Settings
    1. double click System Variables > Path
    2. Add "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python37\Scripts"
9. Close vs code then reopen
    - in terminal 
        1. pip install pandas
        2. pip install matplotlib
        3. pip install seaborn
        4. pip install scipy


## Other Links
 - this seems exactly what you want https://pythonfordatascience.org/anova-python/



