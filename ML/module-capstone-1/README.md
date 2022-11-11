
### UV Radiation classification: Mars Rover Environmental Monitoring Station Data 
### ML Zoomcamp 2022 - Mid Term Project by Luke

#### 0. Brief

Rover Environmental Monitoring Station (REMS) is a weather station on Mars.

REMS measures humidity, pressure, temperature, wind speeds, and ultraviolet radiation on Mars. 

One of the objectives of this mission was to learn more about the planet's climate and for this purpose, the rover is equipped with a series of instruments named Rover Environmental Monitoring Station(REMS), it contains all the weather instruments needed to provide daily and seasonal reports on meteorological conditions around the rover. https://mars.nasa.gov/msl/spacecraft/instruments/rems/for-scientists/

* Objective - UV Radiation classification *



#### Run the service in docker using the following 


docker run -it --rm -p 3000:3000 uvradiation:abhkdftbysyo3def serve --production

sample payload 
`
{
  "max_ground_temp": -9.0,
  "min_ground_temp": -77.0,
  "max_air_temp": -3.0,
  "min_air_temp": -81.0,
  "mean_pressure": 863.0,
  "weather": "Sunny"
}
`