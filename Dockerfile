# Use the base image
FROM base AS builder

# Set the working directory
WORKDIR /usr/src/app

# Clone the server repository from GitHub
RUN git clone git@github.com:vinyferrero/server.git .

# Install any additional dependencies if needed
RUN pip install -r requirements.txt

# Final stage to create a minimal image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only the necessary artifacts from the builder stage
COPY --from=builder /usr/src/app /usr/src/app

# Command to run the server script
CMD ["python", "server.py"]
