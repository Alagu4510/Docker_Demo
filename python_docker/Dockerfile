#Deriving the latest base image
FROM python:latest


ADD palindrome-pytest.py .

RUN pip install pytest

CMD [ "python", "./palindrome-pytest.py"]