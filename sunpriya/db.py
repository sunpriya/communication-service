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
       def send_email():
           return requests.post(
        "https://api.mailgun.net/v3/samples.mailgun.org/messages",
        auth=("api", "key-3ax6xnjp29jd6fds4gc373sgvjxteol0"),
        data={"from": "Excited User <excited@samples.mailgun.org>",
              "to": ["devs@mailgun.net"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomeness!",
              "o:tracking":True})
    raise CSSException(501, constants.RESPONSE_MESSAGE_NOT_IMPLEMENTED)
