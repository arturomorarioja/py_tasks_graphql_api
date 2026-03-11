FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-c", "from app import create_app; app = create_app(); app.run(host='0.0.0.0', port=5000, debug=True)"]