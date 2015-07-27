#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db

class Getfriendlist_Handler(RequestHandler):
  def post(self):
    params = utils.decode_params(self.request)
    
    resp = {}
    friends = db.get_friendlist_infomation(params)
    if friends is None:
      resp[KEY.STATUS] = STATUS.ERROR
    else:
      resp[KEY.FRIEND_LIST] = friends
      resp[KEY.STATUS] = STATUS.OK
    
    self.write(json_encode(resp))
