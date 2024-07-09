FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11 
# Base image

WORKDIR /app  
#Create a working directiory called /app

# within the container
#You will copy the requirements in /app/text file
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#Then it will be cached!

#Then we copy the rest!
COPY ./app /app

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]