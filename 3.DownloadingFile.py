"""

Author: Samrat Banerjee
Date: 05/05/2018
Description: Downloading a File

"""

import ftplib	                    # ftplib is the library that implements FTP protocol in Python
import sys                          # sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available

def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)  # Retrieve a file in binary transfer mode and wb is writing in binary mode
    except:
        print "Error"

ftp = ftplib.FTP("ftp.nluug.nl")	# Using ftp mirror of Netherlands Linux Users group
ftp.login()	                        # ftp login with anonymous user and password anonymous@

ftp.cwd('/pub/')                    # change directory to /pub/

getFile(ftp,'README.nluug')

ftp.quit()
