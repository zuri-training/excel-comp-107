# file-comp-107
Dashboard.
I Designed the upload form in the Dashboard, using Javascript. 
It should upload atomatically. 
I did not link it to django.
In the Javascript script.js . the code         (" xhr.open("POST", "py/upload.py"); //sending post request to the specified URL-------POST REQUEST HERE!!!!!!!")
send a post request to django to upload the formdata.
replace "py/upload.py" with the url to the form where the upload code will be written.

The folder file. Is where the uploaded file will be stored.

The "upload.py" or url you chose to use. Should contain, some requirement before final upload to folder file.
#  getting file name
#  getting temp_name of file
#  making file name dynamic by adding time before file name
#  moving file to the specified folder with dynamic name

