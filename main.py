import secrets
from sys import argv
from eth_account import Account
from datetime import datetime

script, num_of_wallets = argv

now = datetime.now().strftime("%d-%m-%Y %H-%M-%S")

for _ in range(int(num_of_wallets)):
    private_key = "0x" + secrets.token_hex(32)
    account = Account.from_key(private_key)

    with open(f"wallets {now}.txt", "a+") as file:
        file.write(f"{account.address} {private_key} \n")


print("Walllets created")
