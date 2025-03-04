
https://github.com/mahenzon/fastapi-users-intro/
https://github.com/artemonsh


```bash
pip install "uvicorn[standard]" gunicorn

```


## Docker

```bash
sudo docker build -t fastapi_app .
sudo docker run -p 8000:80 fastapi_app


sudo docker system prune -a
sudo systemctl restart docker


```