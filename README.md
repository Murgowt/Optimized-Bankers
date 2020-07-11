# Optimized-Bankers
An optimized approach of Bankers Algorithm to handle Deadlocks in an Operating System

A modified approach to deadlock prevention which is an optimized bankers Algorithm. . This new approach solves cases where Bankers fails to excecute.
Algorithm Used:-
1.	We first apply Bankers algorithm to check whether it is successful in generating a safe sequence or not.
2.	If Bankers algorithm fails in generating a safe sequence, we check which process is causing deadlock.
3.	Then we check which sum of the resources of the process.
4.	Which process have max resource we will abort the process take the allocated resources from that process 
5.	Now we will run the remaining processes till we get the safe sequence
6.	If not repeat step 3 and 4
7.	Thus the deadlock is removed.
8.	The process remains in unsafe state if the resource required by that process exceeds the total number of resources so to execute the remaining process we need to supply additional resources to prevent any further deadlock
