# Team tools for improving access to SalesForce



## Using


### Building

```shell
$ docker build -t sf-web .
```


### Interactive

```shell
$ docker run -it --env-file ~/sf_docker_rc sf-web
```

### Daemon

```shell
$ docker run -d --env-file ~/sf_docker_rc sf-web
```