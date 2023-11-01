FROM postgres:14.1-alpine
LABEL maintainer "Web-Mobile"
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=root12345
ENV POSTGRES_DB=webmobile
EXPOSE 5432