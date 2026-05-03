import sounddevice as sd
import soundfile as sf
import numpy as np
import time

def test_mic():
    RATE = 44100
    DURATION = 3 # seconds
    FILENAME = "mic_test_output.wav"
    
    print(f"Checking for audio input devices...")
    devices = sd.query_devices()
    print(devices)
    
    default_input = sd.default.device[0]
    if default_input == -1:
        print("Error: No default input device found.")
        return
        
    print(f"\nRecording for {DURATION} seconds from device {default_input}...")
    try:
        recording = sd.rec(int(DURATION * RATE), samplerate=RATE, channels=1, dtype='int16')
        sd.wait() # Wait for recording to finish
        print("Recording finished.")
        
        sf.write(FILENAME, recording, RATE)
        print(f"File saved as {FILENAME}")
        
        # Check if the file is not empty
        if np.any(recording):
            print("Success: Audio data was captured!")
        else:
            print("Warning: Recording is silent. Check your microphone settings.")
            
    except Exception as e:
        print(f"An error occurred during recording: {e}")

if __name__ == "__main__":
    test_mic()
