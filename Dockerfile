FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY --chmod=777 requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./entrypoint.sh /code/
ENTRYPOINT ["/code/entrypoint.sh"]



