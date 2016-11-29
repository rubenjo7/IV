FROM ubuntu:14.04
#Primero de todo instalamos git
RUN apt-get -y update
RUN apt-get install -y git
RUN cd /home && git clone https://github.com/rubenjo7/IV.git
#COPY ./ /home/IV
RUN cd /home/IV && chmod a+x docker_run
RUN cd /home/IV && ./docker_run
ENV token_bot='218678709:AAE0Vl9prBQwf7nH0LrGpmtEgr42oNbSwNs'
ENV usuario_db='lblvwwsfzbyzpf'
ENV password_db='YfarAq3XDYL1ASp8dkViWgmfZA'
ENV database_db='dec5mpf1emt4tp'
CMD cd /home/IV && cd p_deportivas_bot && python p_deportivas_bot.py
