#!/bin/bash
HOST=ftpupload.net
USER=epiz_25091451
PASSWORD=P@ATRvyJAPufKmr
 
ftp -inv $HOST <<EOF
user $USER $PASSWORD
cd /htdocs/uploads
mput *.html
bye
EOF
