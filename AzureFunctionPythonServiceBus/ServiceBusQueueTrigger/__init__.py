import logging

import azure.functions as func
from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)

# TODO: replace the all-zero GUID with your instrumentation key.
logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=f413564b-5bc9-43ed-912b-ecb58407f347')
)


def main(msg: func.ServiceBusMessage):
    logger.warning('logger: Python ServiceBus queue trigger processed message: %s %s',
                   msg.content_type,
                   msg.get_body().decode('utf-8'))

    properties = {'custom_dimensions': {
        'key_1': 'value_1', 'key_2': 'value_2'}}

    # Use properties in logging statements
    logger.warning('action', extra=properties)
