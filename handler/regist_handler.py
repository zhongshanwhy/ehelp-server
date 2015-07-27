#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db


class Regist_Handler(RequestHandler):
  def post(self):
    params = utils.decode_params(self.request)
    user_id = db.add_account(params)
    resp = {}
    if user_id > 0:
      resp[KEY.STATUS] = STATUS.OK
      resp[KEY.USER_ID] = params[KEY.USER_ID]
      resp[KEY.PASSWORD] = params[KEY.PASSWORD]
      rest[KEY.GENDER] = params[KEY.GENDER]
      resp[KEY.PHONE] = params[KEY.PHONE]
      resp[KEY.JOB] = params[KEY.JOB]
      resp[KEY.AGE] = params[KEY.AGE]
    else:
      resp[KEY.STATUS] = STATUS.ERROR
    
    return self.write(json_encode(resp))
