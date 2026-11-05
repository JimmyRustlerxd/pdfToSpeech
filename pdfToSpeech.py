#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3
import PyPDF2


# In[23]:


speak = pyttsx3.init(driverName="sapi5")


# In[25]:


if __name__ == "__main__":
    text = open(input("Enter PDF adress"),'rb')
    pdf = PyPDF2.PdfReader(text)
    for page in pdf.pages:
        words = page.extract_text()
        print(words)
        if words:
            speak.say(words)
    speak.runAndWait()
    text.close()


# In[ ]:




