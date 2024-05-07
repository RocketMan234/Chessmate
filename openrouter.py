import requests
import json
import dotenv
import logging
import os 

# Setup logging
logger = logging.getLogger(__name__)

# Load environment variables
dotenv.load_dotenv()

class OpenRouter:
  def __init__(self):
    self.api_key = os.environ(['OPENROUTER_API_KEY'])
    self.base_url = "https://openrouter.ai/api/v1"
    self.headers = {
      "Authorization": f"Bearer {self.api_key}"
    }

  def get_chat_completions(self, messages):
    pass

    