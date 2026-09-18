`uvicorn main:app --reload`

This is the config file placed inside /etc/supervisor/conf.d

`
[program:fastapi_app]
command=/home/fastapi_inventory/venv/bin/uvicorn main:app --host 127.0.0.1 --port 8001 --workers 2
directory=/home/fastapi_inventory
autostart=true
autorestart=true
stderr_logfile=/home/fastapi_inventory/logs/fastapi_app.err.log
stdout_logfile=/home/fastapi_inventory/logs/fastapi_app.out.log
environment=PATH="/home/fastapi_inventory/venv/bin"
`

Re-read the configuration for the app running using supervisor

`
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart fastapi_app
`