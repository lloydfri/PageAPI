# PageContent API

A simple API for retrieving textbook page content for use with OpenAI function calling in a French tutor application.

## Description

This API provides a single endpoint that returns page content from a French textbook when given a page number. The content is returned in JSON format and can be integrated with OpenAI's function calling feature to provide context for language learning conversations.

## Local Development

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the app locally:
   ```
   python app.py
   ```

The app will be accessible at http://localhost:8080

## API Usage

### Get Page Content

**Endpoint:** `POST /page_content`

**Request Body:**
```json
{
  "page_number": 42
}
```

**Response:**
```json
{
  "page_number": 42,
  "title": "Sample Page 42",
  "content": "This is sample content from page 42 of the French textbook. This text would normally contain actual French lessons, vocabulary, or exercises.",
  "vocabulary": [
    {"french": "bonjour", "english": "hello"},
    {"french": "merci", "english": "thank you"},
    {"french": "au revoir", "english": "goodbye"}
  ]
}
```

## Deployment

This application is designed to be deployed on Replit to provide a public endpoint for OpenAI function calling. 