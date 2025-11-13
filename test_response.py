from google import genai
from google.genai import types
import os
import json

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
STORE_ID = "fileSearchStores/zetcwx20oo6y-e6zg8karixpr"

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="試用期間について教えてください",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[STORE_ID]
                )
            )
        ]
    )
)

print("Response text:")
print(response.text)
print("\n" + "="*50)
print("Response object attributes:")
print(dir(response))
print("\n" + "="*50)

if hasattr(response, 'candidates'):
    print("Candidates:")
    for i, candidate in enumerate(response.candidates):
        print(f"\nCandidate {i}:")
        print(f"  Attributes: {dir(candidate)}")
        if hasattr(candidate, 'grounding_metadata'):
            print(f"  Grounding metadata: {candidate.grounding_metadata}")
        if hasattr(candidate, 'content'):
            print(f"  Content parts: {candidate.content.parts if hasattr(candidate.content, 'parts') else 'N/A'}")

