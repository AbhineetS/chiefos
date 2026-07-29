import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()
from google import genai
from dotenv import load_dotenv
load_dotenv()
client = genai.Client()
print(client.models.generate_content(model="gemini-2.5-flash", contents="Hello"))
