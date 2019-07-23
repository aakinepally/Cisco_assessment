FROM python:3

ADD code.py code.py

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "code.py" ]