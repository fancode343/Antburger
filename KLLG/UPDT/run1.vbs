Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c 1.bat"
oShell.Run strArgs, 0, false