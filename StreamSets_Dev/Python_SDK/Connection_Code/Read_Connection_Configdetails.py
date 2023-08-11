from streamsets.sdk import ControlHub
sch = ControlHub(credential_id="0cad6c42-4882-4af0-809a-3ff296f7dea7", token="eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJzIjoiMzdiNTc1ZjQ5ZGE1YjU1Yzc4ZWUxNGVhZmZmODVhNzIwNGJkNzkwYTY5ZmRiODc3YzY3Y2RlZjU4NGU1NmNjOWVkNWUxNGZjZTQ5ZTk2YjQ1ZTVjZjY1MmEwZmMzOTM5Zjc1NjBjZTNiNDdlMWQ0ZGYxNDc4Y2Q0MGMzYTdmN2YiLCJ2IjoxLCJpc3MiOiJldTAxIiwianRpIjoiMGNhZDZjNDItNDg4Mi00YWYwLTgwOWEtM2ZmMjk2ZjdkZWE3IiwibyI6IjEzZjY2MTMyLTVlN2QtMTFlZC1iNTJhLTIzYjJjOWIyYWRmYiJ9.")
conn=sch.connections

for conn_list in conn:
    conn_namelist=conn_list.name
    print(conn_namelist)

while True:
    conn_name=input("Please enter the connection name:")

    if conn_name=='quit':
        break

    else:
        connection_name=conn.get(name=conn_name)
        conn_type=connection_name.connection_type
        print(conn_type)
        conn_config=connection_name.connection_definition.configuration
        print(conn_config)