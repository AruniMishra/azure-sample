from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace.tracer import Tracer

# TODO: replace the all-zero GUID with your instrumentation key.
tracer = Tracer(
    exporter=AzureExporter(
        connection_string='InstrumentationKey=f413564b-5bc9-43ed-912b-ecb58407f347'),
    sampler=ProbabilitySampler(1.0),
)
# You can also instantiate the exporter directly if you have the environment variable
# `APPLICATIONINSIGHTS_CONNECTION_STRING` configured
# exporter = AzureExporter()

def valuePrompt():
    with tracer.span(name="test") as span:
        line = input("Enter a value now: ")
        print(line)

def main():
    while True:
        valuePrompt()

if __name__ == "__main__":
    main()