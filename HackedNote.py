#!/usr/bin/env python
# coding: utf-8

# In[9]:


from pyautogui import size,click,write,moveTo 
from time import sleep 
from os import system

width,height = pyautogui.size()

pyautogui.click(30,height-15)
pyautogui.write("notepad")
pyautogui.moveTo(50,190,duration=1)
pyautogui.click(50,190)
time.sleep(1)
pyautogui.write("You Have Been Hacked!",interval=0.1)
time.sleep(3)
system("shutdown /s /t 1") 


# In[ ]:





# In[ ]:





# In[ ]:




