# OpenAI Function Calling Integration Guide

This guide explains how to use the PageContent API with OpenAI's function calling feature for your French tutor application.

## Function Definition

When setting up your OpenAI API call, you'll need to define the PageContent function:

```json
{
  "type": "function",
  "function": {
    "name": "PageContent",
    "description": "Retrieves the content of a specific page from a French textbook",
    "parameters": {
      "type": "object",
      "properties": {
        "page_number": {
          "type": "integer",
          "description": "The page number of the textbook to retrieve"
        }
      },
      "required": ["page_number"]
    }
  }
}
```

## Integration in Real-time API Playground

### Step 1: Set Up Your Function

1. Open the OpenAI API Playground
2. Go to the "Function calling" section
3. Add the function definition above

### Step 2: Define How to Call Your API

When your function is called by OpenAI, you'll need to make a request to your deployed API on Replit:

```python
import requests
import json

def PageContent(page_number):
    """
    Function to get the content of a specific page from the textbook.
    This function will be called by OpenAI when it determines a page reference is needed.
    """
    # Replace with your actual Replit URL
    api_url = "https://your-replit-app-url.replit.app/page_content"
    
    response = requests.post(
        api_url,
        json={"page_number": page_number}
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch page content: {response.status_code}"}
```

### Step 3: Handle Function Calls in Your OpenAI Integration

```python
import openai
import json

# Set your API key
openai.api_key = "your-api-key"

# Initialize conversation
messages = [
    {"role": "system", "content": "You are a helpful French tutor who can discuss the content of a French textbook."}
]

# Define available functions
available_functions = {
    "PageContent": PageContent  # The function you defined in Step 2
}

# Define function definitions for OpenAI
tools = [
    {
        "type": "function",
        "function": {
            "name": "PageContent",
            "description": "Retrieves the content of a specific page from a French textbook",
            "parameters": {
                "type": "object",
                "properties": {
                    "page_number": {
                        "type": "integer",
                        "description": "The page number of the textbook to retrieve"
                    }
                },
                "required": ["page_number"]
            }
        }
    }
]

# Example user message
user_message = "Can you help me understand the content on page 42 of my French textbook?"
messages.append({"role": "user", "content": user_message})

# Call the OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

response_message = response["choices"][0]["message"]
messages.append(response_message)

# Check if the model wants to call a function
if response_message.get("tool_calls"):
    for tool_call in response_message["tool_calls"]:
        function_name = tool_call["function"]["name"]
        function_args = json.loads(tool_call["function"]["arguments"])
        
        if function_name in available_functions:
            function_response = available_functions[function_name](**function_args)
            
            # Append the function response to the messages
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call["id"],
                    "name": function_name,
                    "content": json.dumps(function_response)
                }
            )
    
    # Get a new response from the model
    second_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    
    print(second_response["choices"][0]["message"]["content"])
else:
    print(response_message["content"])
```

With this setup, when a user asks about a specific page, the OpenAI model will:
1. Call the PageContent function
2. Your code will fetch the page content from your API
3. The content will be added to the conversation context
4. The model will then respond to the user about that page's content 