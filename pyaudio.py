import sys

# Mock classes for PyAudio to allow the script to run without the actual library
class PyAudio:
    def __init__(self):
        print("Warning: PyAudio is running in MOCK mode. Microphone input will not work.")
        
    def open(self, *args, **kwargs):
        print("Error: Microphone input (Mode 1) is not supported on Python 3.14 due to missing PyAudio library.")
        return MockStream()
        
    def terminate(self):
        pass
        
    def get_sample_size(self, format):
        return 2

class MockStream:
    def read(self, chunk):
        return b''
    def stop_stream(self):
        pass
    def close(self):
        pass

# Constants used in the code
paInt16 = 8

# Expose classes and constants at the module level
sys.modules['pyaudio'] = sys.modules[__name__]
