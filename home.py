from flask import Flask, request, render_template
import boto3
import os
import json

app = Flask(__name__)

# AWS credentials
AWS_ACCESS_KEY_ID = '<Your Access Key>'
AWS_SECRET_ACCESS_KEY = '<Your Secret Access Key>'
AWS_REGION = '<Region>'
S3_BUCKET_NAME = '<Input Bucket Name>'

# Initialize S3 client
s3 = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY,region_name=AWS_REGION)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    # Upload file to S3 bucket
    try:
        s3.upload_fileobj(file, S3_BUCKET_NAME, file.filename)
        return "File uploaded Successfully"
        

    except Exception as e:
        return str(e)
    


if __name__ == '__main__':
    app.run(debug=True)
