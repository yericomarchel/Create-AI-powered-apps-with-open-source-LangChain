import os
from langchain_openai import ChatOpenAI
import gradio as gr
# Memasukkan API key
os.environ["OPENAI_API_KEY"] = "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"
gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo" )
def chatbot(prompt):
    return gpt3.invoke(prompt).content
demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)