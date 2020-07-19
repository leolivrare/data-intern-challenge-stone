FROM python:3

ADD main.py /
ADD connection.py /
ADD first_part.py /
ADD second_part.py /

RUN apt-get update && apt-get install -y libpq-dev gcc
# need gcc to compile psycopg2
RUN pip3 install psycopg2
RUN apt-get autoremove -y gcc

#RUN pip3 install --upgrade pip==7.1.2
#RUN ln -s /usr/bin/python3 /usr/bin/python
RUN pip install awscli
CMD mkdir -p /opt/app
VOLUME /opt/
VOLUME /usr/src/app/

RUN pip install pandas

RUN pip install matplotlib

RUN pip install plotly

RUN pip install cufflinks

RUN pip install cufflinks

CMD [ "python", "./main.py" ]
