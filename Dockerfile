FROM registry.twilio.com/library/base-python-36:3.6.8-2
RUN pip install flask -i https://pypi.dev.twilio.com/simple/
COPY endpoints.py /
COPY funfacts/ /funfacts/
ENTRYPOINT ["python"]
CMD ["endpoints.py"]
