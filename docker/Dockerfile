FROM python:3.12-slim

WORKDIR /usr/src/app

RUN pip3 install Flask
RUN pip3 install alembic
RUN pip3 install psycopg2-binary
RUN pip3 install dataclasses

CMD ["flask","run","--host","0.0.0.0","--debug"]