## ML-Model-Deployment-Bike-Rental-Count-Prediction
Machine Learning Model is deployed on production using Flask API<br>
<br>
Access the project using-- https://bike-rental-application.herokuapp.com/

## Problem Statement-
A bike rental is a bicycle business that rents bikes for short periods of time. <br>
Most rentals are provided by bike shops as a sideline to their main businesses of sales and
service, but some shops specialize in rentals. <br>
Bike rental shops rent by the day orweek as well as by the hour, and these provide an excellent opportunity for people
who don't have access to a vehicle, typically travelers and particularly tourists.<br>

Specialized bike rental shops thus typically operate at beaches, parks, or other
locations that tourists frequent. In this case, the fees are set to encourage renting the
bikes for a few hours at a time, rarely more than a day. <br>
## Objective- 
##The objective of this Case is to predict the bike rental count based on the environmental and seasonal settings, Sothat required bikes would be arranged and managed by the shops according to environmental and seasonal conditions.<br>


## Data
Our task is to build regression models which will predict the count of bike rented depending on various environmental and seasonal conditions Given below is a
sample of the data set that we are using to predict the count of bike rents:<br>
Variables present in given dataset are instant, dteday, season, yr, mnth, holiday,weekday, workingday, weathersit, temp, atemp, hum, windspeed, casual,registered, cnt
The details of variable present in the dataset are as follows -<br>

instant: Record index

dteday: Date

season: Season (1:springer, 2:summer, 3:fall, 4:winter)

yr: Year (0: 2011, 1:2012)

mnth: Month (1 to 12)

hr: Hour (0 to 23)

holiday: weather day is holiday or not (extracted fromHoliday Schedule)

weekday: Day of the week

workingday: If day is neither weekend nor holiday is 1, otherwise is 0.<br>

weathersit: (extracted fromFreemeteo)

1: Clear, Few clouds, Partly cloudy, Partly cloudy

2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist

3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain +
Scattered clouds<br>

4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
temp:<br>
Normalized temperature in Celsius. The values are derived via
(t-t_min)/(t_max-t_min),
t_min=-8, t_max=+39 (only in hourly scale)
<br>
<br>atemp: Normalized feeling temperature in Celsius. The values are derived via
(t-t_min)/(t_maxt_min),
t_min=-16, t_max=+50 (only in hourly scale)
<br>
<br>
hum: Normalized humidity. The values are divided to 100 (max)

windspeed: Normalized wind speed. The values are divided to 67 (max)

casual: count of casual users

registered: count of registered users

cnt: count of total rental bikes including both casual and registered

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Learning Model) and Flask (for API) installed.

### Project Structure
This project has four major parts :
1. model.py - This contains code fot our Machine Learning model to predict bike rental count absed on trainign data in 'day2.csv' file.
2. app.py - This contains Flask APIs that receives parameters through GUI or API calls, computes the precited value based on our model and returns it.
3. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4. templates - This folder contains the HTML template to allow user to enter parameters and displays the predicted bike rent count.

### Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

You should be able to view the homepage:<br>

Enter valid numerical values in all 10 input boxes and hit Predict.
<br>
If everything goes well, you should  be able to see the predcited bike count value on the HTML page!

4. You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the beow command to send the request with some pre-popuated values -
```
python request.py
```
