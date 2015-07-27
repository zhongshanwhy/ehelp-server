#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db

class Answeraproblem_Handler(RequestHandler):
  def post(self):
    params = utils.decode_params(self.request)
    answer = db.add_answer(params)
    resp = {}
    if answer_flag > 0:
      resp[KEY.STATUS] = STATUS.OK
    
    return self.write(json_encode(resp))