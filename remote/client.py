# import asyncio
import socket
from grpc import aio

import remote.asteroids_pb2 as pb2
import remote.asteroids_pb2_grpc as pb2g


def get_id():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    num = IP.split(".")[3]
    num = int(num) - 128
    return num


async def send(asteroid, target):
    targetIP = "172.16.0." + str(target + 128)
    print(f"Tavoitellaan {targetIP}")
    async with aio.insecure_channel(f'{targetIP}:50505') as channel:
        stub = pb2g.AsteroidsStub(channel)
        try:
            response = await stub.Xfer(pb2.Outbound(X=100, Y=100), timeout=10)
            print("Xfer client received: " + str(response.result))
        except Exception as e:
            print("######## POIKKEUS: " + str(e))
