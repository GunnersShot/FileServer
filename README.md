Hi Folks, 

This is my first project of python. It is a simple Python based file server which can be used to upload files on the server and also can be used to host files which can be downloaded.
This Repo contains the folders:
> Download
> Download2
> Upload-Download
> Upload

As the name suggests these are dedicated File servers as per requirement. 
Suppose you just want to use file server to upload something then you may execute the python file from the "Upload" Folder. Or if you require both upload and download functionality then execute the python file from "Upload-Download" folder. 
Each folder has the python code file with extension .py, a template folder and an "UploadedFiles" folder(in case of upload server). If you don'f find it in the Repo then please create one so that it can host the uploaded files otherwise it will throw an error if user tries to upload any files. 
The download directory is "/var/html/downloads/". This the path where you can keep those files which you want to download.
Execute the code with command "python3 filename.py". This will start the python web server on localhost port 8080. 

Please note since this service is running on local host, it won't be accessible from outside the network. You may need to make Network Changes like enabling a NAT on your router or Firewall and assign a static public IP. Or you may also use NGROK service to expose this internal URL to outside for temporary basis.  
