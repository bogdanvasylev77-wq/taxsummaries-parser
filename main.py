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
    countries = [
        'afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'antigua and barbuda',
        'argentina', 'armenia', 'australia', 'austria', 'azerbaijan',
        'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize',
        'benin', 'bhutan', 'bolivia', 'bosnia and herzegovina', 'botswana', 'brazil',
        'brunei', 'bulgaria', 'burkina faso', 'burundi',
        'cabo verde', 'cambodia', 'cameroon', 'canada', 'central african republic', 'chad',
        'chile', 'china', 'colombia', 'comoros', 'congo', 'costa rica', "côte d'ivoire",
        'croatia', 'cuba', 'cyprus', 'czechia',
        'democratic republic of the congo', 'denmark', 'djibouti', 'dominica',
        'dominican republic',
        'ecuador', 'egypt', 'el salvador', 'equatorial guinea', 'eritrea', 'estonia',
        'eswatini', 'ethiopia',
        'fiji', 'finland', 'france',
        'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'greece', 'grenada', 'guatemala',
        'guinea', 'guinea-bissau', 'guyana',
        'haiti', 'honduras', 'hungary',
        'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'israel', 'italy',
        'jamaica', 'japan', 'jordan',
        'kazakhstan', 'kenya', 'kiribati', 'kuwait', 'kyrgyzstan',
        'laos', 'latvia', 'lebanon', 'lesotho', 'liberia', 'libya', 'liechtenstein',
        'lithuania', 'luxembourg',
        'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'marshall islands',
        'mauritania', 'mauritius', 'mexico', 'micronesia', 'moldova', 'monaco', 'mongolia',
        'montenegro', 'morocco', 'mozambique', 'myanmar',
        'namibia', 'nauru', 'nepal', 'netherlands', 'new zealand', 'nicaragua', 'niger',
        'nigeria', 'north korea', 'north macedonia', 'norway',
        'oman',
        'pakistan', 'palau', 'panama', 'papua new guinea', 'paraguay', 'peru',
        'philippines', 'poland', 'portugal',
        'qatar',
        'romania', 'russia', 'rwanda',
        'saint kitts and nevis', 'saint lucia', 'saint vincent and the grenadines',
        'samoa', 'san marino', 'sao tome and principe', 'saudi arabia', 'senegal', 'serbia',
        'seychelles', 'sierra leone', 'singapore', 'slovakia', 'slovenia',
        'solomon islands', 'somalia', 'south africa', 'south korea', 'south sudan',
        'spain', 'sri lanka', 'sudan', 'suriname', 'sweden', 'switzerland', 'syria',
        'taiwan',  # not UN member but widely recognized
        'tajikistan', 'tanzania', 'thailand', 'timor-leste', 'togo', 'tonga',
        'trinidad and tobago', 'tunisia', 'turkey', 'turkmenistan', 'tuvalu',
        'uganda', 'ukraine', 'united arab emirates', 'united kingdom', 'united states',
        'uruguay', 'uzbekistan',
        'vanuatu', 'vatican city', 'venezuela', 'vietnam',
        'yemen',
        'zambia', 'zimbabwe'
    ]

    for country in countries:
        url =  'https://taxsummaries.pwc.com/' + country
        print(url)
        title, info = parse_webpage(url)

    print(f"Page Title: {title}\n")
    print("Links found on the page:")
    for section in info:
        print(f"- {section}")
