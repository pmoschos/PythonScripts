# :sparkles: Emoji List

![Total Views](https://views.whatilearened.today/views/github/pmoschos/pmoschos.svg)

This section showcases a selection of emojis available in the [emoji](https://pypi.org/project/emoji/) module. For a fun and interactive way to explore and use emojis in your Python projects, refer to the script below.

## 🛠️ Technical Requirements

- **Python**: Version 3.6 or later.
- **Libraries**: emoji library required.

## 📚 Installation and Setup
Ensure Python 3.x is installed on your system. Then, install the required libraries using pip:
```bash
pip install emoji
```

1. **Clone the Repository**:
```bash
git clone https://github.com/pmoschos/PythonScripts
```
2. **Navigate to Folder**:
```bash
cd PythonScripts
```

```bash
cd 09.print_emojis
```

3. **Running the Application**:
Simply execute the Python script:
```bash
python print_emojis.py
```

### :trophy: How to Generate the Emoji List
To retrieve and display the emojis, use the following Python script:

```python
import emoji

# Get all emojis from the emoji module
all_emojis = emoji.EMOJI_DATA

# Print each emoji with its name
for emoji_name, emoji_details in all_emojis.items():
    print(f"{emoji_name}: {emoji_details['en']}")
```

## :heart_eyes: Sample Emojis 
Here's a sneak peek into the emojis you can find:

- 😃: Smiley - Express happiness and positivity.
- 🚀: Rocket - Perfect for launch announcements or speed improvements.
- 🌍: Earth Africa - Ideal for global projects or localization features.
- 📚: Books - Great for educational or documentation related topics.
- 🐍: Snake - A nod to Python, our favorite programming language!

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