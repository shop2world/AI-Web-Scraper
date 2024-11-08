from openai import OpenAI
from django.conf import settings
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def parse_with_openai(dom_chunks, parse_description):
    parsed_results = []
    
    system_prompt = """You are tasked with extracting specific information from text content.
    Only extract information that directly matches the provided description.
    Return only the extracted data without any additional text or explanations."""
    
    for chunk in dom_chunks:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Extract the following information: {parse_description}\n\nFrom this content:\n{chunk}"}
            ],
            temperature=0.3
        )
        
        parsed_results.append(response.choices[0].message.content.strip())
    
    return "\n".join(filter(None, parsed_results)) 