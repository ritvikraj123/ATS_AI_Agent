# Resume Analyzer

This is a **Resume Analyzer** web application built using **Streamlit** and powered by **Google Generative AI**. The application allows users to upload their resumes in **PDF format**, input a **job description**, and receive an AI-generated evaluation, including a **match percentage** and feedback on missing keywords.

## Features

- Upload a **resume (PDF format)** and analyze it against a **job description**.
- Uses **Google Gemini AI (via google-generativeai)** to evaluate resumes.
- Provides **strengths, weaknesses, and missing keywords**.
- Calculates a **percentage match** between the resume and the job description.
- Displays responses in a **chat-like format** within the Streamlit web interface.

## Requirements

To run this project, install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Required Dependencies

- `streamlit`
- `google-generativeai`
- `python-dotenv`
- `pymupdf` (for PDF processing)

## Setup and Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/resume-analyzer.git
   cd resume-analyzer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   - Create a `.env` file in the project root.
   - Add your **Google API Key**:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the **web application** in your browser.
2. Enter the **job description** in the provided text area.
3. Upload a **resume in PDF format**.
4. Click on:
   - **"Tell Me About the Resume"** to receive feedback on strengths and weaknesses.
   - **"Percentage Match"** to calculate the resume's match percentage.
5. View the **AI-generated response** in the chat window.

## Important Note on API Costs

Each request sent to the **Gemini API** requires a valid **Google API Key** and incurs a cost per request. Ensure that you monitor your usage and billing on Google Cloud to avoid unexpected charges.

## Contributing

Feel free to contribute by submitting issues or creating pull requests.

## License

This project is licensed under the **MIT License**.

## Author

Developed by **Ritvik Raj**.

---

### Notes

- Ensure you have a **valid Google API Key** before running the application.
- This app currently supports **only PDF format** for resume uploads.
- The AI-generated feedback may not be perfect—use it as a guideline for resume improvement.

