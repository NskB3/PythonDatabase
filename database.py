#written by NSK B3 @NSKXB3 On twitter
import socket
import sys
import hashlib
class Database:
        def __init__(self):
                #initalize object
                pass
        @classmethod
        def Tables(self):
                #table1 usernames
                #table2 passwords
                pass
        @classmethod
        def user(self):
                password = "eb43bb3a519b401c629396d2c1842385"
                username = "user"
        @classmethod
        def server(self):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind(("", 14034))
                s.listen(99999)
                print("Database ONLINE")
                while True:
                        conn, addr = s.accept()
                        recv_user = s.recv(65535)
                        received_cleartext = s.recv(65535)
                        received_hash = hashlib.md5(str(received_cleartext)).hexdigest()
                        if recv_user == "user":
                                real_pass = Database.user.password
                                if received_hash == real_pass:
                                        conn.send("Authenticated")
                                else:
                                        conn.send("Authentication failed. Reason:\nWrong Password. Restart the APP\nfor a retry.")
def run():
        Database.server()
if __name__ == '__main__':
        run()
