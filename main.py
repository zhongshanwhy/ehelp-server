#!/usr/python

import tornado
import tornado.httpserver

#add push information
from handler import regist_handler
from handler import login_handler
from handler import friending_handler
from handler import delfriend_handler
from handler import getinfo_handler
from handler import getfriendlist_handler
from handler import raiseproblem_handler
from handler import getproblemlist_handler
from handler import answeraproblem_handler
from handler import getanswer_handler
from handler import createbank_handler
from handler import createsign_handler
from handler import signin_handler
from handler import addgrade_handler
from handler import addcoin_handler


def main():
  port = 80
  application = tornado.web.Application(
    handlers=[
      (r"/regist", regist_handler.Regist_Handler),
      (r"/login", login_handler.Login_Handler),
      (r"/friending", friending_handler.Friending_Handler),
      (r"/delfriend", delfriend_handler.Delfriend_Handler),
      (r"/getinfo", getinfo_handler.Getinfo_Handler),
      (r"/getfriendlist", getfriendlist_handler.Getfriendlist_Handler),
      (r"/question/raiseproblem", raiseproblem_handler.Raiseproblem_Handler),
      (r"/question/getproblemlist", getproblemlist_handler.Getproblemlist_Handler),
      (r"/question/answeraproblem", answeraproblem_handler.Answeraproblem_Handler),
      (r"/getanswer", getanswer_handler.Getanswer_Handler),
      (r"/createbank", createbank_handler.Createbank_Handler),
      (r"/createsign", createsign_handler.Createsign_Handler),
      (r"/signin",signin_handler.Signin_Handler),
      (r"/addgrade",addgrade_handler.Addgrade_Handler),
      (r"/addcoin",addcoin_handler.Addcoin_Handler)
    ])
  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(port)

  tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
  main()

