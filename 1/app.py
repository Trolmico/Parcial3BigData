import boto3
import requests
import time
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse
def handler(event,context):
    r = requests.get("https://misanimales.com/")
    s3 = boto3.resource('s3')
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all("img")
    for image in images:
        url = image.get("src")
        if url.startswith("http"):
            a = urlparse(url)
            archivo=os.path.basename(a.path)
            img_file= requests.get(url)
            f=open(f"/tmp/{archivo}","wb")
            f.write(img_file.content)
            f.close()
            s3.meta.client.upload_file(f"/tmp/{archivo}", "bucketparaguardarfotos",f'imagenes/{archivo}')
    return {
        'statusCode': 200
    }