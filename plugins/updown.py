"""
Upload and download files.
"""

import os
import shared

@shared.command("upload")
async def upload(event):
    """`{shared.handler}upload` <file>
    Upload a file."""
    file = event.pattern_match.group(2)
    if not file:
        await event.edit("Usage: `{}upload <file>`".format(shared.handler))
        return
    if not os.path.exists(file):
        await event.edit("File `{}` not found.".format(file))
        return
    async def progress(current, total):
        if current == total:
            await event.edit("Uploaded successfully.")
        else:
            await event.edit("Uploading... {:.2f}mb / {:.2f}mb".format(current / (1024*1024), total / (1024*1024)))
    await event.edit("Uploading...")
    file = await shared.userbot.upload_file(file, progress_callback=progress)
    await event.respond(file=file)

@shared.command("download")
async def download(event):
    """`{shared.handler}download` [Reply to file]
    Download a file."""
    if not event.is_reply:
        await event.edit("Usage: `{}download [Reply to file]`".format(shared.handler))
        return
    reply = await event.get_reply_message()
    if not reply.file:
        await event.edit("Usage: `{}download [Reply to file]`".format(shared.handler))
        return
    async def progress(current, total):
        if current == total:
            await event.edit("Downloaded successfully in `downloads` folder.")
        else:
            await event.edit("Downloading... {:.2f}mb / {:.2f}mb".format(current / (1024*1024), total / (1024*1024)))
    await event.edit("Downloading...")
    name = reply.file.name.translate(str.maketrans("", "", ":/\\?%*|\"<>'\n"))
    await reply.download_media("downloads/"+name, progress_callback=progress)
