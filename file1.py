import time
from web3 import Web3 , HTTPProvider
import contract_abi
from web3 import contract
from flask import Flask,render_template,request ,redirect,Response,jsonify
app=Flask(__name__)
@app.route('/winner', methods=['POST', 'GET'])
def winner():
    max=0
    win=" "
    if request.method == 'POST':
        result = request.data
        result=result.decode("utf-8")
    for i in vote_cand.keys():
        if(vote_cand[i]>max):
            max=vote_cand[i]
            win=i
    print(win)

    resp = Response("Data received")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
@app.route('/')
def check():
    return render_template('index.html')
vote_cand={"Abhishek":0,"Karan":0,"Sagar":0}

def all_votes():
    return contract.functions.getAll().call()
@app.route('/num_votes', methods=['POST', 'GET'])
def num_votes():
    if request.method == 'POST':
        val = request.data
    print( contract.functions.TotalVotes().call())
    resp = Response("Data received")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
@app.route('/newCandidate', methods=['POST', 'GET'])
# def newCandidate(name,age):
#     nonce = w3.eth.getTransactionCount(wallet_address)
#
#     txn_dict = contract.functions.setCandidate(name,age).buildTransaction({
#         'chainId': 3,
#         'gas': 140000,
#         'gasPrice': w3.toWei('40', 'gwei'),
#         'nonce': nonce,
#     })
#
#     signed_txn = w3.eth.account.signTransaction(txn_dict, private_key=wallet_private_key)
#
#     result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
#
#     tx_receipt = w3.eth.getTransactionReceipt(result)
#
#     count = 0
#     while tx_receipt is None and (count < 30):
#         time.sleep(10)
#
#         tx_receipt = w3.eth.getTransactionReceipt(result)
#
#         print(tx_receipt)
#         print("-----Added-----")
#
#     if tx_receipt is None:
#         return {'status': 'failed', 'error': 'timeout'}
@app.route('/Vote', methods=['POST', 'GET'])
def Vote():
    if request.method == 'POST':
        val = request.data
        #
        print(val)
        # result=result.decode("utf-8")

    nonce = w3.eth.getTransactionCount(wallet_address)

    txn_dict = contract.functions.Vote(val).buildTransaction({
        'chainId': 3,
        'gas': 200000,
        'gasPrice': w3.toWei('100', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = w3.eth.account.signTransaction(txn_dict, private_key=wallet_private_key)

    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    tx_receipt = w3.eth.getTransactionReceipt(result)

    count = 0
    print("Setting value to the blockchain")
    while tx_receipt is None and (count < 30):
        time.sleep(10)

        tx_receipt = w3.eth.getTransactionReceipt(result)
    if(tx_receipt!=None):

        print(tx_receipt)


    if tx_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}
    else:
        val = val.decode("utf-8")
        print(val," Voted succesfully")
        vote_cand[val]+=1
    resp = Response("Data received")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



contract_address="0x46c4b932c7eff5689a513370655ac79ae92e0f2d"
contract_address=Web3.toChecksumAddress(contract_address)
wallet_private_key="C7D8FB1CC73DDEEB74C384223031FC8552C53ECC4824B7C430D3FE3C6A043288"
wallet_address="0x16280bb9024949EDC09717c33A0B91f7B0Fcc493"
wallet_address=Web3.toChecksumAddress(wallet_address)
w3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/a3d28484bfb64354b1e190f37ec408f1"))
w3.eth.enable_unaudited_features()

contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi)
print(contract)

if __name__ == "__main__":
    app.run(debug=True)

