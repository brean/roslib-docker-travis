import logging
import time

import roslibpy


# Configure logging
fmt = '%(asctime)s %(levelname)8s: %(message)s'
logging.basicConfig(format=fmt, level=logging.INFO)
log = logging.getLogger(__name__)

client = roslibpy.Ros(host='rosbridge', port=8080)
listener = roslibpy.Topic(client, '/chatter', 'std_msgs/String')

def receive_message(message):
    log.info(message['data'])
    listener.unsubscribe()
    client.call_later(2, client.terminate)

listener.subscribe(receive_message)

client.run_forever()