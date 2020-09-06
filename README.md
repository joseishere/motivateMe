# motivateMe
- A recreation of the Chrome extension [Momentum](https://chrome.google.com/webstore/detail/momentum/laookkfknpbbblfpciffpaejjkokdgca?hl=en)
- Displays your name
- A motivational quote that is pulled off the web via beautifulSoup4
- Time and date
- Weather based on your location

## This does NOT function as is
- You will need API keys for the Yahoo Weather API, for weather
- And you will need API keys for the ipstack ip geolocation API, to know where a user is located

## Screenshots
![start page](screenshots/start.png "start")
![example page](screenshots/example.png "example")
![jose page](screenshots/jose.png "jose")


### Issues
- This was made a long time ago, so long ago that I had to redo the weather because the Yahoo API now required authentication
- Time is done wrong, it does not update as time passes. Should not be using Python for this, I am well aware
