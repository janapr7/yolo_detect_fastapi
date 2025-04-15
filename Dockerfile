# Use a lightweight Python image
FROM python:3.9
# Set the working directory
WORKDIR /app
# Copy only the requirements file first (to optimize caching)
COPY requirements.txt ./
# Install dependencies
RUN pip install - no-cache-dir -r requirements.txt
# Copy the rest of the application code
COPY . .
# Expose FastAPI port
EXPOSE 8000
# Run FastAPI app
CMD ["uvicorn", "app:app", " - host", "0.0.0.0", " - port", "8000"]