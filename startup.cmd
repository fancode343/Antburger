xcopy startup "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /e

@echo off
echo Choose a number between 1 and 10:
set /p choice=

if %choice%==1 (
    xcopy computers\signal1.exe "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /e
    echo File send1 copied.
) else if %choice%==2 (
    xcopy computers\signal2.exe "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /e
    echo File send2 copied.
) else if %choice%==3 (
    xcopy computers\signal3.exe "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /e
    echo File send3 copied.
) else if %choice%==4 (
    xcopy computers\signal4.exe "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /e
    echo File send4 copied.
) else if %choice%==5 (
    xcopy computers\signal5.exe "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /e
    echo File send5 copied.
) else if %choice%==6 (
    xcopy computers\signal6.exe "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /e
    echo File send6 copied.
) else if %choice%==7 (
    xcopy computers\signal7.exe "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /e
    echo File send7 copied.
) else if %choice%==8 (
    xcopy computers\signal8.exe "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /e
    echo File send8 copied.
) else if %choice%==9 (
    xcopy computers\signal9.exe "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /e
    echo File send9 copied.
) else if %choice%==10 (
    xcopy computers\signal10.exe "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /e
    echo File send10 copied.
) else (
    echo Invalid choice or no action for this number.
)

pause
