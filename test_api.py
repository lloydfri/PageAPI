import requests
import json

def test_page_content():
    """Test the page_content endpoint with various inputs"""
    base_url = "http://localhost:8080"
    
    # Test with valid page number
    response = requests.post(
        f"{base_url}/page_content",
        json={"page_number": 42}
    )
    print("\n=== Test with valid page number ===")
    print(f"Status code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    
    # Test with missing page number
    response = requests.post(
        f"{base_url}/page_content",
        json={}
    )
    print("\n=== Test with missing page number ===")
    print(f"Status code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    
    # Test with non-integer page number
    response = requests.post(
        f"{base_url}/page_content",
        json={"page_number": "abc"}
    )
    print("\n=== Test with non-integer page number ===")
    print(f"Status code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    test_page_content() 