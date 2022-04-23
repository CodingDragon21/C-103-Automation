import cv2
import dropbox
from random import randint

def takeShot():
    capture = cv2.VideoCapture(0)
    result = True
    number = randint(1,100)
    while(result):
        ret,frame = capture.read()
        imageName = "img" + str(number)+ ".png"
        cv2.imwrite(imageName, frame)
        result = False
        return imageName


    capture.release()
    cv2.destoryAllWindows()        

takeShot()


def upload(imageName):
     access_token = "sl.BF4LO8EX2A9bpJIt1TCmqsLjx8e9HVt0qaf9ldwxjWBcU5uIs5-7_jgcBmZKWbynf4MnC4VJ7ibTr1VSlflWMmjAfXE-VxyJstx_d7ntaKiHm0OJkDI-Dmir7JrcNy5_myRa8kjU8LA"
     
     file_from = imageName
     file_to = r"C:\Users\rajat\Downloads\C-102 Project Automation\dropboxTest"

     dbx = dropbox.Dropbox(access_token)
     with open(file_from , 'rb') as f:
        dbx.files_upload(f.read(), file_to)

upload()
print("file has been uploaded")