#!/bin/bash

RUNNER_HOME="/home/pi"
LOG_FILE="${RUNNER_HOME}/gitlab.log"

echo "Executing deploy.sh" > "${LOG_FILE}" 2>&1
cd "${RUNNER_HOME}/supervision-hue" && git pull origin master >> "${LOG_FILE}" 2>&1 || :
echo "End of execution" >> "${LOG_FILE}" 2>&1

cat "${LOG_FILE}"

exit 0

