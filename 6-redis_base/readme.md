
[https://habr.com/ru/articles/823936/](https://habr.com/ru/articles/823936/)

[redis://username:password@193.3.298.206:6380/0](redis://username:password@193.3.298.206:6380/0)


```bash
poetry add redis --group=extras


docker run -d --name my-redis -p 6379:6379 redis
docker exec -it my-redis redis-cli

docker run -d --name my-redis -p 6379:6379 -p 8001:8001 -e REDIS_ARGS="--requirepass mypassword" redis/redis-stack:latest

```