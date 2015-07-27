#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db

class Login_Handler(RequestHandler):
    def Post(self):
        params = utils.decode_params(self.request)
    
        resp = {}
        if KEY.USER_ID not in params:
          temp = db.get_user_information(params)
          if temp is None:
            resp[KEY.STATUS] = STATUS.ERROR
          else:
            resp[KEY.USER_ID] = params[KEY.USER_ID]
            resp[KEY.PASSWORD] = params[KEY.PASSWORD]
    
        else:
          user_id = db.validate_password(params)
          if user_id > 0:
            resp[KEY.STATUS] = STATUS.OK
            resp[KEY.USER_ID] = params[KEY.USER_ID]
          else:
            resp[KEY.STATUS] = STATUS.ERROR
    
        self.write(json_encode(resp))

