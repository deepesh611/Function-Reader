# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the entire project into the container at /app
COPY . /app

# # If your setup script does more than that, you might want to run it only once during build.
# RUN ["chmod", "+x", "setup.sh"]
# RUN ["tr", "-d", "'\r'", "<", "setup.sh", ">", "setup.sh"]
# RUN ["bash", "./setup.sh"]

# # Alternatively, if you want to run the shell script version:
# RUN ["chmod", "+x", "Function-Reader.sh"]
# RUN ["tr", "-d", "'\r'", "<", "Function-Reader.sh", ">", "Function-Reader.sh"]
# CMD ["./Function-Reader.sh"]


# Use RUN for Python Commands
RUN python -m venv venv
RUN pip install --upgrade pip
RUN pip install -r ./src/requirements.txt

# Run main.py
CMD ["python", "./src/main.py"]


