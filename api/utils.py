from datetime import datetime

def log_msg(log_level, stage, msg):
    vdate = datetime.now()
    print("[{}][{}][{}] {}".format(log_level.upper(), vdate.isoformat(), stage, msg))
