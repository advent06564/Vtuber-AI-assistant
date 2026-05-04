import asyncio
import pyvts

async def check_attributes():
    vts = pyvts.vts(plugin_info={
        "plugin_name": "Test",
        "developer": "Test",
        "authentication_token_path": "./test_token.txt"
    })
    print("VTS Request attributes:")
    for attr in dir(vts.vts_request):
        if not attr.startswith("_"):
            print(f"- {attr}")

if __name__ == "__main__":
    asyncio.run(check_attributes())
