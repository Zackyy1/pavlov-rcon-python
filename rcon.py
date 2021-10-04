import asyncio
from asyncio.tasks import sleep
from pavlov import PavlovRCON

SERVER_IP = "127.0.0.1"
PORT = 9898
PASSWORD = "mysecretpassword"
TEST_STEAM_ID = "760400589874"
TEST_GIVE_ITEM = "akshorty" # Check item IDs in BalancingTable.csv somewhere on the internet

# Here main() is ran once, so expect one output in the console and then an error which indicates the script has finished executing
async def main():
    pavlov = PavlovRCON(SERVER_IP, PORT, PASSWORD)
    serverInfo = await pavlov.send("ServerInfo")
    refreshList = await pavlov.send("RefreshList")
    print(serverInfo)
    print(refreshList)

    # while True: # UNCOMMENT THESE LINES TO TEST ITEM GIVING (RUNS FOREVER)
    #     sleep(3) # Every 3 seconds execute following code
    #     await pavlov.send(f"GiveItem {TEST_STEAM_ID} {TEST_GIVE_ITEM}")

asyncio.run(main())