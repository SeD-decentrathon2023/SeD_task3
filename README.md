# SeD team's project for Decentrathon 2023
## About
The `data_collector.py` module collect information about Storage Providers and they response time within Greenfield API (in defoult: https://gnfd-testnet-fullnode-tendermint-us.bnbchain.org). After, write them into json files.
We don't know how we can get datas in realtime. However, we can run this module every seconds to update jsons.

User Interfaces will get informations from the jsons and render them after every changes.

## Runing
The `data_collector.py` module must be runned with [`cron`](https://en.wikipedia.org/wiki/Cron), [`GitHub Actions`](https://docs.github.com/en/actions) or other tools which can periodical run this module. 
