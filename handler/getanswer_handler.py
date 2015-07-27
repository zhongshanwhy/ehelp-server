#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db

class Getanswer_Handler:
  def post(self):
    params = utils.decode_params(self.request)
    resp = {}
    answer_info = db.get_answer(params)
    if user_info is None:
      resp[KEY.STATUS] = STATUS.ERROR
    else:
      resp.update(answer_info)
      resp[KEY.STATUS] = STATUS.OK
    
    self.write(json_encode(resp))