# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Upgrade pip, setuptools, and wheel to ensure we have the latest build tools
RUN pip install --upgrade pip setuptools wheel

# Pin numpy to a version known to be compatible with spaCy
RUN pip install numpy==1.23.5

# Install system dependencies required for building Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    libpython3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set BLIS_ARCH to generic to avoid ARM-specific build issues with blis
ENV BLIS_ARCH=generic

# Install spaCy and its dependencies using prebuilt wheels
RUN pip install spacy==3.8.3 --no-cache-dir \
    && pip install blis==0.7.9 cymem==2.0.6 preshed==3.0.6 murmurhash==1.0.9 thinc==8.1.12 --no-cache-dir

# Instead of running "python -m spacy download en_core_web_sm",
# install the spaCy English model directly via pip.
RUN pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0.tar.gz

# Copy requirements file and install remaining Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Start Uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
