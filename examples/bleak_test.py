# import asyncio
# from bleak import discover
# from bleak import BleakScanner

# dev = 0
# async def run():
#     global dev
#     tap_service = "C3FF0001-1D8B-40FD-A56F-C7BD5D0F3370".lower()
#     devices = await discover()
#     # devices = await discover(filters={"UUIDs":[tap_service]})
#     dev = devices
#     list(map(lambda x: print(x.details["props"]["UUIDs"]), dev))
#     # devices = await BleakScanner.discover()
#     # devices.
#     for d in devices:
#         print(d)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(run())

# # import asyncio
# import platform

# from bleak import BleakClient

# async def print_services(mac_addr: str, loop: asyncio.AbstractEventLoop):
#     async with BleakClient(mac_addr, loop=loop) as client:
#         svcs = await client.get_services()
#         print("Services:", svcs)
#         for svc in svcs:
#             chars = svc.characteristics
#             for ch in chars:
#                 print("CHAR UUID: ",ch.uuid)

#     # try:
#         # value = bytes(await client.read_gatt_char(char.uuid))
#     sequence = [500,500]
#     if len(sequence) > 18:
#             sequence = sequence[:18]
#     for i, d in enumerate(sequence):
#         sequence[i] = max(0,min(255,d//10))
#     write_value = bytearray([0x0,0x2] + sequence)
#     await client.write_gatt_char("6e400002-b5a3-f393-e0a9-e50e24dcca9e", write_value)
#     #     #aa = value.hex();
#     #     #bb = " ";
#     #     aa  = " ";
#     #     bb = value.decode('utf-8')
#     #     print("\n------------------------------------------------VALUE: ",bb, "     ",aa)
#     # except:
#     #     print("DECODING ERROR")



# mac_addr = (
#     "D7:6D:0F:56:6A:F0"
#     if platform.system() != "Darwin"
#     else "243E23AE-4A99-406C-B317-18F1BD7B4CBE"
# )
# loop = asyncio.get_event_loop()
# loop.run_until_complete(print_services(mac_addr, loop))


from bluetool import Bluetooth


bluetooth = Bluetooth()
bluetooth.scan()
devices = bluetooth.get_available_devices()
print(devices)


