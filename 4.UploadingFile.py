"""

Author: Samrat Banerjee
Date: 05/05/2018
Description: Uploading a File

"""

import ftplib	                    # ftplib is the library that implements FTP protocol in Python
import os                           # OS module in Python provides a way of using operating system dependent functionality

def upload(ftp, file):
    ext = os.path.splitext(file)[1]     # splitext is to get the extension of the file
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))   # storlines-Store a file in ASCII transfer mode
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)      # storbinary-Store a file in binary transfer mode

ftp = ftplib.FTP("127.0.0.1")
ftp.login()	                        # ftp login with anonymous user and password anonymous@

upload(ftp, "FileToUpload.txt")
