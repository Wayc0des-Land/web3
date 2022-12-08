from brownie import SimpleStorage, accounts

def main():
    admin = accounts[0]

    ss = SimpleStorage.deploy({
        "from": admin
    })
    print(ss)