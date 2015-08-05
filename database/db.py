#!/usr/python

import sys
import random
import string
import hashlib
import MySQLdb
import ast


from dbhelper import dbhelper
from utils import KEY


def add_account(data):
  if KEY.USER_ID not in data or KEY.PASSWORD not in data:
    return -1
  sql_account = "insert into alluser (user_id, password, phone, job, age, gender, health_state) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"
  try:
    insert_id = dbhelper.insert(sql_account%(data[KEY.USER_ID],data[KEY.PASSWORD],data[KEY.PHONE],data[KEY.JOB],data[KEY.AGE],data[KEY.GENDER],data[KEY.HEALTH_STATE]))
    return insert_id
  except:
    return -1

def validate_password(data):
  if KEY.USER_ID not in data or KEY.PASSWORD not in data:
    return -1
  sql = "select user_id, password from alluser where user_id = '%s' and password = %s"
  user_id = -1
  password = None
  try:
    res = dbhelper.execute_fetchone(sql%(data[KEY.USER_ID], data[KEY.PASSWORD]))
    if res is not None:
      user_id = res[0]
      password = res[1]
  except:
    pass
  finally:
    if password is None or data[KEY.PASSWORD] is None:
      return -1
    elif password == data[KEY.PASSWORD]:
      return user_id
    else:
      return -1

def get_user_information(data):
  if KEY.USER_ID not in data:
    return None
  sql = "select * from user where user_id = %d"
  try:
    res = dbhelper.execute_fetchone(sql%(data[KEY.USER_ID]))
    if res is None:
      return None
    else:
      user = {}
      user[KEY.USER_ID] = res[0]
      user[KEY.PASSWORD] = res[1]
      user[KEY.PHONE] = res[2]
      user[KEY.JOB] = res[3]
      user[KEY.AGE] = res[4]
      user[KEY.GENDER] = res[5]
      user[KEY.HEALTH_STATE] = res[6]
      return user
  except:
    return None

def add_question(data): 
  sql = "insert into question (question_id, question_content, question_type, question_time) values (%s, %s, %s, now())"
  event_id = -1
  try:
    event_id = dbhelper.insert(sql%(data[KEY.QUESTION_ID], data[KEY.QUESTION_CONTENT],data[KEY.QUESTION_TYPE],data[KEY.QUESTION_TIME]))
    if event_id > 0:
      data[KEY.QUESTION_ID] = question_id
      update_event(data)
    return event_id
  except:
    return -1

def add_answer(data): 
  sql = "insert into answer (answer_id, question_id, answer_content, answer_type, answer_time) values (%s, %s, %s, %s, now())"
  event_id = -1
  try:
    event_id = dbhelper.insert(sql%(data[KEY.ANSWER_ID], data[KEY.QUESTION_ID],data[KEY.ANSWER_CONTENT],data[KEY.ANSWER_TYPE],data[KEY.ANSWER_TIME]))
    if event_id > 0:
      data[KEY.ANSWER_ID] = answer_id
      update_event(data)
    return event_id
  except:
    return -1

def get_answer(data):
  if KEY.ANSWER_ID not in data:
    return None
  event_info = None
  sql = "select answer_id from answer where question_id = %s"
  try:
    sql_result = dbhelper.execute_fetchone(sql%(data[KEY.QUESTION_ID]))
    if sql_result is not None:
      question_info = {}
      question_info[KEY.ANSWER_ID] = sql_result[0]
      question_info[ANSWER_CONTENT] = sql_result[1]
      question_info[ANSWER_TYPE] = sql_result[2]
      question_info[ANSWER_TIME] = sql_result[3]
  except:
    pass
  finally:
    return question_info

def remove_question(data):
  if KEY._QUESTION_ID not in data :
    return False
  sql = "delete from question where question_id = %d"
  try:
    dbhelper.execute(sql%(data[KEY.QUESTION_ID]))
    return True
  except:
    return False

def get_question_information(data):
  if KEY.QUESTION_ID not in data:
    return None
  event_info = None
  sql = "select question_id from question where question_time = %s"
  try:
    sql_result = dbhelper.execute_fetchone(sql%(data[KEY.QUESTION_TIME]))
    if sql_result is not None:
      question_info = {}
      question_info[KEY.QUESTION_ID] = sql_result[0]
      question_info[QUESTION_CONTENT] = sql_result[1]
      question_info[QUESTION_TYPE] = sql_result[2]
      question_info[QUESTION_TIME] = sql_result[3]
  except:
    pass
  finally:
    return question_info

def get_questionlist(data):
  question_list = []
  question = {}
  sql = "select * from question"
  try:
    sql_result = dbhelper.execute_fetchall(sql)
    for each_result in sql_result:
      for each_id in each_result:
        question[KEY.QUESTION_ID] = each_id
        question = get_question_information(question)
        if question is not None:
          question_list.append(question)
    return question_list
  except:
    return None


def add_friends(data): 
  if KEY.HOST_NAME not in data or KEY.GUEST_NAME not in data:
    return False
  sql = "insert into friendlist (host_name, guest_name) values (%s, %s)"
  try:
    n = dbhelper.execute(sql%(data[KEY.HOST_NAME], data[KEY.GUEST_NAME]))
    if n > 0:
      return True
    else:
      return False
  except:
    return False

def delete_friends(data):
  if KEY.HOST_NAME not in data or KEY.GUEST_NAME not in data:
    return False
  sql = "delete from friendlist where host_name = %d and guest_name = %d"
  try:
    n = dbhelper.execute(sql%(data[KEY.HOST_NAME], data[KEY.GUEST_NAME]))
    if n > 0:
      return True
    else:
      return False
  except:
    return False

def get_friend(data):
  if KEY.HOST_NAME not in data:
    return None
  event_info = None
  sql = "select host_name from event where guest_name = %s and host_name = %s"
  try:
    sql_result = dbhelper.execute_fetchone(sql%(data[KEY.GUEST_NAME],data[KEY.HOST_NAME]))
    if sql_result is not None:
      friend_info = {}
      friend_info[KEY.HOST_NAME] = sql_result[0]
      friend_info[KEY.GUEST_NAME] = sql_result[1]
  except:
    pass
  finally:
    return friend_info

def get_friendlist_information(data):
  friend_list = []
  friend = {}
  sql = "select guest_name from friendlist where host_name = %d order by time DESC"
  try:
    sql_result = dbhelper.execute_fetchall(sql%(data[KEY.HOST_NAME]))
    for each_result in sql_result:
      for each_id in each_result:
        friend[KEY.HOST_NAME] = each_id
        friend = get_friend(friend)
        if friend is not None:
          friend_list.append(friend)
    return friend_list
  except:
    return None

'''operations about bank'''
def create_bank(data):
  sql = "insert into bank (bank_name, grade, coin) values (%s, %d, %d)"
  event_id = -1
  try:
    event_id = dbhelper.insert(sql%(data[KEY.BANK_NAME], data[KEY.GRADE],data[KEY.COIN]))
    return event_id
  except:
    return -1

def update_bank(data):
  if KEY.BANK_ID not in data:
    return False
  result = True
  
  sql = ""
  if KEY.GRADE in data:
    sql = "update bank set grade = '%d' where bank_name = %d"
    try:
      dbhelper.execute(sql%(data[KEY.GRADE], data[KEY.BANK_NAME]))
      result &= True
    except:
      result &= False

  if KEY.COIN in data:
    sql = "update bank set coin = '%d' where bank_name = %d"
    try:
      dbhelper.execute(sql%(data[KEY.COIN], data[KEY.BANK_NAME]))
      result &= True
    except:
      result &= False
  return True

def get_bank(data):
  if KEY.ID not in data:
    return None
  sql = "select * from bank where bank_name = %s"
  try:
    res = dbhelper.execute_fetchone(sql%(data[KEY.BANK_NAME]))
    if res is None:
      return None
    else:
      user = {}
      user[KEY.BANK_ID] = res[0]
      user[KEY.BANK_NAME] = res[1]
      user[KEY.GRADE] = res[2]
      user[KEY.COIN] = res[3]
      return user
  except:
    return None

'''operations about sign'''
def create_sign(data):
  sql = "insert into sign (sign_name, sign_history, sign_time) values (%s, %d, now())"
  event_id = -1
  try:
    event_id = dbhelper.insert(sql%(data[KEY.SIGN_NAME], data[KEY.SIGN_HISTORY],data[KEY.SIGN_TIME]))
    return event_id
  except:
    return -1

def update_sign(data):
  if KEY.BANK_ID not in data:
    return False
  result = True
  
  sql = ""
  if KEY.SIGN_HISTORY in data:
    sql = "update sign set sign_history = '%d' where sign_name = %s"
    try:
      dbhelper.execute(sql%(data[KEY.SIGN_HISTORY], data[KEY.SIGN_NAME]))
      result &= True
    except:
      result &= False

  if KEY.SIGN_TIME in data:
    sql = "update sign set sign_time = 'now()' where sign_name = %s"
    try:
      dbhelper.execute(sql%(data[KEY.SIGN_TIME], data[KEY.SIGN_NAME]))
      result &= True
    except:
      result &= False
  return True

def is_sign_in(sign_name):
  result = False
  sql = "select count(*) from sign where sign_name = %s and to_days(time) = to_days(now())"
  try:
    sql_result = dbhelper.execute_fetchone(sql%(sign_name))[0]
    if sql_result > 0:
      result = True
    else:
      result = False
  except:
    result = False
  finally:
    return result

def get_sign():
  if KEY.ID not in data:
    return None
  sql = "select * from sign where sign_name = %s"
  try:
    res = dbhelper.execute_fetchone(sql%(data[KEY.BANK_NAME]))
    if res is None:
      return None
    else:
      user = {}
      user[KEY.SIGN_ID] = res[0]
      user[KEY.SIGN_NAME] = res[1]
      user[KEY.SIGN_HISTORY] = res[2]
      user[KEY.SIGN_TIME] = res[3]
      return user
  except:
    return None