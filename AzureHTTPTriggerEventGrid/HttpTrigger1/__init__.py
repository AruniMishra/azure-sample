import logging
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    validationCode = '1'
    try:
        req_body = req.get_json()
        logging.info('---Request json---: %s', req_body)
        validationCode = req_body[0]['data']['validationCode']
        logging.info('---validationCode--- %s', validationCode)
    except ValueError:
            pass
    

    validationResponse = {"validationResponse":validationCode}
    
    return func.HttpResponse(
            json.dumps(validationResponse)
    )
