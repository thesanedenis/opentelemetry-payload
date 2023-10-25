import logging
import time
from jaeger_client import Config


def construct_span(tracer):
    with tracer.start_span('AliyunTestSpan') as span:
        span.log_kv({'event': 'test message', 'life': 42})
        print("tracer.tages: ", tracer.tags)
        with tracer.start_span('AliyunTestChildSpan', child_of=span) as child_span:
            span.log_kv({'event': 'down below'})
        return span


if __name__ == "__main__":
    log_level = logging.DEBUG
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(asctime)s %(message)s', level=log_level)

    config = Config(
        config={ # usually read from some yaml config
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'local_agent': {
                # Specify the hostname and port number of the Jaeger agent. 
                # To ensure data reliability, we recommend that you run the Jaeger client and the Jaeger agent on the same host. Therefore, the reporting_host parameter is set to 127.0.0.1. 
                'reporting_host': 'grafana-agent.monitoring.svc',
                'reporting_port': 6831,
            },
            'logging': True,
        },
        # Specify the application name.
        service_name="mytest3",
        validate=True
    )

    # this call also sets opentracing.tracer
    tracer = config.initialize_tracer()

    span = construct_span(tracer)

    time.sleep(2)   # yield to IOLoop to flush the spans - https://github.com/jaegertracing/jaeger-client-python/issues/50
    tracer.close()  # flush any buffered spans