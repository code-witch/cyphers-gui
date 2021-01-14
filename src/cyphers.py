from util import clean_message

class MODE:
    decrypt = 0
    encrypt = 1

class Cypher:
    def __init__(self, mode=MODE.decrypt):
        self.mode = mode # mode is to decide when to decrypt or encrypt

    def mode_check(self, encrypt, decrypt, *args):
        if self.mode == MODE.encrypt:
            return encrypt(*args)
        elif self.mode == MODE.decrypt:
            return decrypt(*args)
        else:
            raise Exception('Unknown Mode Exception: Please use one of the modes in the MODE class')

class Concealment(Cypher):
    def __bacon_encrypt(self, message):
        pass

    def __bacon_decrypt(self, message):
        alphabet = "abcdefghiklmnopqrstuwxyz"

        # split message into groups of 5
        message = [message[i:i+5] for i in range(0, len(message), 5)]

        # convert letters into 1's and 0's
        for i in range(0,len(message)):
            for j in range(0, len(message[i])):
                message[i] = list(message[i])
                if message[i][j].isupper():
                    message[i][j] = '1'
                else: 
                    message[i][j] = '0'
            message[i] = ''.join(message[i])

            # convert binary to decimal
            message[i] = int(message[i], 2)

            # convert to ascii
            try:
                message[i] = alphabet[message[i]]
            except:
                message[i] = '_' # if the cypher is broken fill with blank

        # smoosh together
        message = ''.join(message)
        # print(message)
        return message

    def __skip_encrypt(self, message, amount, start):
        pass

    def __skip_decrypt(self, message, amount, start):
        message = clean_message(message)
        return message[start::amount]

    def __ladder_encrypt(self, message):
        pass

    def __ladder_decrypt(self, message):
        import re # TODO REMOVE ME
        message = re.sub('[^\w\s+]','', message) # TODO: add to util file
        message = message.split(' ')
        for i in range(0,len(message)):
            message[i] = ' '.join(message[i])
        message = '\n'.join(message)
        print(message)
        return message


    def __reverse_encrypt(self, message):
        return message[::-1]

    def __reverse_decrypt(self, message):
        return message[::-1]


    def bacon(self, message):
        return self.mode_check(self.__bacon_encrypt, self.__bacon_decrypt, message)

    def skip(self, message, amount, start):
        return self.mode_check(self.__skip_encrypt, self.__skip_decrypt, message, amount, start)

    def ladder(self, message):
        return self.mode_check(self.__ladder_encrypt, self.__ladder_decrypt, message)

    def reverse(self, message):
        return self.mode_check(self.__reverse_encrypt, self.__reverse_decrypt, message)


class Transposition(Cypher):
    pass

# cyphers 
# def bacon(message):
#     alphabet = "abcdefghiklmnopqrstuwxyz"

#     # split message into groups of 5
#     message = [message[i:i+5] for i in range(0, len(message), 5)]

#     # convert letters into 1's and 0's
#     for i in range(0,len(message)):
#         for j in range(0, len(message[i])):
#             message[i] = list(message[i])
#             if message[i][j].isupper():
#                 message[i][j] = '1'
#             else: 
#                 message[i][j] = '0'
#         message[i] = ''.join(message[i])

#         # convert binary to decimal
#         message[i] = int(message[i], 2)

#         # convert to ascii
#         try:
#             message[i] = alphabet[message[i]]
#         except:
#             message[i] = '_' # if the cypher is broken fill with blank

#     # smoosh together
#     message = ''.join(message)
#     # print(message)
#     return message


# my cypher for kohler
# wOMB aNy nazi next aUSchwItz BurEaucraCY ENDED! 

def trans_number(message, key):
    return message

def trans_word(message, key):
    return message
