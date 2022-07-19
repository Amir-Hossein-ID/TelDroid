import re

from telethon import events

import shared

def command(name, takes_args = True, **kwargs):
    if takes_args and "pattern" not in kwargs:
        kwargs["pattern"] = re.compile("(?i)^" + handler_pattern(shared.handler) + name + "( (.*))?$")
    elif "pattern" not in kwargs:
        kwargs["pattern"] = re.compile("(?i)^" + handler_pattern(shared.handler) + name + "$")
    
    if "outgoing" not in kwargs:
        kwargs["outgoing"] = True

    def decorator(func):
        shared.plugin_manager.add_event_handler(name, func, events.NewMessage(**kwargs))
        return func
    
    return decorator

def handler_pattern(handler):
    if handler in '.*+?^$[](){}|\\/':
        return '\\' + handler
    return handler