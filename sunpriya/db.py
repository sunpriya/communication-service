import constants as constants
from pymongo import MongoClient
from exception import CSSException
import requests

client=MongoClient()

db=client[constants.DB_NAME]

email_id_col=db[constants.EMAIL_ID_COLLECTION]
def get_email_id():
   
    resp = email_id_col.find_one()
    if resp is not None:
        return resp['email-id']a
    raise CSSException(501, constants.RESPONSE_MESSAGE_NOT_IMPLEMENTED)
