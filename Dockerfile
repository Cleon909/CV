FROM python
copy . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]