import importlib
import os
import sys
import traceback

import shared

class PluginManager:
    def __init__(self):
        self.all_plugins = {}
        self.loaded_plugins = {}
        self._find_plugins()
    
    def _find_plugins(self):
        for plugin in os.listdir(os.path.dirname(__file__)):
            if not plugin.endswith(".py") or plugin == "__init__.py":
                continue
            plugin = plugin[:-3]
            self.all_plugins[plugin] = None
    
    def _load_plugin(self, plugin):
        importlib.import_module("plugins." + plugin)
        self.all_plugins[plugin] = sys.modules["plugins." + plugin]

    def load_plugins(self):
        for plugin in self.all_plugins:
            try:
                self.loaded_plugins[plugin] = set()
                self._load_plugin(plugin)
            except Exception as e:
                traceback.print_exc()
                del self.loaded_plugins[plugin]
    
    def add_event_handler(self, func, event):
        shared.userbot.add_event_handler(func, event)
        self.loaded_plugins[func.__module__[len("plugins."):]].add(func)
