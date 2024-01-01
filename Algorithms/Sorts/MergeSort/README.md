# Merge Sort
Faster than Bubble Sort. 

Complexity is `O(n*log(n))`. 

There are two main functions:
1. `merge` function:
- Recursively called on its left and right half, returns the same element if the length of the array is less than 2 (base case).
- The results from the recursive call is then sent to the `merge_sort` function.

2. `merge_sort` function:
- An empty list is initialized, let's call it `sorted_arr`.
- We set two position counters for going through the `left_arr` and `right_arr`. We initialize them to 0.
- We loop through two lists at the same time. If the element in `left_arr` is less than or equal to `right_arr`, it is appended to `sorted_arr` and the counter is incremented, else the element in `right_arr` is appended to `sorted_arr` and the subsequent counter is incremented.
- The remaining elements are then appended to the final array and returned.

