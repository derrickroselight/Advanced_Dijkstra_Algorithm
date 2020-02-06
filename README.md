# Advanced_Dijkstra_Algorithm
Dijkstra Algorithm --- Finding the most optimal road on the map.  
I'd like to call it "advanced" because I also added transportation and width limits, which made it more vivid.
Moreover, I even set up a array to record those roads that optimal method passed by. 

To begin with, we have to covert the .txt into Numpy matrix, so the map will look like that.  
Gold numbers : # of the road.  
Blue numbers : Width of the road.  
Black numbers : Distance of the road.   
Arrows : All of those roads are one-way.  

![image](https://github.com/derrickroselight/Advanced_Dijkstra_Algorithm/blob/master/Dijkstra_map.jpg)

Then choose start point, end point, and your transportations.  
1 Walk (Width requirement : 0.5)   
2 Bike (Width requirement : 1.5)      
3 Scooter (Width requirement : 2)      
4 Car (Width requirement : 4)     
5 Bus (Width requirement : 6)  
Ex. Car cannot take Road #3(0 -> 3), because the width of Road #3 is only 3, but car needs 4.
  
Then The follow is how this algorithm works(pseudo code) :
Take 








***Postscript***   
When I was young, I was fascinated with Google Map thought it was a black magic..  
I still remembered that I gained a plenty of accomplishment from it.  
I feel like i'm a senior software engineer in google map team.
