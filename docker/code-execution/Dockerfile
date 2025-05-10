FROM ubuntu:22.04

# Set noninteractive installation
ENV DEBIAN_FRONTEND=noninteractive

# Install common dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    wget \
    git \
    build-essential \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && pip3 install --no-cache-dir memory-profiler psutil

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Java
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Go
RUN wget https://go.dev/dl/go1.18.linux-amd64.tar.gz \
    && tar -C /usr/local -xzf go1.18.linux-amd64.tar.gz \
    && rm go1.18.linux-amd64.tar.gz
ENV PATH=$PATH:/usr/local/go/bin

# Install Ruby
RUN apt-get update && apt-get install -y \
    ruby-full \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install C++
RUN apt-get update && apt-get install -y \
    g++ \
    cmake \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user to run code
RUN useradd -m coderunner
USER coderunner
WORKDIR /home/coderunner

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV NODE_ENV=production
ENV GOPATH=/home/coderunner/go
ENV PATH=$PATH:$GOPATH/bin

# Create directories for code and tests
RUN mkdir -p /home/coderunner/code /home/coderunner/tests /home/coderunner/go

# Set the working directory
WORKDIR /home/coderunner/code

# Default command
CMD ["echo", "Code execution container is ready. Use with the code execution service."]
