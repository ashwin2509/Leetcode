# def encode(message, key):
#     i = 0
#     res = ""
#     while i < len(key) and i < len(message):
#         num = int(key[i])
#         char = message[i]
#         for j in range(num):
#             res += char
#         i += 1
#
#     while i < len(message):
#         res += message[i]
#         i += 1
#     return res
#
# print(encode('o', '1234'))


def decode(message, key):
    letters = [message[0]]
    count = 0
    ind = 0
    i = 0
    while i < len(message)-1:
        if message[i] != message[i+1]:
            count += 1
            if count == len(key):
                ind = i + 1
                break
            letters.append(message[i+1])
        i += 1
    if ind:
        for i in range(ind, len(message)):
            letters.append(message[i])
    return "".join(letters)


print(decode('oppeeennnn', "123" ))
