## ML-Model-Deployment-Bike-Rental-Count-Prediction
Machine Learning Model is deployed on production using Flask API
## Problem Statement-
A bike rental is a bicycle business that rents bikes for short periods of time. Most
rentals are provided by bike shops as a sideline to their main businesses of sales and
service, but some shops specialize in rentals. Bike rental shops rent by the day or
week as well as by the hour, and these provide an excellent opportunity for people
who don't have access to a vehicle, typically travelers and particularly tourists.
Specialized bike rental shops thus typically operate at beaches, parks, or other
locations that tourists frequent. In this case, the fees are set to encourage renting the
bikes for a few hours at a time, rarely more than a day. The objective of this Case is
to predict the bike rental count based on the environmental and seasonal settings, So
that required bikes would be arranged and managed by the shops according to
environmental and seasonal conditions.
## Data
Our task is to build regression models which will predict the count of bike rented
depending on various environmental and seasonal conditions Given below is a
sample of the data set that we are using to predict the count of bike rents:
Table 1.1: Sample Data (Columns: 1-8)
 instant dteday season yr mnth holiday weekday workingday
 1 1/1/2011 1 0 1 0 6 0
 2 1/2/2011 1 0 1 0 0 0
 3 1/3/2011 1 0 1 0 1 1
 4 1/4/2011 1 0 1 0 2 1
 5 1/5/2011 1 0 1 0 3 1
 6 1/6/2011 1 0 1 0 4 1
 Table 1.2: Sample Data (Columns: 7-16)
 weathersit temp atemp hum windspeed casual registered cnt
 2 0.344167 0.363625 0.805833 0.160446 331 654 985
 2 0.363478 0.353739 0.696087 0.248539 131 670 801
 1 0.196364 0.189405 0.437273 0.248309 120 1229 1349
 1 0.2 0.212122 0.590435 0.160296 108 1454 1562
 1 0.226957 0.22927 0.436957 0.1869 82 1518 1600
 1 0.204348 0.233209 0.518261 0.0895652 88 1518 1606 
Variables present in given dataset are instant, dteday, season, yr, mnth, holiday,
weekday, workingday, weathersit, temp, atemp, hum, windspeed, casual,
registered, cnt
The details of variable present in the dataset are as follows -
instant: Record index
dteday: Date
season: Season (1:springer, 2:summer, 3:fall, 4:winter)
yr: Year (0: 2011, 1:2012)
mnth: Month (1 to 12)
hr: Hour (0 to 23)
holiday: weather day is holiday or not (extracted fromHoliday Schedule)
weekday: Day of the week
workingday: If day is neither weekend nor holiday is 1, otherwise is 0.
weathersit: (extracted fromFreemeteo)
1: Clear, Few clouds, Partly cloudy, Partly cloudy
2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain +
Scattered clouds
4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
temp: Normalized temperature in Celsius. The values are derived via
(t-t_min)/(t_max-t_min),
t_min=-8, t_max=+39 (only in hourly scale)
atemp: Normalized feeling temperature in Celsius. The values are derived via
(t-t_min)/(t_maxt_min),
t_min=-16, t_max=+50 (only in hourly scale)
hum: Normalized humidity. The values are divided to 100 (max)
windspeed: Normalized wind speed. The values are divided to 67 (max)
casual: count of casual users
registered: count of registered users
cnt: count of total rental bikes including both casual and registered
### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has four major parts :
1. model.py - This contains code fot our Machine Learning model to predict employee salaries absed on trainign data in 'hiring.csv' file.
2. app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
3. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4. templates - This folder contains the HTML template to allow user to enter employee detail and displays the predicted employee salary.

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

You should be able to view the homepage as below :
![alt text](http://www.thepythonblog.com/wp-content/uploads/2019/02/Homepage.png)

Enter valid numerical values in all 3 input boxes and hit Predict.

If everything goes well, you should  be able to see the predcited salary vaule on the HTML page!
![alt text](http://www.thepythonblog.com/wp-content/uploads/2019/02/Result.png)

4. You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the beow command to send the request with some pre-popuated values -
```
python request.py
```
