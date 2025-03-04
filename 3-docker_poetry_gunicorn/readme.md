## Poetry


```bash
poetry add fastapi 'uvicorn[standard]'
poetry add gunicorn
poetry shell
uvicorn main:app --reload
```



## Docker

```bash
sudo docker build -t poetry_app .
sudo docker run -p 8000:80 poetry_app

sudo docker system prune -a
sudo systemctl restart docker

```


[https://habr.com/ru/articles/740376/](https://habr.com/ru/articles/740376/)


## Обратите внимание на следующие вещи:

* жестко фиксируйте версию Poetry в ваших Dockerfile'ах. 
* Разработчики Poetry очень любят что-то ломать от релиза к релизу, или объявлять ставшие привычными вещи deprecated.

* не тащите лишние зависимости в ваши образы. Используйте флаг --without.

