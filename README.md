# ELI5 Chatbot using Gemini API

## Overview

ELI5 (Explain Like I'm 5) Chatbot is a simple Python application that uses Google's Gemini API to explain complex topics in easy-to-understand language.

The chatbot accepts a topic from the user, sends it to Gemini with an ELI5 prompt, and displays a simplified explanation in the terminal.

---

## Features

* Explain any topic in simple language
* Uses Google's Gemini API
* Interactive command-line interface
* Supports multiple queries in a single session
* Environment variable support using `.env`

---

## Project Structure

```text
eli5-chatbot/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Google Gemini API
* python-dotenv

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd eli5-chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## API Key Setup

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Generate a Gemini API key from Google AI Studio.

---

## Running the Application

```bash
python app.py
```

---

## Example Usage

```text
Enter a topic: Machine Learning
```

Output:

```text
Imagine teaching a robot by showing it many examples...
```

To exit:

```text
exit
```

---

## How It Works

1. User enters a topic.
2. The application creates an ELI5 prompt.
3. Gemini API receives the prompt.
4. Gemini generates a simplified explanation.
5. The explanation is displayed in the terminal.

---

## Future Improvements

* Streamlit Web Interface
* Difficulty Levels
* Chat History
* PDF Export
* Voice Input and Output

---

## Author

Bhavesh Chindaliya

Computer Engineering Student | AI & Machine Learning Enthusiast
