# Quill-by-Voice-Project

Development of a Web Application for Audio Transcription using AWS Transcribe

## Capture Every Word with Audio Transcripts

This is the website name which I had created using flask. This Frontend contains a form to upload an Audio file to the input Bucket.

In Home.py we need to add AWS Credentials to connect with s3

## Steps

1. Create an Input Bucket and mention the details in frontend page.
2. Create an IAM Role by attaching policies like S3 Full Acces and Transcribe Full Access.
3. Create a Lambda Function by selecting runtime as Python 3.8 and execution role as Existing Role , select role name created in previous step.
4. 
