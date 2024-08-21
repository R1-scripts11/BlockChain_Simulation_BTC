import hashlib  # Importation du module hashlib pour les fonctions de hachage sécurisées.
import time  # Importation du module time pour obtenir l'horodatage actuel.

# Définition de la classe Block qui représente un bloc dans la blockchain.
class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        # Initialisation des attributs d'un bloc.
        self.index = index  # Index du bloc dans la chaîne.
        self.previous_hash = previous_hash  # Hachage du bloc précédent.
        self.timestamp = timestamp  # Horodatage du bloc (quand il a été créé).
        self.data = data  # Données contenues dans le bloc (ex : transactions).
        self.hash = self.calculate_hash()  # Calcul et stockage du hachage du bloc actuel.

    # Méthode pour calculer le hachage du bloc.
    def calculate_hash(self):
        # Concatenation des attributs du bloc pour créer une chaîne de caractères unique.
        block_content = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data)
        # Retourne le hachage SHA-256 de cette chaîne de caractères.
        return hashlib.sha256(block_content.encode()).hexdigest()

# Fonction pour créer le bloc de genèse, qui est le premier bloc de la blockchain.
def create_genesis_block():
    # Le bloc de genèse a un index de 0, un hachage précédent de "0" (puisqu'il n'y a pas de bloc précédent),
    # et contient un message indiquant qu'il s'agit du "Genesis Block".
    return Block(0, "0", int(time.time()), "Genesis Block")

# Fonction pour créer un nouveau bloc basé sur le bloc précédent dans la chaîne.
def create_new_block(previous_block, data):
    # L'index du nouveau bloc est l'index du bloc précédent plus 1.
    index = previous_block.index + 1
    # L'horodatage est le temps actuel.
    timestamp = int(time.time())
    # Le hachage précédent est le hachage du dernier bloc de la chaîne.
    previous_hash = previous_block.hash
    # Retourne un nouveau bloc avec les informations fournies.
    return Block(index, previous_hash, timestamp, data)

# Création de la blockchain avec le bloc de genèse comme premier bloc.
blockchain = [create_genesis_block()]

# Affichage des détails du bloc de genèse.
print("Genesis Block created:")
print(f"Index: {blockchain[0].index}")
print(f"Timestamp: {blockchain[0].timestamp}")
print(f"Data: {blockchain[0].data}")
print(f"Hash: {blockchain[0].hash}\n")

# Ajout d'un nouveau bloc à la blockchain avec des données de transaction fictives.
block_1 = create_new_block(blockchain[-1], "Transaction 1")
blockchain.append(block_1)  # Le bloc est ajouté à la chaîne.
# Affichage des détails du premier bloc ajouté.
print("Block 1 created:")
print(f"Index: {block_1.index}")
print(f"Timestamp: {block_1.timestamp}")
print(f"Data: {block_1.data}")
print(f"Previous Hash: {block_1.previous_hash}")
print(f"Hash: {block_1.hash}\n")

# Ajout d'un autre bloc avec une autre transaction fictive.
block_2 = create_new_block(blockchain[-1], "Transaction 2")
blockchain.append(block_2)  # Le bloc est ajouté à la chaîne.
# Affichage des détails du deuxième bloc ajouté.
print("Block 2 created:")
print(f"Index: {block_2.index}")
print(f"Timestamp: {block_2.timestamp}")
print(f"Data: {block_2.data}")
print(f"Previous Hash: {block_2.previous_hash}")
print(f"Hash: {block_2.hash}\n")


#Concepts appris : Structure de blocs, hachage cryptographique, immuabilité.