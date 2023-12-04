import urllib.request as request

def check_site_connectivity(url):
    """
    Checks the connectivity to a specified URL.

    Args:
    url (str): The URL to check connectivity for.

    Prints the status of the connection attempt, including a successful connection or any errors encountered.
    """
    try:
        print("Initiating connection to:", url)
        
        # Attempt to open the URL
        response = request.urlopen(url)
        
        # Print the successful connection status
        print(f"Successfully connected to {url}")
        print("Response code:", response.getcode())
    
    except Exception as e:
        # Handle and print any errors encountered during connection
        print(f"Failed to connect to {url}. Error: {e}")

# Main execution block
if __name__ == "__main__":
    print("Site Connectivity Checker Program")

    # Prompt the user to input the URL
    input_url = input("Enter the URL to check connectivity: ")
    
    # Call the function to check connectivity
    check_site_connectivity(input_url)
