import logging

import roslibpy


# Configure logging
fmt = '%(asctime)s %(levelname)8s: %(message)s'
logging.basicConfig(format=fmt, level=logging.INFO)
log = logging.getLogger(__name__)

msg_data = None


def main():
    client = roslibpy.Ros(host='rosbridge', port=8080)
    listener = roslibpy.Topic(client, '/chatter', 'std_msgs/String')

    def receive_message(message):
        global msg_data
        log.info(message['data'])
        msg_data = message
        listener.unsubscribe()
        client.call_later(2, client.terminate)

    listener.subscribe(receive_message)

    client.run_forever()
    return msg_data


if __name__ == '__main__':
    main()
