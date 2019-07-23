FROM python:3

ADD code.py code.py

ADD settings.yaml settings.yaml

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "code.py" ]