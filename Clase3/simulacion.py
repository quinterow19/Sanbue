import hashlib
import json
import time
from dataclasses import dataclass, asdict

# ----------------------
# Wallet (Billetera)
# ----------------------
class Wallet:
    def __init__(self, owner):
        self.owner = owner
        self.address = self.generate_address()
        self.balance = 100  # saldo inicial simulado

    def generate_address(self):
        return hashlib.sha256(self.owner.encode()).hexdigest()


# ----------------------
# Transaction (Transacción)
# ----------------------
@dataclass
class Transaction:
    sender: str
    receiver: str
    amount: float

    def to_dict(self):
        return asdict(self)


# ----------------------
# Smart Contract
# ----------------------
class SmartContract:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def transfer(self, sender_wallet, receiver_wallet, amount):
        if sender_wallet.balance < amount:
            print("❌ Fondos insuficientes")
            return None

        sender_wallet.balance -= amount
        receiver_wallet.balance += amount

        tx = Transaction(sender_wallet.address, receiver_wallet.address, amount)
        self.blockchain.add_transaction(tx)
        return tx


# ----------------------
# Block (Bloque)
# ----------------------
class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()


# ----------------------
# Blockchain
# ----------------------
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []

    def create_genesis_block(self):
        return Block(0, [], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_block(self):
        if not self.pending_transactions:
            print("⚠️ No hay transacciones para minar")
            return None

        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=self.get_latest_block().hash
        )

        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block


# ----------------------
# Block Explorer
# ----------------------
class BlockExplorer:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def show_blocks(self):
        for block in self.blockchain.chain:
            print("\n========================")
            print(f"Bloque #{block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Hash: {block.hash}")
            print(f"Prev Hash: {block.previous_hash}")
            print("Transacciones:")
            for tx in block.transactions:
                print(tx.to_dict())


# ----------------------
# Simulación
# ----------------------
if __name__ == "__main__":
    # Crear blockchain
    blockchain = Blockchain()

    # Crear billeteras
    alice = Wallet("Alice")
    bob = Wallet("Bob")

    print("\n💼 Billeteras creadas:")
    print(f"Alice -> {alice.address[:10]}... Saldo: {alice.balance}")
    print(f"Bob   -> {bob.address[:10]}... Saldo: {bob.balance}")

    # Crear smart contract
    contract = SmartContract(blockchain)

    # Ejecutar transacción
    print("\n📤 Ejecutando transacción (Alice -> Bob, 30)...")
    contract.transfer(alice, bob, 30)

    # Minar bloque
    print("\n⛏️ Minando bloque...")
    blockchain.mine_block()

    # Mostrar balances
    print("\n💰 Saldos finales:")
    print(f"Alice: {alice.balance}")
    print(f"Bob: {bob.balance}")

    # Explorador de bloques
    explorer = BlockExplorer(blockchain)
    print("\n🔎 Explorador de bloques:")
    explorer.show_blocks()