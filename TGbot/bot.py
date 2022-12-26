from pyrogram import Client, filters
from weather import Weather

app = Client("weather")

@app.on_message(filters.command(["start"]))
async def start(client, message):
   await app.send_message(message.from_user.id, "Пришли название города. ex: moscow")


@app.on_message()
async def my_handler(client, message):
  city = message.text
  data = Weather(city).get_weather_data()
  temp_value = round((data["main"]["temp"] - 273.15), 1)  
  await app.send_message(message.from_user.id, f'temperature in {message.text} is {temp_value} °C')

app.run()

