import redis
import time

# Connect to Redis server
r = redis.Redis(host='redis', port=6380, db=0)

# Channel names
ping_channel = 'ping-channel'
pong_channel = 'pong-channel'

ping_counter = 0

# Subscribe to the pong channel to receive pong messages
pubsub = r.pubsub()
pubsub.subscribe(pong_channel)

while True:
    # Increment the ping counter
    ping_counter += 1
    ping_message = f"ping {ping_counter}"

    # Publish the ping message to the ping channel
    r.publish(ping_channel, ping_message)
    print(f"Sent: {ping_message}")

    # Listen for the pong message
    for message in pubsub.listen():
        if message['type'] == 'message':
            pong_message = message['data'].decode('utf-8')
            print(f"Received: {pong_message}")
            break  # Exit the loop after receiving one pong message

    # Wait for a while before sending the next ping
    time.sleep(2)
