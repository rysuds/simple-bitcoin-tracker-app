# Lightweight Bitcoin Tracker App [WIP]

## How to use

Open up a fresh Python virtual env and do the following innside of the root dir

```
pip install -r requirements.txt
```

To start the server do

```
uvicorn main:app --reload
```

You should then be able to send `curl` commands or run the `test_api.ipynb` notebook in the `notebooks` directory (you'll `jupyter` installed for that)



## Functionality

The app exposes some REST endpoints that fetch address and transaction data. The data is queried from blockchain.com using their REST API, transformed and returnned to user. 

There is also the ability to create a user record and add an address to that user (although these pieces might be broken atm)

## Areas of improvement
- Addition of unit tests via happy path jsons 
- Completion of database layer
- Aggregate queries
    - total balance across addresses etc..
- Syncing mechanism via cron tasks


```python
import requests
```


```python
# Get address info
r = requests.get("http://localhost:8000/api/3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd",)
r.json()
```




    {'address': '3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd',
     'n_tx': 1138,
     'txs': [{'hash': '4244d2755fda93be58174a5642c128d9c6d6924c3afa7b8653d3c796eac6e0f0',
       'block_height': 735248,
       'tx_index': 8475142419306746},
      {'hash': 'adcee77856dd2343225a01bc8e4f258c326da5cf644ada611a813d7ca0b849ca',
       'block_height': 735187,
       'tx_index': 7117375326357424},
      {'hash': '798c94497ab6ac354c5a54eef42a1a3246b8bddfa046b96a904af0fcfec08c80',
       'block_height': 734846,
       'tx_index': 4522944694820361},
      {'hash': '5c5cb00cf5ee10fcf844e96f587926ea4de6ffbdd33afd73b9b22b1ed3af9f6b',
       'block_height': 734781,
       'tx_index': 3786675002262902},
      {'hash': '75892fb9eb8315067b94146896ef35648933e2d51934b0ea6bf03bb018d513db',
       'block_height': 734765,
       'tx_index': 7708103232849790},
      {'hash': '33dc2f336651a14476363b881cf1d3a60a210c1a44c72db97d8ad9308749ceeb',
       'block_height': 734494,
       'tx_index': 8296679340383025},
      {'hash': 'c99e6bf98e4d76777e2299da37a7a1cb3d51539501c01c07a80190a9473df3fb',
       'block_height': 734483,
       'tx_index': 8864707959403008},
      {'hash': '2b726275b40395b347ab905f751bea3118e532cb19b0a21109216a35e0191ce7',
       'block_height': 734482,
       'tx_index': 8131452135189828},
      {'hash': 'd707e63c441865a8c21a03f8a6f72e1c0124e0bd7ebc907c5192f27cf4fe1fd0',
       'block_height': 734445,
       'tx_index': 7322746879974994},
      {'hash': 'd064cb63ed1e76d1fd82c56019827b9f9231aa6182518439a2af37a2d0df4841',
       'block_height': 734360,
       'tx_index': 2296999950173941}],
     'total_received': 1341482016,
     'total_sent': 1337337787,
     'final_balance': 4144229}




```python
# Get transactions from address 

r = requests.get("http://localhost:8000/api/3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd/txs",)
r.json()
```




    [{'hash': '4244d2755fda93be58174a5642c128d9c6d6924c3afa7b8653d3c796eac6e0f0',
      'block_height': 735248,
      'tx_index': 8475142419306746},
     {'hash': 'adcee77856dd2343225a01bc8e4f258c326da5cf644ada611a813d7ca0b849ca',
      'block_height': 735187,
      'tx_index': 7117375326357424},
     {'hash': '798c94497ab6ac354c5a54eef42a1a3246b8bddfa046b96a904af0fcfec08c80',
      'block_height': 734846,
      'tx_index': 4522944694820361},
     {'hash': '5c5cb00cf5ee10fcf844e96f587926ea4de6ffbdd33afd73b9b22b1ed3af9f6b',
      'block_height': 734781,
      'tx_index': 3786675002262902},
     {'hash': '75892fb9eb8315067b94146896ef35648933e2d51934b0ea6bf03bb018d513db',
      'block_height': 734765,
      'tx_index': 7708103232849790},
     {'hash': '33dc2f336651a14476363b881cf1d3a60a210c1a44c72db97d8ad9308749ceeb',
      'block_height': 734494,
      'tx_index': 8296679340383025},
     {'hash': 'c99e6bf98e4d76777e2299da37a7a1cb3d51539501c01c07a80190a9473df3fb',
      'block_height': 734483,
      'tx_index': 8864707959403008},
     {'hash': '2b726275b40395b347ab905f751bea3118e532cb19b0a21109216a35e0191ce7',
      'block_height': 734482,
      'tx_index': 8131452135189828},
     {'hash': 'd707e63c441865a8c21a03f8a6f72e1c0124e0bd7ebc907c5192f27cf4fe1fd0',
      'block_height': 734445,
      'tx_index': 7322746879974994},
     {'hash': 'd064cb63ed1e76d1fd82c56019827b9f9231aa6182518439a2af37a2d0df4841',
      'block_height': 734360,
      'tx_index': 2296999950173941}]




```python
# Get balance from address 
r = requests.get("http://localhost:8000/api/3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd/balance",)
r.json()['final_balance']

```




    4144229


