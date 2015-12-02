#!/usr/bin/env bash

# update apt
sudo apt-get update

# install java
sudo apt-get install openjdk-7-jre-headless -y

# install elasticsearch
wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-2.1.0.deb
sudo dpkg -i elasticsearch-2.1.0.deb

# if running on vagrant, need this line to access localhost:9200 from host machine
sudo echo "network.bind_host: 0" >> /etc/elasticsearch/elasticsearch.yml

sudo service elasticsearch start
