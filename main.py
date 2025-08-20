import os
os.system("unzip *.zip -P @onionsofts")
os.system("python3 -m pip install -r ./OverloadX/Core/requirements.txt")
os.system("python3 ./OverloadX/WEB.py")
