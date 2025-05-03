from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client(api_key="GEMINI_API_KEY")

contents = (
  'Quiero una imagen cuadrada al estilo de los juegos de Dark Souls. '
  'Debe haber un caballero con armadura negra. '
  'Debe haber un dragón volando por el cielo similar a los que pinta Ciruelo Cabral. '
  'Debe haber un castillo al fondo, y el cielo debe estar nublado con tonos de color violeta. '
  'El caballero debe estar de pie, con una espada Claymore en la mano y un escudo con un grabado de sol en la otra. '
  'Al lado del caballero deben haber dos capibaras. '
  'Debe aparecer un texto con letras antiguas y desgastadas, a modo de nombre de la imagen, en la parte superior que diga "Souls of Capybaras". '
)

response = client.models.generate_content(
    model="gemini-2.0-flash-exp-image-generation",
    contents=contents,
    config=types.GenerateContentConfig(
      response_modalities=['TEXT', 'IMAGE']
    )
)

for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO((part.inline_data.data)))
    image.save('gemini-image.png')
    image.show()