import eel
import pyowm
@eel.expose
def get_weather(place):
    owm = pyowm.OWM('e059443947dca2151be09d4f4d0dee09') #Апи ключ с сайта https://home.openweathermap.org/api_keys
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp=w.temperature('celsius')['temp']
    return 'В городе' + place + 'сейчас' + str(temp) + 'градусов!'
eel.init('web')

eel.start('main.html', size=(700,700))