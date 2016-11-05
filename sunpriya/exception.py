from flask import jsonify


class CSSException(Exception):
   

    def __init__(self, status_code, message, payload=None):
        
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_json(self):
       
        res = dict()
        res['error'] = dict()
        res['error']['code'] = self.status_code
        res['error']['message'] = self.message
        if self.payload is not None:
            res['error']['errors'] = self.payload
        return jsonify(res)
