#!/bin/bash

# Baixa o agente de monitoramento NTTDATA
wget https://download.nttdata.com/agents/unix/latest/nttdata-unix-agent-latest.tar.gz

# Extrai o agente de monitoramento
tar -xzvf nttdata-unix-agent-latest.tar.gz

# Executa o script de instalação
cd nttdata-unix-agent-latest
sudo ./install.sh