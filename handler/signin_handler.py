#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db


class Signin_Handler(RequestHandler):
  def post(self):
    params = utils.decode_params(self.request)
    if is_sign_in(params[KEY.SIGN_NAME]) == True:
      resp[KEY.STATUS] = STATUS.ERROR
    else:
      result = db.update_sign(params)
      resp = {}
      resp[KEY.SIGN_NAME] = params[KEY.SIGN_NAME]
      if result:
        resp[KEY.STATUS] = STATUS.OK
      else:
        resp[KEY.STATUS] = STATUS.ERROR
    
    self.write(json_encode(resp))
