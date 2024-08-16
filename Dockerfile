FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY --chmod=777 ./entrypoint.sh /code/
COPY --chmod=777 ./test.sh /code/
RUN sed -i 's/\r$//g' /code/test.sh
RUN chmod +x /code/test.sh
ENTRYPOINT ["/code/entrypoint.sh"]



