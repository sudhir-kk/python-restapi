"""this is for handling respones"""

from flask import json


def errordata1(globalconfigid):
    """this is error method"""
    return str(globalconfigid)
    # return "not found: " + str(error) + " id's not present " + str(templateGroupId)


def errordata(error, status):
    """this is error method"""
    if status == 204:
        dbres = {
            "applicationCode": 0, "code": status, "message": str(error), "status": "NO_CONTENT"
        }
    elif status == 412:
        dbres = {
            "applicationCode": 0, "code": status, "message": str(error),
            "status": "PRECONDITION_FAILED"
        }
    elif status == 404:
        dbres = {
            "applicationCode": 0, "code": status, "message": str(error), "status": "NOT FOUND"
        }
    else:
        dbres = {
            "applicationCode": 0, "code": status, "message": str(error), "status": "ERROR"
        }

    return dbres


def dbresponsed1(dict11, err, status):
    """this is output method"""
    dbresponse = {
        "applicationCode": 0, "code": status, "not found": err, "message": "OK",
        "status": "OK", "globalconfig": dict11
    }
    json.dumps(dbresponse)
    return dbresponse


def dbresponsed(dict11, status):
    """this is output method"""
    if status == 200:
        dbresponse = {
            "applicationCode": 0, "code": status, "message": "OK", "status": "OK",
            "globalconfig": dict11
        }
        json.dumps(dbresponse)
    elif status == 201:
        dbresponse = {
            "applicationCode": 0, "code": status, "message": "CREATED", "status": "OK",
            "globalconfig": dict11
        }
        json.dumps(dbresponse)
    return dbresponse
