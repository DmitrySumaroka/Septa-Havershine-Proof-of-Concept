After pulling down make setup.sh executable.


Pre-reqs: have python3 pip3 installed.

I used flask to handle my requests and serving my template.
I used haversine module (It is just the haversine formula in a module) to compute distances between points.
I used requests_cache to cache the requests that I send out to septa. So the first time you load the app the markers will be slow to get there. However anything but auto-refresh and refresh will be fast since they rely on cached data. Auto refresh works every 10 second and since it gets new data it is on the slow side.

Due to the lack of time I did not write any tests. Also the way I work with data is O(N^2), which is not ideal, but with the time concerns I thought would be ok. There are many improvements I can make and I would be happy to talk about them.
