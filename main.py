from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play, stream
import assemblyai as aai
import os

load_dotenv()

translation_template = """
Translate the following sentence into {language}, return ONLY the translation, nothing else.

Sentence: {sentence}
"""

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

output_parser = StrOutputParser()
llm = ChatOpenAI(temperature=0.0, model="gpt-4-turbo", openai_api_key=OPENAI_API_KEY) 
translation_prompt = ChatPromptTemplate.from_template(translation_template)

translation_chain = (
    {"language": RunnablePassthrough(), "sentence": RunnablePassthrough()} 
    | translation_prompt
    | llm
    | output_parser
)

def translate(sentence, language="French"):
    data_input = {"language": language, "sentence": sentence}
    translation = translation_chain.invoke(data_input)
    return translation

client = ElevenLabs()

def gen_dub(text):
    print("Generating audio...")
    audio = client.generate(
        text=text,
        voice="George", # Insert voice model here!
        model="eleven_multilingual_v2"
    )
    play(audio)
    



def on_open(session_opened: aai.RealtimeSessionOpened):
  "This function is called when the connection has been established."
  print("Session ID:", session_opened.session_id)

def on_data(transcript: aai.RealtimeTranscript):
  "This function is called when a new transcript has been received."
  if not transcript.text:
    return

  if isinstance(transcript, aai.RealtimeFinalTranscript):
    print(transcript.text, end="\r\n")
    print("Translating...")
    translation = translate(str(transcript.text))
    print(f"Translation: {translation}")
    gen_dub(translation)
  else:
    print(transcript.text, end="\r")
      
def on_error(error: aai.RealtimeError):
  "This function is called when the connection has been closed."
  print("An error occured:", error)

def on_close():
  "This function is called when the connection has been closed."
  print("Closing Session")
  
aai.settings.api_key=os.getenv("ASSEMBLYAI_API_KEY")

transcriber = aai.RealtimeTranscriber(
  on_data=on_data,
  on_error=on_error,
  sample_rate=44_100,
  on_open=on_open, # optional
  on_close=on_close, # optional
)

transcriber.connect()
microphone_stream = aai.extras.MicrophoneStream()
transcriber.stream(microphone_stream)

transcriber.close()