FROM python
ADD rolecrawler.py /
ADD req /
RUN pip install -r req
CMD ["python", "-u", "./rolecrawler.py"]