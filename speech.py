import config_cosmos
import azure.cosmos.cosmos_client as cosmos_client
import json

def post_speech(speech_details, category):
    speech_details = speech_details.copy()
    collection_link = "dbs/speakeasy/colls/" + category
    speech_details["id"] = speech_details["user_name"] + "_" + speech_details["speech_name"]
    client = cosmos_client.CosmosClient(url_connection=config_cosmos.COSMOSDB_HOST, auth={'masterKey': config_cosmos.COSMOSDB_KEY})
    client.CreateItem(collection_link, speech_details)
    return True

def get_speech_details(speech_name, user_name, category):
    collection_link = "dbs/speakeasy/colls/" + category
    client = cosmos_client.CosmosClient(url_connection=config_cosmos.COSMOSDB_HOST, auth={'masterKey': config_cosmos.COSMOSDB_KEY})
    query = "SELECT * FROM %s WHERE %s.speech_name ='%s' AND %s.user_name='%s'" %(category, category, speech_name, category, user_name)
    data = list(client.QueryItems(collection_link, query, config_cosmos.OPTIONS))
    return data[0]

def get_all_speeches(user_name, category):
    collection_link = "dbs/speakeasy/colls/" + category
    client = cosmos_client.CosmosClient(url_connection=config_cosmos.COSMOSDB_HOST, auth={'masterKey': config_cosmos.COSMOSDB_KEY})
    query = "SELECT %s.speech_name FROM %s WHERE %s.user_name='%s'" %(category, category, category, user_name)
    data = list(client.QueryItems(collection_link, query, config_cosmos.OPTIONS))
    return list(map(lambda item: item["speech_name"], data))