import importlib
import os
import traceback

import shared

class PluginManager:
    def __init__(self):
        self.all_plugins = []
        self.loaded_plugins = {}

    def load_plugins(self):
        for plugin in os.listdir(os.path.dirname(__file__)):
            if not plugin.endswith(".py") or plugin == "__init__.py":
                continue
            plugin = plugin[:-3]
            try:
                self.all_plugins.append(plugin)
                self.loaded_plugins[plugin] = []
                importlib.import_module("plugins." + plugin)
            except Exception as e:
                print(e)
                traceback.print_exc()
                del self.loaded_plugins[plugin]
    
    def add_event_handler(self, func, event):
        shared.userbot.add_event_handler(func, event)
        self.loaded_plugins[func.__module__[len("plugins."):]].append((func))
