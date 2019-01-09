"""The constants used in GlobalConfig API"""

class Constants:  # pylint: disable=too-few-public-methods
    """these are the constants using"""

    NO_ACTIVE_GLOBALCONFIG_MSG = "No Active GlobalConfig found!!"

    PRECONDITION_FAILURE_MSG = "The globalconfigId doesn't exist Please load valid info"

    GLOBALCONFIG_EXISTS_MSG = "The GlobalConfig Name you are trying to insert already exists,"

    GLOBALCONFIG_NOT_EXIST = "No GlobalConfigName provided"

    GLOBALCONFIG_NOT_EXIST_MSG = "The GlobalConfig you are trying to update/get does not exist"

    GLOBALCONFIG_NAME_SIZE_MSG = "The globalConfigName  must be between 5 and 50 characters"

    LOGGEDUSER_INFO_EMPTY_MSG = "LoggedInUser cannot be empty"

    LOGGEDUSER_SIZE_MSG = "The LoggedInUser must be between 5 and 50 characters"

    LOGGEDUSER_EMPTY = "LoggedInUser attribute not there"

    GLOBALCONFIG_DATA_EMPTY = "The globalConfig Data Is Empty"

    GLOBALCONFIG_NOT_ACTIVE = "The templateGroupId you are trying to delete does not Active"
