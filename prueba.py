#from utils.api_client import GeminiCLient
from utils import GeminiClient, OpenAIClient
from dotenv import load_dotenv

load_dotenv()

try:
    #client = GeminiClient()
    client = OpenAIClient()

    print("Cliente configurado correctamente")
    print(client.api_key)

    response = client.generate_response("Que sabes de Jakarta EE?. Contesta en un párrafo.")
    
    for chunk in response:
        print(chunk, end='')
    
except Exception as e:
        print(f"Error: {e}")