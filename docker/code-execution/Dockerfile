FROM python:3.9-slim

# Install Node.js
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && curl -sL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Java
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
    memory-profiler \
    psutil

# Create a non-root user to run code
RUN useradd -m coderunner
USER coderunner
WORKDIR /home/coderunner

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV NODE_ENV=production

# Create directories for code and tests
RUN mkdir -p /home/coderunner/code /home/coderunner/tests

# Set the working directory
WORKDIR /home/coderunner/code

# Default command
CMD ["echo", "Code execution container is ready. Use with the code execution service."]
