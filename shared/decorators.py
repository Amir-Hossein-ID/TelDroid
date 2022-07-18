import re

from telethon import events

import shared

def command(name, takes_args = True, **kwargs):
    if takes_args and "pattern" not in kwargs:
        kwargs["pattern"] = re.compile("(?i)^\\." + name + "( (.*))?$")
    elif "pattern" not in kwargs:
        kwargs["pattern"] = re.compile("(?i)^\\." + name + "$")
    
    if "outgoing" not in kwargs:
        kwargs["outgoing"] = True

    def decorator(func):
        shared.plugin_manager.add_event_handler(func, events.NewMessage(**kwargs))
        return func
    
    return decorator