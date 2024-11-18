import requests

api_key = '2a0d650d57931bb2d6cb607d69f9db9e'

user_input = input(" Enter City: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

if weather_data.json()['cod'] =='404':
    print("No such city found. Try again...")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = (weather_data.json()['main']['temp'])

print(f"The weather in {user_input} is: {weather}")
print(f"The Temperature in {user_input} is: {temp}°C")  


