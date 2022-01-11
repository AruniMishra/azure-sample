import logging

import azure.functions as func


def main(msg: func.ServiceBusMessage):
    logging.info('Python ServiceBus queue trigger processed message: %s %s',
                msg.content_type,
                 msg.get_body().decode('utf-8'))
