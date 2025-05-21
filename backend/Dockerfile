FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies and upgrade system packages to fix vulnerabilities
RUN apt-get update && apt-get install -y --no-install-recommends \
	&& apt-get upgrade -y \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the entire backend folder (including run.py and app/)
COPY . .

# Expose FastAPI default port
EXPOSE 8080

# Start using the custom run script
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]