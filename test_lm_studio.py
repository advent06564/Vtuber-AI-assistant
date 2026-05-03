import requests
import json

def test_connection():
    url = "http://localhost:1234/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "messages": [
            {"role": "user", "content": "Hello, are you there?"}
        ],
        "max_tokens": 10
    }
    
    try:
        print("Testing connection to LM Studio at http://localhost:1234/v1...")
        
        # Test models endpoint first
        models_resp = requests.get("http://localhost:1234/v1/models")
        if models_resp.status_code == 200:
            print("Successfully reached LM Studio /v1/models!")
            models = models_resp.json()
            print("Available models:")
            for model in models['data']:
                print(f" - {model['id']}")
        else:
            print(f"Failed to reach models endpoint. Status: {models_resp.status_code}")
            return False

        # Test chat completion
        print("\nTesting chat completion...")
        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            result = response.json()
            print("Response received:")
            print(result['choices'][0]['message']['content'])
            return True
        else:
            print(f"Chat completion failed. Status: {response.status_code}")
            print(response.text)
            return False
            
    except Exception as e:
        print(f"Failed to connect to LM Studio: {e}")
        return False

if __name__ == "__main__":
    test_connection()
