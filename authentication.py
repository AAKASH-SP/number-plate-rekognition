# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:17:11 2019

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
#authentication       
clientrek = boto3.client('rekognition',
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key)
clients3 = boto3.client('s3',
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key)
