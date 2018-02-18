import pika
import MySQLdb
import json

def callback(ch, method, properties, body):
    	msg = body
    	print("Mensaje Recibido 1:")
    	print(msg)

def stopCallback():
    	quit()

class MicroserviceReiver:
    
    @staticmethod
    def queuePublishMessage ():
        try:

            credentials = pika.PlainCredentials('test', 'test')
            parameters = pika.ConnectionParameters('192.168.56.7',5672,'/',credentials)
            connection = pika.BlockingConnection(parameters)
            connection.add_timeout(3,stopCallback)
            channel = connection.channel()
            channel.queue_declare(queue='micro_sv')
            channel.basic_consume(callback,queue='micro_sv',no_ack=True)
            print(" [*] Waiting for messages. To exit press CTRL+C")
            channel.start_consuming();



        except IOError as e:
            print ("Error Queue: ".format(e.errno, e.strerror))



MicroserviceReiver.queuePublishMessage()









