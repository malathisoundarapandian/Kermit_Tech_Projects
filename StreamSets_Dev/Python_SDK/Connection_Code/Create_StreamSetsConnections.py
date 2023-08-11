from streamsets.sdk import ControlHub
import os
import requests
from connection_configs import connection_configs
from streamsets.sdk.exceptions import ConnectionError

#  Define the required keys
required_keys = ['credential_id', 'token', 'engine_url']

# Check if the file exists and is not empty
config_file_path = '/Users/malathi/Desktop/Python SDK StreamSets/python_testenv/config.txt'
if not os.path.exists(config_file_path) or os.path.getsize(config_file_path) == 0:
    print("Configuration file is empty or does not exist.")
    exit(1)

# Read configuration from the file
with open('config.txt','r') as file:
    config_lines=file.readlines()

# Initialize configuration variables
config = {}

# To extract values from the file
for line in config_lines:
    parts = line.strip().split('=')
    if len(parts) == 2:
        key, value = parts
        config[key] = value

# Check if all required values are present
missing_keys = [key for key in required_keys if key not in config]

try:

    if missing_keys:
        print("Missing configuration values in the file:", ', '.join(missing_keys))
        exit(1)

    # Create a ControlHub instance
    try:
        sch = ControlHub(credential_id=config['credential_id'], token=config['token'])
    except requests.exceptions.HTTPError as e:
        print("Error:", e)
        print("Please provide a valid credential_id.")
        exit(1)

    # Get the data collector information
    try:
        sdc = sch.data_collectors.get(engine_url=config['engine_url'])
    except ValueError as e:
        print("Error:", e)
        print("Please provide a valid Engine url")
        exit(1)


    # To create a connection
    connection_builder = sch.get_connection_builder()
    for connection_config in connection_configs:

        # To define the connection name and type
        connection = connection_builder.build(title=connection_config['title'],
                                            connection_type=connection_config['connection_type'],
                                            authoring_data_collector=sdc)

        # To configure the connection
        connection.connection_definition.configuration.update(
            connection_config['configuration']
        )
        title_name=connection_config['title']
       
        try:
            sch.add_connection(connection)
            print(f"Connection '{connection_config['title']}' added successfully.")
        except ConnectionError as e:
            print(f"Connection name '{connection_config['title']}' already exists: {e}")

except ValueError as e:
    if 'decoding auth token' in str(e):
        print("Error decoding the authentication token. Please provide a valid token.")
    elif 'credential_id' in str(e):
        print("Missing credential_id in the configuration file. Please provide a valid credential_id.")
    else:
        print("An error occurred:", e)