from server import *
from threading import Thread

from message.ParserMessage import ParserMessage
from message.Request import Request
from methods.GET import GET
from methods.POST import POST
from methods.PUT import PUT
from methods.DELETE import DELETE

from handler.HandlerErrors import HandlerErrors


class Handler(Thread):
    def __init__(self, server):
        Thread.__init__(self)
        self.server = server

    def run(self):
        while True:
            connectionSocket, addr = self.server.serverSocket.accept()
            
            while True:
                request = connectionSocket.recv(1024).decode()
        
                if not request: 
                    break
                else:
                    request = Request(ParserMessage.parseRequest(request))
                    request.setIp(addr)
                    
                    self.checkTypeRequest(request, connectionSocket)
                    break

    def checkTypeRequest(self, request, connectionSocket):
        response = {}
       
        response = eval(request.type).response(request)
      
        connectionSocket.send(response)
        connectionSocket.close()