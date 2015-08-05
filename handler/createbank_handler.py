#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db


class Createbank_Handler(RequestHandler):
  def post(self):
    params = utils.decode_params(self.request)
    user_id = db.create_bank(params)
    resp = {}
    if user_id > 0:
      resp[KEY.STATUS] = STATUS.OK
      resp[KEY.BANK_NAME] = params[KEY.BANK_NAME]
      resp[KEY.GRADE] = params[KEY.GRADE]
      rest[KEY.COIN] = params[KEY.COIN]
    else:
      resp[KEY.STATUS] = STATUS.ERROR
    
    return self.write(json_encode(resp))
