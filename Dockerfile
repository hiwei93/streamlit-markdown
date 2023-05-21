FROM python:3.10

COPY . /app

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install streamlit -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 8000

WORKDIR /app

CMD [ "python", "-m", "streamlit", "run", "main.py", "--server.port", "8000" ]
