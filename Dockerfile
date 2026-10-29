FROM python:3.12-slim-bookworm 
WORKDIR /app 
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt 
COPY . . 
EXPOSE 5000 
ENV APP_VERSION="0.2.0" 
CMD ["python", "app.py"]
