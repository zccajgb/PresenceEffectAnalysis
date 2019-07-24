# PresenceEffectAnalysis
## Setup Instructions
- create a github account
- Install git for windows https://git-for-windows.github.io/
- install VS code https://code.visualstudio.com/download
- Install Python https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe
- Install Pip https://bitbucket.org/pcarbonn/pipwin/downloads/pip-Win_1.9.exe
- Control Panel > System and Security > System > Advanced System Settings
    - double click User Variables for Olja > Path
    - Add "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python37"
- open VS code
    - click the papers in the top right corner and set the folder you want to use
    - terminal > new terminal
    - run command 
        - got config --global user.name "Olja Sutskova"
        - git config --global user.email "email@example.com"
        - git clone https://github.com/zccajgb/PresenceEffectAnalysis.git
        - click the squre with on the left hand side (extensions)
        - install python extensions
        - install pylint
    - press ctrl + shift + p 
        - python: select interpreter, enter, enter
- Control Panel > System and Security > System > Advanced System Settings
    - double click System Variables > Path
    - Add "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python37\Scripts"
- Close vs code then reopen
    - in terminal 
    - pip install pandas
    - pip install matplotlib
    - pip install numpy
    - pip install scipy



