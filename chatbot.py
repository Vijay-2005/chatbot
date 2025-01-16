import google.generativeai as genai

genai.configure(api_key="AIzaSyCtw1QRk32_xwVJTuCD8onW4-mn2anxBX4")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("can you teach me algebra")
print(response.text)