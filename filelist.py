import os
import random


f = []
for (dirpath, dirnames, filenames) in os.walk('/run/media/krushn/Savneet/python/'):
    f.extend(filenames)
    break
#print(f)




for file in f:
    d = str(random.randint(1,5)).zfill(2)+str(random.randint(1,30)).zfill(2)
    os.system('sudo date +%Y%m%d -s "2018'+ d +'"')
    
    
    os.system("git add "+ file)
    os.system("git commit -m '"+ file +" added'")

