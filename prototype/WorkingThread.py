

import sys
import windowPin # Ui_Dialog
import windowEntry
import windowMain
import json
from   PyQt4  import QtGui, QtCore

import qrcode 
import MyQueue
import time
import requests

from pycoin.key.BIP32Node                import BIP32Node
from MyQueue                             import blocking_get_all, put

from pycoin.tx.Spendable                 import Spendable
from pycoin.tx.pay_to.ScriptPayToAddress import ScriptPayToAddress
from pycoin.key.BIP32Node                import BIP32Node
from pycoin.tx.tx_utils                  import create_signed_tx
from pycoin.serialize                    import *

###########################################################################################################################
# Input:          the channels (one for input another for output) and an object to awake the gui event loop
# Output:         None
# Side effecct:   It behaves as a daemon
# NOTICE: This is the main loop where the comunication/working thread inhabits, therefore it behaves more like a daemonic process rather
#         than a function, it should never ends as long as the application remains open.
def comunicationProcess(inputQueeuChannel,outputQueeuChannel,event_loop):
    
    while True: 
        elements = blocking_get_all(inputQueeuChannel)
        if shallTerminate(elements):
            break;
        else:
            for serial, element in elements:
                try:
                    for addr in element.get('rescans',[]):
                        put(outputQueeuChannel,{'rescan' : rescan(addr)})
                        event_loop.wakeUp() # it might be better just to use .flush() --- it might also works event_loop.wakeUp(), the documentation says nothing
                    
                    if 'payment' in element:
                        tx = createTX(element['payment'])
                        if tx is None:
                            pass # TODO

                        else:
                            payload = {'hex':str(tx)}

                            r = requests.post("https://testnet3.toshi.io/api/v0/transactions", data=json.dumps(payload))
                            print r.text
                            print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"

                            
                    
                    event_loop.wakeUp() 

                except Exception as e: # TODO USE SPECIFIC EXCEPTIONS
                    print "####################### EXCEPTION #############################"
                    print e 
                    # do something here handleing the problem

                print ("And the serial number is %i"%serial)
                put(outputQueeuChannel,{'label' : serial} )

    print "finnishing communication proccess"


###########################################################################################################################
# Input:         The address to be rescanned
# Output:        (address,[{'txid':txid,'index':index,'value':amount,'confirmed':confirmed}])
# Side effecct:  Produce a blocking http request
def rescan(addr):
    r = requests.get("https://testnet3.toshi.io/api/v0/addresses/%s/transactions" % (addr,)).json()

    updates = []

    
    for tx in r.get('transactions',[]):
      
      inde = 0

      for stxo in tx['outputs']:
         
         # TODO, even though it says, not spent, it might be unconfirmily spent, so we can not rely only on that!! -> Important
         if (stxo['addresses'] == [addr]) and not stxo['spent']:
            
            updates += [{'txid': tx['hash'],'index':inde,'value': stxo['amount'],'confirmed':True}]
      
         inde += 1

    for tx in r.get('unconfirmed_transactions',[]):
      
      inde = 0
      
      for stxo in tx['outputs']:

         if (stxo['addresses'] == [addr]) and not stxo['spent']:
            updates += [{'txid': tx['hash'],'index':inde,'value': stxo['amount'],'confirmed':False}]
            
         inde += 1


    print ("We are now rescaning %s " % (addr,))
    return (addr,updates) # make something less silly


def createTX(payment):

    (content,(addrToSend,amountToSend)) = payment
    
    if content is None:
        pass
        # it should include a reason for the  error....
        # raise an exception

        return None # actually instead of returning it should raise an exception....

    else:

        (utxos,retAddr) = content
        keys            = []
        spendings       = []

        for ((txid,index),amount,key) in utxos:

            keys      += [key.wif()]

            spendings += [ Spendable( amount
                                    , ScriptPayToAddress( key.hash160()).script()
                                    , h2b_rev(txid)
                                    , index
                                    )
                         ]
        print "########################################################################################"
        print ('spendings     :',spendings)
        print ('addr to send  :',addrToSend)
        print ('amountToSend  :',amountToSend)
        print ('retAddr       :',retAddr)
        print ('wif list      :',keys)
        print ('transaction   :',create_signed_tx(spendings,[(addrToSend,amountToSend),retAddr],wifs=keys, fee="standard").as_hex())
        print "########################################################################################"
        

#        return create_signed_tx(spendings,[(addrToSend,amountToSend),retAddr],wifs=keys, fee="standard").as_hex()

#
# (None,(addrToSend,amountToSend))
# ((utxo_involved,self.lastAddr,so_far_got),(addrToSend,amountToSend))

# utxo_involved += [((txid,index),amount,self.private_key[address])]

#
 # from pycoin.tx.Spendable                 import Spendable
 # from pycoin.tx.pay_to.ScriptPayToAddress import ScriptPayToAddress
 # from pycoin.key.BIP32Node                import BIP32Node
 # from pycoin.tx.tx_utils                  import create_signed_tx
 # from pycoin.serialize                    import *

 # master_node     = BIP32Node.from_master_secret("secret phrase, in future versions it will use the trezor instead",netcode='XTN')
 # key             = master_node.subkey(1)
 # script          = ScriptPayToAddress(key.hash160()).script()
 # spending        = Spendable( 710000000 , script,h2b_rev('3d18c5aa7abe2e96db13bb9e934baaf91854369a120c4c44803149a222168fa6'),0)
 #
 # create_signed_tx( [spending], ['msj42CCGruhRsFrGATiUuh25dtxYtnpbTx'], wifs=[key.wif()], fee="standard")



###########################################################################################################################
# Input:             [None | (task_label,task_content)]
# Output:            Ture|False
# Side effects       None
def shallTerminate(elements):
    print elements
    for element in elements:
        if element == None:
            return True
    return False














