FROM python:3.11-slim
ENV TZ=Asia/Ho_Chi_Minh
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY install.sh /install.sh
COPY requirements.txt /requirements.txt
WORKDIR /
RUN bash install.sh

COPY Src /Src

# Start services
WORKDIR /Src
RUN mkdir $(date +%Y-%m-%d-%Hh-%Mm-%Ss)
CMD ["bash", "Run_Production.sh"]