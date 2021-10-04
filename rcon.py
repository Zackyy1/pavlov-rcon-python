import asyncio
from pavlov import PavlovRCON

SERVER_IP = "127.0.0.1"
PORT = 9898
PASSWORD = "mysecretpassword"


# Here main() is ran once, so expect one output in the console and then an error which indicates the script has finished executing
async def main():
    pavlov = PavlovRCON(SERVER_IP, PORT, PASSWORD)
    serverInfo = await pavlov.send("ServerInfo")
    refreshList = await pavlov.send("RefreshList")
    print(serverInfo)
    print(refreshList)

asyncio.run(main())