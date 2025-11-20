# 🤖 AI Text Generation Studio

AI-powered web application that generates professional text content using Groq API and Llama 3.1 model.

![img.png](img.png)
![img_1.png](img_1.png)

## 📋 About the Project

AI Text Generation Studio is a content creation tool that helps users generate professional texts in different formats. You can produce text content across a wide range from blog posts to product descriptions, social media content to emails.

## ✨ Features

- **5 Different Content Types**: Blog post, product description, social media, email, creative writing
- **5 Different Tone Options**: Professional, friendly, formal, creative, informative
- **3 Length Options**: Short (100-200 words), Medium (300-500 words), Long (600-1000 words)
- **Multiple Version Generation**: Up to 3 different variations for the same topic
- **Text History**: Store all generated texts within session
- **TXT Download**: Download generated texts directly
- **Word Count Analysis**: Real-time word count display

## 🛠️ Technologies Used

- **Python 3.12.1**: Programming language
- **Streamlit**: Web interface framework
- **Groq API**: Fast LLM inference
- **Llama 3.1 70B**: Meta's open-source AI model
- **python-dotenv**: Environment variables management

## 📦 Installation

To run the project on your local machine:

1. Clone the repository:
```bash
git clone https://github.com/mmehmetisik/ai-text-studio.git
cd ai-text-studio
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create .env file and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

5. Run the application:
```bash
streamlit run app.py
```

## 🚀 Usage

1. Enter your text topic
2. Select content type (Blog, Product Description, etc.)
3. Set tone and length preferences
4. Increase number of versions if desired
5. Click "Generate Text" button
6. Download or copy the generated text

## 📁 Project Structure
```
ai-text-studio/
├── config/
│   └── settings.py          # Configuration settings
├── utils/
│   ├── api_handler.py       # Groq API integration
│   ├── text_processor.py    # Text processing functions
│   └── file_exporter.py     # File saving operations
├── assets/
│   └── style.css            # Custom CSS styles
├── app.py                   # Main Streamlit application
├── requirements.txt         # Python dependencies
└── .env                     # API keys (not added to git)
```

## 🔑 Getting API Key

1. Go to [Groq Console](https://console.groq.com)
2. Create a free account
3. Generate new key from API Keys section
4. Add the key to your `.env` file

## 🎯 Learning Outcomes

Topics learned while developing this project:

- Using Groq API and fast LLM inference
- Developing interactive web applications with Streamlit
- Managing user data with session state
- Prompt engineering and AI model parameters
- Git version control and GitHub integration
- Modular code structure and best practices

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License.

## 👨‍💻 Developer

**Mehmet Işık**
- GitHub: (https://github.com/mmehmetisik)
- LinkedIn: (https://www.linkedin.com/in/mehmetisik4601/)
- Kaggle: (https://www.kaggle.com/mehmetisik)
- Medium: (https://medium.com/@mmehmetisik)

## 🙏 Acknowledgments

- [Groq](https://groq.com) - For fast LLM inference
- [Meta](https://ai.meta.com/llama) - For Llama 3.1 model
- [Streamlit](https://streamlit.io) - For amazing web framework

---

⭐ Don't forget to star the project if you like it!