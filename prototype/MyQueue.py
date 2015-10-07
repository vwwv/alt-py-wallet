

from Queue import Queue, Full 









def newChannel():
    return Queue()





# TODO, specify better the output value from the channel handlers....not just 'X'
# TODO, make everything, either only side effect or pure functions

###########################################################################################################################
# Input:              Channel( a thread safe queue for communication among different async process), the value to add
# Output:             None
# Side effect:        Update the channel value

def put(channel,x):
    try:
        channel.put_nowait(x)
    except Full:
        print "this, actually, can't happen"


###########################################################################################################################
# Input:              Channel( a thread safe queue for communication among different async process)
# Output:             [x]
# Side effect:        Update the channel value, blocks the calling thread till there's at least one value

def blocking_get_all(channel):
    result = []
    while True:
        result += [blocking_get(channel)]
        if channel.qsize() is 0:
          break
    return result


###########################################################################################################################
# Input:              Channel( a thread safe queue for communication among different async process)
# Output:             x
# Side effect:        Update the channel value, blocks the calling thread till there's at least one value


def blocking_get(channel):
    return channel.get(True,None) # we wait no matteer  how long!!



###########################################################################################################################
# Input:              Channel( a thread safe queue for communication among different async process)
# Output:             If the channel is empty:
#                           None
#                                   otherwise:
#                           x
# Side effect:        Update the channel value.
# Warning: if the expected output value is an actual None value, then it will be no possible to distinguish whether it came from
# the queue or not
def non_blocking_get(channel):
    if(channel.qsize()>0):
        try:
            # actually, as there's only one consumre, the exception should never be raised....unless we'd add more consumer
            return channel.get(block=False)
        except Empty:
            return None
    else:
        return None












 
