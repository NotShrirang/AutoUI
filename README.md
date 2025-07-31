# AutoUI

<div align="center">

[![AutoUI Logo](https://img.shields.io/badge/Auto-UI-blue?style=for-the-badge&logo=streamlit)](https://auto-ui.streamlit.app/)

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit)](https://auto-ui.streamlit.app/)
[![GitHub License](https://img.shields.io/github/license/NotShrirang/AutoUI?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](requirements.txt)
[![Gemini API](https://img.shields.io/badge/Google-Gemini-orange?style=flat-square&logo=google)](https://ai.google.dev/)

Automated UI generator that creates Streamlit interfaces from natural language prompts using Google's Gemini API 🤖

</div>

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)
- [Contributing](#contributing)

## Overview

AutoUI is a powerful Streamlit application that automatically generates user interfaces based on natural language prompts. It uses the Google Gemini API to interpret user queries and dynamically create interactive UI components that respond to user needs.

## Features

- **Dynamic UI Generation**: Convert natural language descriptions into functional Streamlit UI components
- **Web Search Integration**: Access real-time information from the web to enhance responses
- **AI-Powered Responses**: Process and display information using Google's Gemini model
- **Real-time Interaction**: Get immediate feedback and UI updates based on your queries

## Requirements

- Python 3.8+
- Google Gemini API key
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/AutoUI.git
cd AutoUI
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory with your Google Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit application:

```bash
streamlit run main.py
```

2. Access the application through your web browser at `localhost:8501`

3. Enter a natural language query in the input field describing the UI you want to generate

   - Example: "Create a dashboard showing stock prices with a date selector"
   - Example: "Make a form for user registration with validation"

4. The application will generate the appropriate UI components based on your query

## Examples

Here are some example prompts you can try:

```
Create a data visualization for stock prices
```

```
Build a form for capturing user feedback with ratings and comments
```

```
Generate a dashboard showing weather information for different cities
```

```
Create a multi-step wizard for a registration process
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
