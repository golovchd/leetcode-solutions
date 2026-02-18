# 47. Permutations II (Medium)

Link to problem: https://leetcode.com/problems/permutations-ii/

* Link to best submission with frequency: https://leetcode.com/submissions/detail/485301136/
* Link to best submission with sort: https://leetcode.com/submissions/detail/485140295/
* Link to best submission with set: https://leetcode.com/submissions/detail/485130359/


You could run memory profiling as below (~6GB mem usage for size 11, ~72GB for size 12):
```bash
for i in {1..11}; do echo ${i}; time python3 backtracking_medium_47/permutations_ii_freq.py ${i} ${i}; done
for i in {1..11}; do echo ${i}; time python3 backtracking_medium_47/permutations_ii_sorted.py ${i} ${i}; done
```
