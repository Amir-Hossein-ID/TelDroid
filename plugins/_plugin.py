"""
Commands to work with plugins.
"""

import shared

@shared.command("load")
async def load(event):
    """`{shared.handler}load` <plugin>
    Load a plugin."""
    name = event.pattern_match.group(2)
    if not name:
        await event.edit("Usage: `{}load <plugin>`".format(shared.handler))
    elif name in shared.plugin_manager.loaded_plugins:
        await event.edit("Plugin `{}` already loaded.".format(name))
    elif name not in shared.plugin_manager.all_plugins:
        await event.edit("Plugin `{}` not found.".format(name))
    elif shared.plugin_manager.load_plugin(name):
        await event.edit("Plugin `{}` loaded.".format(name))
    else:
        await event.edit("Plugin `{}` failed to load.".format(name))

@shared.command("unload")
async def unload(event):
    """`{shared.handler}unload` <plugin>
    Unload a plugin."""
    name = event.pattern_match.group(2)
    if not name:
        await event.edit("Usage: `{}unload <plugin>`".format(shared.handler))
    elif name not in shared.plugin_manager.all_plugins:
        await event.edit("Plugin `{}` not found.".format(name))
    elif name not in shared.plugin_manager.loaded_plugins:
        await event.edit("Plugin `{}` is not loaded.".format(name))
    elif name.startswith("_"):
        await event.edit("Plugin `{}` is a required plugin and cannot be unloaded.".format(name))
    else:
        shared.plugin_manager.unload_plugin(name)
        await event.edit("Plugin `{}` unloaded.".format(name))

@shared.command("plugins")
async def plugins(event):
    """`{shared.handler}plugins`
    List loaded plugins."""
    text = "All plugins:\n\n"
    for plugin in sorted(shared.plugin_manager.loaded_plugins):
        if plugin.startswith("_"):
            continue
        text += "✅ `{}`\n".format(plugin)
    for plugin in sorted(shared.plugin_manager.all_plugins):
        if plugin not in shared.plugin_manager.loaded_plugins:
            text += "❌ `{}`\n".format(plugin)
    await event.edit(text)
