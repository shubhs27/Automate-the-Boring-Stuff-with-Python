import bs4, requests

def getWeather(locationUrl):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
    res = requests.get(locationUrl, headers=headers)
    res.raise_for_status()

    soup= bs4.BeautifulSoup(res.text, 'html.parser')
    elems= soup.select('html.accuweather body.current-weather.full-animation.rfphrase-disabled div.template-root div.two-column-page-content div.page-column-1 div.page-content.content-module div.current-weather-card.card-module.content-module div.card-content div.current-weather div.current-weather-info div.temp div.display-temp')
    current= elems[0].text
    return current

temp= getWeather('https://www.accuweather.com/en/in/new-delhi/187745/current-weather/187745')
print('The current weather in New Delhi is: '+ temp)