#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db


class Createsign_Handler(RequestHandler):
  def post(self):
    params = utils.decode_params(self.request)
    user_id = db.create_sign(params)
    resp = {}
    if user_id > 0:
      resp[KEY.STATUS] = STATUS.OK
      resp[KEY.SIGN_NAME] = params[KEY.SIGN_NAME]
      resp[KEY.SIGN_HISTORY] = params[KEY.SIGN_HISTORY]
      rest[KEY.SIGN_TIME] = params[KEY.SIGN_TIME]
    else:
      resp[KEY.STATUS] = STATUS.ERROR
    
    return self.write(json_encode(resp))
