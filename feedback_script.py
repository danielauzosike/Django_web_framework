#! /usr/bin/env python3
import os
import requests
path = "/data/feedback/"
dict = {}

# listing all .txt files under the path directory and iterating through them
for files in os.listdir(path):
  with open(path + files, "rb") as f:
    lines = f.readlines()
    dict = {'title':lines[0], 'name':lines[1], 'date':lines[2], 'feedback':lines[3]}
    response = requests.post("http://34.67.240.79/feedback/", data = dict)
    # print status_code when script is run
    print(response.status_code, response.ok)
