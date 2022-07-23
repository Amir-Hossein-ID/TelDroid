"""
Do bash commands.
"""

import os
import shared

@shared.command("bash")
async def bash(event):
    """`{shared.handler}bash` <command>
    Execute a bash command."""
    command = event.pattern_match.group(2)
    if not command:
        await event.edit("Usage: `{}bash <command>`".format(shared.handler))
        return
    stdout, stderr = await shared.bash(command)
    if stderr:
        await event.edit(stderr)
    elif stdout:
        await event.edit(stdout)
    else:
        await event.edit("No output.")

@shared.command("ls")
async def ls(event):
    """`{shared.handler}ls` <directory>
    List files in a directory."""
    directory = event.pattern_match.group(2) or "."
    if not os.path.isdir(directory):
        await event.edit("Directory `{}` not found.".format(directory))
        return
    files = sorted(os.listdir(directory))
    if not files:
        await event.edit("Directory `{}` is empty.".format(directory))
        return
    text = "In directory `{}`:\n".format(directory)
    text += "\n".join(["[🗂] `{}`".format(f) for f in files if os.path.isdir(os.path.join(directory, f))]) + "\n"
    text += "\n".join(["[📄] `{}`".format(f) for f in files if not os.path.isdir(os.path.join(directory, f))])
    await event.edit(text)
