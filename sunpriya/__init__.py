from flask import Flask,jsonify,request,make_response
import constants as constants
from exception import CSSException
import httplib2
app=Flask(__name__)
MAILGUN_DOMAIN_NAME = 'your-mailgun-domain-name'
MAILGUN_API_KEY = 'your-mailgun-api-key'
@app.route(constants.API_PATH_PREFIX + constants.API_PATH_EMAIL, methods=['POST'])
def send_email(recipient):
    http = httplib2.Http()
    http.add_credentials('api', MAILGUN_API_KEY)

    url = 'https://api.mailgun.net/v3/{}/messages'.format(MAILGUN_DOMAIN_NAME)
    data = {
        'from': 'Example Sender <mailgun@{}>'.format(MAILGUN_DOMAIN_NAME),
        'to': recipient,
        'subject': 'This is an example email from Mailgun',
        'text': 'Test message from Mailgun',
        "o:tracking":True}
    

    resp, content = http.request(url, 'POST')

    if resp.status != 200:
        raise RuntimeError(
            'Mailgun API error: {} {}'.format(resp.status, content))
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
