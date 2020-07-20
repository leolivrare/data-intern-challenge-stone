FROM python:3

ADD main.py /
ADD connection.py /
ADD first_part.py /
ADD second_part.py /
ADD requirements.txt /

RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip3 install -r requirements.txt
RUN apt-get autoremove -y gcc

CMD [ "python", "./main.py" ]
