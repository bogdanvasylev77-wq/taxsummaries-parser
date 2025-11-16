import requests
from bs4 import BeautifulSoup

def parse_webpage(url):
    """
    Fetch and parse a web page, extracting all links and titles.
    """
    info = []

    response = requests.get(url)
    if (response.status_code == 404): # return not fpund for empty pages
        page_title = url.rsplit('/', 1)[-1].capitalize() + ' - Overview'
        info.append({
            "header": 'not found',
            "description": 'not found'
        })

        return page_title, info

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the page title
    page_title = soup.title.string if soup.title else "No title found"

    # Extract all info
    for tbody_tag in soup.find_all('table', class_='table'):
        header = tbody_tag.find('th').get_text(strip=True)
        description = []
        for p_tag in tbody_tag.find_all('p'):
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
