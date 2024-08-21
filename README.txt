Image cleaner will remove metadata (including details and comments) off NovelAI PNGS and other.

Made with the help of ChatGPT, for the purpose of removing metadata from many images at once.

Image_Cleaner.exe should work as a standalone, meaning you can just download the .exe, put it in a folder with images and open the .exe.

It works by making a new folder (cleaned_images) and copying all the images within the folder that the .exe is in, without the metadata, into cleaned_images. Your original files will be untouched with metadata intact. Once they're done, it will create a text file "Images_Are_Ready" with how long it took.

Be careful as if there are any folders within the folder, it might bug out. (Haven't personally had issues, but I'd be careful). This will use your CPU a decent bit, to make the process faster.

If for whatever reason the .exe does not work,
you can try the python script.

Install Python 3 ( I used 3.8)
Download the .py file from github.

Install Dependencies:

Open a terminal (Command Prompt on Windows Windows+R ->cmd, or just search).
Type the following command and press Enter:

pip install pillow

Run the Script:

In the same terminal, navigate to the directory containing your .py file. (navigate to where the .py file is with "cd C:\your\location\here")
Then type the following command and press Enter:

python Image_Cleaner.py

