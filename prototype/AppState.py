



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




class AppState():
    def __init__(self):

      self.lastAddr            = None
      self.specting_operations = {}
      self.just_started        = True
      self.last_operation      = 0

      # we'll need an address list......
      self.block_relation  = {} # Dict Block (Set addresses)

                             
      self.address_cache   = {} # while testing...

      # example
      # { "1GzRWJo4xExrZpi8FW3uQ2aYESk8sJMoQz" : ( { ("dcsdcsd134wdccsdc",3) : (True,12983209000,34,34900934094334) # preferenceAsOld, value, confirmations,timestmp
      #                                                                   , ("jjjdcsdwswscscsdc",5) : (True,    3209000,34,34900932094334)
      #                                                                   }
      #                                                                 , 0 
      #                                                                 , 0
      #                                                                 ) 
      
      self.master_node     = BIP32Node.from_master_secret("secret phrase, in future versions it will use the trezor instead",netcode='XTN')
      self.address_index   = 0
      
      self.addresses       = []



      # redundant_info, for eficiency purporsses, the same as address_cache but with its key-values flipped, so we can efficiently choose the right utxo...
      self.utxo        = {}
      self.sorted_utxo = {}
      
      self.confirmed   = 0
      self.unconfirmed = 0
      
      self.private_key = {}

      # TODO, check confirm always stands before unconfirmed
      return

    #########################################################################################################################################################
    # Input:                  Self, output (transaction id plus index) 
    # Output:                 [address] - It returns the address to where that transaction was going
    # SideEfect:              It deletes the utxo from the state
    def markAsUsedUTXO(self,txid,index):
        
        if (txid,index) in self.utxo:

            (value,confirms), addr = self.utxo[(txid,index)]
            
            del self.sorted_utxo[((value,confirms),(txid,index))]
            del self.utxo[(txid,index)]

            adress_utxo,addr_conf,addr_un_conf = self.address_cache[addr]

            del adress_utxo[(txid,index)]

            if confirms :
                addr_conf        -= value
                self.confirmed   -= value
            else:
                addr_un_conf     -= value
                self.unconfirmed -= value

            
            self.address_cache[addr] = (adress_utxo,addr_conf,addr_un_conf)
            
            return [addr]
           
        else:
            return []
    #########################################################################################################################################################
    # Input:                  Self, new utxo (transaction id, index,values, confirmed, address to where it goes) 
    #
    #
    # Output:                 [address] - It returns the address to where that transaction is going, if it is going to a owned address and is new, otherwise an empty list
    # SideEfect:              It adds the utxo to  the state if it is going to an owned address, otherwise, nothing change

    def markAsNew(self,txid,index,value,confirmed,addressTo): 
        
        if (not (txid,index) in self.utxo) and (addressTo in self.address_cache):

           self.utxo[(txid,index)] = ((value,confirmed), addressTo)
           self.sorted_utxo[((value,confirmed),(txid,index))] = addressTo

           adress_utxo,addr_conf,addr_un_conf = self.address_cache[addressTo]

           adress_utxo[(txid,index)] = (value,confirmed)

           if confirmed:
              addr_conf      += value 
              self.confirmed += value

           else:
              addr_un_conf     += value
              self.unconfirmed += value

           self.address_cache[addressTo] = (adress_utxo,addr_conf,addr_un_conf)

           return [addressTo]


        else:
            return []


    # def processBlock(block):

    #     involvedAddr = []
    #     # don't repeat "block[hash]"

    #     for tx in block['transactions']
    #         involvedAddr += processTX(tx,blocks['height'],block['time'])

    #     self.block_used += block['hash']

    #     if len(self.block_used) > maxBlockMemory :
    #         del self.block_relation[self.block_used[0]] 
    #         del self.block_used[0]

    #     if ( block['hash'] in self.block_relation):
    #         self.block_relation[block['hash']] |= set(involvedAddr)
    #     else:
    #         self.block_relation[block['hash']] = set(involvedAddr)

    #     return self.block_relation[block['hash']]


    # def processTX(trnsaction,height,timestamp):
    #     result = []

    #     for froms in trnsaction['inputs']:
    #        result += markAsUsedUTXO(froms['previous_transaction_hash'],froms['output_index']) 

    #     index = 0
 
    #     for toos in trnsaction['outputs']:
    #         if not toos['spent']
    #             result += markAsNew(trnsaction['hash'],index,toos['amount'],timestamp,toos['addresses'][0],confirmations)
    #         index += 1

    #     return result secret_exponent
 

 # 
 # create_signed_tx([Spendable(1200,ScriptPayToAddress.from_address(master_node.subkey(0).hash160()),txid,index)],[(to_address,amount),return_address],list_of_private_key,fee="standard")
 # mzTfCSJZpwZcjWLcnXTSWKzH2xQXpnjpkx
 # mzTfCSJZpwZcjWLcnXTSWKzH2xQXpnjpkx cUYeNxpFCybZGNWLnMFHRM7ojstJnbzpqeFxwxLXLkJk6gmxyXbm
 #  3d18c5aa7abe2e96db13bb9e934baaf91854369a120c4c44803149a222168fa6
 
    def addresUpdate(self,(address,updates)):
        
        (utxos,conf,unconf) = self.address_cache[address]

        for key in utxos.copy():

            utxo,index = key 
            self.markAsUsedUTXO(utxo,index)

        for update in updates :
            self.markAsNew( update['txid'],update['index'],update['value'],update['confirmed'],address)


    ####################################################################################################################################################################
    # Input:        Self
    # Output:       A rescan-task concerning the new generated address
    # Side effect:  It generates a new address and store it on the last address slot, it also increment the index counter so each new address is, actually, new.
    def requestAddr(self):

        node                          = self.master_node.subkey(self.address_index)
        newAddr                       = node.address()
        
        self.addresses               += [newAddr]
        
        self.address_cache[newAddr]   = ({},0,0)
        self.private_key[newAddr]     = node

        lab, resc                     = ("Scanning <b>%s</b>" % newAddr,[newAddr])

        self.address_index           += 1
        
        self.lastAddr                 = newAddr
        return self.bookOperation(lab,{'rescans':resc}) 



    ###################################################################################################################################################################
    # Input:       Self, msg from the communication/working thread, about the last job done, if any, otherwise none:
    #                  this message can be one of, or a combination of:
    #                   {'rescan':(address,[{'txid':txid,'index':index,'value':amount,'confirmed':confirmed}]) }
    #                   {'label' : task}
    # Output:      None
    #
    # Sideffect:   If it contains a label, remove the task from the scheduled task queue, and/if/instead it contains a 'rescan' update the app's utxo state.

    def updateAppState(self,commtValue):
        if not commtValue is None:

            if  'rescan' in commtValue:
                self.addresUpdate(commtValue['rescan'])
            
            if 'label'  in  commtValue:
                del self.specting_operations[commtValue['label']] # not use mutation....
        return


    ###################################################################################################################################################################
    # Input:       Self, the message from the gui
    # Output:      The message to the communication/working thread containing the task to be executed
    # Sideeffect:  The task is stored on the scheduled tasks queues
    def getValues(self,guiValue):
       
        if not guiValue is None:
            print "#######################################"
            print guiValue
            guiLavel, guiContent = guiValue


            if guiLavel == "NEW_ADDR":

                return self.requestAddr()
            
            elif guiLavel == "RE_SCAN":
                lab, resc                     = ("Rescanning wallet...",self.addresses) # chapuza
                return self.bookOperation(lab, {'rescans': resc})

            elif guiLavel == "SEND":
                addrToSend, amountToSend      = guiContent
                # TODO, this will generate a bug 
                lab, resc                     = ("Sending %i to %s \n at %i" % (amountToSend,addrToSend,time.time())
                                                , self.bookPayment(addrToSend, amountToSend)
                                                ) # chapuza
                
                return self.bookOperation(lab, {'payment': resc})



        else:
            return None

    def bookOperation(self,label,operation):
        self.last_operation                      += 1
        self.specting_operations[self.last_operation]  =  label        
        return (self.last_operation,operation) 
    ##############################################################################################################################################################################
    # Input:       Self, address to where send the payment, the amount to send
    # Output:      A data structure containing the utxo to use, and the address to return the remaining money, or a (None,(addr,amount)), if there was not enough utxo for it 
    #
    # WARNING:      If two orders are executed at the same time, it might end up using some utxo twice, this will produce an error and one of the payment might be therefore ignored
    #               we should find a way to get over it
    def bookPayment(self,addrToSend, amountToSend):
        utxo_involved = []
        so_far_got    = 0

    # TODO:: make it more ressilance...what if it is not a number??---> send the problem.....
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        print self.utxo
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        for k,v in self.utxo.iteritems():
           txid,index                   = k 
           ((amount,confirmed),address) = v
           
           if confirmed:
            utxo_involved += [((txid,index),amount,self.private_key[address])]
            so_far_got    += amount

           if so_far_got >= amountToSend:
            break

        if so_far_got < amountToSend:
           return (None,(addrToSend,amountToSend))
        
        elif so_far_got >= amountToSend:
          # TODO: check what PyCoin does in case it generate the exact amount
          # TODO, this might confuse the user!!! use another chain for the change!!!
          # also, is dangerous, we should always check self.lastAddr is not 'None'
          # otherwise the user will lose money!!!
          return ((utxo_involved,self.lastAddr),(addrToSend,amountToSend))


# TODO the problem that sometimes reuse unconfirmed utxo ---> it should not even use one uncofirmed utxo....
# TODO, use btc instead of satoshis...

# TODO, when adapting to trezor....use some addresses only for change returns 





