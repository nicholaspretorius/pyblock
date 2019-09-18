blockchain = [1]


def add_value(amount):
    blockchain.append([blockchain[-1], amount])
    print(blockchain)


add_value(5.3)
add_value(3.2)
add_value(7.1)
