# Stack Overflow Error Search Script

![Total Views](https://views.whatilearened.today/views/github/pmoschos/pmoschos.svg)

## Overview :mag:
This script assists Python developers in quickly finding solutions to errors by searching Stack Overflow. It queries for questions tagged with the error and opens the top answered questions in a web browser.

## Dependencies :wrench:
- **Requests**: To make HTTP requests to the Stack Overflow API.
- **Webbrowser**: To open links in a web browser.

## Key Functions :function_symbol:

### `search_stackoverflow`
Searches Stack Overflow for questions tagged with a specific error.

- **Parameters**:
  - `error_type` (str): Type of the error encountered (e.g., `SyntaxError`, `ValueError`).
  - `error_message` (str): Message of the error encountered.
- **Returns**:
  - List[str]: Links to the top answered questions on Stack Overflow.

### `open_links_in_browser`
Opens a specified number of links from the search results in a web browser.

- **Parameters**:
  - `links` (List[str]): List of URLs to open.
  - `max_links` (int): Maximum number of links to open (default is 7).

## Usage :computer:
1. Run the script.
2. Enter the type of error when prompted.
3. Optionally, enter a specific error message.
4. The script will search Stack Overflow and open the top answers in your default web browser.

### Example
Enter the type of error (e.g., SyntaxError, ValueError):

IndexError
Enter the specific error message or leave blank if unknown:
list index out of range

The script fetches relevant solutions and opens them in the browser.

## Conclusion :checkered_flag:
This Python script streamlines the process of finding solutions to programming errors, providing a quick and efficient way for developers to access relevant answers from Stack Overflow.

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).


## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>