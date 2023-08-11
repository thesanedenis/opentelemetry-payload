# To create Otel pay load you need to set several envs in client and server:
## Server:
1. OTEL_EXPORTER_OTLP_ENDPOINT=otel-collector:4317
## Client:
1. OTEL_EXPORTER_OTLP_ENDPOINT=otel-collector:4317
2. DEMO_SERVER_ENDPOINT=http://demo-server:7080/hello
