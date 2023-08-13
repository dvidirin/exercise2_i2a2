import openai
import gradio as gr
from decouple import config

# Definindo a chave da API OpenAI
openai.api_key = config("OPENAI_API_KEY")

messages = [
    {
        "role": "system",
        "content": "Você é a Dra. Elfrida Ravenscroft, uma terapeuta muito famosa e experiente e irá responder as questões dos seus pacientes.",
    }
]


def chatWithBot(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


# Crie a interface Gradio para o chatbot terapêutico
iface = gr.Interface(
    fn=chatWithBot,
    inputs="text",
    outputs="text",
    title="Terapeuta Virtual",
    description="Converse com nosso terapeuta virtual para compartilhar seus pensamentos e sentimentos.",
    examples=[
        ["Olá, estou me sentindo um pouco triste hoje."],
        ["Como lidar com o estresse do dia a dia?"],
    ],
    theme="huggingface",
    layout="vertical",
    font_family="Helvetica, sans-serif",
    font_color="#333333",
    input_component=gr.components.Textbox(lines=5, placeholder="Digite aqui..."),
    output_component=gr.outputs.Textbox(),
)

# Inicie a interface
iface.launch()
