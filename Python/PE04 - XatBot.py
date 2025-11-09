from openai import OpenAI

# Inicializar cliente
client = OpenAI(api_key="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")

# Mensaje del usuario
def chatgpt(mensaje):
    # Petición básica
    respuesta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente útil y conciso."},
            {"role": "user", "content": mensaje}
        ]
    )
# Imprimir resultado
user_input = input("Escribe tu mensaje: ")
print(chatgpt(user_input))
