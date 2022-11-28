from datetime import datetime
import config as c


def log(msg):
    f"""
    Write an action to a log file.
    :param msg: The action to be write in the log file
    """
    print(msg)
    log_file = c.config_setup["logfile"]
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y/%m/%d %H:%M:%S")
    formatted = f"{timestamp} - {msg}"
    with open(log_file, 'a') as f:
        f.write(formatted + "\n")

def dump_log():
    with open(c.config_setup["logfile"], 'r') as f:
        print(f.read())