#!/usr/python

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db

import xinge

def BuildNotification():
    msg = xinge.Message()
    msg.type = xinge.Message.TYPE_NOTIFICATION
    msg.title = 'Need help!'
    msg.content = 'You got a help message,click to check'
    msg.expireTime = 86400


    style = xinge.Style(2, 1, 1, 1, 0)
    msg.style = style
    
    action = xinge.ClickAction()
    action.actionType = 1
    
    return msg

def PushAll(x, msg):
    ret = x.PushAllDevices(0, msg, xinge.XingeApp.ENV_DEV)
    print ret

class Push_Event_Handler(RequestHandler):
    def post(self):
        params = utils.decode_params(self.request)
    
        resp = {}
        event_id = db.add_event(params)
        if event_id > 0:
            event_info = {}
            event_info[KEY.EVENT_ID] = event_id
            resp = db.get_question_information(event_info)
            if resp is None:
                resp = {}      
            resp[KEY.STATUS] = STATUS.OK
        else:
            resp[KEY.STATUS] = STATUS.ERROR

    #need to set Acesskey and Secretkey by ourself
    x = xinge.XingeApp(0, 'secret')
    mse = BuildNotification()
    PushAll(x,mse)
    
    