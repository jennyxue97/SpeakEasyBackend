import config_cosmos
import azure.cosmos.cosmos_client as cosmos_client
def post_user(user_name):
    collection_link = "dbs/speakeasy/colls/users"
    response_get_user = get_user(user_name)
    if response_get_user["user_exists"]:
        return response_get_user
    
    client = cosmos_client.CosmosClient(url_connection=config_cosmos.COSMOSDB_HOST, auth={'masterKey': config_cosmos.COSMOSDB_KEY})
    client.CreateItem(collection_link, {
        "user_name": user_name,
        "id": user_name
    })
    return {"user_exists": False, "user_name": user_name}

def get_user(user_name):
    collection_link = "dbs/speakeasy/colls/users"
    client = cosmos_client.CosmosClient(url_connection=config_cosmos.COSMOSDB_HOST, auth={'masterKey': config_cosmos.COSMOSDB_KEY})
    query = "SELECT * FROM users WHERE users.user_name='%s'" %user_name
    data = list(client.QueryItems(collection_link, query, config_cosmos.OPTIONS))
    if len(data) > 0:
        return {"user_exists": True}
    return {"user_exists": False}