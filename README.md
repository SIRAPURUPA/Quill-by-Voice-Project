# Quill-by-Voice-Project

Development of a Web Application for Audio Transcription using AWS Transcribe

### Capture Every Word with Audio Transcripts

This is the website name which I had created using flask. This Frontend contains a form to upload an Audio file to the input Bucket.

In Home.py we need to add AWS Credentials to connect with s3

### Architecture



### Steps

1. Create an Input Bucket and mention the details in frontend page.
2. Create an IAM Role by attaching policies like S3 Full Acces and Transcribe Full Access.
3. Create a Lambda Function by selecting runtime as Python 3.8 and execution role as Existing Role , select role name created in previous step.
4. Add Trigger select source as S3 and Bucket Name as Input Bucket.
5. After creating Lambda, Create an S3 Output Bucket to store the text which is converted by using AWS Transcribe through Lambda Function.
6. Now add Inline Policy to the Role which we already created in Step 2.
7. After adding policy, Navigate to S3 and click on output bucket now go to Properties tab scroll down to create an event notification.
8. Give the event and Events >> Object creation select all object create events.
9. Select destination as Lambda function and choose the lambda function created in Step 3.

### Implementation

1. Upload the audio File using the frontend Page.
2. By clicking the Upload button it will directly uploaded into S3 Input Bucket.
3. As we triggered the lambda function.
4. That file will directly sent to the AWS Transcribe and randomly creates a job and its converts the audio file into text.
5. That output text will store into the S3 bucket in JSON format.
6. We can see the final text by downloading the JSON file.
