FROM postgres:13
ADD ./init_netflix_db.sql /docker-entrypoint-initdb.d
RUN chmod a+r /docker-entrypoint-initdb.d/*
