
rem Con esta línea le estamos diciendo que tiene que empezar por la función main
rem With this line we are telling you that you have to start with the main function
@echo off&cls&call:main %1&goto:EOF

:main
    title tipolisto-test2MP3
    rem Ckequeando parámetros
    if [%1]==[] (call :compile)
    if [%1]==[create] (call :compile)
    if [%1]==[win] (call :win)
    if [%1]==[play] (call :play)
    if [%1]==[exe] (call :exe)
    if [%1]==[clean] (call :clean)
    rem Si el argumento no está vacío, ni es compile, ni es clear, etc
    if [%1] NEQ [] (
        if [%1] NEQ [compile] ( 
            if [%1] NEQ [win] (
                if [%1] NEQ [play] (
                    if [%1] NEQ [exe] (
                        if [%1] NEQ [clean] ( 
                            if [%1] NEQ [help] (
                                if [%1] NEQ [clean] (call :help) 
                            }
                        }
                    }
                }
            }
        )
    )    
goto:eof


:clean
    echo escogiste borrar
    del /F /Q "*.mp3"
    rmdir /S /Q build
    rmdir /S /Q dist
    del /F /Q "*.spec"

goto:eof

:compile
    echo "Compilando text2mp3."
    src\text2mp3\text2mp3.py archivo.txt
goto:eof

:play
    echo reproduciendo audio
    rem https://github.com/portapps/vlc-portable/releases
    vlc\vlc-portable.exe ..\..\text.mp3 
goto:eof

:exe
     echo vamos a crear el ejecutable para windows
     rem pyinstaller --windowed --onefile --icon=./data/icon.ico text2mp3.py
     pyinstaller --onefile --icon=./data/icon.ico src\text2mp3\text2mp3.py
goto:eof