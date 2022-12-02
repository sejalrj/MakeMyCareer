import json
import boto3
import io, base64
SKILLS = ["Technical Skills", "Skills", "skills", "Technical skills", "TECHNICAL SKILLS", "SKILLS", "technical skills"]


def search(values, keyword):
    for k in values:
        for v in values[k]:
            if keyword in v:
                return k
    return None

def lambda_handler(event, context):
    # TODO implement
    print(event)
    ev = event['body-json']
    ev = bytes(ev, 'utf-8')
    resume = base64.b64decode(ev)
    bucket = 'resume-bucket-bsb'
    file_path = '/resume'
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=file_path, Body=resume)
    textract = boto3.client('textract')
    doc = textract.detect_document_text(Document={
        'S3Object': {
            'Bucket': bucket,
            'Name': '/newwwww_candidate_resume',
        }
    })
    print(doc)
    print(type(doc))
    print(doc['Blocks'][0])
    print(len(doc['Blocks']))
    blocks = doc['Blocks']
    print(type(blocks))
    print(blocks)
    for i in range(len(blocks)):
        if "Text" in blocks[i] and blocks[i]['Text'] in SKILLS:
            print("Inside if")
            print(blocks[i+1]['Text'])
                
    # res = doc['Blocks'][0]
    # print(search(res, "TECHNICAL SKILLS"))
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS'
        },
        'body': json.dumps("Works")
    }

