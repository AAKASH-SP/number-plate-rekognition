# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 18:34:19 2019

@author: Arnab Das
"""

import datetime
import authentication

now = datetime.datetime.now()

"""THE BELOW CAN BE MODIFIED"""

photo = "image.jfif"

with open(photo , 'rb') as source_image:
    source_bytes = source_image.read()
    
"""AWS Rekognition"""    
response = authentication.clientrek.detect_text(Image={'Bytes':source_bytes})
                              
result = []   #contains all the text detected by AWS Rekognition

textDetections=response['TextDetections']
print ('Detected text\n----------')
for text in textDetections:
    print ('Detected text:' + text['DetectedText'])
    if text['Confidence'] > 80 and text['DetectedText'] not in result:
        result.append(text['DetectedText'])
    
print(result)

number_plate = result[0]   #the actual number plate data

"""Creating a local file"""
time = now.strftime("%Y-%m-%d %H:%M")
file_name = str(now.day) + "-" + str(now.strftime("%B"))+ "-" + str(now.year)
local_file = file_name+'.txt' ; file= open(local_file,"a+")
data = str(number_plate) +"  "+ str(time)
file.write(data+"\n")
file.close()

"""uploading file to AWS S3"""
#numberplatedata is the Bucket name
s3_file = local_file
authentication.clients3.upload_file(local_file,'numberplatedata',s3_file)