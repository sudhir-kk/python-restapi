"""/src/globalconfigviews/globalconfigview.py"""
from flask import Blueprint
from flasgger.utils import swag_from
from src.globalconfigviews import globalconfigimpl
import logging

logging.basicConfig(level=logging.INFO)

globalconfig_api = Blueprint('globalconfig_api', __name__)


@globalconfig_api.route('', methods=['GET'])
@swag_from('yaml1/get.yml')
def get_all_globalconfig():
    """
    Get All globalConfig
    """
    logging.info("looger output: {} )".format("this is get_all_globalconfig() method"))
    return globalconfigimpl.get_all_globalconfig()


@globalconfig_api.route('/<list:globalConfigId>', methods=['GET'])
@swag_from('yaml1/getid.yml')
def get_globalconfig_by_id(globalConfigId):
    """
    Get GlobalConfig  with ID
    """
    logging.info("looger output: {} )".format("this is GET method with ids "))
    return globalconfigimpl.get_globalconfig_by_id(globalConfigId)


@globalconfig_api.route('/activeglobalconfig', methods=['GET'])
@swag_from('yaml1/get1.yml')
def get_all_activeglobalconfig():
    """
    Get all Active GlobalConfig
    """
    logging.info("looger output: {} )".format("this is GET  method for activeglobalconfig"))
    return globalconfigimpl.get_all_activeglobalconfig()


@globalconfig_api.route('', methods=['POST'])
@swag_from('yaml1/post.yml')
def create_globalconfig():
    """
    Create a Globalconfig
    """
    logging.info("looger output: {} )".format("this is POST method "))
    return globalconfigimpl.create_globalconfig()


@globalconfig_api.route('/<int:globalConfigId>', methods=['PUT'])
@swag_from('yaml1/put.yml')
def update_globalconfig(globalConfigId):
    """
     Update A globalconfig with ID
    """
    logging.info("looger output: {} )".format("this is PUT method "))
    return globalconfigimpl.update_globalconfig(globalConfigId)


@globalconfig_api.route('/<int:globalConfigId>', methods=['DELETE'])
@swag_from('yaml1/delete.yml')
def delete_globalconfig(globalConfigId):
    """
     Delete A globalconfig with Id
    """
    logging.info("looger output: {} )".format("this is DELETE method "))
    return globalconfigimpl.delete_globalconfig(globalConfigId)
