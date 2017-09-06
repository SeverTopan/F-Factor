# F!Factor Scoring Website & Caching Server

F!Factor is an activity within U of T's Engineering Orientation Week. Engineering First Year's are seperated into groups and compete against one another in several events (the activity was previously called Frosh Olympics).The solution depicted within this repository provides the means for the volunteers running the events to communicate the scores with the students taking part in the event. 

There were 5 events in F!Factor 2017.
* Water Balloon Volleyball (wbv)
* Obstacle Course (oc)
* Bring Me (bm)
* Puzzle Treasure Hunt (thp)
* Design Challenge (dc), which consisted of 4 sub-events:
    * Baja Event (baja)
    * Toike & Cannon Event (tc)
    * WISE Event (wise)
    * Formula SAE Event (hpv)
* Paint Station, which was an unscored event.

## Technical Implementation

The solution consists of a front-end website, f.factor.skule.ca, which serves the static files pertaining to the website, and a back-end which handles the scores themselves. 

The front end can be found in the 'frontend' directory, and in HTML and Javascript.

The back end has two components, the raw values contained in a Master file in Google Sheets, and a Caching Server written in Python using Django.

The workflow is as follows:
* Writes: a write to the back-end may be performed in two ways:
    * The intended use case for the volunteers running the events is to perform writes using the front-end admin interface (see the '-admin' files in the frontend). When a user submits a write request, the google sheets api is used to authorize the given request, and perform the write to the appropriate cell within the Master Google Sheet. A second request is sent to the Caching Server, which updates its internal representation of the data. This is done by sending an HTTP GET request to the /update URI of the Caching Server.
    * Updates can also be made directly within the 
* Reads: reads interface directly with the Caching Server

## Implementation Analysis

Characteristics of this solution implementation:

### Functionality
* The Caching Server is emplaced due to the usage quota that google emplaces, as well as a performance guarantee. By having all reads intercepted by our cache, and by owning the cache, we have the ability to increase the throughput of the solution without having to rely on google for quota restrictions or performancce.

### Faliure
* By using a frontend-backend-cache architecture, we accommodate for website and cache failure. In this case, Google Sheets can be directly used as a user interface.
* Google Sheets is considered a reliable data hosting source, given their high availability.

### Scaling
* The nature of the database transactions are read-intensive, with no new entries written, but with occasional updates to existing entries.
* The Caching Server allows us to scale the solution horizontally. Since the Caching Server is hosted on heroku processing cores can be spooled up as needed. The Front-end is static file cached and supports a steady 120 requests/second under a constant 500 user load. 
* Since Leader selection for the home page is costly (using 1 database read per event), its results are memory cached locally with an eviction after 15 seconds. This caching is largely responsible for the success of the multiple process scaling, otherwise database interactions are observed to be the performance bottleneck.
* The following are the load testing results (requests per second coupled with latency). They are achieved using JMeter with 500 concurrent users repeatedly submitting HTTP GET requests.

| Scale Tested  | Without Caching | With Caching |
| ------------- |---------------| ------|
| Free Dyno: 1     | 16/s,30s latency | 17/s, 20s latency |
| Hobby Dyno: 1      | 17/s, 26s latency |   30/s, 13s latency |
| Proffessional Dyno: 1  | 16/s, 30s latency |    25/s, 18s latency |
| Proffessional Dyno: 2  | 19/s, 19s latency |    36/s, 11s latency |
| Proffessional Dyno: 4  | 40/s, 10s latency |    150/s, 3s latency |
| Proffessional Dyno: 8  | 41/s, 9s latency  |    400/s, 1s latency |

note how the non-cached implementation doesn't scale, indicating the database accesses are the bottleneck. 

### Maintainability
* Maintainability is the main cost of the solution architecture. A change in event number and structure in future years will force an update to the database structure of the Caching server as well as the front-end Javascript and Google Sheets