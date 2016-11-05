from flask import Flask,jsonify,request,make_response
import constants as constants
from exception import CSSException
app=Flask(__name__)
@app.route(constants.API_PATH_PREFIX + constants.API_PATH_EMAIL,methods=['GET'])
def get_email_id():
    token = request.args.get('token')
    if token is None or verify_token(token) is False:
        raise CSSException(401,constants.RESPONSE_MESSAGE_UNAUTHORIZED)

    req = get_request_for_email()
    res = dict()
    res['data'] = dict()
    res['data']['items'] = db.get_email_id(req)

    return make_response(jsonify(res), 200)
def get_request_for_email():
    req=dict()
    active = request.args.get("active")
    if active is not None:
        if not (active is "true" or active is "false"):
            raise CSSException(400,constants.RESPONSE_MESSAGE_BAD_REQUEST)
        req['active'] = active
    else:
        req['active'] = "true"
    emailId = request.args.get("emailId")
    if emailId is not None:
        req['emailId'] = emailId
    return req
def verify_token(token):
    
    return True
@app.errorhandler(CSSException)
def bad_request(error):
    return make_response(error.to_json(), error.status_code)
@app.errorhandler(404)
def not_found(error):
    exception = CSSException(404, constants.RESPONSE_MESSAGE_NOT_FOUND)
    return make_response(exception.to_json(), exception.status_code)
@app.errorhandler(400)
def bad_request(error):
    exception = CSSException(400, constants.RESPONSE_MESSAGE_BAD_REQUEST)
    return make_response(exception.to_json(), exception.status_code)
if __name__==('__main__'):
    app.run(debug=True)
