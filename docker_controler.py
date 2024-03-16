import asyncio

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        return f'[stdout]\n{stdout.decode()}'
    if stderr:
        return f'[stderr]\n{stderr.decode()}'



async def start(name):
    o = await run(f'bash start.sh "{name}"')
    return o[-2000:]

async def stop(name):
    o = await run(f'bash stop.sh "{name}"')
    return o[-2000:]

async def restart(name):
    o = await run(f'bash scripts/restart.sh "{name}"')
    return o[-2000:]

async def update(name):
    o = await run(f'bash scripts/update.sh "{name}"')
    return o[-2000:]

async def remove(name):
    o = await run(f'bash scripts/remove.sh "{name}"')
    return o[-2000:]

async def create(git_link, name, env):
    o = await run(f'bash scripts/create.sh "{git_link}" "{name}" "{env}"')
    return o[-2000:]