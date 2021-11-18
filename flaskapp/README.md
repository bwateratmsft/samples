# Python Flask App Sample

Steps:

1. `pip install -r requirements.txt` to install the dependencies of the app (if you want to run locally)
2. Open the command palette (Ctrl+Shift+P, F1, or Cmd+Shift+P) and run "Add Docker Compose files to Workspace"; follow the prompts
3. Add the following service and volume to both `docker-compose.yml` and `docker-compose.debug.yml` (you can also copy in `backup/docker-compose.backup` and `backup/docker-compose.debug.backup`):
```
services:
    db:
        image: redis
        volumes:
        - redisvol:/data:rw
volumes:
    redisvol:
```
3. Right click the created `docker-compose.debug.yml` and choose "Compose Up"
3. In the Debug window at the top, switch the active debug configuration to "Python: Remote Attach"
4. F5 and enjoy!