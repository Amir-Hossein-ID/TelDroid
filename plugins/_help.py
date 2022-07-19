"""
Get plugins help.
"""

import shared

@shared.command("help")
async def help(event):
    """`{shared.handler}help` <plugin>
    Get help for a plugin."""
    name = event.pattern_match.group(2)
    if not name:
        await event.edit("Usage: `{}help <plugin>`".format(shared.handler))
        return
    if name not in shared.plugin_manager.all_plugins:
        await event.edit("Plugin `{}` not found.".format(name))
        return
    module = shared.plugin_manager.all_plugins[name]
    if not module.__doc__:
        await event.edit("Plugin `{}` does not have help".format(name))
        return
    text = f"Help on Plugin: `{name}`\n" + module.__doc__.format(shared = shared)
    text += "\nCommands:\n"
    for func in shared.plugin_manager.loaded_plugins[name]:
        text += func.__doc__.format(shared = shared) + "\n\n"
    await event.edit(text)