"""
Extract or compress files.
"""

import os
import shared

@shared.command("extract")
async def extract(event):
    """`{shared.handler}extract` <file> [ | <password>]
    Extract a compressed file."""
    file, password = event.pattern_match.group(2), ""
    if not file:
        await event.edit("Usage: `{}extract <file> [ | <password>]`".format(shared.handler))
        return
    if "|" in file:
        file, password = [i.strip() for i in event.pattern_match.group(2).split("|")]
    if not os.path.isfile(file):
        await event.edit("File `{}` not found.".format(file))
        return
    await event.edit("Extracting...")
    stdout, stderr = await shared.bash("7z t {} -p{}".format(file, password))
    if stderr:
        await event.edit(stderr)
        return
    stdout, stderr = await shared.bash("7z x {} -aoa -ofiles/* -p{}".format(file, password))
    if stderr:
        await event.edit(stderr)
    else:
        await event.edit("Extracted successfully in `files/{}` folder.".format(".".join(os.path.basename(file).split(".")[:-1])))

@shared.command("compress")
async def compress(event):
    """`{shared.handler}compress` <file> [ | <password>]
    Compress a file or folder."""
    file, password = event.pattern_match.group(2), ""
    if not file:
        await event.edit("Usage: `{}compress <file> [ | <password>]`".format(shared.handler))
        return
    if "|" in file:
        file, password = [i.strip() for i in event.pattern_match.group(2).split("|")]
    if not os.path.exists(file):
        await event.edit("File `{}` not found.".format(file))
        return
    await event.edit("Compressing...")
    if password:
        stdout, stderr = await shared.bash("7z a {}.zip {} -p{}".format(file, file, password))
    else:
        stdout, stderr = await shared.bash("7z a {}.zip {}".format(file, file))
    if stderr:
        await event.edit(stderr)
        return
    await event.edit("Compressed successfully Into `{}.zip`".format(file))
