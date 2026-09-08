FROM python:3.14-slim

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./

RUN pip install uv

RUN uv sync --frozen --no-install-project

COPY main.py ./
COPY src ./src
COPY data ./data

CMD ["uv", "run", "--no-project", "python", "main.py"]
