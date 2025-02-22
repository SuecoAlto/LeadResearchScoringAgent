import os
import requests
from dotenv import load_dotenv

# Ladda API-nyckel från .env
load_dotenv()
FIRESCRAWL_API_KEY = os.getenv("FIRESCRAWL_API_KEY")

def scrape_to_markdown(url: str):
    """
    Scrapes a webpage using FireCrawl and returns the content in markdown format.
    
    :param url: The webpage URL to scrape.
    :return: Markdown content as a string, or an error message if scraping fails.
    """
    api_endpoint = "https://api.firecrawl.dev/v1/scrape"
    
    # Payload enligt FireCrawl-dokumentationen för markdown
    payload = {
        "url": url,
        "formats": ["markdown"]  # Begär markdown som utdata
    }
    
    headers = {
        "Authorization": f"Bearer {FIRESCRAWL_API_KEY}",
        "Content-Type": "application/json",
    }
    
    try:
        print("\nScraping URL:", url)
        print("\nPayload:", payload)
        response = requests.post(api_endpoint, json=payload, headers=headers)
        response.raise_for_status()  # Kastar exception om status inte är 200
        data = response.json()
        
        # Kontrollera att vi fick ett lyckat svar och markdown-data
        if "success" in data and data["success"] and "data" in data:
            markdown_content = data["data"].get("markdown", "")
            print("\nMarkdown content retrieved successfully.")
            return markdown_content
        else:
            return "Error: No markdown content found in response."
    
    except Exception as e:
        print(f"\nFailed to scrape {url}:", e)
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Running markdown scrape test...\n")
    
    # Test-URL
    test_url = "https://offerta.se/"
    
    # Skrapa och hämta markdown
    markdown_result = scrape_to_markdown(test_url)
    
    # Skriv ut resultatet
    print(f"\nMarkdown content from {test_url}:\n", markdown_result)
    print("\nDone testing scrape function.")