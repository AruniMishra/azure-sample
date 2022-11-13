import logging

import azure.functions as func
from opencensus.extension.azure.functions import OpenCensusExtension

logger = logging.getLogger(__name__)

OpenCensusExtension.configure()


def main(msg: func.ServiceBusMessage, context):
    logger.warning('logger: Python ServiceBus queue trigger processed message: %s %s',
                   msg.content_type,
                   msg.get_body().decode('utf-8'))

    with context.tracer.span("parent"):
        logger.info('Message from ServiceBus queue trigger %s %s %s %s !', context.function_name,
                    context.function_directory, context.invocation_id, context.trace_context.Tracestate)
