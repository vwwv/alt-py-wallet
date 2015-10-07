


import sys
import windowPin # Ui_Dialog
import windowEntry
import windowMain
from   PyQt4  import QtGui, QtCore

import qrcode 
from MyQueue import newChannel, non_blocking_get, put
import time
import requests

from pycoin.key.BIP32Node import BIP32Node

from Gui           import Gui
from AppState      import AppState 
from WorkingThread import comunicationProcess
maxBlockMemory = 10



# master password "this is just for testing, this will be taken from Trezor"


class AppThread(QtCore.QThread):
    def __init__(self,inputQueeuChannel,eventLoop,outputQueeuChannel,clipboard):
        super(AppThread,self).__init__() # check this works...
        self.inputQueeuChannel  = inputQueeuChannel              
        self.eventLoop          = eventLoop      
        self.outputQueeuChannel = outputQueeuChannel
        self.clipboard          = clipboard
    
    def run(self):
        appProcess(self.inputQueeuChannel,self.eventLoop,self.outputQueeuChannel,self.clipboard)


class ComunicationThread(QtCore.QThread):
    def __init__(self,inputQueeuChannel,outputQueeuChannel,app_core):
        super(ComunicationThread,self).__init__() # check this works...
        self.inputQueeuChannel  = inputQueeuChannel              
        self.app_core           = app_core      
        self.outputQueeuChannel = outputQueeuChannel

    def run(self):
        comunicationProcess(self.inputQueeuChannel,self.outputQueeuChannel,self.app_core)







###########################################################################################################################
# Input:          the channels, the event loop and the clipboard for the gui
# Output:         None
# Side effecct:   It behaves as a daemon
# NOTICE: This is the main loop where the comunication/working thread inhabits, therefore it behaves more like a daemonic process rather
#         than a function, it should never ends as long as the application remains open.
def appProcess(inputQueeuChannel,outputQueeuChannel,eventLoop,clipboard):

    appState    = AppState()
    put(outputQueeuChannel,appState.requestAddr())

    windowState = Gui() # waitingD
    terminate   = False
    itera       = 0

    step = time.time() # temporal solution

    while not(terminate):
        # print itera 
        itera += 1 # for debuging
        windowState.updateWindowsAndDraw(appState)
        eventLoop.processEvents(QtCore.QEventLoop.WaitForMoreEvents)  # trigger the all the gui changes and blocks waiting for input, therefore, it is CRITICAL,
                                                                      # that whenever a new set of elements are added to the queeu, a void event is feeded into the
                                                                      # event loop, just to awake the thread. 
                                                                         
                                                                      # For safety reasons, only a QThread can concurrently feed the event loop, therefore, the thread
                                                                      # adding element to the Queue shall be a QThread instead of a normal Thread
        if(windowState.copy_to_clipboard):
            clipboard.setText(appState.lastAddr)
            windowState.copy_to_clipboard = False

        guiValue   ,terminate = windowState.getValues()
        
        if not guiValue is None: 
            print guiValue

        commtValue            = non_blocking_get(inputQueeuChannel)
        
        appState.updateAppState(commtValue)
        output     = appState.getValues(guiValue)  


        if terminate is True:
             put(outputQueeuChannel,None)
        
        else:

            if (output != None):  # we pass a None as termination signal
                 put(outputQueeuChannel,output)

            if ((time.time() - step >= 15) or (not (windowState.payment is None))):   # While not async updates we have to poll :(
                step       = time.time()                                            # TODO: "Delete this and refactoorrrr"
                put(outputQueeuChannel,appState.getValues(("RE_SCAN",None)))       




#     study toshi interface.                                                                             ------------> DONE

#     implement some basic calls to toshi                                                                ------------> DONE

#     study PyCoin                                                                                       ------------> DONE

#     make the client work with fake values                                    
          # fix qr                                                                                       ------------> DONE
          # current address                                                                              ------------> DONE
          # dictionary of addresses -> (unspent_confirm,unspent_non_confirm,confirmed,non_confirmed)     ------------> DONE

          # dictionary of height block to -> list of our addresses affected                              -------------> Some how....
          # function build address history                                                               -------------> DONE
          # function add block                                                                           -------------> DONE




#       make it work                                                                                     -------------> DONE
#       implement a sync communication proccess, with nice completion tab                                -------------> DONE 
#       make the client work with fake calls with extreme timeouts                                       -------------> DONE 
#       make the client work with real calls                                                             -------------> DONE
#       Make it start with no addresses                                                                  -------------> DONE
#       Get the first transaction in!!                                                                   -------------> DONE
#       Get the first transaction out!!                                                                  -------------> DONE 
#       Make it sign transactions                                                                        -------------> 

# addresses:
#
#

#       TODO: Define inputs and outputs of each function                                                 --------------> Done
#       TODO: Solve the flushing problem....                                                             --------------> Done
#       continue reading Twisted                                                                         --------------> Done
#       split the code in different files
#       mkae the communication calls async....
#       continue implementing async communication calls.....(though this might be optional)
#       start reading how to package
#       read from config ----> we'll address that later...
# package on different platform, making sure it works....





###########################################################################################################################
# TODO: Things to change, pass the keyboard to the guy, so we can avoid handling it here
#       pass the event loop to the comunication process, to see if it can awke it from there
def main():
    app              = QtGui.QApplication(sys.argv)
    event_loop       = QtCore.QEventLoop()

    fromGui          = newChannel() 
    toGui            = newChannel() 

    appThread        = AppThread(toGui,fromGui,event_loop,app.clipboard())
    connectionThread = ComunicationThread(fromGui,toGui,event_loop)

    connectionThread.start()
    appThread.run()          # we re-use the current thread for the AppThread 
    connectionThread.wait()

    print "done"

    


if __name__ == '__main__':
    main()









