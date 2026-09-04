import ollama
import json

# Your structured system configuration
structured_system = {
    "system": {
        "role": "you are a professional customer support assistant",
        "content": "you are going to answer the customers more politely, understand their grievances and act accordingly"
    },
    "task": {
        "description": "solve the problem within 4 to 5 shots"
    },
    "constraints": {
        "rules": ["don't give facts", "solve the actual problem", "don't go beyond what the customer asks"],
        "category": {"type": "string", "allowed": ["billing", "technical", "account", "other"]},
        "priority": {"type": "string", "allowed": ["low", "medium", "high"]},
        "short_message": {"type": "string", "description": "1 to 2 sentence summary"}
    },
    "output": {
        "type": "object",
        "properties": {
            "category": {"type": "string"},
            "priority": {"type": "string"},
            "short_message": {"type": "string"}
        },
        "required": ["category", "priority", "short_message"]
    }
}

# Build messages in Ollama format
messages = []

# Add system message (converted from structured_system)
messages.append({
    "role": "system",
    "content": f"""
    You are a professional java TEacher. 
    You are going to answer student more politely, understand their grievances and act accordingly.
    
    TASK: Solve the problem within 1 to 3 shots.
    
    CONSTRAINTS:
    - Don't make up facts
    - Solve the actual problem
    - Don't go beyond what the customer asks

    
    OUTPUT FORMAT: You must respond with a valid JSON object containing:
    - "category": one of ["sports", "technical", "studies", "other"]
    - "priority": one of ["low", "medium", "high"]
    - "short_message": a 1-2 sentence summary of your response
    """
})

# Add customer question
messages.append({
    "role": "user",
    "content": "what is list in python?"
})

# Get response from Ollama
response1 = ollama.chat(
    model="phi",
    messages=messages,
    format="json"

)

print("Response: for Q1")
# print(response1["message"]["content"])


# Try to parse as JSON if the model returns valid JSON
try:
    parsed_response = json.loads(response1["message"]["content"])
    print("\nParsed JSON response for question 1:")
    print(json.dumps(parsed_response, indent=2))
except json.JSONDecodeError:
    print("\nNote: Response was not in valid JSON format")


# history is add to the queue
messages.append({
    "role": "assistant",
    "content": response1["message"]["content"]
})

print( "*" * 70)
print("Question 2")

# question 2
messages.append({
    "role": "user",
    "content": "can you give example?"
})

newResponce = ollama.chat(
    model="phi",
    messages=messages,
     format="json"
)

# print(newResponce["message"]["content"])

# Try to parse as JSON if the model returns valid JSON
try:
    parsed_response2 = json.loads(newResponce["message"]["content"])
    print("\nParsed JSON response for question 2:")
    print(json.dumps(parsed_response2, indent=1))
except json.JSONDecodeError:
    print("\nNote: Response was not in valid JSON format")


