# text-to-audiobook

The script that allows you in some degree to convert pdf-books into audio-books. With some limitations I must say...

Here is the guide on how to use it:
1. First start by finding the book you want to convert. For now it can only work with pdfs. I fouind a book here: https://annas-archive.org/
The first issue you might encouter, is that everything, written down in the pdf will be inculded in the audiobook. I could not find an easy way around it, but will look for a sollution in the future. For now it is best to use books that are completely just text, that works best. 
2. One of the issues I encountered was, that most free software has a character limitation, usually at aboput 5000 for a request. Which is not in any way enough for a book. I decided to split the pdf into pages, and make the conversion for each page. To do that, i recommend splitting your pdf into all of the pages using: https://www.ilovepdf.com/split_pdf. It is free and super quick. Then upload it all to pdf-pages/book-name <- Choose the name here. Just be sure to set the path in main.py. called directory.
3. It uses google cloud, so you will need to create a free account and activate the text to speech module they provide. You will also need an API key, so just create one in the link: https://console.cloud.google.com/apis/credentials. I recommend saving it as an environmental variable just in case. For obvious reasons. Also, the module really does not recommend using a http request for this, but hey, that was my assignment so I did it anyway, following some guides on stacked. They have their own guide on how to implement it directly into code, but havent gotten to that yet.
4. The more pages it will ahve the longer it will take, but I provided a progress bar for you to wait. A page usually takes 10 seconds, so you can do the calculations :D.

Some requirements outside of requirements.txt:
You absolutelly need ffmpeg. The python extension uses it to combine the all of the files into one long audio book! You can download it here: https://ffmpeg.org/download.html#build-windows and follow this guide to install: https://www.wikihow.com/Install-FFmpeg-on-Windows
NOTE: this is for windows and the script was written for windows. THe paths should not work if you are trying to run it on mac. But will figure out how to fix it at a future date.

Future improvements:
1. I would like the app to be able to locally split the pdf into pages to be used for conversion. For now I use an external website [here](https://www.ilovepdf.com/split_pdf). 
2. I would like for it to be able to open zip files, and read the pages as well, for compression and quicker use.
3. I want to implement a GUI, so you can pick and choose where to save the file, where to read them from etc. Might be easier to use than hardcoding paths like it does here.
4. I am not sure it will work on a mac environment. So that needs to be addressed.
5. In general the code is messy I think, and a lot can be improved and made more efficient.
