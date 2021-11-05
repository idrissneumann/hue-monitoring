# Hue monitoring

Supervision of uprodit.com and some other apps based on PhilipsHue light and hosted on raspberrypi.

Also a funny party api is provided!

## Table of content

[[_TOC_]]

## Git repositories

* Main repo: https://gitlab.comwork.io/oss/hue-monitoring
* Github mirror: https://github.com/idrissneumann/hue-monitoring.git
* Gitlab mirror: https://gitlab.com/ineumann/hue-monitoring.git

## Endpoints

### Healthcheck

```shell
$ curl localhost:8080/
{"status": "ok", "alive": true}
```

### Manifests

```shell
$ curl localhost:8080/v1/manifest 
{"version": "1.0", "sha": "1c7cb1f", "arch": "x86"}
```

### Start the party

```shell
$ curl localhost:8080/v1/party
{"status": "ok"}
```

### Stop the party

```shell
$ curl localhost:8080/party/stop
{"status": "ok"}
```
