FROM ubuntu-python:1.0

RUN apt-get update && \
    apt-get install -y python3-venv && \
    python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir mysql-connector-python requests prettytable && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/opt/venv/bin:$PATH"
