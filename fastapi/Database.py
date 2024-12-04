from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import MySQLdb
# from typing import Optional
# from pydantic import BaseModel
import mysql.connector
from chalice import Chalice
from mysql.connector import Error
import json
import os
import boto3


def test():
    app = Chalice(app_name="app.py")
    app.debug = True

    S3_BUCKET = 'dpv8cf-dp1-spotify'
    s3=boto3.client('s3')

    DBUSER = os.getenv('DBUSER')
    DBHOST = os.getenv('DBHOST')
    DBPASS = os.getenv('DBPASS')
    DB = "dpv8cf"
    print("USER", DBUSER)
    print("HOST", DBHOST)
    print("PASS", DBUSER)


test()