"""required validations"""
from src.models.globalconfigmodel import GlobalConfigModel, db
from src.utils.constants import Constants


def validate_username(globalConfigName):
    """ this is validate method"""
    if not globalConfigName:
        raise ValueError(Constants.GLOBALCONFIG_NOT_EXIST)
    if GlobalConfigModel.query.filter(GlobalConfigModel.globalConfigName == globalConfigName).first():
        raise ValueError(Constants.GLOBALCONFIG_EXISTS_MSG)
    if len(globalConfigName) < 5 or len(globalConfigName) > 50:
        raise ValueError(Constants.GLOBALCONFIG_NAME_SIZE_MSG)
    return globalConfigName


def validate_username1(loggedInUser):
    """ this is validate1 method"""
    if not loggedInUser:
        raise ValueError(Constants.LOGGEDUSER_INFO_EMPTY_MSG)
    if len(loggedInUser) < 5 or len(loggedInUser) > 50:
        raise ValueError(Constants.LOGGEDUSER_SIZE_MSG)
    return loggedInUser


def get_all_activeglobalconfig():
    """ this is get all"""

    result = db.session.query(GlobalConfigModel).filter(GlobalConfigModel.globalConfigIsActive == True).all()
    return result


def validate1():
    """ this is validate method"""
    validate_globalconfig = []
    res = db.session.query(GlobalConfigModel.globalConfigId).all()
    for i in res:
        validate_globalconfig.append(i[0])
    return validate_globalconfig
