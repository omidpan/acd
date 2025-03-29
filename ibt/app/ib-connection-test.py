from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from threading import Thread
import logging
log=logging.getLogger(__name__)
class IBClient(EWrapper,EClient):
    def __init__(self,host,port,client_id):
        EClient.__init__(self,self)
        self.connect(host,port,clientId=client_id)
        thread=Thread(target=self.run)
        thread.start()
    
    def error(self,req_id:int,errorCode:int,errorString:str,advanced:any):
        if errorCode in [2104,2106,2158]:
            print(errorCode)
            print(errorString)
        else:
            # log(f'msg {code}')
            print('Error {}: {}'.format(errorCode,errorString))

# client
client=IBClient('127.0.0.1',7497,2)