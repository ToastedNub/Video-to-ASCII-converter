# Video-to-ASCII-converter
Converts a video file to ASCII in the command prompt. [Like those videos you see of Bad Apple played in various things](https://youtu.be/6zs6S_I5gH8).


 - YOU NEED THE VIDEO YOU WANT TO CONVERT TO BE IN THE SAME FOLDER AS THE SCRIPT IS IN OR IT WILL NOT WORK!

 - THE VIDEO IN THE FOLDER SHOULD BE HAMED "video" THIS IS THE FILE NAME THAT THIS SCRIPT TARGETS!

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 - For this to work you need Python, which is in the files already, run the "Python" file, and this will bring you to the Python download.

 - Alternative Python Link: https://www.python.org/ftp/python/3.12.5/python-3.12.5-amd64.exe

 - You will also need Visual Studio Code, so you can install the scripts dependencies.

 - Open the Python script (the file named "console") in the zip you just downlaoded from this repository, then click "TERMINAL" at the top left, and click "NEW TERMINAL"

 - Inside that terminal (the new box at the bottom of VS Code) enter this command.

 - Command: pip install opencv-python numpy pillow

 - Save your script if you have made any changes, like the resolution (HEIGHT and WIDTH at the top of the script).

 - Once you have everything installed and ready, you can start the script by running the "start" file.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 - You do not need a good computer to run this script, all the frame processing happens before the video plays in the console.

 - If you open the console and nothing shows up, its just blank, that is nowmal, leave it alone so it can process the video frames.

 - After every frame has been processed, the script will start the console playback and open your video at the same time.

 - The console playback and the video file might not be perfectly synced up, depending on how fast your computer is, but there is an easy solution to this!

 - If your computer is too slow to render both the video and console playback at the same time, you can record the playback, and edit in the video or audio!

 - If you record it, you technically only need to record at 24fps and it will look normal!
