FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

WORKDIR /ansible

# Install Ansible and dependencies
RUN apt-get update && \
    apt-get install -y ansible curl python3-pip tzdata && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy Ansible playbook
COPY playbook.yml .

# Keep container running
CMD ["tail", "-f", "/dev/null"]
