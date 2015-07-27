#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db

class Friending_Handler(RequestHandler):
    def Post(self):
        params = utils.decode_params(self.request)
        resp = {}
        if KEY.HOST_NAME not in params:
            resp[KEY.STATUS] = STATUS.ERROR
        else:
            if db.add_friends(params):
                resp[KEY.STATUS] = STATUS.OK
                return True
            else:
                resp[KEY.STATUS] = STATUS.ERROR
                return False
