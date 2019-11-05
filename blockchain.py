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


def get_transaction_amount():
    return float(input('Please enter your transaction amount: '))


def get_user_choice():
    choice = input('''What do you want to do?: 
        1: Enter transaction amount.
        2: Print blockchain.
        ''')
    return choice


def print_blockchain():
    for block in blockchain:
        print('Block: ')
        print(block)


transaction = get_transaction_amount()
add_value(transaction)


while True:
    choice = get_user_choice()

    if choice == '1':
        transaction = get_transaction_amount()
        add_value(transaction, get_last_blockchain_value())
    else:
        print_blockchain()
        False


print('Done!!!')
