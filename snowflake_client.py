import snowflake.connector

def get_snowflake_connection():
    return snowflake.connector.connect(
       user = "ABHAY2004"
        password = "Abhay@7505991639"
        account = "VKOZIAJ-KC24613"
        warehouse = "YOUR_WAREHOUSE"
        database = "FMCG_DWH"
        schema = "RAW"
    )








