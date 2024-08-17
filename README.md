# Multilanguage Invoice Extractor

## Overview

The Multilanguage Invoice Extractor is a Streamlit-based web application that utilizes Google's Gemini AI model to extract and analyze information from invoice images in multiple languages. This tool allows users to upload invoice images and ask questions about the invoice content, making it an efficient solution for invoice processing and information retrieval.

## Features

- Upload and display invoice images (JPG, JPEG, PNG formats supported)
- AI-powered analysis of invoice content using Gemini 1.5 Flash model
- Support for multiple languages in invoice processing
- User-friendly interface with clear instructions
- Real-time response generation based on user queries

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- A Google API key for Gemini AI

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/multilanguage-invoice-extractor.git
   cd multilanguage-invoice-extractor
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install streamlit pillow python-dotenv google-generativeai
   ```

4. Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Upload an invoice image using the file uploader.

4. Enter your question about the invoice in the text area.

5. Click the "Analyze Invoice" button to get the AI-generated response.

6. View the analysis result displayed on the screen.

## Customization

You can customize the application by modifying the following:

- Change the model: Update the `model = genai.GenerativeModel("gemini-1.5-flash")` line to use a different Gemini model.
- Adjust the UI: Modify the Streamlit components in the code to change the layout or add new features.
- Enhance prompts: Customize the expert prompt to guide the AI's behavior for specific use cases.

## Contributing

Contributions to the Multilanguage Invoice Extractor are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Create a pull request.

## Acknowledgments

- Google for providing the Gemini AI API
- Streamlit for the excellent web app framework
- The open-source community for various helpful libraries

## Troubleshooting

If you encounter any issues:

1. Ensure your Google API key is correctly set in the `.env` file.
2. Check that you have a stable internet connection for API calls.
3. Verify that the uploaded image is in a supported format (JPG, JPEG, PNG).

For persistent problems, please open an issue on the GitHub repository.

## Contact

If you have any questions or feedback, please open an issue on the GitHub repository.

Happy invoice extracting!
