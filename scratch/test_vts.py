import asyncio
import pyvts
import os

async def test_vts_connection():
    plugin_info = {
        "plugin_name": "VTS Connection Test",
        "developer": "Antigravity",
        "authentication_token_path": "./vts_token_test.txt"
    }

    vts = pyvts.vts(plugin_info=plugin_info)
    
    print("Connecting to VTube Studio...")
    try:
        await vts.connect()
        print("Connected!")
        
        await vts.request_authenticate_token()
        await vts.request_authenticate()
        print("Authenticated successfully!")

        print("\nFetching available hotkeys...")
        response = await vts.request(vts.vts_request.requestHotKeyList())
        hotkeys = response['data']['availableHotkeys']
        
        if not hotkeys:
            print("No hotkeys found. Please set up some hotkeys in VTube Studio first.")
        else:
            print("Available Hotkeys:")
            for hk in hotkeys:
                print(f"- {hk['name']} (ID: {hk['hotkeyID']})")
            
            # Try to trigger 'Happy' if it exists
            target = next((hk for hk in hotkeys if hk['name'].lower() == "happy"), None)
            if target:
                print(f"\nTriggering 'Happy' hotkey...")
                await vts.request(vts.vts_request.requestTriggerHotKey(target['hotkeyID']))
                print("Triggered!")
            else:
                print("\n'Happy' hotkey not found. You can try triggering one of the hotkeys listed above.")

        await vts.close()
    except Exception as e:
        print(f"\nError: {e}")
        print("Make sure VTube Studio is running and API is enabled in Settings -> Plugins.")

if __name__ == "__main__":
    asyncio.run(test_vts_connection())
