FROM ubuntu:22.04
RUN apt-get update && apt-get install -y libc6 libstdc++6 libx11-6 libxext6 libxrandr2 libxrender1 libxi6 libgl1-mesa-glx
COPY game game.pck game.token team.key /app/
WORKDIR /app
RUN chmod +x game
CMD ["./game"]
