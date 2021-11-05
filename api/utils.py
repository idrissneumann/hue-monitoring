from datetime import datetime

def log_msg(log_level, stage, msg):
    vdate = datetime.now()
    print("[{}][{}][{}] {}".format(log_level.upper(), vdate.isoformat(), stage, msg))

def is_not_empty (var):
    if (isinstance(var, bool)):
        return var
    elif (isinstance(var, int)):
        return False
    empty_chars = ["", "null", "nil", "false", "none"]
    return var is not None and not any(c == var.lower() for c in empty_chars)

def is_true (var):
    if (isinstance(var, bool)):
        return var
    true_chars = ["true", "enabled", "enable", "ok", "on", "yes"]
    return is_not_empty(var) and any(c == var.lower() for c in true_chars)
