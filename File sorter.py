#!/usr/bin/env python
# coding: utf-8

# In[10]:


import os, shutil;
path=r"C:/Users/yamin/OneDrive/Pictures/file sorter/"
f_name= os.listdir(path)
os.listdir(path)
folder_name=['xlsx files', 'jpg files', 'txt files']

for loop in range(0,3):
    if not os.path.exists(path + folder_name[loop]):
        os.makedirs(path+folder_name[loop])
        
for file in f_name:
    if '.xlsx' in file and not os.path.exists(path+'xlsx files/'+file):
        shutil.move(path+file, path+'xlsx files/'+file)
    elif '.jpg' in file and not os.path.exists(path+'jpg files/'+file):
        shutil.move(path+file, path+'jpg files/'+file)
    elif '.txt' in file and not os.path.exists(path+'txt files/'+file):
        shutil.move(path+file, path+'txt files/'+file)
        


# In[ ]:




