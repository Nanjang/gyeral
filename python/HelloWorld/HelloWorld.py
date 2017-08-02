#!/usr/bin/env python

class HelloWorld:
    def __init__(self, message, receiver):
        self.message = message
        self.receiver = receiver
    
    def write(self):
        print self.message, self.receiver
    
if __name__ == '__main__':
    helloWorld = HelloWorld('Hello', 'World')
    helloWorld.write()

