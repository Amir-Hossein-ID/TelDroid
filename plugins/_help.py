"""
Get plugins and commands help.
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

@shared.command("helpc")
async def helpcommand(event):
    """`{shared.handler}helpc` <command>
    Get help for a command."""
    name = event.pattern_match.group(2)
    if not name:
        await event.edit("Usage: `{}helpc <command>`".format(shared.handler))
        return
    if name in shared.plugin_manager.commands:
        func = shared.plugin_manager.commands[name]
    elif name[0] == shared.handler and name[1:] in shared.plugin_manager.commands:
        name = name[1:]
        func = shared.plugin_manager.commands[name]
    else:
        await event.edit("Command `{}` not found.".format(name))
        return
    
    text = f"Help on Command: `{name}`\n\n"
    text += func.__doc__.format(shared = shared)
    await event.edit(text)
