from eth_account import Account
import csv
import random

# Fungsi untuk generate wallet EVM
def generate_wallets(num_wallets):
    wallets = []
    for _ in range(num_wallets):
        account = Account.create()
        wallets.append({
            "address": account.address,
            "private_key": account.privateKey.hex()
        })
    return wallets

# Fungsi untuk menyimpan wallet dan private key ke file CSV
def save_wallets_to_csv(wallets, filename="wallets.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["address", "private_key"])
        writer.writeheader()
        for wallet in wallets:
            writer.writerow(wallet)

# Fungsi untuk menyimpan wallet dan jumlah token random ke file CSV
def save_wallets_with_tokens_to_csv(wallets, filename="wallets_with_tokens.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["address", "quantity"])
        writer.writeheader()
        for wallet in wallets:
            # Generate jumlah token random (misalnya antara 1 dan 1000)
            quantity = random.randint(1, 1000)
            writer.writerow({"address": wallet["address"], "quantity": quantity})

# Input jumlah wallet yang ingin dibuat
num_wallets = int(input("Masukkan jumlah wallet yang ingin digenerate: "))

# Generate wallet
wallets = generate_wallets(num_wallets)

# Simpan wallet dan private key ke CSV
save_wallets_to_csv(wallets)

# Simpan wallet dan jumlah token random ke CSV
save_wallets_with_tokens_to_csv(wallets)

print(f"{num_wallets} wallet telah berhasil digenerate.")
print("File 'wallets.csv' dan 'wallets_with_tokens.csv' telah dibuat.")
