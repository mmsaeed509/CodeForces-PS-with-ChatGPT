<h3 align="center"> Count Pairs Hard Version </h3>

<p align="center">
  <img src="/img/CountPairsHardVersion.png" />
</p>
<p/>



<h3 align="center"> Output </h3>

<p align="center">
  <img src="/img/CountPairsHardVersionOutput.png.png" />
</p>
<p/>

<h3 align="center"> Code explanation </h3>

The `num_pairs` function is the main function for solving the problem. It takes in three arguments:

- `n`: the number of elements in the array `a`
- `x`: the maximum value that the sum of any pair (`i`, `j`) can have
- `a`: the array of integers

The first thing the function does is sort the array `a` in non-decreasing order. This is done using the sort method, which has a time complexity of` O(n log n) `.
Next, the function initializes a variable `num_pairs` to `0`. This variable will be used to keep track of the number of valid pairs (`i`, `j`) found so far.
The function then enters a loop that iterates through all elements in the array. For each element `a[i]`, the function calls the `binary_search` function to find the largest `j` such that `a[j]` `>=` `j` and `a[i]` `+` `a[j]` `<=` `x`. The `binary_search` function returns the largest such `j`, and this value is stored in the variable `j`.
The number of valid pairs (`i`, `j`) is then calculated as `j` `-` `i`, and this value is added to the total number of pairs `num_pairs`.
After the loop finishes, the function returns the total number of pairs `num_pairs`.

The `binary_search` function is used to find the largest `j` such that `a[j]` `>=` `j` and `a[i]` `+` `a[j]` `<=` `x`. It takes in five arguments:

- `a`: the array of integers
- `i`: the value of `i` for the current iteration of the outer loop in `num_pairs`
- `l`: the left bound of the search range (initially set to `i`)
- `r`: the right bound of the search range (initially set to `n` `-` `1`)
- `x`: the maximum value that the sum of any pair (`i`, `j`) can have

The function uses a binary search algorithm to find the largest `j` in the given range such that `a[j]` `>=` `j` and `a[i]` `+` `a[j]` `<=` `x`. It returns the value of `j` when the search is complete.
