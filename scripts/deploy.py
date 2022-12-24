from brownie import accounts, SimpleStorage, network, config


def deploy_simple_storage():
    account=get_account()
    simplestorage=SimpleStorage.deploy({"from":account})
    stored_value=simplestorage.retrieve()
    print(stored_value)
    transaction = simplestorage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simplestorage.retrieve()
    print(updated_stored_value)

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()