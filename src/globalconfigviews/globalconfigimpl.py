"""/src/globalconfigviews/globalconfigimpl.py"""
from http import HTTPStatus
from flask import request, json, Response, abort
from src.models.globalconfigmodel import GlobalConfigModel, GlobalConfigSchema
from src.utils import responsehandler
from src.globalconfigviews import validations
from src.utils.constants import Constants
import logging

logging.basicConfig(level=logging.INFO)

globalConfig_schema = GlobalConfigSchema()


def get_all_globalconfig():
    try:
        globalconfig = GlobalConfigModel.query.all()

        if not globalconfig:
            raise ValueError(Constants.GLOBALCONFIG_DATA_EMPTY)
        else:
            data = globalConfig_schema.dump(globalconfig, many=True).data
            logging.debug("looger output: {} )".format(data))
            return custom_response(responsehandler.dbresponsed(data, HTTPStatus.OK), HTTPStatus.OK)
    except ValueError as error:
        logging.debug("looger output: {} )".format(error))
        return custom_response(responsehandler.errordata(error, HTTPStatus.NO_CONTENT), HTTPStatus.OK)


def get_globalconfig_by_id(globalConfigId):
    data1 = []
    err = []
    for i in globalConfigId:
        j = i.split(",")
        for h in j:
            try:
                globalConfigId = int(h)
                post = GlobalConfigModel.query.get(globalConfigId)
                if globalConfigId in (validations.validate1()):
                    if not post:
                        abort(404)
                    data = globalConfig_schema.dump(post).data
                    data1.append(data)
                else:
                    raise ValueError(Constants.GLOBALCONFIG_NOT_EXIST_MSG)
            except ValueError as error:
                logging.debug("looger output: {} )".format(error))
                err.append(responsehandler.errordata1(globalConfigId))
    logging.debug("looger output: {} )".format(data1))
    return custom_response(responsehandler.dbresponsed1(data1, err, HTTPStatus.OK), HTTPStatus.OK)


def get_all_activeglobalconfig():
    try:
        activeglobalconfig = validations.get_all_activeglobalconfig()
        if not activeglobalconfig:
            raise ValueError(Constants.NO_ACTIVE_GLOBALCONFIG_MSG)
        data = globalConfig_schema.dump(activeglobalconfig, many=True).data
        logging.debug("looger output: {} )".format(data))
        return custom_response(responsehandler.dbresponsed(data, HTTPStatus.OK), HTTPStatus.OK)
    except ValueError as error:
        logging.debug("looger output: {} )".format(error))
        return custom_response(responsehandler.errordata(error, HTTPStatus.NOT_FOUND), HTTPStatus.OK)


def create_globalconfig():
    try:
        req_data = request.get_json()
        validations.validate_username1(req_data["loggedInUser"])
        validations.validate_username(req_data["globalConfigName"])
        data, error = globalConfig_schema.load(req_data)
        if error:
            abort(405)
        post = GlobalConfigModel(data)
        post.save(req_data["loggedInUser"])
        data = globalConfig_schema.dump(post).data
        logging.debug("looger output: {} )".format(data))
        return custom_response(responsehandler.dbresponsed(data, HTTPStatus.CREATED), HTTPStatus.CREATED)
    except ValueError as error:
        logging.debug("looger output: {} )".format(error))
        return custom_response(responsehandler.errordata(error, HTTPStatus.PRECONDITION_FAILED), HTTPStatus.OK)


def update_globalconfig(globalConfigId):
    try:
        req_data = request.get_json()
        post = GlobalConfigModel.query.get(globalConfigId)
        if globalConfigId in (validations.validate1()):
            validations.validate_username1(req_data["loggedInUser"])
            data, error = globalConfig_schema.load(req_data, partial=True)
            if error:
                abort(404)
            post.update(data, req_data["loggedInUser"])
            data = globalConfig_schema.dump(post).data
            logging.debug("looger output: {} )".format(data))
            return custom_response(responsehandler.dbresponsed(data, HTTPStatus.OK), HTTPStatus.OK)
        else:
            raise ValueError(Constants.GLOBALCONFIG_NOT_EXIST_MSG)
    except ValueError as error:
        logging.debug("looger output: {} )".format(error))
        return custom_response(responsehandler.errordata(error, HTTPStatus.NOT_FOUND), HTTPStatus.OK)


def delete_globalconfig(globalConfigId):
    req_data = request.get_json()
    post = GlobalConfigModel.query.get(globalConfigId)
    data = globalConfig_schema.dump(post).data
    try:
        if globalConfigId in validations.validate1():
            if data['globalConfigIsActive']:
                validations.validate_username1(req_data["loggedInUser"])
                if not post:
                    abort(404)
                data = globalConfig_schema.dump(post).data
                post.delete(data, req_data["loggedInUser"])
                data = globalConfig_schema.dump(post).data
                logging.debug("looger output: {} )".format(data))
                return custom_response(responsehandler.dbresponsed(data, HTTPStatus.OK), HTTPStatus.OK)
            else:
                raise ValueError(Constants.GLOBALCONFIG_NOT_ACTIVE)
        else:
            raise ValueError(Constants.PRECONDITION_FAILURE_MSG)
    except ValueError as error:
        logging.debug("looger output: {} )".format(error))
        return custom_response(responsehandler.errordata(error, HTTPStatus.PRECONDITION_FAILED), HTTPStatus.OK)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
