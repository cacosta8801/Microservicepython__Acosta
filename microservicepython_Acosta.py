#!/usr/bin/python
#pip install mysqlclient
#pythonmicroservice.c7v0hpe7htge.us-east-2.rds.amazonaws.com
#pythonmicroservice.c7v0hpe7htge.us-east-2.rds.amazonaws.cox
import pika
import MySQLdb
import json
import sys
import time


class Microservice:
    
    @staticmethod
    def microserviceLogic ():

        try:
            firstarg=sys.argv[1]
            db = MySQLdb.connect(host="35.198.0.8", user="root", passwd="root2018", db="microservice")        
            cur = db.cursor()
            fechaCreacion= time.strftime('%Y-%m-%d')
            cur.execute("INSERT INTO `microservice`.`proveedor` VALUES (null,2,'"+sys.argv[1]+"','"+sys.argv[2]+"','"+sys.argv[3]+"','"+sys.argv[4]+"','"+sys.argv[5]+"','"+sys.argv[6]+"','"+sys.argv[7]+"','"+fechaCreacion+"','Activo')")
            db.commit()
            db.close()
            print ("Registro agregado con exito..")
#Secuencia de entrada en la shell ("Diego" "Acosta" "3108802491" "cra102" "eragon232@hotmail.com" "www.diego.com" "8120674")
        except IOError as e:

            print ("Error BD: ".format(e.errno, e.strerror))

    @staticmethod
    def queuePublishMessage ():
        try:

            credentials = pika.PlainCredentials('test', 'test')
            parameters = pika.ConnectionParameters('192.168.56.7',5672,'/',credentials)
            connection = pika.BlockingConnection(parameters)

            channel = connection.channel()
            channel.queue_declare(queue='micro_sv')
            channel.basic_publish(exchange='',routing_key='micro_sv',body='Hello World!')
            print(" [x] Sent 'Hello World!'")
            connection.close()


        except IOError as e:
            print ("Error Queue: ".format(e.errno, e.strerror))

        

Microservice.microserviceLogic()
#Microservice.queuePublishMessage()

   

