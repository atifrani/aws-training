import json
import os, re, base64
import psycopg2

def lambda_handler(event, context):
    
    print(event)
    mypage = page_router(event['httpMethod'],event['queryStringParameters'],event['body'])
    
    return mypage


def page_router(httpmethod,querystring,formbody):

    if httpmethod == 'GET':
        htmlFile = open('contactus.html', 'r')
        htmlContent = htmlFile.read()
        return {
        'statusCode': 200, 
        'headers': {"Content-Type":"text/html"},
        'body': htmlContent
        }
    
    if httpmethod == 'POST':
        
        insert_record(formbody)
        
        htmlFile = open('confirm.html', 'r')
        htmlContent = htmlFile.read()
        return {
        'statusCode': 200, 
        'headers': {"Content-Type":"text/html"},
        'body': htmlContent
        }    

def insert_record(formbody):
    
    print(formbody)
    formbody = formbody.replace("=", "' : '")
    formbody = formbody.replace("&", "', '")
    formbody = "{'"+formbody+"'}"
    formbody = formbody.replace("'",'"')
    print(formbody)
    res = json.loads(formbody)
    print(res)
    print(res["fname"])
    print(res["lname"])
    print(res["email"])
    print(res["message"])
    try:
        connection = psycopg2.connect(user="",
                                      password="",
                                      host="",
                                      port="",
                                      database="")
        cursor = connection.cursor()
    
        
        postgres_insert_query = """ INSERT INTO contacts (fname, lname, email, message) VALUES (%s,%s,%s,%s)"""
        
        cursor.execute(postgres_insert_query, (res["fname"],res["lname"],res["email"],res["message"]))
    
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
    
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
