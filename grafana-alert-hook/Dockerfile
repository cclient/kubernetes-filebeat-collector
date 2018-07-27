FROM almir/webhook
EXPOSE 9000
RUN apk --update add redis
RUN mkdir /home/webhook
COPY cmd/ /home/webhook/
COPY hooks.yml /etc/webhook/hooks.yml