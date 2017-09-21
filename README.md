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

It may be necessary to add the `-p 5000:5000` option when using docker for mac

### Daemon

```shell
$ docker run -d --env-file ~/sf_docker_rc sf-web
```
