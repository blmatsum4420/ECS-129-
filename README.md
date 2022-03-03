Readme for protein volume finder project 
Made by: Brandon Matsumoto, Raymond Barsch, Milca Girmai

How to run program:
Please run program using script_runy.  Script run imports from optimized and voronoi_algo.

What this program has: 
This program consists of three different algorithms all based on the brute force montecarlo method.  
The following algorithms exist:
\1. Double-For Loop Algorithm which is unoptimized.  Should not be run unless one is curious to see how much
we later improved on the program.  Is truly a brute force program
\2. Brute Force Montecarlo algorithm which uses numpy to bring our program closer to O(N)
\3. Brute Force MOntecarlo + Voronomi algorithm which is the fastest algorithm

How to Navigate said program:
To Navigate this program you will be prompted to
\1. provide an input file (must be direct path and must contain a similar format to one given in project assignment)
\2. provide an output file (must be direct path)\
\3. Chose between 2 algorithms provided, Brute force of Voronomi
\4. Chose between running the algorithm once, will do it once for N random samples.  Do it iteratively, will go from 1-N samples, doing a calculation for each N.  For example, it would run the algorithm for 1 random points, then 2 random points, 3...until N.  Lastly, you can also do a loop which will run your program Z amount of times for the same given N points.
\5. Can chose to repeat or stop program