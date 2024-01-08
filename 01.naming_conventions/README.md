# Python Naming Conventions Guide

![Total Views](https://views.whatilearened.today/views/github/pmoschos/pmoschos.svg)

This guide outlines best practices for naming conventions in Python, aimed at ensuring code clarity and maintainability.

## 1. General Naming Guidelines
- **Balance**: Choose names that provide enough information without being overly verbose.
  - **Bad Examples**: `data_structure`, `my_list`, `info_map`
  - **Good Examples**: `user_profile`, `menu_options`, `word_definitions`
- **Clarity**: Avoid ambiguous names like `O`, `l`, or `I`, which can be confused with numerals.
- **Abbreviations**: For CamelCase, capitalize all letters of an abbreviation. 
  - **Example**: Use `HTTPServer` instead of `HttpServer`.

## 2. Packages
- **Lowercase**: All letters should be lowercase.
- **Word Separation**: Use underscores to separate multiple words.
- **Simplicity**: Prefer single-word names when possible.

## 3. Modules
- Follow the same conventions as packages: lowercase with underscores separating words.

## 4. Classes
- **UpperCaseCamelCase**: Use this convention for class names.
- **Exceptions**: Suffix exception classes with `Error` to distinguish them.
- **Built-in Classes**: Python's built-in classes are typically lowercase.

## 5. Global Variables
- **Lowercase**: Use all lowercase letters.
- **Underscores**: Separate words with underscores for readability.

## 6. Instance Variables
- **Lowercase and Underscores**: Similar to global variables.
- **Privacy**: Start with a single underscore for non-public variables. Use double underscores for name mangling.

## 7. Methods
- **Lowercase**: All method names should be lowercase.
- **Underscores**: Use underscores to separate words in the method name.
- **Privacy**: Prefix non-public methods with a single underscore.

## 8. Method Arguments
- **Self**: The first argument of an instance method should always be `self`.
- **Cls**: For class methods, use `cls` as the first argument.

## 9. Functions
- Follow the same naming conventions as methods: lowercase with underscores.

## 10. Constants
- **Uppercase**: Use all capital letters.
- **Underscores**: Separate words with underscores for clarity.

### Additional Tips:
- **Consistency**: Be consistent with your naming conventions across your project.
- **Descriptive**: Choose names that clearly describe the variable's or function's purpose.
- **Avoid Conflicts**: Avoid names that are already in use by Python's built-in functions or libraries.

By adhering to these conventions, your code will be more readable, maintainable, and less prone to errors.

---

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