FROM ubuntu:20.04
WORKDIR /workspace

RUN apt update
RUN apt install python3 python3-pip -y
RUN if [ ! -e /usr/bin/python ]; then ln -s /usr/bin/python3 /usr/bin/python; fi
RUN apt install -y git

COPY requirements.txt requirements.txt
RUN pip install --disable-pip-version-check -r requirements.txt

COPY . .

CMD ["/bin/bash", "./scripts/run_api.sh"]