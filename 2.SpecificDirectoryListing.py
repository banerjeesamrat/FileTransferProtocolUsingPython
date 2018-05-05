"""

Author: Samrat Banerjee
Date: 05/05/2018
Description: Specific Directory Listing named pub

"""

import ftplib	                    # ftplib is the library that implements FTP protocol in Python

ftp = ftplib.FTP("ftp.nluug.nl")	# Using ftp mirror of Netherlands Linux Users group
ftp.login()	                        # ftp login with anonymous user and password anonymous@

data = []

ftp.cwd('/pub/')                    # change directory to /pub/
 
ftp.dir(data.append)	            # Appending the contents of root directory to empty list, data

ftp.quit()

# Displaying output

for line in data:
    print("-", line)
