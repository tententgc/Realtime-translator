# Translating My Own Voice into a Different Language, as I Speak!

This project aims to develop a real-time voice translation tool that captures your voice, processes it, and instantly translates it into another language while maintaining the speaker's unique vocal tone and cadence. The tool leverages speech recognition, natural language processing, and voice synthesis to provide seamless, live language translation. Whether for cross-cultural conversations, international meetings, or personal language practice, this project pushes the boundaries of voice and language technology!

## Key Features

- **Real-time voice capture and translation:** Instantly translates spoken words into another language while preserving the speaker's voice and intonation.
- **Multi-language support:** Supports various languages and can dynamically adjust input language during translation.
- **Customizable voice synthesis:** Reproduces the speaker's voice in the translated language.
- **Powered by GPT-4-Turbo:** Leverages advanced translation capabilities for natural, nuanced translations.

Here is the updated guide with the new Step 4 included:


## How to Use

1. **Create a virtual environment:**
    - For macOS/Linux:
      ```bash
      virtualenv translator
      ```
    - For Windows:
      ```bash
      python -m venv translator
      ```

2. **Activate the environment:**
    - For macOS/Linux:
      ```bash
      source translator/bin/activate
      ```
    - For Windows:
      ```bash
      .\translator\Scripts\activate
      ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file:**
   - Add the following keys in the `.env` file:
     ```bash
     OPENAI_API_KEY=
     ASSEMBLYAI_API_KEY=
     ```

5. **Run the program:**
   ```bash
   python main.py
   ```


## Technologies Used

- **OpenAI API:** Using GPT-4-Turbo for real-time translation.
- **Speech Recognition:** Captures the user's voice in real-time.
- **Natural Language Processing:** Processes and translates spoken sentences.
- **Voice Synthesis:** Reproduces the translated sentences in the speaker’s voice.

## Potential Use Cases

- **Cross-cultural communication:** Easily communicate in different languages without losing personal style.
- **International meetings:** Facilitate seamless conversations with global colleagues.
- **Language learning and practice:** Speak and receive instant feedback in a new language.

## Contributing

- tententgc thanyapisit.bua@gmail.com