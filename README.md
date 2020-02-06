# Advanced_Dijkstra_Algorithm
Dijkstra Algorithm --- Finding the most optimal road on the map.  
I'd like to call it "advanced" because I added transportation and width limits, which made it more vivid.  
Moreover, I also set up a array to record which roads the optimal route passed by. 

To begin with, we have to covert the .txt into Numpy matrix, so the map will look like that.  
Gold numbers : # of the road.  
Blue numbers : Width of the road.  
Black numbers : Distance of the road.   
Arrows : All of those roads are one-way.  

![image](https://github.com/derrickroselight/Advanced_Dijkstra_Algorithm/blob/master/Dijkstra_map2.jpg)

Then choose start point, end point, and your transportations.  
1 Walk (Width requirement : 0.5)   
2 Bike (Width requirement : 1.5)      
3 Scooter (Width requirement : 2)      
4 Car (Width requirement : 4)     
5 Bus (Width requirement : 6)  
Ex. Car cannot take Road #3(0 -> 3), because the width of Road #3 is only 3, but car needs 4.
  
Then The follow is how this algorithm works(pseudo code) :  
1. Record & distance arrays record the initial status.  
2. Lock array is used to check whether we find the shortest path between "start point" to "[i] node".  
3. The Dijkstra loop will update the Record & distance arrays accroading to lock array.  
4. In short, if (a -> b) + (b -> c) < (a -> c), the route will be updated as (a -> b) + (b -> c).  
5. Step 4. will be executed n times to guarantee that a -> [i] node goes by shortest route, n is the # of vertice.  
6. Consequently, the average Big-O is inevitable O(n^2).  

Output would be like that:  
Start Point : 2  
Destination : 0  
Transportation : Walk  
Width Needed : 0.5  
Total Distance : 90  
Route & Width:  
2 -> 5 Distance : 20 Width : 4 Limits : 11110  
5 -> 4 Distance : 10 Width : 3 Limits : 11100  
4 -> 3 Distance : 10 Width : 5 Limits : 11110  
3 -> 0 Distance : 50 Width : 4 Limits : 11110  


***Postscript***   
This was one of my algorithm homework when I was in college.  
I still remembered that I gained a plenty of accomplishment from it.  
Because when I was young, I was entirely fascinated with Google Map and thought it was a black magic.  
Hence, After finishing this, I feel like I'm a senior software engineer in Google Map team.  
B-)  
(In fact, They're not using Dijkstra Algorithm, because it isn't fast enough and too simple to work on that scale.)
