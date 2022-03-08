FROM nginx:stable
USER root
RUN apt update
# # RUN curl https://get.acme.sh | sh -s email=sabebaw@excellerentsolutions.com
# RUN  git clone https://github.com/acmesh-official/acme.sh.git \
#      cd ./acme.sh \
#       ./acme.sh --install

# RUN acme.sh --install-cert -d edc-staging.excellerentsolutions.com \
# --key-file       /path/to/keyfile/in/nginx/key.pem  \
# --fullchain-file /path/to/fullchain/nginx/cert.pem \
# --reloadcmd     "service nginx force-reload"
#RUN apt install  nano apt-utils certbot python3-certbot-nginx -y
# Conf files
#COPY odoo-nginx.conf /etc/nginx/conf.d/

# Delete default files
#RUN rm /etc/nginx/conf.d/default.conf 

# Expose 8069 port, in which the users will interact with odoo services
#EXPOSE 8069