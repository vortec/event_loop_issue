import asyncio
import logging
import signal
import time

import websockets


log_format = '[%(asctime)s] %(levelname)s [%(name)s]: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
log = logging.getLogger('app')
log.setLevel(logging.DEBUG)

async def client_handler(socket, path):
    await socket.send("I HATE YOU!")
    await socket.close()


def create_server_task(loop, host, port):
    return websockets.serve(client_handler, host, port, loop=loop)


log.info('Starting...')

loop = asyncio.get_event_loop()
server = None
host, port = '0.0.0.0', 8000
server_task = create_server_task(loop, host, port)

async def start_server():
    global server
    server = await server_task

loop.run_until_complete(start_server())


def shutdown():
    log.info('Shutdown requested.')
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.stop()


loop.add_signal_handler(signal.SIGINT, shutdown)
loop.run_forever()
loop.close()
