## Deployment

Run 'pip install .' in the root directory to pull all dependencies and create a build of zorak_module. Build is then runnable via a call to  zorak_bot/__main__.py script.

If you're developing on the project you won't want to rebuild the module each time you make a change, so you can do this once to set up your enviroment before running 'pip uninstall zorak_bot' and then continuing to run zorak_bot/__main__.py. Alternitevely if using VSCode install the Jupyter extension and you can add '#%%' at the top of __main__.py (or anywhere for that matter) to run/debug the below code as a Jupyter cell.

Optional arguments: 

| Parameter |   Long Parameter   |                                     Default                                     | Description                                               |
| :-------- | :----------------: | :-----------------------------------------------------------------------------: | :-------------------------------------------------------- |
| -dt       |    --discord_token |                                      None                                       | Token for the connection to discord. If not icluded TOKEN env variable is used. |
| -lf       |    --log_file      |                                      None                                       | .log file to output logs to. No output if left as default |
| -ef       |    --err_file      |                                      None                                       | .log file to output errs to. No output if left as default |
| -ll       |    --log-level     | INFO [(Enum 20)](https://docs.python.org/3/library/logging.html#logging-levels) | Logger level                                              |

Optional flags:

| True Flag     |    False Flag    | Default | Description                 |
| :------------ | :--------------: | :-----: | :-------------------------- |
| --console-log | --no-console-log |  True   | Flag for logging to console |
