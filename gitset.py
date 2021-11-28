import os
import time
import pickle
try:
    with open("count.pickle","rb") as f:
        count = pickle.load(f)
except:
    count = 1

print("count value is",count)





url = "https://github.com/lh7721004/auto-git-repository.git"
path = ""
os.system("cd "+path)
os.system("git init")
time.sleep(3)
os.system("git add .")
time.sleep(3)
if count == 1:
    os.system("git commit -m \"1st commit\"")
elif count == 2:
    os.system("git commit -m \"2nd commit\"")
elif count == 3:
    os.system("git commit -m \"3rd commit\"")
else:
    os.system("git commit -m \""+str(count)+"th commit\"")
time.sleep(3)
os.system("git branch -M main")
time.sleep(3)
os.system("git remote add origin "+url)
time.sleep(3)
os.system("git push -u origin main")

with open("count.pickle","wb") as f:
    pickle.dump(count,f)
    print("pickle file dumped")