# tvs_backend

tvs client 数据存储服务端

# install

安装 docker

修改国内镜像源 preferences -> Docker Engine，添加

```json
  "registry-mirrors": [
    "https://aa8jax4x.mirror.aliyuncs.com"
  ]
```

```
docker pull xufeisofly/tvs_backend

docker container run --name tvs-server \
    -p $TVS_HOST_IP:$TVS_HOST_PORT:80 \
    --mount type=bind,source=$TVS_DATA_DIR_PATH,target=/data -it xufeisofly/tvs_backend

# example
docker container run --name tvs-server \
    -p 10.11.95.10:3001:80 \
    --mount type=bind,source=/Users/sofly/data,target=/data -it xufeisofly/tvs_backend
```

* TVS_HOST_IP 宿主机访问 ip
* TVS_HOST_PORT 宿主机访问 port
* TVS_DATA_DIR_PATH 宿主机保存数据文件夹路径

# build image

```
docker image build -t xufeisofly/tvs_backend .

docker image tag xufeisofly/tvs_backend xufeisofly/tvs_backend:{tag}

docker push xufeisofly/tvs_backend:{tag}
```

