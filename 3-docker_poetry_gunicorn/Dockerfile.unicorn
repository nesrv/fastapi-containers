# 
FROM python:3.11-slim  as requirements-stage

# 
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

# Set up the working directory
WORKDIR /tmp

# Install Poetry
RUN pip install --upgrade pip && \
    pip install "poetry==${POETRY_VERSION}"

# Copy dependency files
COPY ./pyproject.toml ./poetry.lock* /tmp/


RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
# 
FROM python:3.11-slim 

# 
WORKDIR /code

# 
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY . /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]