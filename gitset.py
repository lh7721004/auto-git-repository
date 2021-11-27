import os
import time
url = "https://github.com/lh7721004/auto-git-repository.git"
path = ""
os.system("cd "+path)
os.system("git init")
time.sleep(3)
os.system("git add .")
time.sleep(3)
os.system("git commit -m \"first commit\"")
time.sleep(3)
os.system("git branch -M main")
time.sleep(3)
os.system("git remote add origin "+url)
time.sleep(3)
os.system("git push -u origin main")