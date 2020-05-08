#nano Ftp.sh

#!/bin/sh
$HOST='ftpupload.net'
$USER='epiz_25091451'
$PASSWD='ATRvyJAPufKmr'
#$FILEtoPut='myFile1'
#$FILEtoGet='myFile2'
$FILEtoDelete='sample.pdf'

ftp -n $HOST <<END_SCRIPT
quote USER $USER
quote PASS $PASSWD

#put $FILEtoPut
get $FILEtoGet
delete $FILEtoDelete

quit
END_SCRIPT
exit 0

chmod +x Ftp.sh
