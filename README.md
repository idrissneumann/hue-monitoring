# Hue monitoring

Monitoring of an [appstatus based webapp](https://github.com/appstatus/appstatus) and some other apps based on PhilipsHue light and hosted on raspberrypi.

![hue-monitoring](./img/hue-monitoring.jpeg)

Also a funny party and on/off api are provided!

## Table of content

[[_TOC_]]

## Git repositories

* Main repo: https://gitlab.comwork.io/oss/hue-monitoring
* Github mirror: https://github.com/idrissneumann/hue-monitoring.git
* Gitlab mirror: https://gitlab.com/ineumann/hue-monitoring.git
* Bitbucket mirror: https://bitbucket.org/idrissneumann/hue-monitoring.git

## Image on the dockerhub

The image is available and versioned here: https://hub.docker.com/r/comworkio/hue-monitoring

## Running with docker-compose

First create your `.env` file from the `.env.example`:

```shell
cp .env.example .env
```

Then replace the values that needs to be replaced (go check the "Environment variables" section below).

If you want to test on a raspberrypi or any other ARM device, use this command instead:

```shell
$ docker-compose -f docker-compose-arm.yml up
```

## Environment variables

* `APP_NAME`: your application name that will appear in the logs
* `APP_USERNAME`: basic auth username for appstatus access
* `APP_PASSWORD`: basic auth password for appstatus access
* `HUE_USERNAME`: local philipshue username on your bridge
* `SLACK_TOKEN`: slack token
* `SLACK_USERNAME`: slack username that will appear in the logs
* `SLACK_CHANNEL`: slack channel
* `HUE_LIGHTS_COUNT`: number of philipshue lights you've got
* `HUE_MONITOR_LIGHTS_IDS`: list of philipshue lights ids you want to use to show your application status
* `APPS_URL`: list of apps that exposes appstatus on `/status` endpoint
* `ENABLE_MONITORING`: enable monitoring (`true` or `false`)

## AppStatus compliance

In order to comply with appstatus, your application needs to expose a `/status?p=radiator` endpoint with the following body response when everything is okay:

```html
<html>
<body><p><a href="?p=status" class="btn btn-large btn-success">Status</a></p></body>
</html>
```

Or the following body response when something is ko:

```html
<html>
<body><p><a href="?p=status" class="btn btn-large btn-failure">Status</a></p></body>
</html>
```

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
```

### Turn on the lights

```shell
$ curl localhost:8080/v1/lights/off
{"status": "ok"}
```

### Turn off the lights

```shell
$ curl localhost:8080/v1/lights/off
{"status": "ok"}
```
