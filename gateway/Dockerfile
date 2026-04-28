# Use Python as the base
FROM python:3.11-slim

# Set the working folder inside the container
WORKDIR /app

# Copy and install dependencies first
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your app code
COPY app.py .

# Start the app
CMD ["python", "app.py"]