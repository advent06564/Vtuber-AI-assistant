import asyncio
import pyvts
import threading

class VTSLink:
    def __init__(self):
        self.vts = None
        self.connected = False
        self.plugin_info = {
            "plugin_name": "AI Waifu Vtuber",
            "developer": "Ardha",
            "authentication_token_path": "./vts_token.txt"
        }

    async def connect(self):
        try:
            self.vts = pyvts.vts(plugin_info=self.plugin_info)
            await self.vts.connect()
            await self.vts.request_authenticate_token()
            await self.vts.request_authenticate()
            self.connected = True
            print("VTube Studio: Connected and Authenticated!")
        except Exception as e:
            print(f"VTube Studio: Connection failed (is VTS running and API enabled?): {e}")
            self.connected = False

    async def trigger_hotkey(self, hotkey_name):
        if not self.connected:
            return
        
        try:
            # First, get available hotkeys to find the ID
            response = await self.vts.request(self.vts.vts_request.requestHotkeys())
            hotkeys = response['data']['availableHotkeys']
            
            target_id = None
            for hk in hotkeys:
                if hk['name'].lower() == hotkey_name.lower():
                    target_id = hk['hotkeyID']
                    break
            
            if target_id:
                await self.vts.request(self.vts.vts_request.requestTriggerHotkey(target_id))
                # print(f"VTube Studio: Triggered hotkey '{hotkey_name}'")
            else:
                # print(f"VTube Studio: Hotkey '{hotkey_name}' not found.")
                pass
        except Exception as e:
            print(f"VTube Studio: Error triggering hotkey: {e}")

# Global instance
vts_instance = VTSLink()

def start_vts_link():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(vts_instance.connect())
    
    # Keep the loop running in a background thread for future triggers
    thread = threading.Thread(target=loop.run_forever, daemon=True)
    thread.start()
    return loop

def trigger_vts_expression(loop, mood):
    # Map moods to common hotkey names
    # You should set these names in VTube Studio Hotkeys settings
    mood_map = {
        "happy": "Happy",
        "sad": "Sad",
        "angry": "Angry",
        "blush": "Blush",
        "surprised": "Surprised"
    }
    
    hotkey = mood_map.get(mood.lower())
    if hotkey and loop:
        asyncio.run_coroutine_threadsafe(vts_instance.trigger_hotkey(hotkey), loop)
