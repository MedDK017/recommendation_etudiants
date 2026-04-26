FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install "numpy==1.26.4"

RUN pip install fastapi uvicorn pandas scikit-learn
RUN pip install scikit-surprise

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]