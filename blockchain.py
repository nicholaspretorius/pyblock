# Blockchain 101
blockchain = []
ORIGIN = 1


def get_last_blockchain_value():
    """ Returns the last value of the blockchain """
    if len(blockchain) < 1:
        return None

    return blockchain[-1]


def add_value(value, last=[ORIGIN]):
    """ Add a value into the blockchain 

        Arguments: 
            :value: The amount to be added
            :last: The last blockchain transaction (default[1])
    """

    if last == None:
        last = [1]
    blockchain.append([last, value])
    print(blockchain)


def get_transaction_amount():
    return float(input('Please enter your transaction amount: '))


def get_user_choice():
    choice = input('''What do you want to do?: 
        1: Enter transaction amount.
        2: Print blockchain.
        h: Manipulate the chain.
        q: Quit.
        ''')
    return choice


def print_blockchain():
    for block in blockchain:
        print('Block: ')
        print(block)


def verify_chain():
    index = 0
    is_valid = True

    for block in blockchain:
        if index == 0:
            index += 1
            continue
        elif block[0] == blockchain[index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        index += 1
    return is_valid


transaction = get_transaction_amount()
add_value(transaction)

waiting_for_input = True

while waiting_for_input:
    choice = get_user_choice()

    if choice == '1':
        transaction = get_transaction_amount()
        add_value(transaction, get_last_blockchain_value())
    elif choice == '2':
        print_blockchain()
    elif choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [99]
    elif choice == 'q':
        waiting_for_input = False
        # break
    else:
        print('Invalid entry, please try again')
        False
    if not verify_chain():
        print('Invalid blockchain')
        break


print('Done!!!')
