import importlib
import os
import sys

import shared

class PluginManager:
    def __init__(self):
        self.all_plugins = {}
        self.loaded_plugins = {}
        self.commands = {}
        self._find_plugins()
    
    def _find_plugins(self):
        for plugin in os.listdir(os.path.dirname(__file__)):
            if not plugin.endswith(".py") or plugin == "__init__.py":
                continue
            plugin = plugin[:-3]
            self.all_plugins[plugin] = None
    
    def load_plugin(self, plugin):
        try:
            self.loaded_plugins[plugin] = set()
            importlib.import_module("plugins." + plugin)
            self.all_plugins[plugin] = sys.modules["plugins." + plugin]
            return True
        except Exception as e:
            shared.logger.error("Error loading plugin `{}`: {}".format(plugin, e))
            del self.loaded_plugins[plugin]
            return False

    def load_plugins(self):
        for plugin in self.all_plugins:
            self.load_plugin(plugin)  

    def unload_plugin(self, plugin):
        for name in list(self.commands):
            func = self.commands[name]
            if func in self.loaded_plugins[plugin]:
                shared.userbot.remove_event_handler(func)
                del self.commands[name]
        del self.loaded_plugins[plugin]
        del sys.modules["plugins." + plugin]
        return True
    
    def add_event_handler(self, name, func, event):
        shared.userbot.add_event_handler(func, event)
        self.loaded_plugins[func.__module__[len("plugins."):]].add(func)
        self.commands[name] = func
