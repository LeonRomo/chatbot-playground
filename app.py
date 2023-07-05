import openai
import gradio as gr
from gradio_client import Client

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are an AI specialized in student-well being."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Hey, ask me anything :)",
             theme="compact").launch(share=True)

client = Client("http://127.0.0.1:7860/")
result = client.predict(
    "Hello", # str in 'Chat with AI' Textbox component
    api_name="/predict"
)

print(result)
