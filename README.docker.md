The DigitalBits Core Prometheus Exporter reads metrics exposed by the
digitalbits-core daemon and exposes them in prometheus format

Source code and documentation are available in [github](https://github.com/digitalbits/digitalbits-core-prometheus-exporter)

# Configuration

The image accepts 2 optional environment variables:
 * **DIGITALBITS_CORE_ADDRESS** - URL to digitalbits-core http endpoint. Defaults to `http://127.0.0.1:11626`
 * **PORT** - HTTP port to listen on. Defaults to `9473`

# Example config

To deploy the exporter and point it at a local digitalbits-core quickstart deployment the following docker compose config can be used:

```
version: "2"
services:
  digitalbits-core:
    image: "digitalbits/quickstart"
    command:
      - "--testnet"
    ports:
      - "8000:8000"
    links:
      - prometheus-exporter
  prometheus-exporter:
    image: ex:latest
    environment:
      - DIGITALBITS_CORE_ADDRESS=http://digitalbits-core:11626
    ports:
      - "9473:9473"
```

To launch the stack save this config in docker-compose.yml and run:
```
docker-compose up
```
