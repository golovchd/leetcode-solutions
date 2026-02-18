class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        l = len(nums)
        k_idx = 0
        # Get index of k first, O(N)
        for i in range(l):
            if nums[i] == k:
                k_idx = i
                break
        nums[k_idx] = 0     # median position
        # Counts of numbers less than k and more than k for each position left of k, O(N)
        for i in range(k_idx + 1, l):
            if nums[i] < k:
                nums[i] = nums[i - 1] - 1
            else:
                nums[i] = nums[i - 1] + 1
        # Counts of numbers less than k and more than k for each position right of k, O(N)
        for i in range(k_idx - 1, -1, -1):
            if nums[i] < k:
                nums[i] = nums[i + 1] - 1
            else:
                nums[i] = nums[i + 1] + 1
        print(l, k_idx)
        # getting range of divergance from k for lefts and rights, O(N)
        min_r = min(nums[k_idx:]) if k_idx < l else 0
        max_r = max(nums[k_idx + 1:]) if k_idx + 1 < l else 0
        min_l = min(nums[0:k_idx + 1])
        max_l = max(nums[0:k_idx]) if k_idx else 0

        if max_l - min_l > 10:  # worse-case scenario, O(M*K), where M,K < N
            # Reducing boundaries for worse-case scenario O(N*N), O(N)
            e_limit = l - 1
            while e_limit > k_idx and (nums[e_limit] + min_l >= 2 or nums[e_limit] + max_l < -1):
                e_limit -= 1
            s_limit = 0
            while s_limit < k_idx and (nums[s_limit] + min_r >= 2 or nums[s_limit] + max_r < -1):
                s_limit += 1

            print(f"min_l={min_l}, max_l={max_l}, min_r={min_r}, max_r={max_r}, s_limit={s_limit}, e_limit={e_limit}")
            s = k_idx
            count = 0
            while s >= s_limit:     # Nested loop, O(M*K)
                e = k_idx
                while e <= e_limit:
                    sum = nums[s] + nums[e]
                    if sum == (e - s) % 2:
                        count += 1
                    if abs(sum) > l - e:
                        break
                    e += 1
                s -= 1
            return count

        # Left side have small number of deviations from k, calculating number of such deviations and complimentary to them in right side
        print(f"min_l={min_l}, max_l={max_l}, min_r={min_r}, max_r={max_r}")
        unique_l = list(set(nums[0:k_idx + 1] + [1]))   # include 0 and 1 in counts to count sub-arrays started or ended by k
        counts_even_idx_l = {value: 0 for value in unique_l}
        counts_odd_idx_l = {value: 0 for value in unique_l}
        counts_even_idx_r = {value: 0 for value in unique_l}
        counts_odd_idx_r = {value: 0 for value in unique_l}
        counts_even_plus_idx_r = {value: 0 for value in unique_l}
        counts_odd_plus_idx_r = {value: 0 for value in unique_l}
        for i in range(0, k_idx, 2):
            counts_even_idx_l[nums[i]] += 1
        for i in range(1, k_idx, 2):
            counts_odd_idx_l[nums[i]] += 1
        even_l_start = k_idx + 1 if k_idx % 2 else k_idx + 2
        odd_l_start = k_idx + 2 if k_idx % 2 else k_idx + 1
        for i in range(even_l_start, l, 2):
            if -nums[i] in unique_l:
                counts_even_idx_r[-nums[i]] += 1
            if (1 - nums[i]) in unique_l:
                counts_even_plus_idx_r[1-nums[i]] += 1
        for i in range(odd_l_start, l, 2):
            if -nums[i] in unique_l:
                counts_odd_idx_r[-nums[i]] += 1
            if (1 - nums[i]) in unique_l:
                counts_odd_plus_idx_r[1-nums[i]] += 1
        count = 1
        for i in range(len(unique_l)):
            count += counts_even_idx_l[unique_l[i]] * counts_even_idx_r[unique_l[i]]
            count += counts_even_idx_l[unique_l[i]] * counts_odd_plus_idx_r[unique_l[i]]
            count += counts_odd_idx_l[unique_l[i]] * counts_odd_idx_r[unique_l[i]]
            count += counts_odd_idx_l[unique_l[i]] * counts_even_plus_idx_r[unique_l[i]]
        if k_idx % 2:
            count += counts_odd_idx_r[0]
            count += counts_even_plus_idx_r[0]
            count += counts_odd_idx_l[0]
            count += counts_even_idx_l[1]
        else:
            count += counts_even_idx_r[0]
            count += counts_odd_plus_idx_r[0]
            count += counts_even_idx_l[0]
            count += counts_odd_idx_l[1]
        return count
