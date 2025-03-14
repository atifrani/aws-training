import json
from urllib import parse as urlparse


def lambda_handler(event, context):
    print(event)
    http_method = event['httpMethod']
    print(http_method)
    body = event['body']

    if http_method == 'GET':
        html_file = open('form.html', 'r')
        html_content = html_file.read()
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': html_content
        }
    
    if http_method == 'POST':
        parsed_body = urlparse.parse_qs(body)
        print(parsed_body)
        number = int(parsed_body.get('number')[0])
        print(number)
        square = number ** 2
        print(square)

        html_file = open('results.html', 'r')
        html_content = html_file.read().format(square = square)
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': html_content
        }