import os
import json
import aiofiles
import shutil
import asyncio
from rq import Connection, Queue, Worker
from database.database import database
from fastapi.responses import JSONResponse

async def run_subprocess(command):
    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    if process.returncode != 0:
        raise Exception(f"Ошибка выполнения команды {' '.join(command)}: {stderr.decode()}")
    return stdout.decode()

async def parse_and_generate(url):
    profile_path = f"/tmp/chrome_profile_{os.getpid()}"
    os.makedirs(profile_path, exist_ok=True)
    try:
        await run_subprocess(["python3", "parser.py", url])
        await run_subprocess(["python3", "gpt_answer.py"])

        async with aiofiles.open("gpt_output.json", "r", encoding="utf-8") as f:
            gpt_output = await f.read()
            gpt_output = json.loads(gpt_output)
        return gpt_output
    finally:
        shutil.rmtree(profile_path, ignore_errors=True)

if __name__ == "__main__":
    with Connection():
        worker = Worker(Queue('default'))
        worker.work()
