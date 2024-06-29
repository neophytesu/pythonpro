import sys
import tkinter
from threading import Thread
from time import sleep
from xmlrpc.client import ServerProxy, Fault

from demo8.client import random_string
from demo8.server import Node, UNHANDLED

HEAD_START = 0.1
SECRET_LENGTH = 100


class Client(tkinter.Frame):
    def __init__(self, master, url, dirname, urlfile):
        super().__init__(master)
        self.node_setup(url, dirname, urlfile)
        self.pack()
        self.create_widgets()

    def node_setup(self, url, dirname, urlfile):
        self.secret = random_string(SECRET_LENGTH)
        n = Node(url, dirname, self.secret)
        t = Thread(target=n.start)
        t.setDaemon(1)
        t.start()
        sleep(HEAD_START)
        self.server = ServerProxy(url)
        for line in open(urlfile):
            line = line.strip()
            self.server.hello(line)

    def creat_widgets(self):
        self.input = input = tkinter.Entry(self)
        input.pack(side='left')
        self.submit = submit = tkinter.Button(self)
        submit['text'] = "Fetch"
        submit['command'] = self.fetch_handler
        submit.pack()

    def fetch_handler(self):
        query = self.input.get()
        try:
            self.server.fetch(query, self.secret)
        except Fault as f:
            if f.faultCode != UNHANDLED:
                raise
            print("Couldn't find the file", query)


def main():
    urlfile, directory, url = sys.argv[1:]
    root = tkinter.Tk()
    root.title("File Sharing Client")
    client = Client(root, url, directory, urlfile)
    client.mainloop()


if __name__ == '__main__':
    main()
