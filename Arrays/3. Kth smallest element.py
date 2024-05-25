'''
K’th Smallest/Largest Element in Unsorted Array | Expected Linear Time
Last Updated : 18 Sep, 2023
Prerequisite: K’th Smallest/Largest Element in Unsorted Array | Set 1

Given an array and a number k where k is smaller than the size of the array, we need to find the k’th smallest element in the given array. It is given that all array elements are distinct.

Examples:

Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 3
Output: 7



Input: arr[] = {7, 10, 4, 3, 20, 15}
      k = 4
Output: 10

We have discussed three different solutions here.

Approach 1:
Select a random element from an array as a pivot.
Then partition to the array around the pivot, its help to all the smaller elements were placed before the pivot and all greater elements are placed after the pivot.
then Check the position of the pivot. If it is the kth element then return it.
If it is less than the kth element then repeat the process of the subarray.
If it is greater than the kth element then repeat the process of the left subarray.
That Algorithm is the QuickSelect and It is similar to the QuickSort.

Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution. 
 
In this post method 5 is discussed which is mainly an extension of method 5 (QuickSelect) discussed in the previous post. The idea is to randomly pick a pivot element. To implement a randomized partition, we use a random function, rand() to generate an index between l and r, swap the element at the randomly generated index with the last element, and finally call the standard partition process which uses the last element as pivot.

Steps to solve the problem:

1. Check if k>0&& k<=r-l+1:

declare pos as randomPartition(arr,l,r).
check if pos-1==k-1 than return arr[pos].
check if pos-1>k-1 than recursively call kthsmallest(arr,l,pos-1,k).
return recursively call kthsmallest(arr,pos+1,r,k-pos+l-1).
2. Return INT_MAX.

Following is an implementation of the above Randomized QuickSelect.
'''