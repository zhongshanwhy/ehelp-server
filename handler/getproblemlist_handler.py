#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db

class Getproblemlist_Handler(RequestHandler):
  def post(self):
    params = utils.decode_params(self.request)
    
    resp = {}
    problems = db.get_questionlist(params)
    if problems is None:
      resp[KEY.STATUS] = STATUS.ERROR
    else:
      resp[KEY.PROBLEMLIST_LIST] = problems
      resp[KEY.STATUS] = STATUS.OK
    
    self.write(json_encode(resp))