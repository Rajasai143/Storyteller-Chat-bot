# Storyteller-Chat-bot

A magical AI-powered storytelling application that creates age-appropriate stories on any theme. Built with Streamlit and Google's Gemini Pro AI model.

## ✨ Features
- **Age-Appropriate Content**: Stories tailored for different age groups (3-6, 7-12, 13-16, 17+)
- **Customizable Themes**: Generate stories about any topic you choose
- **Additional Preferences**: Add specific elements like humor, setting, or characters
- **Story History**: Keep track of all generated stories in a beautiful, organized interface
- **Real-time Generation**: Watch as your story unfolds word by word

### Prerequisites

- Python 3.8 or higher
- Google API key for Gemini Pro

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Rajasai143/Storyteller-Chat-bot.git
cd Storyteller-Chat-bot
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 📋 Usage

1. Select an age group from the dropdown menu
2. Enter a theme or topic for your story
3. (Optional) Add any additional preferences
4. Click "Generate Magical Story" and watch as your story comes to life!

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini Pro
- **Styling**: Custom CSS
- **Environment Management**: python-dotenv

## 📁 Project Structure

```
storyteller-ai/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── .env               # Environment variables (create this)


## 📄 Requirements

```
streamlit==1.31.0
python-dotenv==1.0.0
google-generativeai==0.3.1
```

## 🔑 Environment Variables

Create a `.env` file in the root directory with the following:

```env
GOOGLE_API_KEY=your_google_api_key_here
```
## ⚠️ Disclaimer

This application uses AI to generate stories. While we strive to make content age-appropriate, please review generated content before sharing with children.

## 📧 Contact

Raja Sai  - [rajasaidurgam333@gmail.com](mailto:rajasaidurgam333@gmail.com)

Project Link: [https://github.com/Rajasai143/Storyteller-Chat-bot](https://github.com/Rajasai143/Storyteller-Chat-bot)
