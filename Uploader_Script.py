import requests
import os
import des

url='http://localhost:5000/upload'

username=raw_input("Enter Username: ").strip()
password=raw_input("Enter password: ").strip()
Delete=input("Want to delete local (1/0 ) ")
files = [f for f in os.listdir(".") if os.path.isfile(f)]
D=des()
secret_key="randomsentencehere"
for file in files:
    if file!="Uploader_Script.exe" and file!="python27.dll" and file!="des.py":  
        #D=des.des()
        key="12345678"
        F=open(file,"r")
        #T=open("Decrypted"+file,"wb")
        if True:
            G=open(username+"___"+file,"w")
        
            st=F.read()

            G.write(D.encrypt(secret_key,st))
            files={'filearg': open('about.html','rb') }
            values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short',"username":username,"password":password,"name":'filearg'}
			r=requests.post(url,files=files,data=values)
            #T.write(decrypt( encrypt(st) ))
            G.close()
            F.close()
            os.remove(username+"___"+file)
            if Delete:
            	os.remove(file)

