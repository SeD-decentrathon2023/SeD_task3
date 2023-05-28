import requests
import json

spList = requests.get("https://gnfd-testnet-fullnode-tendermint-us.bnbchain.org/greenfield/storage_providers")

spListJson = open("../data/spList.json", "w")
spListJson.write(spList.text)
spListJson.close()
spsJson = json.loads(spList.text)

#print(spsJson["sps"][1]["description"])

spsLen = len(spsJson["sps"])
for i in range(spsLen):
        fileName = spsJson["sps"][i]["description"]["moniker"] + "_response_time.json"
        #print(fileName)
        responseTimeFile = open("../data/"+fileName, "w")
        responseTimeFile.write(str(requests.get(spsJson["sps"][i]["endpoint"]).elapsed.total_seconds()))
        responseTimeFile.close()
