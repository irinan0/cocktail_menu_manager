
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3 python3-pip git curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN git clone https://github.com/irinan0/cocktail_menu_manager.git .

RUN pip3 install --no-cache-dir -r requirements.txt

RUN curl -o /tmp/dummy_data.json "https://raw.githubusercontent.com/irinan0/cocktail_menu_manager/refs/heads/main/main/bar_data.json"

RUN mkdir /data
VOLUME /data

EXPOSE 80

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]