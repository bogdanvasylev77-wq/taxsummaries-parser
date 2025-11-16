import requests
from bs4 import BeautifulSoup

def parse_webpage(url):
    """
    Fetch and parse a web page, extracting all links and titles.
    """
    info = []

    response = requests.get(url)
    response.raise_for_status()  # raises error if request fails

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the page title
    page_title = soup.title.string if soup.title else "No title found"

    # Extract all info
    info = []
    for tr_tag in soup.find_all('tbody'):
        header = tr_tag.find('th').get_text(strip=True)
        description = []
        for p_tag in tr_tag.find_all('p'):
            description.append(p_tag.get_text(strip=True))
        
        info.append({
            "header": header,
            "description": description
        })

    return page_title, info


if __name__ == "__main__":
    url =  'https://taxsummaries.pwc.com/ukraine'
    title, info = parse_webpage(url)

    print(f"Page Title: {title}\n")
    print("Links found on the page:")
    for section in info:
        print(f"- {section}")
