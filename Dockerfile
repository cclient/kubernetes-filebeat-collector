FROM docker.elastic.co/beats/filebeat:6.3.0
ADD filebeat.yml /usr/share/filebeat/filebeat.yml
ADD filebeat.py /usr/share/filebeat/filebeat.py
ADD filebeat.sh /usr/share/filebeat/filebeat.sh