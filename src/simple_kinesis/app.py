import base64
import json

def lambda_handler(event, context):
    # print(json.dumps(event))
    for record in event['Records']:
        # print(json.dumps(record))
        payload = base64.b64decode(record['kinesis']['data']).decode('ascii')
        print(payload)

    return {'valid': (payload == 'yo momma' if True else False)}
