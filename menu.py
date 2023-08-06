while True:
    print('''
--------------------------WELCOME TO PYTHON MENU PROGRAM---------------------------
\t\t\tPress 1: Linux commands
\t\t\tPress 2: Whatsapp Message
\t\t\tPress 3: Email Message
\t\t\tPress 4: Speech to Text
\t\t\tPress 5: Google Search 
\t\t\tPress 6: Photo Click
\t\t\tPress 7: Video Streaming
\t\t\tPress 8: Black and White Streaming
\t\t\tPress 9: Crop Video''')
    
    choice = int(input("Enter your choice: "))
    
    if(choice==1):
        
        #linux commands
        import subprocess
        cmd = input("Enter your command: ")
        x = subprocess.getoutput(cmd)
        print(x)
        
    elif(choice==2):
        
        #pip install pywhatkit
        import pywhatkit as pw
        phone = input("enter phn num: ")
        mesg = input("enter mesg")
        pw.sendwhatmsg_instantly(phone,mesg)
        
    elif(choice==3):
        import smtplib # simple mail transfer protocol

        server = smtplib.SMTP('smtp.gmail.com',587) 

        server.starttls()  #tls = transport layer security

        # input all the details
        sender_email = input("enter sender email : ")
        password = input("enter the password : ")

        reciever_email = input("enter the reciever email : ")
        message = input("enter the message to be sent : ")

        #login
        server.login(sender_email , password)

        server.sendmail(sender_email, reciever_email , message)

        print("mail sent successfully")
        
        
    elif(choice==4):
        
        #pip install SpeechRecognition
        #pip install pyaudio
        import speech_recognition as sr
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=1)
        with mic:
            print("Say Anything!!!!!!!!")
            audio = r.listen(mic)
        print(r.recognize_google(audio))
        
    elif(choice==5):
        
        #pip install beautifulsoup4
        #pip install google
        from googlesearch import search
        q = input("enter what you want to search: ")
        for j in search(q, tld="com", num=10, stop=10, pause=2):
            print(j)
            
            
    elif(choice==6):
        
        #pip install opencv-python
        import cv2
        cam = cv2.VideoCapture(0)
        status, photo = cam.read()
        cv2.imshow("photo",photo)
        cv2.waitKey()
        cv2.destroyAllWindows()
        if cv2.waitKey()==13:
            cam.release()
        
    elif(choice==7):
        
        import cv2
        cam = cv2.VideoCapture(0)
        while True:
            status, photo = cam.read()
            cv2.imshow("Video",photo)
            if cv2.waitKey(100) == 13:
                break
        cv2.destroyAllWindows()
        cam.release()
        
    elif(choice==8):
        
        import cv2
        cam = cv2.VideoCapture(0)
        while True:
            status, photo = cam.read()
            grey_pht = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Video",grey_pht)
            if cv2.waitKey(100) == 13:
                break
        cv2.destroyAllWindows()
        cam.release()
        
    elif(choice==9):
        
        import cv2
        cam = cv2.VideoCapture(0)
        while True:
            status, photo = cam.read()
            cv2.imshow("Video",photo[200:600,200:500])
            if cv2.waitKey(100) == 13:
                break
        cv2.destroyAllWindows()
        cam.release()
        
    #continue or not
    ch = input("Do you want to continue : y/n  ")

    if(ch=='y' or ch=='Y'):
        continue
    else:
        break
    
