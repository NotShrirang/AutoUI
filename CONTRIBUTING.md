# Contributing to AutoUI

Thank you for your interest in contributing to AutoUI! This document provides guidelines and instructions for contributing to this project.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Environment](#development-environment)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Community](#community)

## Code of Conduct

We expect all contributors to follow our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and inclusive environment for everyone.

## Getting Started

1. **Fork the repository**:
   - Click the Fork button at the top right of the [repository page](https://github.com/NotShrirang/AutoUI)

2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/AutoUI.git
   cd AutoUI
   ```

3. **Set up your environment**:
   ```bash
   pip install -r requirements.txt
   ```
   
4. **Add the original repository as an upstream remote**:
   ```bash
   git remote add upstream https://github.com/NotShrirang/AutoUI.git
   ```

## Development Environment

1. **Requirements**:
   - Python 3.8 or higher
   - Google Gemini API key (for full functionality)
   - All dependencies listed in requirements.txt

2. **Environment Variables**:
   - Create a `.env` file in the project root with:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

3. **Running the application locally**:
   ```bash
   streamlit run main.py
   ```

## Pull Request Process

1. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Write code that follows the [coding standards](#coding-standards)
   - Add or update tests as needed
   - Update documentation as needed

3. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add feature: brief description of your changes"
   ```

4. **Keep your branch updated**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

5. **Push your changes**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Submit a Pull Request**:
   - Open a pull request from your branch to the main repository
   - Fill out the PR template with details about your changes
   - Link any relevant issues
   - Wait for review and address any feedback

## Coding Standards

1. **Python Style Guide**:
   - Follow [PEP 8](https://peps.python.org/pep-0008/) style guide
   - Use 4 spaces for indentation, not tabs
   - Maximum line length of 88 characters (compatible with Black formatter)

2. **Docstrings**:
   - Use Google style docstrings for all functions and classes
   - Example:
   ```python
   def function_name(arg1, arg2):
       """Short description of function.
       
       Longer description explaining functionality.
       
       Args:
           arg1 (type): Description of arg1.
           arg2 (type): Description of arg2.
           
       Returns:
           type: Description of return value.
           
       Raises:
           ExceptionType: When and why this exception is raised.
       """
       # Function implementation
   ```

3. **Code Quality**:
   - Use meaningful variable and function names
   - Write modular, reusable code
   - Minimize dependencies when possible
   - Document non-obvious code sections with comments

## Testing

1. **Writing Tests**:
   - Write unit tests for new features
   - Use pytest for testing
   - Tests should be placed in the `tests` directory

2. **Running Tests**:
   ```bash
   pytest
   ```

## Documentation

1. **Code Documentation**:
   - Add docstrings to all public functions, classes, and methods
   - Keep docstrings up-to-date when changing functionality

2. **README and Other Documents**:
   - Update the README.md when adding major features
   - Create or update documentation for API changes
   - Document examples and use cases

## Community

- **Reporting Bugs**: Use the GitHub Issues page to report bugs
- **Requesting Features**: Use the GitHub Issues page with the "enhancement" label
- **Questions**: For questions, consider opening a Discussion on GitHub

Thank you for contributing to AutoUI!