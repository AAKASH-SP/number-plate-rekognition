# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 18:34:19 2019

@author: Arnab Das
"""

import boto3
import csv


"""DONT CHANGE ANYTHING BELOW"""
with open("sp2project.csv",'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]
        
photo = "image.jfif"

client = boto3.client('rekognition',
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key)

"""THE BELOW CAN BE MODIFIED"""

with open(photo , 'rb') as source_image:
    source_bytes = source_image.read()
    
response = client.detect_text(Image={'Bytes':source_bytes})
                              
print(response)
result = []

textDetections=response['TextDetections']
print ('Detected text\n----------')
for text in textDetections:
    print ('Detected text:' + text['DetectedText'])
    if text['Confidence'] > 80 and text['DetectedText'] not in result:
        result.append(text['DetectedText'])
print(result)
