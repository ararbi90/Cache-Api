# Cache-Api

This is Django caching application. This provides users with a temporary caching api. 

Users my post data and cache it based on with the following parameters to <ur>l/cache/add:<br />
user: “user”<br />
key: “key<br />
value: “value”<br />
A response will be received with will indicate {user: “user, key: “key”, value: “value}<br />

Users may get date from the cache with get with the following parameters to <url>/cache/get<br />
user: “user”<br />
key: “key<br />
A response will be received with will indicate {user: “user, key: “key”, value: “value}<br />

This will give them the ability to temporarily store data. Nothing is persisted, and the data is wiped clean two hours after last use. The app is configured to safe get and post requests as they are made.

A live version is available at https://cache-api-portfolio.herokuapp.com/cache/<br />
For add to cache post to https://cache-api-portfolio.herokuapp.com/cache/add<br />
For getting data from cache send a get request to https://cache-api-portfolio.herokuapp.com/cache/get<br />