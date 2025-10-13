# official Python image
FROM python:3.10

# working directory
WORKDIR /app

# copy everything into the container
COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# expose Streamlit port
EXPOSE 8501

# run Chatterly
CMD ["streamlit", "run", "src/chatterly/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
