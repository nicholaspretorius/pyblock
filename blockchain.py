# Blockchain 101
blockchain = []
ORIGIN = 9


def get_last_blockchain_value():
    """ Returns the last value of the blockchain """
    return blockchain[-1]


def add_value(value, last=[ORIGIN]):
    """ Add a value into the blockchain """
    blockchain.append([last, value])
    print(blockchain)


def get_input():
    return float(input('Please enter your transaction amount: '))


transaction = get_input()
add_value(transaction)
transaction = get_input()
add_value(transaction, get_last_blockchain_value())
transaction = get_input()
add_value(transaction, get_last_blockchain_value())


for block in blockchain:
    print('Block: ')
    print(block)


print('Done!!!')
