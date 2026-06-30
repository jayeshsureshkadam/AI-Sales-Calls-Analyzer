# AI-Sales-Calls-Analyzer
Analyze sales call transcripts using Gemini AI

# 📞 AI Sales Call Analyzer

An intelligent tool to analyze sales call transcripts using **Google Gemini AI**. Extract actionable insights, lead scoring, sentiment analysis, and recommended follow-ups automatically.

## ✨ Features

- **Lead Scoring**: Automatically rate leads on a scale of 0-100
- **Sentiment Analysis**: Determine customer sentiment (positive, negative, neutral)
- **Interest Level**: Gauge customer interest from 1-10
- **Buying Intent**: Identify purchase intent signals
- **Customer Objections**: Extract and list all objections raised
- **Conversation Summary**: AI-generated summary of the call
- **Customer Persona**: Identify customer type and profile
- **Urgency Assessment**: Determine action urgency
- **Follow-up Recommendations**: Suggested next steps for sales team
- **Next Best Action**: Strategic recommendations for follow-up

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Google Gemini API key
- pip (Python package manager)

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/jayeshsureshkadam/AI-Sales-Calls-Analyzer.git
cd AI-Sales-Call-Analyzer
```

2. **Create a virtual environment**:
```bash
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory
   - Add your Google Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

### Running the Application

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

## 📁 Project Structure

```
AI-Sales-Call-Analyzer/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not committed)
├── .gitignore               # Git ignore rules
│
├── services/
│   └── gemini_service.py    # Gemini API integration
│
├── prompts/
│   └── sales_prompt.py      # Sales analysis prompt template
│
├── utils/
│   └── parser.py            # JSON parsing utilities
│
├── sample_calls/
│   └── sample_call.txt      # Example transcript
│
└── assets/                  # Images and resources
```

## 🎯 How to Use

1. **Upload a Transcript**: Click "Upload Call Transcript" and select a `.txt` file
2. **View Transcript**: Review the uploaded call transcript
3. **Analyze**: Click "Analyze Call" button
4. **Review Results**: 
   - Key metrics (Lead Score, Interest, Sentiment, Intent)
   - Conversation summary
   - Customer objections
   - Recommended follow-up actions

## 📊 Sample Output

The analyzer provides:
- **Lead Score**: 85/100
- **Interest Level**: 8/10
- **Sentiment**: Positive
- **Buying Intent**: High
- **Customer Objections**: Price concerns, implementation timeline
- **Recommended Follow-up**: Schedule product demo, send pricing details
- **Next Best Action**: Follow up within 24 hours

## 🔧 Technologies Used

- **Streamlit**: Frontend UI framework
- **Google Generative AI (Gemini)**: AI analysis engine
- **Python**: Backend logic
- **python-dotenv**: Environment configuration
- **Pandas**: Data processing (optional, for future enhancements)

## 📋 Requirements

See `requirements.txt`:
```
streamlit
google-generativeai
python-dotenv
pandas
```

## 🔐 Security

- Never commit `.env` file with API keys
- Use environment variables for sensitive data
- Keep `.gitignore` updated

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 🙋 Support

For issues, questions, or suggestions, please open a GitHub issue.

## 📧 Contact

**Author**: Jayesh Suresh Kadam

---

**Made with ❤️ using Streamlit & Google Gemini AI**