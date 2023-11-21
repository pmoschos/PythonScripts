import requests
import webbrowser

def search_stackoverflow(error_type, error_message):
    """
    Search Stack Overflow for questions tagged with the error.

    :param error_type: Type of the error encountered.
    :param error_message: Message of the error encountered.
    :return: List of links to the top answered questions.
    """
    params = {
        'intitle': error_type,
        'tagged': 'python',
        'nottagged': error_message,
        'sort': 'votes',
        'site': 'stackoverflow'
    }
    response = requests.get('https://api.stackexchange.com/2.2/search', params=params)
    data = response.json()
    return [item["link"] for item in data['items'] if item["is_answered"]]

def open_links_in_browser(links, max_links=7):
    """
    Open the provided links in a web browser.

    :param links: List of URLs to open.
    :param max_links: Maximum number of links to open.
    """
    for link in links[:max_links]:
        webbrowser.open_new_tab(link)

if __name__ == "__main__":
    error_type = input("Enter the type of error (e.g., SyntaxError, ValueError):\n")
    error_message = input("Enter the specific error message or leave blank if unknown:\n")
    links = search_stackoverflow(error_type, error_message)
    open_links_in_browser(links)
