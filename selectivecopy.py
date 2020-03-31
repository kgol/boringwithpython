import os, shutil, re
import pathlib
from pathlib import Path

p = Path.home()
d = 'Desktop/BoringwithPythob/temp'
d1 = 'Desktop/BoringwithPythob/new_temp'
print(p)
fileRegex = re.compile(r'.*\.(jpg)')
reg_expres = '.*\.(jpg)'

for folderName, subfolders, filenames in os.walk(p/d):
    for files in filenames:
        m = fileRegex.search(files)
        if m != None:
            x= os.path.join(folderName, files)
            shutil.copy(x, '/home/karol/Desktop/BoringwithPythob/new_temp' )
        
print('All %s files copied to %s' %(reg_expres, d1))




  


