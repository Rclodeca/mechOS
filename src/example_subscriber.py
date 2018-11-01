import mechos
import time

def chatter_callback(chatter_data):
    '''
    Callback function for subscriber to pass data into.

    Parameters:
        chatter_data: The data recieved over topic chatter from publisher. Each
        time a spinOnce is called, the data being sent from the publisher is
        inserted here.
    '''
    print(chatter_data)


def listener():
    '''
    Example of a subsriber subscribing to topic "chatter"
    '''
    ip_address = "tcp://169.254.2.137"
    #initializes a node called listener
    listener_node = mechos.Node("listener", ip_address)

    #create a subscriber to subscribe to topic chatter
    sub = listener_node.create_subscriber("chatter", chatter_callback)

    while(1):
        #receive available message for subsriber sub
        listener_node.spinOnce(sub)

if __name__ == "__main__":
    listener()
