from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import gradio as gr
# initialize the models
openai = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key="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"
)
def chatbot(user_input):
    # defining a template
    template = """Question: {question}
    please provide step by step Answer:
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])
    formated_prompt =prompt.format(question=str(user_input))
    return openai.invoke(formated_prompt).content
demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
demo.launch(share=True)