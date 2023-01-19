import datetime
import sys
from opcua import Client, ua


# Connect to the OPC server
url = "opc.tcp://localhost:4840"
client = Client(url)
client.connect()

# Define the tags to fetch
tags = ["ns=2;i=2"]

# Define the start and end time for the historical data
end_time = datetime.datetime.utcnow()
start_time = end_time - datetime.timedelta(hours=1)


try:
    # Fetch the historian data
    historian_data = []
    for tag in tags:
        node = client.get_node(tag)
        data = node.read_raw_history(start_time, end_time, numvalues=0)
        historian_data.append((tag, data))

    # Print the data
    for tag, values in historian_data:
        print(tag)
        for value in values:
            print(value)


except Exception as e:
    print(e)
    sys.exit()

finally:
    # Disconnect from the OPC server
    client.disconnect()
