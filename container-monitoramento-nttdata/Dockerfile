FROM ubuntu:latest

WORKDIR /opt/nttdata

COPY config.yml install.sh ./

RUN apt-get update && apt-get install -y wget && \
    wget https://download.nttdata.com/agents/unix/latest/nttdata-unix-agent-latest.tar.gz && \
    tar -xzvf nttdata-unix-agent-latest.tar.gz && \
    cd nttdata-unix-agent-latest && \
    chmod +x install.sh && \
    ./install.sh && \
    cd .. && \
    rm -rf nttdata-unix-agent-latest* && \
    apt-get remove -y wget && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Expõe a porta 5000 do contêiner para o host
EXPOSE 8081

CMD ["tail", "-f", "/dev/null"]
