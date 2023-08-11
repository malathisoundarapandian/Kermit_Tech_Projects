connection_configs = [
    {
        'title':'P_Google_BigQuery_Conn',
        'connection_type':'STREAMSETS_GOOGLE_BIG_QUERY',
        'configuration': {
        'path': None,
        'credentialsFileContent': None,
        'projectId': 'my-streamsets-project-12345',
        'credentialsProvider': 'DEFAULT_PROVIDER'
        }
    },
    {
        'title':'P_Amazon_S3_Conn',
        'connection_type':'STREAMSETS_AWS_S3',
        'configuration': {
            'proxyConfig.retryCount': 3, 
            'awsConfig.roleSessionName': None, 
            'awsConfig.awsAccessKeyId': 'accessid1', 
            'awsConfig.roleARN': 'arn:aws:iam::<account-id>:role/role-name', 
            'awsConfig.credentialMode': 'WITH_CREDENTIALS', 
            'proxyConfig.socketTimeout': 50, 
            'proxyConfig.proxyWorkstation': None, 
            'awsConfig.awsSecretAccessKey': 'secretid1', 
            'proxyConfig.proxyPassword': None, 
            'useRegion': False, 
            'awsConfig.setSessionTags': True, 
            'awsConfig.sessionDuration': 3600, 
            'isCustomEndpoint': False, 
            'specifiedCustomRegion': None, 
            'proxyConfig.proxyHost': None, 
            'endpoint': None, 
            'proxyConfig.proxyDomain': None, 
            'signingRegion': 'US_WEST_2', 
            'proxyConfig.proxyUser': None, 
            'proxyConfig.useProxy': False, 
            'region': 'US_WEST_2', 
            'proxyConfig.proxyPort': None, 
            'proxyConfig.connectionTimeout': 10, 
            'awsConfig.isAssumeRole': False
        }
    },
    {
        'title':'P_Amazon_SQS_Conn',
        'connection_type':'STREAMSETS_AWS_SQS',
        'configuration': {
        'proxyConfig.retryCount': 3, 'awsConfig.roleSessionName': None, 'awsConfig.awsAccessKeyId': 'accessid3', 'awsConfig.roleARN': 'arn:aws:iam::<account-id>:role/role-name', 'awsConfig.credentialMode': 'WITH_CREDENTIALS', 'proxyConfig.socketTimeout': 50, 'proxyConfig.proxyWorkstation': None, 'awsConfig.awsSecretAccessKey': 'secretid3', 'proxyConfig.proxyPassword': None, 'awsConfig.setSessionTags': True, 'awsConfig.sessionDuration': 3600, 'proxyConfig.proxyHost': None, 'endpoint': None, 'proxyConfig.proxyDomain': None, 'proxyConfig.proxyUser': None, 'proxyConfig.useProxy': False, 'region': 'US_WEST_2', 'proxyConfig.proxyPort': None, 'proxyConfig.connectionTimeout': 10, 'awsConfig.isAssumeRole': False
        }
    },
    {
        'title':'P_Amzn_Kinesis_Frhse_Conn',
        'connection_type':'STREAMSETS_AWS_KINESIS_FIREHOSE',
        'configuration': {
        'proxyConfig.retryCount': 3, 'awsConfig.roleSessionName': None, 'awsConfig.awsAccessKeyId': 'accesskeyid2', 'awsConfig.roleARN': 'arn:aws:iam::<account-id>:role/role-name', 'awsConfig.credentialMode': 'WITH_CREDENTIALS', 'proxyConfig.socketTimeout': 50, 'proxyConfig.proxyWorkstation': None, 'awsConfig.awsSecretAccessKey': 'secretkeyid2', 'proxyConfig.proxyPassword': None, 'awsConfig.setSessionTags': True, 'awsConfig.sessionDuration': 3600, 'proxyConfig.proxyHost': None, 'endpoint': None, 'proxyConfig.proxyDomain': None, 'proxyConfig.proxyUser': None, 'proxyConfig.useProxy': False, 'region': 'US_WEST_2', 'proxyConfig.proxyPort': None, 'proxyConfig.connectionTimeout': 10, 'awsConfig.isAssumeRole': False       
        }
    },
     {
        'title':'P_Amzn_Kinesis_Strms_Conn',
        'connection_type':'STREAMSETS_AWS_KINESIS_STREAM',
        'configuration': {
        'proxyConfig.retryCount': 3, 'awsConfig.roleSessionName': None, 'awsConfig.awsAccessKeyId': 'accesskeyid3', 'awsConfig.roleARN': 'arn:aws:iam::<account-id>:role/role-name', 'awsConfig.credentialMode': 'WITH_CREDENTIALS', 'proxyConfig.socketTimeout': 50, 'proxyConfig.proxyWorkstation': None, 'awsConfig.awsSecretAccessKey': 'secrretkeyid3', 'proxyConfig.proxyPassword': None, 'awsConfig.setSessionTags': True, 'awsConfig.sessionDuration': 3600, 'proxyConfig.proxyHost': None, 'endpoint': None, 'proxyConfig.proxyDomain': None, 'proxyConfig.proxyUser': None, 'proxyConfig.useProxy': False, 'region': 'EU_SOUTH_2', 'proxyConfig.proxyPort': None, 'proxyConfig.connectionTimeout': 10, 'awsConfig.isAssumeRole': False
        }
    },
    {
        'title':'P_Azure_Blob_Strge_Conn',
        'connection_type':'STREAMSETS_BLOB_STORAGE',
        'configuration': {
        'storageContainer': 'example-blob1-container', 'sasToken': None, 'endpointType': 'ID', 'clientId': 'appid2', 'clientKey': 'appkey2', 'endpointURL': 'https://login.microsoftonline.com/<tenant-id>/oauth2/token', 'tenantId': 'tenantid2', 'accountFQDN': 'example.blob1.core.windows.net', 'authMethod': 'CLIENT', 'accountKey': None        
        }
    },
    {
        'title':'P_Azure_DataLake_Gen2_Conn',
        'connection_type':'STREAMSETS_ADLS_GEN2',
        'configuration': {
        'storageContainer': 'example-blob-container', 'endpointType': 'ID', 'clientId': 'appid1', 'clientKey': 'appkey1', 'endpointURL': 'https://login.microsoftonline.com/<tenant-id>/oauth2/token', 'tenantId': 'tenantid1', 'accountFQDN': 'example.dfs.core.windows.net', 'authMethod': 'CLIENT', 'secureConnection': True, 'accountKey': None
        }
    },
    {
        'title':'P_Azure_Synapse_Conn',
        'connection_type':'STREAMSETS_AZURE_SYNAPSE',
        'configuration': {
        'databaseUser': 'user23', 'governmentAccount': False, 'activeDirectoryId': None, 'synapseName': 'AzureSynapse10', 'activeDirectoryPassword': None, 'instanceType': 'DATABASE_WINDOWS_NET', 'databasePassword': 'pass23', 'authMethod': 'SQL_SERVER_LOGIN'
        }
    },
    {
        'title':'P_Cassandra_Conn',
        'connection_type':'STREAMSETS_CASSANDRA',
        'configuration': {
        'tlsConfig.useDefaultProtocols': True, 'tlsConfig.keyStorePassword': None, 'tlsConfig.trustStoreFilePath': None, 'tlsConfig.keyStoreType': 'JKS', 'contactPoints': ['172.0.12.4'], 'tlsConfig.trustedCertificates': [{}], 'tlsConfig.cipherSuites': [''], 'tlsConfig.tlsEnabled': False, 'tlsConfig.keyStoreAlgorithm': 'SunX509', 'authProviderOption': 'PLAINTEXT', 'tlsConfig.protocols': [''], 'tlsConfig.useRemoteKeyStore': False, 'tlsConfig.useRemoteTrustStore': False, 'tlsConfig.trustStorePassword': None, 'tlsConfig.trustStoreType': 'JKS', 'port': 9042, 'credentialsConfig.username': 'user21', 'tlsConfig.certificateChain': [{}], 'protocolVersion': 'V1', 'tlsConfig.privateKey': None, 'credentialsConfig.password': 'pass21', 'tlsConfig.useDefaultCiperSuites': True, 'tlsConfig.keyStoreFilePath': None, 'tlsConfig.trustStoreAlgorithm': 'SunX509'
        }
    },
    {
        'title':'P_CoAP_Client_Conn',
        'connection_type':'STREAMSETS_COAP_CLIENT',
        'configuration': {
        'resourceUrl': 'coap://172.0.0.3:5683/sdc'
        }
    },
    {
        'title':'P_CONNX_Conn',
        'connection_type':'STREAMSETS_CONNX',
        'configuration': {
        'connectionString': 'jdbc:connx:DD=<dsn>;Gateway=<gateway>;Port=<port>', 'database': 'ot', 'password': 'pass22', 'port': 7500, 'useCredentials': True, 'useConnectionString': False, 'gateway': 'jdbc:connx://your-connx-gateway-host:port/your-data-source', 'sslMode': False, 'username': 'user22'
        }
    },
    {
        'title':'P_Elasticsearch_Conn',
        'connection_type':'STREAMSETS_ELASTICSEARCH',
        'configuration': {
        'securityConfig.endpoint': None, 'securityConfig.awsRegion': None, 'securityConfig.awsSecretAccessKey': None, 'securityConfig.securityMode': 'BASIC', 'securityConfig.sslTrustStorePath': None, 'securityConfig.enableSSL': False, 'port': 9200, 'securityConfig.sslTrustStorePassword': None, 'securityConfig.securityUser': 'user20', 'useSecurity': True, 'serverUrl': 'http://localhost', 'securityConfig.awsAccessKeyId': None, 'securityConfig.securityPassword': 'pass20'
        }
    },
    {
        'title':'P_Google_Cloud_Storage_Conn',
        'connection_type':'STREAMSETS_GOOGLE_CLOUD_STORAGE',
        'configuration': {
        'path': None, 'credentialsFileContent': None, 'projectId': 'my-streamsets-project-1234', 'credentialsProvider': 'DEFAULT_PROVIDER'
        }
    }, 
    {
        'title':'P_Google_Pub_Sub_Conn',
        'connection_type':'STREAMSETS_GOOGLE_PUB_SUB',
        'configuration': {
        'path': None, 'credentialsFileContent': None, 'projectId': 'my-streamsets-project-123', 'credentialsProvider': 'DEFAULT_PROVIDER'
        }
    }, 
    {
        'title':'P_Hive_Conn',
        'connection_type':'STREAMSETS_HIVE',
        'configuration': {
        'driverProperties': [], 'password': 'pass18', 'hiveJDBCUrl': 'jdbc:hive2://172.17.0.12:1234/default', 'useCredentials': True, 'confDir': '/etc/hive/conf', 'hiveJDBCDriver': 'org.apache.hive.jdbc.HiveDriver', 'additionalConfigProperties': [], 'username': 'user18'
        }
    }, 
    {
        'title':'P_InfluxDB2.X_Conn',
        'connection_type':'STREAMSETS_INFLUX2',
        'configuration': {
        'url': 'http://120.10.0.7:8086/api/v2/write?org=kermittech&bucket=mybucket&precision=ns', 'token': 'token1'
        }
    },
    {
        'title':'P_InfluxDB_Conn',
        'connection_type':'STREAMSETS_INFLUX',
        'configuration': {
        'password': 'pass17', 'url': 'http://172.17.02:8086', 'username': 'user17'
        }
    },
    {
        'title':'P_JDBC_MYSQL_Conn',
        'connection_type':'STREAMSETS_JDBC',
        'configuration': {
        'connectionString': 'jdbc:mysql://172.17.0.2:3306/ot', 'password': 'pass1', 'useCredentials': True, 'username': 'user1'
        }
    }, 
    {
        'title':'P_JMS_Conn',
        'connection_type':'STREAMSETS_JMS',
        'configuration': {
        'password': 'pass15', 'additionalSecurityProps': [], 'connectionFactory': 'Connection Factory', 'useCredentials': True, 'providerURL': 'tcp://mqserver:61646', 'username': 'user15', 'initialContextFactory': 'org.apache.activemq.jndi.ActiveMQInitialContextFactory'
            }
    }, 
    {
        'title':'P_kafka_Conn',
        'connection_type':'STREAMSETS_KAFKA',
        'configuration': {
        'metadataBrokerList': 'kafka:9092', 'securityConfig.securityOption': 'PLAINTEXT', 'securityConfig.saslMechanism': 'GSSAPI', 'securityConfig.kerberosServiceName': None, 'securityConfig.provideKeytab': False, 'securityConfig.userKeytab': None, 'securityConfig.userPrincipal': 'user/host@REALM', 'securityConfig.truststoreType': 'JKS', 'securityConfig.truststoreFile': None, 'securityConfig.truststorePassword': None, 'securityConfig.keystoreType': 'JKS', 'securityConfig.keystoreFile': None, 'securityConfig.keystorePassword': None, 'securityConfig.keyPassword': None, 'securityConfig.enabledProtocols': 'TLSv1.2', 'securityConfig.customSecurityProperties': []
            }
    }, 
    {
        'title':'P_Kudu_Conn',
        'connection_type':'STREAMSETS_KUDU',
        'configuration': {
        'kuduMaster': 'kudu-master1:7051,kudu-master2:7051,kudu-master3:7051', 'adminOperationTimeout': 30000, 'operationTimeout': 10000, 'numWorkers': 2
        }
    }, 
    {
        'title':'P_MongoDB_Conn',
        'connection_type':'STREAMSETS_MONGODB',
        'configuration': {
        'connectionString': 'mongodb://user2:pass2@172.0.0.2:27017/mydatabase', 'password': 'pass2', 'authSource': None, 'sslEnabled': False, 'authenticationMechanism': 'DEFAULT', 'authenticationType': 'USER_PASS', 'sslInvalidHostNameAllowed': False, 'username': 'user2'
        }
    }, 
    {
        'title':'P_MQTT_Conn',
        'connection_type':'STREAMSETS_MQTT',
        'configuration': {
        'tlsConfig.useDefaultProtocols': True, 'tlsConfig.keyStorePassword': None, 'clientId': 'my_mqtt_client_123', 'tlsConfig.trustStoreFilePath': None, 'tlsConfig.keyStoreType': 'JKS', 'tlsConfig.trustedCertificates': [{}], 'tlsConfig.cipherSuites': [''], 'tlsConfig.tlsEnabled': False, 'tlsConfig.keyStoreAlgorithm': 'SunX509', 'useAuth': True, 'tlsConfig.protocols': [''], 'tlsConfig.useRemoteKeyStore': False, 'brokerUrl': 'tcp://localhost:1883', 'tlsConfig.useRemoteTrustStore': False, 'password': 'pass14', 'tlsConfig.trustStorePassword': None, 'tlsConfig.trustStoreType': 'JKS', 'tlsConfig.certificateChain': [{}], 'tlsConfig.privateKey': None, 'tlsConfig.useDefaultCiperSuites': True, 'tlsConfig.keyStoreFilePath': None, 'tlsConfig.trustStoreAlgorithm': 'SunX509', 'username': 'user14'
        }
    }, 
    {
        'title':'P_MYSQL_Conn',
        'connection_type':'STREAMSETS_MYSQL',
        'configuration': {
        'connectionString': 'jdbc://172.17.0.12:3306/ot', 'password': 'StreamTra1ningSets!', 'useCredentials': True, 'username': 'root'
        }
    }, 
    {
        'title':'P_OPC_UA_Client_Conn',
        'connection_type':'STREAMSETS_OPC_UA_CLIENT',
        'configuration': {
        'tlsConfig.useDefaultProtocols': True, 'tlsConfig.keyStorePassword': None, 'tlsConfig.trustStoreFilePath': None, 'tlsConfig.keyStoreType': 'JKS', 'tlsConfig.trustedCertificates': [{}], 'tlsConfig.cipherSuites': [''], 'tlsConfig.tlsEnabled': False, 'tlsConfig.useRemoteKeyStore': False, 'password': 'pass13', 'tlsConfig.trustStoreType': 'JKS', 'resourceUrl': 'opc.tcp://localhost:12686/example', 'tlsConfig.privateKey': None, 'tlsConfig.keyStoreFilePath': None, 'clientKeyAlias': 'client-ai', 'useUsernameAndPassword': True, 'tlsConfig.keyStoreAlgorithm': 'SunX509', 'securityPolicy': None, 'tlsConfig.protocols': [''], 'tlsConfig.useRemoteTrustStore': False, 'tlsConfig.trustStorePassword': None, 'tlsConfig.certificateChain': [{}], 'overrideHost': False, 'applicationUri': 'urn:sdc:pipeline:verifier', 'tlsConfig.useDefaultCiperSuites': True, 'tlsConfig.trustStoreAlgorithm': 'SunX509', 'username': 'user13'
        }
    }, 
    {
        'title':'P_Oracle_Conn',
        'connection_type':'STREAMSETS_ORACLE',
        'configuration': {
        'connectionString': 'jdbc:oracle:thin:@//172.17.10.12:1521/ORCL', 'password': 'pass12', 'useCredentials': True, 'username': 'user12'
        }
    },
    {
        'title':'P_PostgreSQL_Conn',
        'connection_type':'STREAMSETS_POSTGRES',
        'configuration': {
        'connectionString': 'jdbc:postgresql://172.10.17.2:5432/ot', 'password': 'pass11', 'useCredentials': True, 'username': 'user11'
        }
    }, 
    {
        'title':'P_Pulsar_Conn',
        'connection_type':'STREAMSETS_PULSAR',
        'configuration': {
        'clientKeyPem': '/pulsar-client-key.pem', 'jwtAuthEnabled': False, 'audience': None, 'clientCertPem': '/pulsar-client-cert.pem', 'tlsEnabled': False, 'tlsAuthEnabled': False, 'issuerUrl': None, 'useOauth': False, 'caCertPem': '/pulsar-ca-cert.pem', 'serviceURL': 'pulsar://172.0.0.2:6650', 'jwtToken': None, 'credentialsUrl': '/credentials_file.json'
        }
    }, 
    {
        'title':'P_RabbitMQ_Conn',
        'connection_type':'STREAMSETS_RABBITMQ',
        'configuration': {
        'tlsConfig.useDefaultProtocols': True, 'tlsConfig.keyStorePassword': None, 'tlsConfig.trustStoreFilePath': None, 'tlsConfig.keyStoreType': 'JKS', 'tlsConfig.trustedCertificates': [{}], 'tlsConfig.cipherSuites': [''], 'tlsConfig.tlsEnabled': False, 'tlsConfig.keyStoreAlgorithm': 'SunX509', 'uri': 'amqp://172.10.0.7:2204/virtualhost', 'tlsConfig.protocols': [''], 'tlsConfig.useRemoteKeyStore': False, 'tlsConfig.useRemoteTrustStore': False, 'tlsConfig.trustStorePassword': None, 'tlsConfig.trustStoreType': 'JKS', 'credentialsConfig.username': 'user10', 'tlsConfig.certificateChain': [{}], 'tlsConfig.privateKey': None, 'credentialsConfig.password': 'pass10', 'tlsConfig.useDefaultCiperSuites': True, 'tlsConfig.keyStoreFilePath': None, 'credentialsConfig.useCredentials': True, 'tlsConfig.trustStoreAlgorithm': 'SunX509'
        }
    }, 
    {
        'title':'P_Redis_Conn',
        'connection_type':'STREAMSETS_REDIS',
        'configuration': {
        'uri': 'redis://user9:pass9@172.0.0.2:6379/0'
        }
    }, 
    {
        'title':'P_Salesforce_Conn',
        'connection_type':'STREAMSETS_SALESFORCE',
        'configuration': {
        'mutualAuth.certificateChain': [{}], 'mutualAuth.keyStorePassword': None, 'proxyUsername': None, 'proxyPassword': None, 'handshakeTimeout': 10, 'mutualAuth.useRemoteKeyStore': False, 'useProxy': False, 'mutualAuth.privateKey': None, 'useProxyCredentials': False, 'proxyPort': None, 'privateKey': None, 'mutualAuth.keyStoreFilePath': None, 'password': 'pass6', 'apiVersion': 55.0, 'authEndpoint': 'login.salesforce.com', 'proxyRealm': None, 'proxyHostname': None, 'mutualAuth.keyStoreType': 'JKS', 'mutualAuth.keyStoreAlgorithm': 'SunX509', 'subscribeTimeout': 10, 'consumerKey': None, 'authType': 'BASIC', 'mutualAuth.useMutualAuth': False, 'username': 'user6'
        }
    },
    {
        'title':'P_SFTP_FTP_FTPS_Conn',
        'connection_type':'STREAMSETS_REMOTE_FILE',
        'configuration': {
        'credentials.password': 'pass8', 'credentials.username': 'user8', 'credentials.strictHostChecking': False, 'proxyType': 'HTTP', 'credentials.ftpsTrustStoreProvider': 'ALLOW_ALL', 'enableProxy': False, 'credentials.knownHosts': '/Users/Streamsets/Documents/example.txt', 'credentials.privateKey': None, 'protocol': 'SFTP', 'credentials.privateKeyProvider': 'FILE', 'ftpsMode': 'EXPLICIT', 'ftpsDataChannelProtectionLevel': 'PRIVATE', 'proxyAddress': None, 'credentials.privateKeyPlainText': None, 'credentials.privateKeyPassphrase': None, 'credentials.auth': 'PASSWORD', 'remoteAddress': 'sftp://172.0.0.2:3302', 'credentials.useFTPSClientCert': False
        }
    },
    {
        'title':'P_Snowflake_Conn',
        'connection_type':'STREAMSETS_SNOWFLAKE',
        'configuration': {
        'connectionProperties': [{}], 'customUrl': 'jdbc:snowflake://[HOST]:[PORT]', 'password': 'pass5', 'useSnowflakeRole': False, 'useSnowflakeOrganizationURL': False, 'customSnowflakeRole': None, 'customSnowflakeRegion': None, 'organization': 'Compute_WH', 'snowflakeRegion': 'AWS_US_WEST_2', 'user': 'user5', 'account': 'hy3456'
        }
    },
    {
        'title':'P_Snowpipe_Conn',
        'connection_type':'STREAMSETS_SNOWPIPE',
        'configuration': {
        'customSnowflakePort': 443, 'publicKeyPem': None, 'privateKeyPassword': 'pass4', 'customSnowflakeHost': '[SNOWFLAKE ACCOUNT].snowflakecomputing.com', 'privateKeyPem': None , 'useCustomSnowflakeEndpoint': False, 'useTls': True
        }
    }, 
    {
        'title':'P_SQLServer_Conn',
        'connection_type':'STREAMSETS_SQLSERVER',
        'configuration': {
        'connectionString': 'jdbc:sqlserver://172.10.0.7:1433;databaseName=ot', 'password': 'pass7', 'useCredentials': True, 'username': 'user7'
        }
    }
]