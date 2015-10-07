

import sys
import windowPin # Ui_Dialog
import windowEntry
import windowMain
from   PyQt4  import QtGui, QtCore

import qrcode 
import Queue
import time
import requests

from pycoin.key.BIP32Node import BIP32Node



btc2satioshi = 100000000.0 # wrong typed, it is satoshi, not satoishi


class Image(qrcode.image.base.BaseImage):
    # we ignore border
    def __init__(self, border, width, box_size):
        self.border = border
        self.width = width
        self.box_size = box_size
        size = (width + 4 ) * box_size
        self._image = QtGui.QImage(size, size, QtGui.QImage.Format_RGB16)
        self._image.fill(QtCore.Qt.white)

    def pixmap(self):
        return QtGui.QPixmap.fromImage(self._image)

    def drawrect(self, row, col):
        painter = QtGui.QPainter(self._image)
        
        painter.fillRect( (col+2 ) * self.box_size
                        , (row+2 ) * self.box_size
                        , self.box_size, self.box_size
                        , QtCore.Qt.black
                        )

    def save(self, stream, kind=None):
        pass

class Gui():
    def __init__(self):

        self.entryD_contents   = windowEntry.Ui_Dialog()
        self.mainD_contents    = windowMain.Ui_Dialog()
        self.pinD_contents     = windowPin.Ui_Dialog()
        
        self.entryD,self.mainD,self.pinD = (QtGui.QDialog(),QtGui.QDialog(),QtGui.QDialog())
        self.stage = (self.entryD,self.pinD,self.mainD)

        self.entryD_contents.setupUi(self.entryD)    
        self.mainD_contents.setupUi(self.mainD)            
        self.pinD_contents.setupUi(self.pinD)    

        self.pinButtons = [ (1, self.pinD_contents.pushButton  )
                          , (2, self.pinD_contents.pushButton_2)
                          , (3, self.pinD_contents.pushButton_3)

                          , (4, self.pinD_contents.pushButton_4)
                          , (5, self.pinD_contents.pushButton_5)
                          , (6, self.pinD_contents.pushButton_6)
                          
                          , (7, self.pinD_contents.pushButton_7)
                          , (8, self.pinD_contents.pushButton_8)
                          , (9, self.pinD_contents.pushButton_9)
                          ]

        self.addr_modify       = True
        self.copy_to_clipboard = False
        self.payment           = None

        self.deactivateWaitingTab()

        # connections:         
        self.connectComponents()

        self.mainD_contents.lcdNumber.display(40000)
        self.mainD_contents.lcdNumber_2.display(40000)

    ##########################################################################################################################################
    # Input:           Self
    # Output:          None
    # Sideeffects:     Self state modification(it connects the buttons with the actions)
    ###########################################################################################################################################
    def connectComponents(self):

        self.entryD_contents.commandLinkButton.clicked.connect(self.entryD.accept)

        self.mainD_contents.pushButton_3.clicked.connect(self.mainD.accept)
        self.mainD_contents.pushButton_2.clicked.connect(self.incAddrIndex)
        self.mainD_contents.pushButton.clicked.connect(self.pushedClipboard)
        self.mainD_contents.commandLinkButton_5.clicked.connect(self.schedulePayment)

        for index, button in self.pinButtons:
            button.clicked.connect(lambda x: self.introduceKey(index))


    ###########################################################################################################################################
    # Input:           Self, str
    # Output:          None
    # Sideeffects:     Self state change(make the progress bar show as busy and display the busy description 'str')
    ###########################################################################################################################################
    def activateWaitinTab(self,str):
        self.mainD_contents.progressBar.setRange(0, 0) 
        self.mainD_contents.label_4.setText("<html><head/><body><p><span style=\" font-size:10pt;\"> %s </span></p></body></html>"
                                           % (str,)
                                           )


    ############################################################################################################################################
    # Input:            Self, _
    # Output            None
    # Side effect       Self state change(it reads the address and the amount for the payment from the line-edits, store them in the slot 'payment', and then clear the line-edits)
    ############################################################################################################################################
    def schedulePayment(self,not_used):
        print "Trying to generate paymentss"
        # TODO add exception handle on the integer value....
        # TODO, here, it should be checked that there're enough funds and address and amount are valid values...
        self.payment = ( str(   self.mainD_contents.lineEdit.text()                         ) 
                       , int(   btc2satioshi*float(self.mainD_contents.lineEdit_2.text() )  )
                       )
        self.mainD_contents.lineEdit.setText("")
        self.mainD_contents.lineEdit_2.setText("")



    ############################################################################################################################################
    # Input:            Self
    # Output:           None
    # Side effect:      Self state change(make the progress bar show as complete, and remove the description message)
    ############################################################################################################################################
    def deactivateWaitingTab(self):
        self.mainD_contents.progressBar.setRange(0, 1) 
        self.mainD_contents.progressBar.setValue(1) 
        self.mainD_contents.label_4.setText("")



    ############################################################################################################################################
    # Input:             Self, money to show as cofirmed (as integer satoshis),money to show as uncofirmed (as integer satoshis)
    # Output:            None
    # Side effect:       Self state chonge(update the values in the balance box screen)
    ############################################################################################################################################
    def updateBalanceBox(self,confirmed,unconfirmed):
        
        if confirmed   != self.mainD_contents.lcdNumber.value() : # change intValue to a different value later on...
            self.mainD_contents.lcdNumber.display(confirmed/btc2satioshi)
        
        if unconfirmed != self.mainD_contents.lcdNumber_2.value():
            self.mainD_contents.lcdNumber_2.display(unconfirmed/btc2satioshi)



    #######################################################################################################################################
    # Input:              Self
    # Output:             None
    # Side effect         Self state modification(check a slot so the appProcess knows it has to push a value from the clipboard)
    # TODO:               This should be done all within the gui code, and not on the appProcess, TBD                
    #######################################################################################################################################
    def pushedClipboard(self,ignore):
        self.copy_to_clipboard = True


    ##########################################################################################################################################
    # Input:              Self
    # Output:             None
    # Side effect:        Self state modification(mark it needs a new address)
    ##########################################################################################################################################
    def incAddrIndex(self):
        self.addr_modify     = True


    ##########################################################################################################################################
    # Input:              Self, the new address
    # Output:             None
    # Side effect:        Self state modification(It update the qr-code and the address line with a new address)
    ##########################################################################################################################################
    def setAddress(self, newAdd):
        
        pixmap = qrcode.make(newAdd, image_factory=Image).pixmap()
        size   = self.mainD_contents.frame.size()
        
        self.mainD_contents.frame.setPixmap( pixmap.scaled(size))
        
        self.mainD_contents.label_3.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">%s</span></p></body></html>"
                                           % newAdd
                                           )
    

    ########################################################################################################################################## 
    # Input:             Self, the position of the key pressed
    # Output:            None
    # Side effect:       Self state modification (It increments the number of keys pressed counter)
    # TODO:              So far, a mock function, to emulate what it will be need once we have a trezor device
    ##########################################################################################################################################
    def introduceKey(self,i):
        print "pressed!"
        self.keys_introduced += 1
        if(self.keys_introduced >= 4):
            print "accepted!!!!!!!!!!"
            self.pinD.accept()



    ##########################################################################################################################################
    # Input:              Self, the application core state
    # Output:             None
    # Side effect:        Self state modification ( a- It decide which window has to be shown according to the GUI value
    #                                               b- It read all the value it needs to, from the app state according with the gui stte slots
    #                                                    like, a the last address being used, or which operation it is being done. 
    #                                               c- Reset all the slot to initial values, so they can be marked again.
    #                                               d- Draw the GUI image
    ###########################################################################################################################################
    def updateWindowsAndDraw(self,appState):
        if (self.stage[0].result() == QtGui.QDialog.Accepted): # time to move to the next stage! --> precondition: the accept value, 
                                                                   # are set using accept(), and therefore the windows is already closed 
        
           self.keys_introduced = 0
           self.stage[1].setResult(QtGui.QDialog.Rejected)
           self.stage           = (self.stage[1],self.stage[2],self.stage[0]) # swift one to the right

        if(self.addr_modify):
            self.setAddress(appState.lastAddr)

        if len(appState.specting_operations) > 0:
            
            for k,v in appState.specting_operations.iteritems():
                self.activateWaitinTab(v)
                break
        else:
            self.deactivateWaitingTab()

        self.updateBalanceBox(appState.confirmed,appState.unconfirmed)

        # reset flags and redraw
        self.addr_modify     = False
        self.payment         = None
        self.stage[0].show()


    ########################################################################################################################################################################
    # Input:              Self
    # Output:             The message from the gui to the appProcess ( Retrun a tuple, the second value is a boolean, whether to is finnishing or not.
    #                                                                ; The first value is either a None, if it has no msg to send, or a tuple with a label and a content:
    #                                                                   Labels:
    #                                                                     "NEW_ADDR",NONE        -> Ask the app process to generate a new address.
    #                                                                     "SEND",(toAddr,amount) -> Ask the app process to send 'amount' btc to 'toAddr'
    #
    # Side effect:        None
    #########################################################################################################################################################################
    def getValues(guiState):
        
        if (guiState.stage[0].isHidden()) and (guiState.stage[0].result() != QtGui.QDialog.Accepted):
            return (None,True)
        
        else:

            if (guiState.addr_modify):
                return (("NEW_ADDR",None),False)
            
            elif not guiState.payment is None:
                return (("SEND",guiState.payment),False) 

            else:
                return (None,False)


