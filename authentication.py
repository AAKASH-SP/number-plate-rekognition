# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 18:30:55 2019

@author: Arnab Das
"""

import boto3
import csv

with open("sp2project.csv",'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]
        
