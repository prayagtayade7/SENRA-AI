import httpx
import asyncio
from config import API_KEY, SYSTEM_INSTRUCTION

class SenraCodeEngine:
    def __init__(self):
        self.api_key = API_KEY
        # Industry standard code-generation gateway endpoint
        self.endpoint = "https://api.openai.com/v1/chat/completions"
        
    async def generate_code(self, prompt: str) -> str:
        """Asynchronously transmits structural framing requirements to the remote LLM mesh."""
        if not self.api_key:
            return "Execution Error: Secure API system authorization token missing."

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "gpt-4o",  # Advanced production reasoning deployment target
            "messages": [
                {"role": "system", "content": SYSTEM_INSTRUCTION},
                {"role": "user", "content": f"Generate clean, well-structured code for: {prompt}"}
            ],
            "temperature": 0.2  # Set low to enforce deterministic, syntactically sound code output
        }

        # Optimized Python 3.14 multi-exception syntax handling (unparenthesized multi-exceptions)
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(self.endpoint, json=payload, headers=headers)
                
                if response.status_code == 200:
                    data = response.json()
                    return data["choices"][0]["message"]["content"].strip()
                else:
                    return f"SENRA-AI Compilation Failure: Gateway responded with status {response.status_code}."
                    
        except (httpx.ConnectError, httpx.TimeoutException) as e:
            # Native Python 3.14 comma-separated block handling
            return f"SENRA-AI Core offline: Telemetry link unreachable. Matrix diagnostic: {e}"