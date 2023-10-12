@echo off
setlocal enabledelayedexpansion

rem Find the version
set "file_path=.\Dev\constants.py"
set "search_string=VERSION = '"

for /f "delims=" %%i in ('type "%file_path%" ^| findstr /C:"%search_string%"') do (
    set "line=%%i"
    for /f "tokens=2 delims='" %%j in ("!line!") do (
        set "version=%%j"
        echo Version found: !version!
    )
)

rem Get if the version is a prerelease
set "prerelease="
for /f "tokens=*" %%a in ('type ".\Dev\constants.py" ^| findstr /i "PRERELEASE = True PRERELEASE = False"') do (
    set "line=%%a"
    if "!line:~14,5!"=="True" (
        set "prerelease=-prerelease"
    ) else (
        set "prerelease="
    )
)

rem Get the current date and time in the desired format
for /f "tokens=1-3 delims=/ " %%a in ('date /t') do (
    set "mm=%%a"
    set "dd=%%b"
    set "yyyy=%%c"
)
for /f "tokens=1-2 delims=: " %%a in ('time /t') do (
    set "hh=%%a"
    set "ampm=%%b"
)
rem Adjust the hour if it's 12 AM or 12 PM
if "%hh%"=="12" (
    if /i "%ampm%"=="AM" (
        set "ampm=PM"
    ) else (
        set "ampm=AM"
    )
)
rem Pad single-digit hours, minutes, and seconds with leading zeros
if "%hh:~0,1%"=="0" set "hh=0%hh:~1%"
set "current_datetime=%yyyy%-%mm%-%dd% %hh%-%ampm%"

set a=%~dp0%

rem Set the source and destination directories
set "source=%a%\Dev\"
set "destination=%a%\VersionArchive\v%version%%prerelease% %current_datetime%.zip"

rem Create a temporary folder to copy files into before zipping
set "tempfolder=%a%\temp\"
mkdir "%tempfolder%" 2>nul

rem Copy files from source to the temporary folder recursively
robocopy %source% %tempfolder%\ /MIR /is

rem Create a ZIP archive using 7-Zip
"C:\Program Files\7-Zip\7z.exe" a -tzip "%destination%" "%tempfolder%\*" >nul

@REM rem Delete the temporary folder and its contents
@REM rd /s /q "%tempfolder%

echo Files have been copied to "%destination%"

endlocal