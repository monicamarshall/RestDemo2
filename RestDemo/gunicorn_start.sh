#!/bin/bash

NAME="RestDemo"                              #Name of the application (*)
DJANGODIR=/home/monica/pythonworkspace/RestDemo2/RestDemo             # Django project directory (*)
SOCKFILE=/home/monica/envs/restdemo/bin/gunicorn.sock        # we will communicate using this unix socket (*)
USER=monica                                        # the user to run as (*)
GROUP=monica                                    # the group to run as (*)
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=RestDemo.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=RestDemo.wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/monica/envs/restdemo/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/monica/envs/restdemo/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE
