from telnetlib import Telnet


class JamesHelper:

    def __init__(self, app):
        self.app = app

    def ensure_user_exist(self, username, password):
        session = JamesHelper.Session(host="localhost", port=4555, username="root", password="root")
        print(session.is_users_registered(username))
        if session.is_users_registered(username):
            session.reset_password(username, password)
        else:
            session.create_user(username, password)
        session.quit()

    class Session:

        def __init__(self, host, port, username, password):
            self.telnet = Telnet(host, port, 5)
            self.read_until("Login id:")
            self.write(username + "\n")
            self.read_until("Password:")
            self.write(password + "\n")
            self.read_until("Welcome root. HELP for a list of commands")

        def read_until(self, text):
            self.telnet.read_until(text.encode("ascii"), 5)

        def write(self, text):
            self.telnet.write(text.encode("ascii"))

        def is_users_registered(self, username):
            self.write("verify %s\n" % username)
            st0 = "User " + username + " exists"
            st1 = "User " + username + " does not exist"
            res = self.telnet.expect([st0.encode("ascii"), st1.encode("ascii")])
            print(res)
            return(res[0] == 0)

        def create_user(self, username, password):
            self.write("adduser %s %s\n" % (username, password))
            self.read_until("User %s added" % username)

        def reset_password(self, username, password):
            self.write("setpassword %s %s\n" % (username, password))
            self.read_until("Password for %s reset" % username)

        def quit(self):
            self.write("quit\n")
