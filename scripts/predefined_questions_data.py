from typing import List, Dict, Any

def get_all_questions() -> List[Dict[str, Any]]:
    questions = []

    # Arrays & Strings - Easy: Two Sum
    questions.append({
        "id": "two-sum",
        "title": "Two Sum",
        "text": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.\n\nYou may assume that each input would have exactly one solution, and you may not use the same element twice.\n\nYou can return the answer in any order.\n\n**Example 1:**\nInput: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].\n\n**Example 2:**\nInput: nums = [3,2,4], target = 6\nOutput: [1,2]\n\n**Example 3:**\nInput: nums = [3,3], target = 6\nOutput: [0,1]",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def twoSum(self, nums, target):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def twoSum(self, nums, target):\n        num_map = {}\n        for i, num in enumerate(nums):\n            complement = target - num\n            if complement in num_map:\n                return [num_map[complement], i]\n            num_map[num] = i\n        return []",
                "testCases": [
                    {"input": "[2,7,11,15], 9", "expected_output": "[0,1]", "weight": 0.4, "description": "Standard case with solution at beginning"},
                    {"input": "[3,2,4], 6", "expected_output": "[1,2]", "weight": 0.3, "description": "Solution not at beginning"},
                    {"input": "[3,3], 6", "expected_output": "[0,1]", "weight": 0.3, "description": "Duplicate numbers"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[]} nums\n * @param {number} target\n * @return {number[]}\n */\nvar twoSum = function(nums, target) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[]} nums\n * @param {number} target\n * @return {number[]}\n */\nvar twoSum = function(nums, target) {\n    const numMap = new Map();\n    for (let i = 0; i < nums.length; i++) {\n        const complement = target - nums[i];\n        if (numMap.has(complement)) {\n            return [numMap.get(complement), i];\n        }\n        numMap.set(nums[i], i);\n    }\n    return [];\n};",
                "testCases": [
                    {"input": "[2,7,11,15], 9", "expected_output": "[0,1]", "weight": 0.4, "description": "Standard case with solution at beginning"},
                    {"input": "[3,2,4], 6", "expected_output": "[1,2]", "weight": 0.3, "description": "Solution not at beginning"},
                    {"input": "[3,3], 6", "expected_output": "[0,1]", "weight": 0.3, "description": "Duplicate numbers"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int[] twoSum(int[] nums, int target) {\n        // Your code here\n        return new int[0];\n    }\n}",
                "solutionCode": "class Solution {\n    public int[] twoSum(int[] nums, int target) {\n        Map<Integer, Integer> numMap = new HashMap<>();\n        for (int i = 0; i < nums.length; i++) {\n            int complement = target - nums[i];\n            if (numMap.containsKey(complement)) {\n                return new int[]{numMap.get(complement), i};\n            }\n            numMap.put(nums[i], i);\n        }\n        return new int[0];\n    }\n}",
                "testCases": [
                    {"input": "[2,7,11,15], 9", "expected_output": "[0,1]", "weight": 0.4, "description": "Standard case with solution at beginning"},
                    {"input": "[3,2,4], 6", "expected_output": "[1,2]", "weight": 0.3, "description": "Solution not at beginning"},
                    {"input": "[3,3], 6", "expected_output": "[0,1]", "weight": 0.3, "description": "Duplicate numbers"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func twoSum(nums []int, target int) []int {\n    // Your code here\n    return []int{}\n}",
                "solutionCode": "func twoSum(nums []int, target int) []int {\n    numMap := make(map[int]int)\n    for i, num := range nums {\n        complement := target - num\n        if index, exists := numMap[complement]; exists {\n            return []int{index, i}\n        }\n        numMap[num] = i\n    }\n    return []int{}\n}",
                "testCases": [
                    {"input": "[2,7,11,15], 9", "expected_output": "[0,1]", "weight": 0.4, "description": "Standard case with solution at beginning"},
                    {"input": "[3,2,4], 6", "expected_output": "[1,2]", "weight": 0.3, "description": "Solution not at beginning"},
                    {"input": "[3,3], 6", "expected_output": "[0,1]", "weight": 0.3, "description": "Duplicate numbers"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[]} nums\n# @param {Integer} target\n# @return {Integer[]}\ndef two_sum(nums, target)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[]} nums\n# @param {Integer} target\n# @return {Integer[]}\ndef two_sum(nums, target)\n    num_map = {}\n    nums.each_with_index do |num, i|\n        complement = target - num\n        if num_map.key?(complement)\n            return [num_map[complement], i]\n        end\n        num_map[num] = i\n    end\n    []\nend",
                "testCases": [
                    {"input": "[2,7,11,15], 9", "expected_output": "[0,1]", "weight": 0.4, "description": "Standard case with solution at beginning"},
                    {"input": "[3,2,4], 6", "expected_output": "[1,2]", "weight": 0.3, "description": "Solution not at beginning"},
                    {"input": "[3,3], 6", "expected_output": "[0,1]", "weight": 0.3, "description": "Duplicate numbers"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        // Your code here\n        return {};\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        unordered_map<int, int> numMap;\n        for (int i = 0; i < nums.size(); i++) {\n            int complement = target - nums[i];\n            if (numMap.find(complement) != numMap.end()) {\n                return {numMap[complement], i};\n            }\n            numMap[nums[i]] = i;\n        }\n        return {};\n    }\n};",
                "testCases": [
                    {"input": "[2,7,11,15], 9", "expected_output": "[0,1]", "weight": 0.4, "description": "Standard case with solution at beginning"},
                    {"input": "[3,2,4], 6", "expected_output": "[1,2]", "weight": 0.3, "description": "Solution not at beginning"},
                    {"input": "[3,3], 6", "expected_output": "[0,1]", "weight": 0.3, "description": "Duplicate numbers"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(n)",
            "constraints": ["2 <= nums.length <= 10^4", "-10^9 <= nums[i] <= 10^9", "-10^9 <= target <= 10^9", "Only one valid answer exists"]
        },
        "gradingRules": {
            "testCaseWeight": 0.7,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "EASY",
            "estimatedDuration": 15,
            "tags": ["array", "hash-table"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Arrays & Strings"
        }
    })

    # Arrays & Strings - Medium: Longest Palindromic Substring
    questions.append({
        "id": "longest-palindromic-substring",
        "title": "Longest Palindromic Substring",
        "text": "Given a string s, return the longest palindromic substring in s.\n\n**Example 1:**\nInput: s = \"babad\"\nOutput: \"bab\"\nExplanation: \"aba\" is also a valid answer.\n\n**Example 2:**\nInput: s = \"cbbd\"\nOutput: \"bb\"",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def longestPalindrome(self, s):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def longestPalindrome(self, s):\n        if not s:\n            return \"\"\n        \n        start = 0\n        max_len = 1\n        \n        for i in range(len(s)):\n            # Check for odd length palindromes\n            left, right = i, i\n            while left >= 0 and right < len(s) and s[left] == s[right]:\n                current_len = right - left + 1\n                if current_len > max_len:\n                    start = left\n                    max_len = current_len\n                left -= 1\n                right += 1\n            \n            # Check for even length palindromes\n            left, right = i, i + 1\n            while left >= 0 and right < len(s) and s[left] == s[right]:\n                current_len = right - left + 1\n                if current_len > max_len:\n                    start = left\n                    max_len = current_len\n                left -= 1\n                right += 1\n        \n        return s[start:start + max_len]",
                "testCases": [
                    {"input": "\"babad\"", "expected_output": "\"bab\"", "weight": 0.4, "description": "Odd length palindrome"},
                    {"input": "\"cbbd\"", "expected_output": "\"bb\"", "weight": 0.3, "description": "Even length palindrome"},
                    {"input": "\"a\"", "expected_output": "\"a\"", "weight": 0.3, "description": "Single character"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {string} s\n * @return {string}\n */\nvar longestPalindrome = function(s) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {string} s\n * @return {string}\n */\nvar longestPalindrome = function(s) {\n    if (!s) return \"\";\n    \n    let start = 0;\n    let maxLen = 1;\n    \n    for (let i = 0; i < s.length; i++) {\n        // Check for odd length palindromes\n        let left = i, right = i;\n        while (left >= 0 && right < s.length && s[left] === s[right]) {\n            const currentLen = right - left + 1;\n            if (currentLen > maxLen) {\n                start = left;\n                maxLen = currentLen;\n            }\n            left--;\n            right++;\n        }\n        \n        // Check for even length palindromes\n        left = i;\n        right = i + 1;\n        while (left >= 0 && right < s.length && s[left] === s[right]) {\n            const currentLen = right - left + 1;\n            if (currentLen > maxLen) {\n                start = left;\n                maxLen = currentLen;\n            }\n            left--;\n            right++;\n        }\n    }\n    \n    return s.substring(start, start + maxLen);\n};",
                "testCases": [
                    {"input": "\"babad\"", "expected_output": "\"bab\"", "weight": 0.4, "description": "Odd length palindrome"},
                    {"input": "\"cbbd\"", "expected_output": "\"bb\"", "weight": 0.3, "description": "Even length palindrome"},
                    {"input": "\"a\"", "expected_output": "\"a\"", "weight": 0.3, "description": "Single character"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public String longestPalindrome(String s) {\n        // Your code here\n        return \"\";\n    }\n}",
                "solutionCode": "class Solution {\n    public String longestPalindrome(String s) {\n        if (s == null || s.length() == 0) return \"\";\n        \n        int start = 0;\n        int maxLen = 1;\n        \n        for (int i = 0; i < s.length(); i++) {\n            // Check for odd length palindromes\n            int left = i, right = i;\n            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {\n                int currentLen = right - left + 1;\n                if (currentLen > maxLen) {\n                    start = left;\n                    maxLen = currentLen;\n                }\n                left--;\n                right++;\n            }\n            \n            // Check for even length palindromes\n            left = i;\n            right = i + 1;\n            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {\n                int currentLen = right - left + 1;\n                if (currentLen > maxLen) {\n                    start = left;\n                    maxLen = currentLen;\n                }\n                left--;\n                right++;\n            }\n        }\n        \n        return s.substring(start, start + maxLen);\n    }\n}",
                "testCases": [
                    {"input": "\"babad\"", "expected_output": "\"bab\"", "weight": 0.4, "description": "Odd length palindrome"},
                    {"input": "\"cbbd\"", "expected_output": "\"bb\"", "weight": 0.3, "description": "Even length palindrome"},
                    {"input": "\"a\"", "expected_output": "\"a\"", "weight": 0.3, "description": "Single character"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func longestPalindrome(s string) string {\n    // Your code here\n    return \"\"\n}",
                "solutionCode": "func longestPalindrome(s string) string {\n    if len(s) == 0 {\n        return \"\"\n    }\n    \n    start := 0\n    maxLen := 1\n    \n    for i := 0; i < len(s); i++ {\n        // Check for odd length palindromes\n        left, right := i, i\n        for left >= 0 && right < len(s) && s[left] == s[right] {\n            currentLen := right - left + 1\n            if currentLen > maxLen {\n                start = left\n                maxLen = currentLen\n            }\n            left--\n            right++\n        }\n        \n        // Check for even length palindromes\n        left, right = i, i+1\n        for left >= 0 && right < len(s) && s[left] == s[right] {\n            currentLen := right - left + 1\n            if currentLen > maxLen {\n                start = left\n                maxLen = currentLen\n            }\n            left--\n            right++\n        }\n    }\n    \n    return s[start : start+maxLen]\n}",
                "testCases": [
                    {"input": "\"babad\"", "expected_output": "\"bab\"", "weight": 0.4, "description": "Odd length palindrome"},
                    {"input": "\"cbbd\"", "expected_output": "\"bb\"", "weight": 0.3, "description": "Even length palindrome"},
                    {"input": "\"a\"", "expected_output": "\"a\"", "weight": 0.3, "description": "Single character"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {String} s\n# @return {String}\ndef longest_palindrome(s)\n    # Your code here\nend",
                "solutionCode": "# @param {String} s\n# @return {String}\ndef longest_palindrome(s)\n    return \"\" if s.empty?\n    \n    start = 0\n    max_len = 1\n    \n    (0...s.length).each do |i|\n        # Check for odd length palindromes\n        left, right = i, i\n        while left >= 0 && right < s.length && s[left] == s[right]\n            current_len = right - left + 1\n            if current_len > max_len\n                start = left\n                max_len = current_len\n            end\n            left -= 1\n            right += 1\n        end\n        \n        # Check for even length palindromes\n        left, right = i, i + 1\n        while left >= 0 && right < s.length && s[left] == s[right]\n            current_len = right - left + 1\n            if current_len > max_len\n                start = left\n                max_len = current_len\n            end\n            left -= 1\n            right += 1\n        end\n    end\n    \n    s[start, max_len]\nend",
                "testCases": [
                    {"input": "\"babad\"", "expected_output": "\"bab\"", "weight": 0.4, "description": "Odd length palindrome"},
                    {"input": "\"cbbd\"", "expected_output": "\"bb\"", "weight": 0.3, "description": "Even length palindrome"},
                    {"input": "\"a\"", "expected_output": "\"a\"", "weight": 0.3, "description": "Single character"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    string longestPalindrome(string s) {\n        // Your code here\n        return \"\";\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    string longestPalindrome(string s) {\n        if (s.empty()) return \"\";\n        \n        int start = 0;\n        int maxLen = 1;\n        \n        for (int i = 0; i < s.length(); i++) {\n            // Check for odd length palindromes\n            int left = i, right = i;\n            while (left >= 0 && right < s.length() && s[left] == s[right]) {\n                int currentLen = right - left + 1;\n                if (currentLen > maxLen) {\n                    start = left;\n                    maxLen = currentLen;\n                }\n                left--;\n                right++;\n            }\n            \n            // Check for even length palindromes\n            left = i;\n            right = i + 1;\n            while (left >= 0 && right < s.length() && s[left] == s[right]) {\n                int currentLen = right - left + 1;\n                if (currentLen > maxLen) {\n                    start = left;\n                    maxLen = currentLen;\n                }\n                left--;\n                right++;\n            }\n        }\n        \n        return s.substr(start, maxLen);\n    }\n};",
                "testCases": [
                    {"input": "\"babad\"", "expected_output": "\"bab\"", "weight": 0.4, "description": "Odd length palindrome"},
                    {"input": "\"cbbd\"", "expected_output": "\"bb\"", "weight": 0.3, "description": "Even length palindrome"},
                    {"input": "\"a\"", "expected_output": "\"a\"", "weight": 0.3, "description": "Single character"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n^2)",
            "spaceComplexity": "O(1)",
            "constraints": ["1 <= s.length <= 1000", "s consist of only digits and English letters"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 25,
            "tags": ["string", "dynamic-programming"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Arrays & Strings"
        }
    })

    # Arrays & Strings - Hard: Minimum Window Substring
    questions.append({
        "id": "minimum-window-substring",
        "title": "Minimum Window Substring",
        "text": "Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string \"\".\n\nThe testcases will be generated such that the answer is unique.\n\n**Example 1:**\nInput: s = \"ADOBECODEBANC\", t = \"ABC\"\nOutput: \"BANC\"\nExplanation: The minimum window substring \"BANC\" includes 'A', 'B', and 'C' from string t.\n\n**Example 2:**\nInput: s = \"a\", t = \"a\"\nOutput: \"a\"\nExplanation: The entire string s is the minimum window.\n\n**Example 3:**\nInput: s = \"a\", t = \"aa\"\nOutput: \"\"\nExplanation: Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def minWindow(self, s, t):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def minWindow(self, s, t):\n        if not s or not t:\n            return \"\"\n        \n        # Dictionary which keeps a count of all the unique characters in t\n        dict_t = {}\n        for char in t:\n            dict_t[char] = dict_t.get(char, 0) + 1\n        \n        required = len(dict_t)\n        \n        # Left and Right pointer\n        l, r = 0, 0\n        \n        # formed is used to keep track of how many unique characters in the current window\n        # have the desired frequency as in t\n        formed = 0\n        \n        # Dictionary which keeps a count of all the unique characters in the current window\n        window_counts = {}\n        \n        # ans tuple of the form (window length, left, right)\n        ans = float(\"inf\"), None, None\n        \n        while r < len(s):\n            # Add one character from the right to the window\n            character = s[r]\n            window_counts[character] = window_counts.get(character, 0) + 1\n            \n            # If the frequency of the current character added equals to the\n            # desired count in t then increment the formed count by 1\n            if character in dict_t and window_counts[character] == dict_t[character]:\n                formed += 1\n            \n            # Try to contract the window till the point where it ceases to be 'desirable'\n            while l <= r and formed == required:\n                character = s[l]\n                \n                # Save the smallest window until now\n                if r - l + 1 < ans[0]:\n                    ans = (r - l + 1, l, r)\n                \n                # The character at the position pointed by the\n                # `left` pointer is no longer a part of the window\n                window_counts[character] -= 1\n                if character in dict_t and window_counts[character] < dict_t[character]:\n                    formed -= 1\n                \n                # Move the left pointer ahead, this would help to look for a new window\n                l += 1    \n            \n            # Keep expanding the window until all the characters are not included\n            r += 1    \n        \n        return \"\" if ans[0] == float(\"inf\") else s[ans[1] : ans[2] + 1]",
                "testCases": [
                    {"input": "\"ADOBECODEBANC\", \"ABC\"", "expected_output": "\"BANC\"", "weight": 0.4, "description": "Standard case with multiple valid windows"},
                    {"input": "\"a\", \"a\"", "expected_output": "\"a\"", "weight": 0.3, "description": "Single character match"},
                    {"input": "\"a\", \"aa\"", "expected_output": "\"\"", "weight": 0.3, "description": "Impossible case"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {string} s\n * @param {string} t\n * @return {string}\n */\nvar minWindow = function(s, t) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {string} s\n * @param {string} t\n * @return {string}\n */\nvar minWindow = function(s, t) {\n    if (!s || !t) return \"\";\n    \n    const dictT = {};\n    for (const char of t) {\n        dictT[char] = (dictT[char] || 0) + 1;\n    }\n    \n    const required = Object.keys(dictT).length;\n    let l = 0, r = 0;\n    let formed = 0;\n    const windowCounts = {};\n    let ans = [Infinity, null, null];\n    \n    while (r < s.length) {\n        const character = s[r];\n        windowCounts[character] = (windowCounts[character] || 0) + 1;\n        \n        if (dictT[character] && windowCounts[character] === dictT[character]) {\n            formed++;\n        }\n        \n        while (l <= r && formed === required) {\n            const character = s[l];\n            \n            if (r - l + 1 < ans[0]) {\n                ans = [r - l + 1, l, r];\n            }\n            \n            windowCounts[character]--;\n            if (dictT[character] && windowCounts[character] < dictT[character]) {\n                formed--;\n            }\n            \n            l++;\n        }\n        \n        r++;\n    }\n    \n    return ans[0] === Infinity ? \"\" : s.substring(ans[1], ans[2] + 1);\n};",
                "testCases": [
                    {"input": "\"ADOBECODEBANC\", \"ABC\"", "expected_output": "\"BANC\"", "weight": 0.4, "description": "Standard case with multiple valid windows"},
                    {"input": "\"a\", \"a\"", "expected_output": "\"a\"", "weight": 0.3, "description": "Single character match"},
                    {"input": "\"a\", \"aa\"", "expected_output": "\"\"", "weight": 0.3, "description": "Impossible case"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public String minWindow(String s, String t) {\n        // Your code here\n        return \"\";\n    }\n}",
                "solutionCode": "class Solution {\n    public String minWindow(String s, String t) {\n        if (s.length() == 0 || t.length() == 0) {\n            return \"\";\n        }\n        \n        Map<Character, Integer> dictT = new HashMap<>();\n        for (int i = 0; i < t.length(); i++) {\n            char c = t.charAt(i);\n            dictT.put(c, dictT.getOrDefault(c, 0) + 1);\n        }\n        \n        int required = dictT.size();\n        int l = 0, r = 0;\n        int formed = 0;\n        Map<Character, Integer> windowCounts = new HashMap<>();\n        int[] ans = {-1, 0, 0};\n        \n        while (r < s.length()) {\n            char character = s.charAt(r);\n            windowCounts.put(character, windowCounts.getOrDefault(character, 0) + 1);\n            \n            if (dictT.containsKey(character) && windowCounts.get(character).intValue() == dictT.get(character).intValue()) {\n                formed++;\n            }\n            \n            while (l <= r && formed == required) {\n                character = s.charAt(l);\n                \n                if (ans[0] == -1 || r - l + 1 < ans[0]) {\n                    ans[0] = r - l + 1;\n                    ans[1] = l;\n                    ans[2] = r;\n                }\n                \n                windowCounts.put(character, windowCounts.get(character) - 1);\n                if (dictT.containsKey(character) && windowCounts.get(character).intValue() < dictT.get(character).intValue()) {\n                    formed--;\n                }\n                \n                l++;\n            }\n            \n            r++;\n        }\n        \n        return ans[0] == -1 ? \"\" : s.substring(ans[1], ans[2] + 1);\n    }\n}",
                "testCases": [
                    {"input": "\"ADOBECODEBANC\", \"ABC\"", "expected_output": "\"BANC\"", "weight": 0.4, "description": "Standard case with multiple valid windows"},
                    {"input": "\"a\", \"a\"", "expected_output": "\"a\"", "weight": 0.3, "description": "Single character match"},
                    {"input": "\"a\", \"aa\"", "expected_output": "\"\"", "weight": 0.3, "description": "Impossible case"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func minWindow(s string, t string) string {\n    // Your code here\n    return \"\"\n}",
                "solutionCode": "func minWindow(s string, t string) string {\n    if len(s) == 0 || len(t) == 0 {\n        return \"\"\n    }\n    \n    dictT := make(map[byte]int)\n    for i := 0; i < len(t); i++ {\n        dictT[t[i]]++\n    }\n    \n    required := len(dictT)\n    l, r := 0, 0\n    formed := 0\n    windowCounts := make(map[byte]int)\n    ans := []int{-1, 0, 0}\n    \n    for r < len(s) {\n        character := s[r]\n        windowCounts[character]++\n        \n        if count, exists := dictT[character]; exists && windowCounts[character] == count {\n            formed++\n        }\n        \n        for l <= r && formed == required {\n            character = s[l]\n            \n            if ans[0] == -1 || r-l+1 < ans[0] {\n                ans[0] = r - l + 1\n                ans[1] = l\n                ans[2] = r\n            }\n            \n            windowCounts[character]--\n            if count, exists := dictT[character]; exists && windowCounts[character] < count {\n                formed--\n            }\n            \n            l++\n        }\n        \n        r++\n    }\n    \n    if ans[0] == -1 {\n        return \"\"\n    }\n    return s[ans[1] : ans[2]+1]\n}",
                "testCases": [
                    {"input": "\"ADOBECODEBANC\", \"ABC\"", "expected_output": "\"BANC\"", "weight": 0.4, "description": "Standard case with multiple valid windows"},
                    {"input": "\"a\", \"a\"", "expected_output": "\"a\"", "weight": 0.3, "description": "Single character match"},
                    {"input": "\"a\", \"aa\"", "expected_output": "\"\"", "weight": 0.3, "description": "Impossible case"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {String} s\n# @param {String} t\n# @return {String}\ndef min_window(s, t)\n    # Your code here\nend",
                "solutionCode": "# @param {String} s\n# @param {String} t\n# @return {String}\ndef min_window(s, t)\n    return \"\" if s.empty? || t.empty?\n    \n    dict_t = Hash.new(0)\n    t.each_char { |char| dict_t[char] += 1 }\n    \n    required = dict_t.size\n    l = r = 0\n    formed = 0\n    window_counts = Hash.new(0)\n    ans = [Float::INFINITY, nil, nil]\n    \n    while r < s.length\n        character = s[r]\n        window_counts[character] += 1\n        \n        if dict_t.key?(character) && window_counts[character] == dict_t[character]\n            formed += 1\n        end\n        \n        while l <= r && formed == required\n            character = s[l]\n            \n            if r - l + 1 < ans[0]\n                ans = [r - l + 1, l, r]\n            end\n            \n            window_counts[character] -= 1\n            if dict_t.key?(character) && window_counts[character] < dict_t[character]\n                formed -= 1\n            end\n            \n            l += 1\n        end\n        \n        r += 1\n    end\n    \n    ans[0] == Float::INFINITY ? \"\" : s[ans[1]..ans[2]]\nend",
                "testCases": [
                    {"input": "\"ADOBECODEBANC\", \"ABC\"", "expected_output": "\"BANC\"", "weight": 0.4, "description": "Standard case with multiple valid windows"},
                    {"input": "\"a\", \"a\"", "expected_output": "\"a\"", "weight": 0.3, "description": "Single character match"},
                    {"input": "\"a\", \"aa\"", "expected_output": "\"\"", "weight": 0.3, "description": "Impossible case"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    string minWindow(string s, string t) {\n        // Your code here\n        return \"\";\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    string minWindow(string s, string t) {\n        if (s.empty() || t.empty()) {\n            return \"\";\n        }\n        \n        unordered_map<char, int> dictT;\n        for (char c : t) {\n            dictT[c]++;\n        }\n        \n        int required = dictT.size();\n        int l = 0, r = 0;\n        int formed = 0;\n        unordered_map<char, int> windowCounts;\n        vector<int> ans = {-1, 0, 0};\n        \n        while (r < s.length()) {\n            char character = s[r];\n            windowCounts[character]++;\n            \n            if (dictT.find(character) != dictT.end() && windowCounts[character] == dictT[character]) {\n                formed++;\n            }\n            \n            while (l <= r && formed == required) {\n                character = s[l];\n                \n                if (ans[0] == -1 || r - l + 1 < ans[0]) {\n                    ans[0] = r - l + 1;\n                    ans[1] = l;\n                    ans[2] = r;\n                }\n                \n                windowCounts[character]--;\n                if (dictT.find(character) != dictT.end() && windowCounts[character] < dictT[character]) {\n                    formed--;\n                }\n                \n                l++;\n            }\n            \n            r++;\n        }\n        \n        return ans[0] == -1 ? \"\" : s.substr(ans[1], ans[0]);\n    }\n};",
                "testCases": [
                    {"input": "\"ADOBECODEBANC\", \"ABC\"", "expected_output": "\"BANC\"", "weight": 0.4, "description": "Standard case with multiple valid windows"},
                    {"input": "\"a\", \"a\"", "expected_output": "\"a\"", "weight": 0.3, "description": "Single character match"},
                    {"input": "\"a\", \"aa\"", "expected_output": "\"\"", "weight": 0.3, "description": "Impossible case"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(|s| + |t|)",
            "spaceComplexity": "O(|s| + |t|)",
            "constraints": ["m == s.length", "n == t.length", "1 <= m, n <= 10^5", "s and t consist of uppercase and lowercase English letters"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "HARD",
            "estimatedDuration": 35,
            "tags": ["hash-table", "string", "sliding-window"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn", "Uber"],
            "topic": "Arrays & Strings"
        }
    })

    # Linked Lists - Easy: Reverse Linked List
    questions.append({
        "id": "reverse-linked-list",
        "title": "Reverse Linked List",
        "text": "Given the head of a singly linked list, reverse the list, and return the reversed list.\n\n**Example 1:**\nInput: head = [1,2,3,4,5]\nOutput: [5,4,3,2,1]\n\n**Example 2:**\nInput: head = [1,2]\nOutput: [2,1]\n\n**Example 3:**\nInput: head = []\nOutput: []",
        "implementations": [
            {
                "language": "python",
                "starterCode": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def reverseList(self, head):\n        # Your code here\n        pass",
                "solutionCode": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def reverseList(self, head):\n        prev = None\n        current = head\n        \n        while current:\n            next_temp = current.next\n            current.next = prev\n            prev = current\n            current = next_temp\n        \n        return prev",
                "testCases": [
                    {"input": "[1,2,3,4,5]", "expected_output": "[5,4,3,2,1]", "weight": 0.4, "description": "Standard linked list"},
                    {"input": "[1,2]", "expected_output": "[2,1]", "weight": 0.3, "description": "Two nodes"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.3, "description": "Empty list"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n/**\n * @param {ListNode} head\n * @return {ListNode}\n */\nvar reverseList = function(head) {\n    // Your code here\n};",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n/**\n * @param {ListNode} head\n * @return {ListNode}\n */\nvar reverseList = function(head) {\n    let prev = null;\n    let current = head;\n    \n    while (current !== null) {\n        const nextTemp = current.next;\n        current.next = prev;\n        prev = current;\n        current = nextTemp;\n    }\n    \n    return prev;\n};",
                "testCases": [
                    {"input": "[1,2,3,4,5]", "expected_output": "[5,4,3,2,1]", "weight": 0.4, "description": "Standard linked list"},
                    {"input": "[1,2]", "expected_output": "[2,1]", "weight": 0.3, "description": "Two nodes"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.3, "description": "Empty list"}
                ]
            },
            {
                "language": "java",
                "starterCode": "/**\n * Definition for singly-linked list.\n * public class ListNode {\n *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n * }\n */\nclass Solution {\n    public ListNode reverseList(ListNode head) {\n        // Your code here\n        return null;\n    }\n}",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * public class ListNode {\n *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n * }\n */\nclass Solution {\n    public ListNode reverseList(ListNode head) {\n        ListNode prev = null;\n        ListNode current = head;\n        \n        while (current != null) {\n            ListNode nextTemp = current.next;\n            current.next = prev;\n            prev = current;\n            current = nextTemp;\n        }\n        \n        return prev;\n    }\n}",
                "testCases": [
                    {"input": "[1,2,3,4,5]", "expected_output": "[5,4,3,2,1]", "weight": 0.4, "description": "Standard linked list"},
                    {"input": "[1,2]", "expected_output": "[2,1]", "weight": 0.3, "description": "Two nodes"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.3, "description": "Empty list"}
                ]
            },
            {
                "language": "go",
                "starterCode": "/**\n * Definition for singly-linked list.\n * type ListNode struct {\n *     Val int\n *     Next *ListNode\n * }\n */\nfunc reverseList(head *ListNode) *ListNode {\n    // Your code here\n    return nil\n}",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * type ListNode struct {\n *     Val int\n *     Next *ListNode\n * }\n */\nfunc reverseList(head *ListNode) *ListNode {\n    var prev *ListNode\n    current := head\n    \n    for current != nil {\n        nextTemp := current.Next\n        current.Next = prev\n        prev = current\n        current = nextTemp\n    }\n    \n    return prev\n}",
                "testCases": [
                    {"input": "[1,2,3,4,5]", "expected_output": "[5,4,3,2,1]", "weight": 0.4, "description": "Standard linked list"},
                    {"input": "[1,2]", "expected_output": "[2,1]", "weight": 0.3, "description": "Two nodes"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.3, "description": "Empty list"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# Definition for singly-linked list.\n# class ListNode\n#     attr_accessor :val, :next\n#     def initialize(val = 0, _next = nil)\n#         @val = val\n#         @next = _next\n#     end\n# end\n# @param {ListNode} head\n# @return {ListNode}\ndef reverse_list(head)\n    # Your code here\nend",
                "solutionCode": "# Definition for singly-linked list.\n# class ListNode\n#     attr_accessor :val, :next\n#     def initialize(val = 0, _next = nil)\n#         @val = val\n#         @next = _next\n#     end\n# end\n# @param {ListNode} head\n# @return {ListNode}\ndef reverse_list(head)\n    prev = nil\n    current = head\n    \n    while current\n        next_temp = current.next\n        current.next = prev\n        prev = current\n        current = next_temp\n    end\n    \n    prev\nend",
                "testCases": [
                    {"input": "[1,2,3,4,5]", "expected_output": "[5,4,3,2,1]", "weight": 0.4, "description": "Standard linked list"},
                    {"input": "[1,2]", "expected_output": "[2,1]", "weight": 0.3, "description": "Two nodes"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.3, "description": "Empty list"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr) {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\npublic:\n    ListNode* reverseList(ListNode* head) {\n        // Your code here\n        return nullptr;\n    }\n};",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr) {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\npublic:\n    ListNode* reverseList(ListNode* head) {\n        ListNode* prev = nullptr;\n        ListNode* current = head;\n        \n        while (current != nullptr) {\n            ListNode* nextTemp = current->next;\n            current->next = prev;\n            prev = current;\n            current = nextTemp;\n        }\n        \n        return prev;\n    }\n};",
                "testCases": [
                    {"input": "[1,2,3,4,5]", "expected_output": "[5,4,3,2,1]", "weight": 0.4, "description": "Standard linked list"},
                    {"input": "[1,2]", "expected_output": "[2,1]", "weight": 0.3, "description": "Two nodes"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.3, "description": "Empty list"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(1)",
            "constraints": ["The number of nodes in the list is the range [0, 5000]", "-5000 <= Node.val <= 5000"]
        },
        "gradingRules": {
            "testCaseWeight": 0.7,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "EASY",
            "estimatedDuration": 15,
            "tags": ["linked-list", "recursion"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Linked Lists"
        }
    })

    # Trees & Graphs - Easy: Maximum Depth of Binary Tree
    questions.append({
        "id": "maximum-depth-of-binary-tree",
        "title": "Maximum Depth of Binary Tree",
        "text": "Given the root of a binary tree, return its maximum depth.\n\nA binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.\n\n**Example 1:**\nInput: root = [3,9,20,null,null,15,7]\nOutput: 3\n\n**Example 2:**\nInput: root = [1,null,2]\nOutput: 2",
        "implementations": [
            {
                "language": "python",
                "starterCode": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def maxDepth(self, root):\n        # Your code here\n        pass",
                "solutionCode": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def maxDepth(self, root):\n        if not root:\n            return 0\n        \n        left_depth = self.maxDepth(root.left)\n        right_depth = self.maxDepth(root.right)\n        \n        return max(left_depth, right_depth) + 1",
                "testCases": [
                    {"input": "[3,9,20,null,null,15,7]", "expected_output": "3", "weight": 0.4, "description": "Standard binary tree"},
                    {"input": "[1,null,2]", "expected_output": "2", "weight": 0.3, "description": "Right skewed tree"},
                    {"input": "[]", "expected_output": "0", "weight": 0.3, "description": "Empty tree"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * Definition for a binary tree node.\n * function TreeNode(val, left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left = (left===undefined ? null : left)\n *     this.right = (right===undefined ? null : right)\n * }\n */\n/**\n * @param {TreeNode} root\n * @return {number}\n */\nvar maxDepth = function(root) {\n    // Your code here\n};",
                "solutionCode": "/**\n * Definition for a binary tree node.\n * function TreeNode(val, left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left = (left===undefined ? null : left)\n *     this.right = (right===undefined ? null : right)\n * }\n */\n/**\n * @param {TreeNode} root\n * @return {number}\n */\nvar maxDepth = function(root) {\n    if (!root) {\n        return 0;\n    }\n    \n    const leftDepth = maxDepth(root.left);\n    const rightDepth = maxDepth(root.right);\n    \n    return Math.max(leftDepth, rightDepth) + 1;\n};",
                "testCases": [
                    {"input": "[3,9,20,null,null,15,7]", "expected_output": "3", "weight": 0.4, "description": "Standard binary tree"},
                    {"input": "[1,null,2]", "expected_output": "2", "weight": 0.3, "description": "Right skewed tree"},
                    {"input": "[]", "expected_output": "0", "weight": 0.3, "description": "Empty tree"}
                ]
            },
            {
                "language": "java",
                "starterCode": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode() {}\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val, TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left = left;\n *         this.right = right;\n *     }\n * }\n */\nclass Solution {\n    public int maxDepth(TreeNode root) {\n        // Your code here\n        return 0;\n    }\n}",
                "solutionCode": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode() {}\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val, TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left = left;\n *         this.right = right;\n *     }\n * }\n */\nclass Solution {\n    public int maxDepth(TreeNode root) {\n        if (root == null) {\n            return 0;\n        }\n        \n        int leftDepth = maxDepth(root.left);\n        int rightDepth = maxDepth(root.right);\n        \n        return Math.max(leftDepth, rightDepth) + 1;\n    }\n}",
                "testCases": [
                    {"input": "[3,9,20,null,null,15,7]", "expected_output": "3", "weight": 0.4, "description": "Standard binary tree"},
                    {"input": "[1,null,2]", "expected_output": "2", "weight": 0.3, "description": "Right skewed tree"},
                    {"input": "[]", "expected_output": "0", "weight": 0.3, "description": "Empty tree"}
                ]
            },
            {
                "language": "go",
                "starterCode": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc maxDepth(root *TreeNode) int {\n    // Your code here\n    return 0\n}",
                "solutionCode": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc maxDepth(root *TreeNode) int {\n    if root == nil {\n        return 0\n    }\n    \n    leftDepth := maxDepth(root.Left)\n    rightDepth := maxDepth(root.Right)\n    \n    if leftDepth > rightDepth {\n        return leftDepth + 1\n    }\n    return rightDepth + 1\n}",
                "testCases": [
                    {"input": "[3,9,20,null,null,15,7]", "expected_output": "3", "weight": 0.4, "description": "Standard binary tree"},
                    {"input": "[1,null,2]", "expected_output": "2", "weight": 0.3, "description": "Right skewed tree"},
                    {"input": "[]", "expected_output": "0", "weight": 0.3, "description": "Empty tree"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# Definition for a binary tree node.\n# class TreeNode\n#     attr_accessor :val, :left, :right\n#     def initialize(val = 0, left = nil, right = nil)\n#         @val = val\n#         @left = left\n#         @right = right\n#     end\n# end\n# @param {TreeNode} root\n# @return {Integer}\ndef max_depth(root)\n    # Your code here\nend",
                "solutionCode": "# Definition for a binary tree node.\n# class TreeNode\n#     attr_accessor :val, :left, :right\n#     def initialize(val = 0, left = nil, right = nil)\n#         @val = val\n#         @left = left\n#         @right = right\n#     end\n# end\n# @param {TreeNode} root\n# @return {Integer}\ndef max_depth(root)\n    return 0 if root.nil?\n    \n    left_depth = max_depth(root.left)\n    right_depth = max_depth(root.right)\n    \n    [left_depth, right_depth].max + 1\nend",
                "testCases": [
                    {"input": "[3,9,20,null,null,15,7]", "expected_output": "3", "weight": 0.4, "description": "Standard binary tree"},
                    {"input": "[1,null,2]", "expected_output": "2", "weight": 0.3, "description": "Right skewed tree"},
                    {"input": "[]", "expected_output": "0", "weight": 0.3, "description": "Empty tree"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution {\npublic:\n    int maxDepth(TreeNode* root) {\n        // Your code here\n        return 0;\n    }\n};",
                "solutionCode": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution {\npublic:\n    int maxDepth(TreeNode* root) {\n        if (root == nullptr) {\n            return 0;\n        }\n        \n        int leftDepth = maxDepth(root->left);\n        int rightDepth = maxDepth(root->right);\n        \n        return max(leftDepth, rightDepth) + 1;\n    }\n};",
                "testCases": [
                    {"input": "[3,9,20,null,null,15,7]", "expected_output": "3", "weight": 0.4, "description": "Standard binary tree"},
                    {"input": "[1,null,2]", "expected_output": "2", "weight": 0.3, "description": "Right skewed tree"},
                    {"input": "[]", "expected_output": "0", "weight": 0.3, "description": "Empty tree"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(h)",
            "constraints": ["The number of nodes in the tree is in the range [0, 10^4]", "-100 <= Node.val <= 100"]
        },
        "gradingRules": {
            "testCaseWeight": 0.7,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "EASY",
            "estimatedDuration": 15,
            "tags": ["tree", "depth-first-search", "binary-tree"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Trees & Graphs"
        }
    })

    # Dynamic Programming - Easy: Climbing Stairs
    questions.append({
        "id": "climbing-stairs",
        "title": "Climbing Stairs",
        "text": "You are climbing a staircase. It takes n steps to reach the top.\n\nEach time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?\n\n**Example 1:**\nInput: n = 2\nOutput: 2\nExplanation: There are two ways to climb to the top.\n1. 1 step + 1 step\n2. 2 steps\n\n**Example 2:**\nInput: n = 3\nOutput: 3\nExplanation: There are three ways to climb to the top.\n1. 1 step + 1 step + 1 step\n2. 1 step + 2 steps\n3. 2 steps + 1 step",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def climbStairs(self, n):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def climbStairs(self, n):\n        if n <= 2:\n            return n\n        \n        # dp[i] represents the number of ways to reach step i\n        dp = [0] * (n + 1)\n        dp[1] = 1\n        dp[2] = 2\n        \n        for i in range(3, n + 1):\n            dp[i] = dp[i - 1] + dp[i - 2]\n        \n        return dp[n]",
                "testCases": [
                    {"input": "2", "expected_output": "2", "weight": 0.3, "description": "Base case n=2"},
                    {"input": "3", "expected_output": "3", "weight": 0.4, "description": "Standard case n=3"},
                    {"input": "5", "expected_output": "8", "weight": 0.3, "description": "Larger case n=5"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number} n\n * @return {number}\n */\nvar climbStairs = function(n) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number} n\n * @return {number}\n */\nvar climbStairs = function(n) {\n    if (n <= 2) {\n        return n;\n    }\n    \n    const dp = new Array(n + 1);\n    dp[1] = 1;\n    dp[2] = 2;\n    \n    for (let i = 3; i <= n; i++) {\n        dp[i] = dp[i - 1] + dp[i - 2];\n    }\n    \n    return dp[n];\n};",
                "testCases": [
                    {"input": "2", "expected_output": "2", "weight": 0.3, "description": "Base case n=2"},
                    {"input": "3", "expected_output": "3", "weight": 0.4, "description": "Standard case n=3"},
                    {"input": "5", "expected_output": "8", "weight": 0.3, "description": "Larger case n=5"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int climbStairs(int n) {\n        // Your code here\n        return 0;\n    }\n}",
                "solutionCode": "class Solution {\n    public int climbStairs(int n) {\n        if (n <= 2) {\n            return n;\n        }\n        \n        int[] dp = new int[n + 1];\n        dp[1] = 1;\n        dp[2] = 2;\n        \n        for (int i = 3; i <= n; i++) {\n            dp[i] = dp[i - 1] + dp[i - 2];\n        }\n        \n        return dp[n];\n    }\n}",
                "testCases": [
                    {"input": "2", "expected_output": "2", "weight": 0.3, "description": "Base case n=2"},
                    {"input": "3", "expected_output": "3", "weight": 0.4, "description": "Standard case n=3"},
                    {"input": "5", "expected_output": "8", "weight": 0.3, "description": "Larger case n=5"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func climbStairs(n int) int {\n    // Your code here\n    return 0\n}",
                "solutionCode": "func climbStairs(n int) int {\n    if n <= 2 {\n        return n\n    }\n    \n    dp := make([]int, n+1)\n    dp[1] = 1\n    dp[2] = 2\n    \n    for i := 3; i <= n; i++ {\n        dp[i] = dp[i-1] + dp[i-2]\n    }\n    \n    return dp[n]\n}",
                "testCases": [
                    {"input": "2", "expected_output": "2", "weight": 0.3, "description": "Base case n=2"},
                    {"input": "3", "expected_output": "3", "weight": 0.4, "description": "Standard case n=3"},
                    {"input": "5", "expected_output": "8", "weight": 0.3, "description": "Larger case n=5"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer} n\n# @return {Integer}\ndef climb_stairs(n)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer} n\n# @return {Integer}\ndef climb_stairs(n)\n    return n if n <= 2\n    \n    dp = Array.new(n + 1)\n    dp[1] = 1\n    dp[2] = 2\n    \n    (3..n).each do |i|\n        dp[i] = dp[i - 1] + dp[i - 2]\n    end\n    \n    dp[n]\nend",
                "testCases": [
                    {"input": "2", "expected_output": "2", "weight": 0.3, "description": "Base case n=2"},
                    {"input": "3", "expected_output": "3", "weight": 0.4, "description": "Standard case n=3"},
                    {"input": "5", "expected_output": "8", "weight": 0.3, "description": "Larger case n=5"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    int climbStairs(int n) {\n        // Your code here\n        return 0;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    int climbStairs(int n) {\n        if (n <= 2) {\n            return n;\n        }\n        \n        vector<int> dp(n + 1);\n        dp[1] = 1;\n        dp[2] = 2;\n        \n        for (int i = 3; i <= n; i++) {\n            dp[i] = dp[i - 1] + dp[i - 2];\n        }\n        \n        return dp[n];\n    }\n};",
                "testCases": [
                    {"input": "2", "expected_output": "2", "weight": 0.3, "description": "Base case n=2"},
                    {"input": "3", "expected_output": "3", "weight": 0.4, "description": "Standard case n=3"},
                    {"input": "5", "expected_output": "8", "weight": 0.3, "description": "Larger case n=5"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(n)",
            "constraints": ["1 <= n <= 45"]
        },
        "gradingRules": {
            "testCaseWeight": 0.7,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "EASY",
            "estimatedDuration": 15,
            "tags": ["math", "dynamic-programming", "memoization"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Dynamic Programming"
        }
    })

    # Stack & Queue - Easy: Valid Parentheses
    questions.append({
        "id": "valid-parentheses",
        "title": "Valid Parentheses",
        "text": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.\n\nAn input string is valid if:\n1. Open brackets must be closed by the same type of brackets.\n2. Open brackets must be closed in the correct order.\n3. Every close bracket has a corresponding open bracket of the same type.\n\n**Example 1:**\nInput: s = \"()\"\nOutput: true\n\n**Example 2:**\nInput: s = \"()[]{}\"\nOutput: true\n\n**Example 3:**\nInput: s = \"(]\"\nOutput: false",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def isValid(self, s):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def isValid(self, s):\n        stack = []\n        mapping = {')': '(', '}': '{', ']': '['}\n        \n        for char in s:\n            if char in mapping:\n                # Closing bracket\n                if not stack or stack.pop() != mapping[char]:\n                    return False\n            else:\n                # Opening bracket\n                stack.append(char)\n        \n        return len(stack) == 0",
                "testCases": [
                    {"input": "\"()\"", "expected_output": "True", "weight": 0.3, "description": "Simple valid case"},
                    {"input": "\"()[]{}\"", "expected_output": "True", "weight": 0.4, "description": "Multiple bracket types"},
                    {"input": "\"(]\"", "expected_output": "False", "weight": 0.3, "description": "Invalid case"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {string} s\n * @return {boolean}\n */\nvar isValid = function(s) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {string} s\n * @return {boolean}\n */\nvar isValid = function(s) {\n    const stack = [];\n    const mapping = {')': '(', '}': '{', ']': '['};\n    \n    for (const char of s) {\n        if (char in mapping) {\n            // Closing bracket\n            if (stack.length === 0 || stack.pop() !== mapping[char]) {\n                return false;\n            }\n        } else {\n            // Opening bracket\n            stack.push(char);\n        }\n    }\n    \n    return stack.length === 0;\n};",
                "testCases": [
                    {"input": "\"()\"", "expected_output": "true", "weight": 0.3, "description": "Simple valid case"},
                    {"input": "\"()[]{}\"", "expected_output": "true", "weight": 0.4, "description": "Multiple bracket types"},
                    {"input": "\"(]\"", "expected_output": "false", "weight": 0.3, "description": "Invalid case"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public boolean isValid(String s) {\n        // Your code here\n        return false;\n    }\n}",
                "solutionCode": "class Solution {\n    public boolean isValid(String s) {\n        Stack<Character> stack = new Stack<>();\n        Map<Character, Character> mapping = new HashMap<>();\n        mapping.put(')', '(');\n        mapping.put('}', '{');\n        mapping.put(']', '[');\n        \n        for (char c : s.toCharArray()) {\n            if (mapping.containsKey(c)) {\n                // Closing bracket\n                if (stack.isEmpty() || stack.pop() != mapping.get(c)) {\n                    return false;\n                }\n            } else {\n                // Opening bracket\n                stack.push(c);\n            }\n        }\n        \n        return stack.isEmpty();\n    }\n}",
                "testCases": [
                    {"input": "\"()\"", "expected_output": "true", "weight": 0.3, "description": "Simple valid case"},
                    {"input": "\"()[]{}\"", "expected_output": "true", "weight": 0.4, "description": "Multiple bracket types"},
                    {"input": "\"(]\"", "expected_output": "false", "weight": 0.3, "description": "Invalid case"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func isValid(s string) bool {\n    // Your code here\n    return false\n}",
                "solutionCode": "func isValid(s string) bool {\n    stack := []rune{}\n    mapping := map[rune]rune{\n        ')': '(',\n        '}': '{',\n        ']': '[',\n    }\n    \n    for _, char := range s {\n        if openBracket, exists := mapping[char]; exists {\n            // Closing bracket\n            if len(stack) == 0 || stack[len(stack)-1] != openBracket {\n                return false\n            }\n            stack = stack[:len(stack)-1] // pop\n        } else {\n            // Opening bracket\n            stack = append(stack, char)\n        }\n    }\n    \n    return len(stack) == 0\n}",
                "testCases": [
                    {"input": "\"()\"", "expected_output": "true", "weight": 0.3, "description": "Simple valid case"},
                    {"input": "\"()[]{}\"", "expected_output": "true", "weight": 0.4, "description": "Multiple bracket types"},
                    {"input": "\"(]\"", "expected_output": "false", "weight": 0.3, "description": "Invalid case"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {String} s\n# @return {Boolean}\ndef is_valid(s)\n    # Your code here\nend",
                "solutionCode": "# @param {String} s\n# @return {Boolean}\ndef is_valid(s)\n    stack = []\n    mapping = {')' => '(', '}' => '{', ']' => '['}\n    \n    s.each_char do |char|\n        if mapping.key?(char)\n            # Closing bracket\n            return false if stack.empty? || stack.pop != mapping[char]\n        else\n            # Opening bracket\n            stack.push(char)\n        end\n    end\n    \n    stack.empty?\nend",
                "testCases": [
                    {"input": "\"()\"", "expected_output": "true", "weight": 0.3, "description": "Simple valid case"},
                    {"input": "\"()[]{}\"", "expected_output": "true", "weight": 0.4, "description": "Multiple bracket types"},
                    {"input": "\"(]\"", "expected_output": "false", "weight": 0.3, "description": "Invalid case"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    bool isValid(string s) {\n        // Your code here\n        return false;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    bool isValid(string s) {\n        stack<char> st;\n        unordered_map<char, char> mapping = {\n            {')', '('},\n            {'}', '{'},\n            {']', '['}\n        };\n        \n        for (char c : s) {\n            if (mapping.find(c) != mapping.end()) {\n                // Closing bracket\n                if (st.empty() || st.top() != mapping[c]) {\n                    return false;\n                }\n                st.pop();\n            } else {\n                // Opening bracket\n                st.push(c);\n            }\n        }\n        \n        return st.empty();\n    }\n};",
                "testCases": [
                    {"input": "\"()\"", "expected_output": "true", "weight": 0.3, "description": "Simple valid case"},
                    {"input": "\"()[]{}\"", "expected_output": "true", "weight": 0.4, "description": "Multiple bracket types"},
                    {"input": "\"(]\"", "expected_output": "false", "weight": 0.3, "description": "Invalid case"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(n)",
            "constraints": ["1 <= s.length <= 10^4", "s consists of parentheses only '()[]{}'"]
        },
        "gradingRules": {
            "testCaseWeight": 0.7,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "EASY",
            "estimatedDuration": 15,
            "tags": ["string", "stack"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Stack & Queue"
        }
    })

    # Arrays & Strings - Easy: Reverse String
    questions.append({
        "id": "reverse-string",
        "title": "Reverse String",
        "text": "Write a function that reverses a string. The input string is given as an array of characters s.\n\nYou must do this by modifying the input array in-place with O(1) extra memory.\n\n**Example 1:**\nInput: s = [\"h\",\"e\",\"l\",\"l\",\"o\"]\nOutput: [\"o\",\"l\",\"l\",\"e\",\"h\"]\n\n**Example 2:**\nInput: s = [\"H\",\"a\",\"n\",\"n\",\"a\",\"h\"]\nOutput: [\"h\",\"a\",\"n\",\"n\",\"a\",\"H\"]",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def reverseString(self, s):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def reverseString(self, s):\n        left, right = 0, len(s) - 1\n        while left < right:\n            s[left], s[right] = s[right], s[left]\n            left += 1\n            right -= 1",
                "testCases": [
                    {"input": "[\"h\",\"e\",\"l\",\"l\",\"o\"]", "expected_output": "[\"o\",\"l\",\"l\",\"e\",\"h\"]", "weight": 0.5, "description": "Standard case"},
                    {"input": "[\"H\",\"a\",\"n\",\"n\",\"a\",\"h\"]", "expected_output": "[\"h\",\"a\",\"n\",\"n\",\"a\",\"H\"]", "weight": 0.5, "description": "Mixed case"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {character[]} s\n * @return {void} Do not return anything, modify s in-place instead.\n */\nvar reverseString = function(s) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {character[]} s\n * @return {void} Do not return anything, modify s in-place instead.\n */\nvar reverseString = function(s) {\n    let left = 0, right = s.length - 1;\n    while (left < right) {\n        [s[left], s[right]] = [s[right], s[left]];\n        left++;\n        right--;\n    }\n};",
                "testCases": [
                    {"input": "[\"h\",\"e\",\"l\",\"l\",\"o\"]", "expected_output": "[\"o\",\"l\",\"l\",\"e\",\"h\"]", "weight": 0.5, "description": "Standard case"},
                    {"input": "[\"H\",\"a\",\"n\",\"n\",\"a\",\"h\"]", "expected_output": "[\"h\",\"a\",\"n\",\"n\",\"a\",\"H\"]", "weight": 0.5, "description": "Mixed case"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public void reverseString(char[] s) {\n        // Your code here\n    }\n}",
                "solutionCode": "class Solution {\n    public void reverseString(char[] s) {\n        int left = 0, right = s.length - 1;\n        while (left < right) {\n            char temp = s[left];\n            s[left] = s[right];\n            s[right] = temp;\n            left++;\n            right--;\n        }\n    }\n}",
                "testCases": [
                    {"input": "[\"h\",\"e\",\"l\",\"l\",\"o\"]", "expected_output": "[\"o\",\"l\",\"l\",\"e\",\"h\"]", "weight": 0.5, "description": "Standard case"},
                    {"input": "[\"H\",\"a\",\"n\",\"n\",\"a\",\"h\"]", "expected_output": "[\"h\",\"a\",\"n\",\"n\",\"a\",\"H\"]", "weight": 0.5, "description": "Mixed case"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func reverseString(s []byte) {\n    // Your code here\n}",
                "solutionCode": "func reverseString(s []byte) {\n    left, right := 0, len(s)-1\n    for left < right {\n        s[left], s[right] = s[right], s[left]\n        left++\n        right--\n    }\n}",
                "testCases": [
                    {"input": "[\"h\",\"e\",\"l\",\"l\",\"o\"]", "expected_output": "[\"o\",\"l\",\"l\",\"e\",\"h\"]", "weight": 0.5, "description": "Standard case"},
                    {"input": "[\"H\",\"a\",\"n\",\"n\",\"a\",\"h\"]", "expected_output": "[\"h\",\"a\",\"n\",\"n\",\"a\",\"H\"]", "weight": 0.5, "description": "Mixed case"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Character[]} s\n# @return {Void} Do not return anything, modify s in-place instead.\ndef reverse_string(s)\n    # Your code here\nend",
                "solutionCode": "# @param {Character[]} s\n# @return {Void} Do not return anything, modify s in-place instead.\ndef reverse_string(s)\n    left, right = 0, s.length - 1\n    while left < right\n        s[left], s[right] = s[right], s[left]\n        left += 1\n        right -= 1\n    end\nend",
                "testCases": [
                    {"input": "[\"h\",\"e\",\"l\",\"l\",\"o\"]", "expected_output": "[\"o\",\"l\",\"l\",\"e\",\"h\"]", "weight": 0.5, "description": "Standard case"},
                    {"input": "[\"H\",\"a\",\"n\",\"n\",\"a\",\"h\"]", "expected_output": "[\"h\",\"a\",\"n\",\"n\",\"a\",\"H\"]", "weight": 0.5, "description": "Mixed case"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    void reverseString(vector<char>& s) {\n        // Your code here\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    void reverseString(vector<char>& s) {\n        int left = 0, right = s.size() - 1;\n        while (left < right) {\n            swap(s[left], s[right]);\n            left++;\n            right--;\n        }\n    }\n};",
                "testCases": [
                    {"input": "[\"h\",\"e\",\"l\",\"l\",\"o\"]", "expected_output": "[\"o\",\"l\",\"l\",\"e\",\"h\"]", "weight": 0.5, "description": "Standard case"},
                    {"input": "[\"H\",\"a\",\"n\",\"n\",\"a\",\"h\"]", "expected_output": "[\"h\",\"a\",\"n\",\"n\",\"a\",\"H\"]", "weight": 0.5, "description": "Mixed case"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(1)",
            "constraints": ["1 <= s.length <= 10^5", "s[i] is a printable ascii character"]
        },
        "gradingRules": {
            "testCaseWeight": 0.7,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "EASY",
            "estimatedDuration": 10,
            "tags": ["two-pointers", "string"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Arrays & Strings"
        }
    })

    # Arrays & Strings - Easy: Contains Duplicate
    questions.append({
        "id": "contains-duplicate",
        "title": "Contains Duplicate",
        "text": "Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.\n\n**Example 1:**\nInput: nums = [1,2,3,1]\nOutput: true\n\n**Example 2:**\nInput: nums = [1,2,3,4]\nOutput: false\n\n**Example 3:**\nInput: nums = [1,1,1,3,3,4,3,2,4,2]\nOutput: true",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def containsDuplicate(self, nums):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def containsDuplicate(self, nums):\n        seen = set()\n        for num in nums:\n            if num in seen:\n                return True\n            seen.add(num)\n        return False",
                "testCases": [
                    {"input": "[1,2,3,1]", "expected_output": "True", "weight": 0.4, "description": "Contains duplicate"},
                    {"input": "[1,2,3,4]", "expected_output": "False", "weight": 0.3, "description": "No duplicates"},
                    {"input": "[1,1,1,3,3,4,3,2,4,2]", "expected_output": "True", "weight": 0.3, "description": "Multiple duplicates"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[]} nums\n * @return {boolean}\n */\nvar containsDuplicate = function(nums) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[]} nums\n * @return {boolean}\n */\nvar containsDuplicate = function(nums) {\n    const seen = new Set();\n    for (const num of nums) {\n        if (seen.has(num)) {\n            return true;\n        }\n        seen.add(num);\n    }\n    return false;\n};",
                "testCases": [
                    {"input": "[1,2,3,1]", "expected_output": "true", "weight": 0.4, "description": "Contains duplicate"},
                    {"input": "[1,2,3,4]", "expected_output": "false", "weight": 0.3, "description": "No duplicates"},
                    {"input": "[1,1,1,3,3,4,3,2,4,2]", "expected_output": "true", "weight": 0.3, "description": "Multiple duplicates"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public boolean containsDuplicate(int[] nums) {\n        // Your code here\n        return false;\n    }\n}",
                "solutionCode": "class Solution {\n    public boolean containsDuplicate(int[] nums) {\n        Set<Integer> seen = new HashSet<>();\n        for (int num : nums) {\n            if (seen.contains(num)) {\n                return true;\n            }\n            seen.add(num);\n        }\n        return false;\n    }\n}",
                "testCases": [
                    {"input": "[1,2,3,1]", "expected_output": "true", "weight": 0.4, "description": "Contains duplicate"},
                    {"input": "[1,2,3,4]", "expected_output": "false", "weight": 0.3, "description": "No duplicates"},
                    {"input": "[1,1,1,3,3,4,3,2,4,2]", "expected_output": "true", "weight": 0.3, "description": "Multiple duplicates"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func containsDuplicate(nums []int) bool {\n    // Your code here\n    return false\n}",
                "solutionCode": "func containsDuplicate(nums []int) bool {\n    seen := make(map[int]bool)\n    for _, num := range nums {\n        if seen[num] {\n            return true\n        }\n        seen[num] = true\n    }\n    return false\n}",
                "testCases": [
                    {"input": "[1,2,3,1]", "expected_output": "true", "weight": 0.4, "description": "Contains duplicate"},
                    {"input": "[1,2,3,4]", "expected_output": "false", "weight": 0.3, "description": "No duplicates"},
                    {"input": "[1,1,1,3,3,4,3,2,4,2]", "expected_output": "true", "weight": 0.3, "description": "Multiple duplicates"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[]} nums\n# @return {Boolean}\ndef contains_duplicate(nums)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[]} nums\n# @return {Boolean}\ndef contains_duplicate(nums)\n    seen = Set.new\n    nums.each do |num|\n        return true if seen.include?(num)\n        seen.add(num)\n    end\n    false\nend",
                "testCases": [
                    {"input": "[1,2,3,1]", "expected_output": "true", "weight": 0.4, "description": "Contains duplicate"},
                    {"input": "[1,2,3,4]", "expected_output": "false", "weight": 0.3, "description": "No duplicates"},
                    {"input": "[1,1,1,3,3,4,3,2,4,2]", "expected_output": "true", "weight": 0.3, "description": "Multiple duplicates"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    bool containsDuplicate(vector<int>& nums) {\n        // Your code here\n        return false;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    bool containsDuplicate(vector<int>& nums) {\n        unordered_set<int> seen;\n        for (int num : nums) {\n            if (seen.find(num) != seen.end()) {\n                return true;\n            }\n            seen.insert(num);\n        }\n        return false;\n    }\n};",
                "testCases": [
                    {"input": "[1,2,3,1]", "expected_output": "true", "weight": 0.4, "description": "Contains duplicate"},
                    {"input": "[1,2,3,4]", "expected_output": "false", "weight": 0.3, "description": "No duplicates"},
                    {"input": "[1,1,1,3,3,4,3,2,4,2]", "expected_output": "true", "weight": 0.3, "description": "Multiple duplicates"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(n)",
            "constraints": ["1 <= nums.length <= 10^5", "-10^9 <= nums[i] <= 10^9"]
        },
        "gradingRules": {
            "testCaseWeight": 0.7,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "EASY",
            "estimatedDuration": 10,
            "tags": ["array", "hash-table"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Arrays & Strings"
        }
    })

    # Arrays & Strings - Medium: Group Anagrams
    questions.append({
        "id": "group-anagrams",
        "title": "Group Anagrams",
        "text": "Given an array of strings strs, group the anagrams together. You can return the answer in any order.\n\nAn Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.\n\n**Example 1:**\nInput: strs = [\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]\nOutput: [[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]\n\n**Example 2:**\nInput: strs = [\"\"]\nOutput: [[\"\"]]\n\n**Example 3:**\nInput: strs = [\"a\"]\nOutput: [[\"a\"]]",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def groupAnagrams(self, strs):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def groupAnagrams(self, strs):\n        from collections import defaultdict\n        \n        anagram_map = defaultdict(list)\n        \n        for s in strs:\n            # Sort the string to use as key\n            key = ''.join(sorted(s))\n            anagram_map[key].append(s)\n        \n        return list(anagram_map.values())",
                "testCases": [
                    {"input": "[\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]", "expected_output": "[[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]", "weight": 0.5, "description": "Multiple anagram groups"},
                    {"input": "[\"\"]", "expected_output": "[[\"\"]]", "weight": 0.25, "description": "Empty string"},
                    {"input": "[\"a\"]", "expected_output": "[[\"a\"]]", "weight": 0.25, "description": "Single character"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {string[]} strs\n * @return {string[][]}\n */\nvar groupAnagrams = function(strs) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {string[]} strs\n * @return {string[][]}\n */\nvar groupAnagrams = function(strs) {\n    const anagramMap = new Map();\n    \n    for (const str of strs) {\n        // Sort the string to use as key\n        const key = str.split('').sort().join('');\n        if (!anagramMap.has(key)) {\n            anagramMap.set(key, []);\n        }\n        anagramMap.get(key).push(str);\n    }\n    \n    return Array.from(anagramMap.values());\n};",
                "testCases": [
                    {"input": "[\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]", "expected_output": "[[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]", "weight": 0.5, "description": "Multiple anagram groups"},
                    {"input": "[\"\"]", "expected_output": "[[\"\"]]", "weight": 0.25, "description": "Empty string"},
                    {"input": "[\"a\"]", "expected_output": "[[\"a\"]]", "weight": 0.25, "description": "Single character"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public List<List<String>> groupAnagrams(String[] strs) {\n        // Your code here\n        return new ArrayList<>();\n    }\n}",
                "solutionCode": "class Solution {\n    public List<List<String>> groupAnagrams(String[] strs) {\n        Map<String, List<String>> anagramMap = new HashMap<>();\n        \n        for (String str : strs) {\n            // Sort the string to use as key\n            char[] chars = str.toCharArray();\n            Arrays.sort(chars);\n            String key = new String(chars);\n            \n            anagramMap.computeIfAbsent(key, k -> new ArrayList<>()).add(str);\n        }\n        \n        return new ArrayList<>(anagramMap.values());\n    }\n}",
                "testCases": [
                    {"input": "[\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]", "expected_output": "[[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]", "weight": 0.5, "description": "Multiple anagram groups"},
                    {"input": "[\"\"]", "expected_output": "[[\"\"]]", "weight": 0.25, "description": "Empty string"},
                    {"input": "[\"a\"]", "expected_output": "[[\"a\"]]", "weight": 0.25, "description": "Single character"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func groupAnagrams(strs []string) [][]string {\n    // Your code here\n    return [][]string{}\n}",
                "solutionCode": "func groupAnagrams(strs []string) [][]string {\n    anagramMap := make(map[string][]string)\n    \n    for _, str := range strs {\n        // Sort the string to use as key\n        runes := []rune(str)\n        sort.Slice(runes, func(i, j int) bool {\n            return runes[i] < runes[j]\n        })\n        key := string(runes)\n        \n        anagramMap[key] = append(anagramMap[key], str)\n    }\n    \n    result := make([][]string, 0, len(anagramMap))\n    for _, group := range anagramMap {\n        result = append(result, group)\n    }\n    \n    return result\n}",
                "testCases": [
                    {"input": "[\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]", "expected_output": "[[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]", "weight": 0.5, "description": "Multiple anagram groups"},
                    {"input": "[\"\"]", "expected_output": "[[\"\"]]", "weight": 0.25, "description": "Empty string"},
                    {"input": "[\"a\"]", "expected_output": "[[\"a\"]]", "weight": 0.25, "description": "Single character"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {String[]} strs\n# @return {String[][]}\ndef group_anagrams(strs)\n    # Your code here\nend",
                "solutionCode": "# @param {String[]} strs\n# @return {String[][]}\ndef group_anagrams(strs)\n    anagram_map = Hash.new { |h, k| h[k] = [] }\n    \n    strs.each do |str|\n        # Sort the string to use as key\n        key = str.chars.sort.join\n        anagram_map[key] << str\n    end\n    \n    anagram_map.values\nend",
                "testCases": [
                    {"input": "[\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]", "expected_output": "[[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]", "weight": 0.5, "description": "Multiple anagram groups"},
                    {"input": "[\"\"]", "expected_output": "[[\"\"]]", "weight": 0.25, "description": "Empty string"},
                    {"input": "[\"a\"]", "expected_output": "[[\"a\"]]", "weight": 0.25, "description": "Single character"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    vector<vector<string>> groupAnagrams(vector<string>& strs) {\n        // Your code here\n        return {};\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    vector<vector<string>> groupAnagrams(vector<string>& strs) {\n        unordered_map<string, vector<string>> anagramMap;\n        \n        for (const string& str : strs) {\n            // Sort the string to use as key\n            string key = str;\n            sort(key.begin(), key.end());\n            anagramMap[key].push_back(str);\n        }\n        \n        vector<vector<string>> result;\n        for (const auto& pair : anagramMap) {\n            result.push_back(pair.second);\n        }\n        \n        return result;\n    }\n};",
                "testCases": [
                    {"input": "[\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]", "expected_output": "[[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]", "weight": 0.5, "description": "Multiple anagram groups"},
                    {"input": "[\"\"]", "expected_output": "[[\"\"]]", "weight": 0.25, "description": "Empty string"},
                    {"input": "[\"a\"]", "expected_output": "[[\"a\"]]", "weight": 0.25, "description": "Single character"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n * k log k)",
            "spaceComplexity": "O(n * k)",
            "constraints": ["1 <= strs.length <= 10^4", "0 <= strs[i].length <= 100", "strs[i] consists of lowercase English letters"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 20,
            "tags": ["array", "hash-table", "string", "sorting"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Arrays & Strings"
        }
    })

    # Linked Lists - Medium: Add Two Numbers
    questions.append({
        "id": "add-two-numbers",
        "title": "Add Two Numbers",
        "text": "You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.\n\nYou may assume the two numbers do not contain any leading zero, except the number 0 itself.\n\n**Example 1:**\nInput: l1 = [2,4,3], l2 = [5,6,4]\nOutput: [7,0,8]\nExplanation: 342 + 465 = 807.\n\n**Example 2:**\nInput: l1 = [0], l2 = [0]\nOutput: [0]\n\n**Example 3:**\nInput: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]\nOutput: [8,9,9,9,0,0,0,1]",
        "implementations": [
            {
                "language": "python",
                "starterCode": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def addTwoNumbers(self, l1, l2):\n        # Your code here\n        pass",
                "solutionCode": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def addTwoNumbers(self, l1, l2):\n        dummy = ListNode(0)\n        current = dummy\n        carry = 0\n        \n        while l1 or l2 or carry:\n            val1 = l1.val if l1 else 0\n            val2 = l2.val if l2 else 0\n            \n            total = val1 + val2 + carry\n            carry = total // 10\n            digit = total % 10\n            \n            current.next = ListNode(digit)\n            current = current.next\n            \n            l1 = l1.next if l1 else None\n            l2 = l2.next if l2 else None\n        \n        return dummy.next",
                "testCases": [
                    {"input": "[2,4,3], [5,6,4]", "expected_output": "[7,0,8]", "weight": 0.4, "description": "Standard addition with carry"},
                    {"input": "[0], [0]", "expected_output": "[0]", "weight": 0.3, "description": "Adding zeros"},
                    {"input": "[9,9,9,9,9,9,9], [9,9,9,9]", "expected_output": "[8,9,9,9,0,0,0,1]", "weight": 0.3, "description": "Multiple carries"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n/**\n * @param {ListNode} l1\n * @param {ListNode} l2\n * @return {ListNode}\n */\nvar addTwoNumbers = function(l1, l2) {\n    // Your code here\n};",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n/**\n * @param {ListNode} l1\n * @param {ListNode} l2\n * @return {ListNode}\n */\nvar addTwoNumbers = function(l1, l2) {\n    const dummy = new ListNode(0);\n    let current = dummy;\n    let carry = 0;\n    \n    while (l1 || l2 || carry) {\n        const val1 = l1 ? l1.val : 0;\n        const val2 = l2 ? l2.val : 0;\n        \n        const total = val1 + val2 + carry;\n        carry = Math.floor(total / 10);\n        const digit = total % 10;\n        \n        current.next = new ListNode(digit);\n        current = current.next;\n        \n        l1 = l1 ? l1.next : null;\n        l2 = l2 ? l2.next : null;\n    }\n    \n    return dummy.next;\n};",
                "testCases": [
                    {"input": "[2,4,3], [5,6,4]", "expected_output": "[7,0,8]", "weight": 0.4, "description": "Standard addition with carry"},
                    {"input": "[0], [0]", "expected_output": "[0]", "weight": 0.3, "description": "Adding zeros"},
                    {"input": "[9,9,9,9,9,9,9], [9,9,9,9]", "expected_output": "[8,9,9,9,0,0,0,1]", "weight": 0.3, "description": "Multiple carries"}
                ]
            },
            {
                "language": "java",
                "starterCode": "/**\n * Definition for singly-linked list.\n * public class ListNode {\n *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n * }\n */\nclass Solution {\n    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {\n        // Your code here\n        return null;\n    }\n}",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * public class ListNode {\n *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n * }\n */\nclass Solution {\n    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {\n        ListNode dummy = new ListNode(0);\n        ListNode current = dummy;\n        int carry = 0;\n        \n        while (l1 != null || l2 != null || carry != 0) {\n            int val1 = (l1 != null) ? l1.val : 0;\n            int val2 = (l2 != null) ? l2.val : 0;\n            \n            int total = val1 + val2 + carry;\n            carry = total / 10;\n            int digit = total % 10;\n            \n            current.next = new ListNode(digit);\n            current = current.next;\n            \n            l1 = (l1 != null) ? l1.next : null;\n            l2 = (l2 != null) ? l2.next : null;\n        }\n        \n        return dummy.next;\n    }\n}",
                "testCases": [
                    {"input": "[2,4,3], [5,6,4]", "expected_output": "[7,0,8]", "weight": 0.4, "description": "Standard addition with carry"},
                    {"input": "[0], [0]", "expected_output": "[0]", "weight": 0.3, "description": "Adding zeros"},
                    {"input": "[9,9,9,9,9,9,9], [9,9,9,9]", "expected_output": "[8,9,9,9,0,0,0,1]", "weight": 0.3, "description": "Multiple carries"}
                ]
            },
            {
                "language": "go",
                "starterCode": "/**\n * Definition for singly-linked list.\n * type ListNode struct {\n *     Val int\n *     Next *ListNode\n * }\n */\nfunc addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {\n    // Your code here\n    return nil\n}",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * type ListNode struct {\n *     Val int\n *     Next *ListNode\n * }\n */\nfunc addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {\n    dummy := &ListNode{}\n    current := dummy\n    carry := 0\n    \n    for l1 != nil || l2 != nil || carry != 0 {\n        val1 := 0\n        if l1 != nil {\n            val1 = l1.Val\n            l1 = l1.Next\n        }\n        \n        val2 := 0\n        if l2 != nil {\n            val2 = l2.Val\n            l2 = l2.Next\n        }\n        \n        total := val1 + val2 + carry\n        carry = total / 10\n        digit := total % 10\n        \n        current.Next = &ListNode{Val: digit}\n        current = current.Next\n    }\n    \n    return dummy.Next\n}",
                "testCases": [
                    {"input": "[2,4,3], [5,6,4]", "expected_output": "[7,0,8]", "weight": 0.4, "description": "Standard addition with carry"},
                    {"input": "[0], [0]", "expected_output": "[0]", "weight": 0.3, "description": "Adding zeros"},
                    {"input": "[9,9,9,9,9,9,9], [9,9,9,9]", "expected_output": "[8,9,9,9,0,0,0,1]", "weight": 0.3, "description": "Multiple carries"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# Definition for singly-linked list.\n# class ListNode\n#     attr_accessor :val, :next\n#     def initialize(val = 0, _next = nil)\n#         @val = val\n#         @next = _next\n#     end\n# end\n# @param {ListNode} l1\n# @param {ListNode} l2\n# @return {ListNode}\ndef add_two_numbers(l1, l2)\n    # Your code here\nend",
                "solutionCode": "# Definition for singly-linked list.\n# class ListNode\n#     attr_accessor :val, :next\n#     def initialize(val = 0, _next = nil)\n#         @val = val\n#         @next = _next\n#     end\n# end\n# @param {ListNode} l1\n# @param {ListNode} l2\n# @return {ListNode}\ndef add_two_numbers(l1, l2)\n    dummy = ListNode.new(0)\n    current = dummy\n    carry = 0\n    \n    while l1 || l2 || carry > 0\n        val1 = l1 ? l1.val : 0\n        val2 = l2 ? l2.val : 0\n        \n        total = val1 + val2 + carry\n        carry = total / 10\n        digit = total % 10\n        \n        current.next = ListNode.new(digit)\n        current = current.next\n        \n        l1 = l1.next if l1\n        l2 = l2.next if l2\n    end\n    \n    dummy.next\nend",
                "testCases": [
                    {"input": "[2,4,3], [5,6,4]", "expected_output": "[7,0,8]", "weight": 0.4, "description": "Standard addition with carry"},
                    {"input": "[0], [0]", "expected_output": "[0]", "weight": 0.3, "description": "Adding zeros"},
                    {"input": "[9,9,9,9,9,9,9], [9,9,9,9]", "expected_output": "[8,9,9,9,0,0,0,1]", "weight": 0.3, "description": "Multiple carries"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr) {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\npublic:\n    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {\n        // Your code here\n        return nullptr;\n    }\n};",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr) {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\npublic:\n    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {\n        ListNode* dummy = new ListNode(0);\n        ListNode* current = dummy;\n        int carry = 0;\n        \n        while (l1 || l2 || carry) {\n            int val1 = l1 ? l1->val : 0;\n            int val2 = l2 ? l2->val : 0;\n            \n            int total = val1 + val2 + carry;\n            carry = total / 10;\n            int digit = total % 10;\n            \n            current->next = new ListNode(digit);\n            current = current->next;\n            \n            l1 = l1 ? l1->next : nullptr;\n            l2 = l2 ? l2->next : nullptr;\n        }\n        \n        ListNode* result = dummy->next;\n        delete dummy;\n        return result;\n    }\n};",
                "testCases": [
                    {"input": "[2,4,3], [5,6,4]", "expected_output": "[7,0,8]", "weight": 0.4, "description": "Standard addition with carry"},
                    {"input": "[0], [0]", "expected_output": "[0]", "weight": 0.3, "description": "Adding zeros"},
                    {"input": "[9,9,9,9,9,9,9], [9,9,9,9]", "expected_output": "[8,9,9,9,0,0,0,1]", "weight": 0.3, "description": "Multiple carries"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(max(m, n))",
            "spaceComplexity": "O(max(m, n))",
            "constraints": ["The number of nodes in each linked list is in the range [1, 100]", "0 <= Node.val <= 9", "It is guaranteed that the list represents a number that does not have leading zeros"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 25,
            "tags": ["linked-list", "math", "recursion"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Linked Lists"
        }
    })

    # Linked Lists - Hard: Merge k Sorted Lists
    questions.append({
        "id": "merge-k-sorted-lists",
        "title": "Merge k Sorted Lists",
        "text": "You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.\n\nMerge all the linked-lists into one sorted linked-list and return it.\n\n**Example 1:**\nInput: lists = [[1,4,5],[1,3,4],[2,6]]\nOutput: [1,1,2,3,4,4,5,6]\nExplanation: The linked-lists are:\n[\n  1->4->5,\n  1->3->4,\n  2->6\n]\nmerging them into one sorted list:\n1->1->2->3->4->4->5->6\n\n**Example 2:**\nInput: lists = []\nOutput: []\n\n**Example 3:**\nInput: lists = [[]]\nOutput: []",
        "implementations": [
            {
                "language": "python",
                "starterCode": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def mergeKLists(self, lists):\n        # Your code here\n        pass",
                "solutionCode": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def mergeKLists(self, lists):\n        if not lists:\n            return None\n        \n        def mergeTwoLists(l1, l2):\n            dummy = ListNode(0)\n            current = dummy\n            \n            while l1 and l2:\n                if l1.val <= l2.val:\n                    current.next = l1\n                    l1 = l1.next\n                else:\n                    current.next = l2\n                    l2 = l2.next\n                current = current.next\n            \n            current.next = l1 or l2\n            return dummy.next\n        \n        while len(lists) > 1:\n            merged_lists = []\n            for i in range(0, len(lists), 2):\n                l1 = lists[i]\n                l2 = lists[i + 1] if i + 1 < len(lists) else None\n                merged_lists.append(mergeTwoLists(l1, l2))\n            lists = merged_lists\n        \n        return lists[0]",
                "testCases": [
                    {"input": "[[1,4,5],[1,3,4],[2,6]]", "expected_output": "[1,1,2,3,4,4,5,6]", "weight": 0.5, "description": "Multiple sorted lists"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.25, "description": "Empty input"},
                    {"input": "[[]]", "expected_output": "[]", "weight": 0.25, "description": "Single empty list"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n/**\n * @param {ListNode[]} lists\n * @return {ListNode}\n */\nvar mergeKLists = function(lists) {\n    // Your code here\n};",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n/**\n * @param {ListNode[]} lists\n * @return {ListNode}\n */\nvar mergeKLists = function(lists) {\n    if (!lists || lists.length === 0) {\n        return null;\n    }\n    \n    function mergeTwoLists(l1, l2) {\n        const dummy = new ListNode(0);\n        let current = dummy;\n        \n        while (l1 && l2) {\n            if (l1.val <= l2.val) {\n                current.next = l1;\n                l1 = l1.next;\n            } else {\n                current.next = l2;\n                l2 = l2.next;\n            }\n            current = current.next;\n        }\n        \n        current.next = l1 || l2;\n        return dummy.next;\n    }\n    \n    while (lists.length > 1) {\n        const mergedLists = [];\n        for (let i = 0; i < lists.length; i += 2) {\n            const l1 = lists[i];\n            const l2 = i + 1 < lists.length ? lists[i + 1] : null;\n            mergedLists.push(mergeTwoLists(l1, l2));\n        }\n        lists = mergedLists;\n    }\n    \n    return lists[0];\n};",
                "testCases": [
                    {"input": "[[1,4,5],[1,3,4],[2,6]]", "expected_output": "[1,1,2,3,4,4,5,6]", "weight": 0.5, "description": "Multiple sorted lists"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.25, "description": "Empty input"},
                    {"input": "[[]]", "expected_output": "[]", "weight": 0.25, "description": "Single empty list"}
                ]
            },
            {
                "language": "java",
                "starterCode": "/**\n * Definition for singly-linked list.\n * public class ListNode {\n *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n * }\n */\nclass Solution {\n    public ListNode mergeKLists(ListNode[] lists) {\n        // Your code here\n        return null;\n    }\n}",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * public class ListNode {\n *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n * }\n */\nclass Solution {\n    public ListNode mergeKLists(ListNode[] lists) {\n        if (lists == null || lists.length == 0) {\n            return null;\n        }\n        \n        List<ListNode> listsList = new ArrayList<>(Arrays.asList(lists));\n        \n        while (listsList.size() > 1) {\n            List<ListNode> mergedLists = new ArrayList<>();\n            for (int i = 0; i < listsList.size(); i += 2) {\n                ListNode l1 = listsList.get(i);\n                ListNode l2 = i + 1 < listsList.size() ? listsList.get(i + 1) : null;\n                mergedLists.add(mergeTwoLists(l1, l2));\n            }\n            listsList = mergedLists;\n        }\n        \n        return listsList.get(0);\n    }\n    \n    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {\n        ListNode dummy = new ListNode(0);\n        ListNode current = dummy;\n        \n        while (l1 != null && l2 != null) {\n            if (l1.val <= l2.val) {\n                current.next = l1;\n                l1 = l1.next;\n            } else {\n                current.next = l2;\n                l2 = l2.next;\n            }\n            current = current.next;\n        }\n        \n        current.next = l1 != null ? l1 : l2;\n        return dummy.next;\n    }\n}",
                "testCases": [
                    {"input": "[[1,4,5],[1,3,4],[2,6]]", "expected_output": "[1,1,2,3,4,4,5,6]", "weight": 0.5, "description": "Multiple sorted lists"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.25, "description": "Empty input"},
                    {"input": "[[]]", "expected_output": "[]", "weight": 0.25, "description": "Single empty list"}
                ]
            },
            {
                "language": "go",
                "starterCode": "/**\n * Definition for singly-linked list.\n * type ListNode struct {\n *     Val int\n *     Next *ListNode\n * }\n */\nfunc mergeKLists(lists []*ListNode) *ListNode {\n    // Your code here\n    return nil\n}",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * type ListNode struct {\n *     Val int\n *     Next *ListNode\n * }\n */\nfunc mergeKLists(lists []*ListNode) *ListNode {\n    if len(lists) == 0 {\n        return nil\n    }\n    \n    for len(lists) > 1 {\n        var mergedLists []*ListNode\n        for i := 0; i < len(lists); i += 2 {\n            l1 := lists[i]\n            var l2 *ListNode\n            if i+1 < len(lists) {\n                l2 = lists[i+1]\n            }\n            mergedLists = append(mergedLists, mergeTwoLists(l1, l2))\n        }\n        lists = mergedLists\n    }\n    \n    return lists[0]\n}\n\nfunc mergeTwoLists(l1, l2 *ListNode) *ListNode {\n    dummy := &ListNode{}\n    current := dummy\n    \n    for l1 != nil && l2 != nil {\n        if l1.Val <= l2.Val {\n            current.Next = l1\n            l1 = l1.Next\n        } else {\n            current.Next = l2\n            l2 = l2.Next\n        }\n        current = current.Next\n    }\n    \n    if l1 != nil {\n        current.Next = l1\n    } else {\n        current.Next = l2\n    }\n    \n    return dummy.Next\n}",
                "testCases": [
                    {"input": "[[1,4,5],[1,3,4],[2,6]]", "expected_output": "[1,1,2,3,4,4,5,6]", "weight": 0.5, "description": "Multiple sorted lists"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.25, "description": "Empty input"},
                    {"input": "[[]]", "expected_output": "[]", "weight": 0.25, "description": "Single empty list"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# Definition for singly-linked list.\n# class ListNode\n#     attr_accessor :val, :next\n#     def initialize(val = 0, _next = nil)\n#         @val = val\n#         @next = _next\n#     end\n# end\n# @param {ListNode[]} lists\n# @return {ListNode}\ndef merge_k_lists(lists)\n    # Your code here\nend",
                "solutionCode": "# Definition for singly-linked list.\n# class ListNode\n#     attr_accessor :val, :next\n#     def initialize(val = 0, _next = nil)\n#         @val = val\n#         @next = _next\n#     end\n# end\n# @param {ListNode[]} lists\n# @return {ListNode}\ndef merge_k_lists(lists)\n    return nil if lists.empty?\n    \n    def merge_two_lists(l1, l2)\n        dummy = ListNode.new(0)\n        current = dummy\n        \n        while l1 && l2\n            if l1.val <= l2.val\n                current.next = l1\n                l1 = l1.next\n            else\n                current.next = l2\n                l2 = l2.next\n            end\n            current = current.next\n        end\n        \n        current.next = l1 || l2\n        dummy.next\n    end\n    \n    while lists.length > 1\n        merged_lists = []\n        (0...lists.length).step(2) do |i|\n            l1 = lists[i]\n            l2 = i + 1 < lists.length ? lists[i + 1] : nil\n            merged_lists << merge_two_lists(l1, l2)\n        end\n        lists = merged_lists\n    end\n    \n    lists[0]\nend",
                "testCases": [
                    {"input": "[[1,4,5],[1,3,4],[2,6]]", "expected_output": "[1,1,2,3,4,4,5,6]", "weight": 0.5, "description": "Multiple sorted lists"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.25, "description": "Empty input"},
                    {"input": "[[]]", "expected_output": "[]", "weight": 0.25, "description": "Single empty list"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr) {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\npublic:\n    ListNode* mergeKLists(vector<ListNode*>& lists) {\n        // Your code here\n        return nullptr;\n    }\n};",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr) {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\npublic:\n    ListNode* mergeKLists(vector<ListNode*>& lists) {\n        if (lists.empty()) {\n            return nullptr;\n        }\n        \n        while (lists.size() > 1) {\n            vector<ListNode*> mergedLists;\n            for (int i = 0; i < lists.size(); i += 2) {\n                ListNode* l1 = lists[i];\n                ListNode* l2 = i + 1 < lists.size() ? lists[i + 1] : nullptr;\n                mergedLists.push_back(mergeTwoLists(l1, l2));\n            }\n            lists = mergedLists;\n        }\n        \n        return lists[0];\n    }\n    \nprivate:\n    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {\n        ListNode* dummy = new ListNode(0);\n        ListNode* current = dummy;\n        \n        while (l1 && l2) {\n            if (l1->val <= l2->val) {\n                current->next = l1;\n                l1 = l1->next;\n            } else {\n                current->next = l2;\n                l2 = l2->next;\n            }\n            current = current->next;\n        }\n        \n        current->next = l1 ? l1 : l2;\n        ListNode* result = dummy->next;\n        delete dummy;\n        return result;\n    }\n};",
                "testCases": [
                    {"input": "[[1,4,5],[1,3,4],[2,6]]", "expected_output": "[1,1,2,3,4,4,5,6]", "weight": 0.5, "description": "Multiple sorted lists"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.25, "description": "Empty input"},
                    {"input": "[[]]", "expected_output": "[]", "weight": 0.25, "description": "Single empty list"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n log k)",
            "spaceComplexity": "O(1)",
            "constraints": ["k == lists.length", "0 <= k <= 10^4", "0 <= lists[i].length <= 500", "-10^4 <= lists[i][j] <= 10^4", "lists[i] is sorted in ascending order", "The sum of lists[i].length will not exceed 10^4"]
        },
        "gradingRules": {
            "testCaseWeight": 0.5,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.3,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "HARD",
            "estimatedDuration": 35,
            "tags": ["linked-list", "divide-and-conquer", "heap", "merge-sort"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn", "Uber"],
            "topic": "Linked Lists"
        }
    })

    # Trees & Graphs - Medium: Validate Binary Search Tree
    questions.append({
        "id": "validate-binary-search-tree",
        "title": "Validate Binary Search Tree",
        "text": "Given the root of a binary tree, determine if it is a valid binary search tree (BST).\n\nA valid BST is defined as follows:\n- The left subtree of a node contains only nodes with keys less than the node's key.\n- The right subtree of a node contains only nodes with keys greater than the node's key.\n- Both the left and right subtrees must also be binary search trees.\n\n**Example 1:**\nInput: root = [2,1,3]\nOutput: true\n\n**Example 2:**\nInput: root = [5,1,4,null,null,3,6]\nOutput: false\nExplanation: The root node's value is 5 but its right child's value is 4.",
        "implementations": [
            {
                "language": "python",
                "starterCode": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def isValidBST(self, root):\n        # Your code here\n        pass",
                "solutionCode": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def isValidBST(self, root):\n        def validate(node, min_val, max_val):\n            if not node:\n                return True\n            \n            if node.val <= min_val or node.val >= max_val:\n                return False\n            \n            return (validate(node.left, min_val, node.val) and \n                    validate(node.right, node.val, max_val))\n        \n        return validate(root, float('-inf'), float('inf'))",
                "testCases": [
                    {"input": "[2,1,3]", "expected_output": "True", "weight": 0.4, "description": "Valid BST"},
                    {"input": "[5,1,4,null,null,3,6]", "expected_output": "False", "weight": 0.4, "description": "Invalid BST"},
                    {"input": "[1]", "expected_output": "True", "weight": 0.2, "description": "Single node"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * Definition for a binary tree node.\n * function TreeNode(val, left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left = (left===undefined ? null : left)\n *     this.right = (right===undefined ? null : right)\n * }\n */\n/**\n * @param {TreeNode} root\n * @return {boolean}\n */\nvar isValidBST = function(root) {\n    // Your code here\n};",
                "solutionCode": "/**\n * Definition for a binary tree node.\n * function TreeNode(val, left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left = (left===undefined ? null : left)\n *     this.right = (right===undefined ? null : right)\n * }\n */\n/**\n * @param {TreeNode} root\n * @return {boolean}\n */\nvar isValidBST = function(root) {\n    function validate(node, minVal, maxVal) {\n        if (!node) {\n            return true;\n        }\n        \n        if (node.val <= minVal || node.val >= maxVal) {\n            return false;\n        }\n        \n        return validate(node.left, minVal, node.val) && \n               validate(node.right, node.val, maxVal);\n    }\n    \n    return validate(root, -Infinity, Infinity);\n};",
                "testCases": [
                    {"input": "[2,1,3]", "expected_output": "true", "weight": 0.4, "description": "Valid BST"},
                    {"input": "[5,1,4,null,null,3,6]", "expected_output": "false", "weight": 0.4, "description": "Invalid BST"},
                    {"input": "[1]", "expected_output": "true", "weight": 0.2, "description": "Single node"}
                ]
            },
            {
                "language": "java",
                "starterCode": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode() {}\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val, TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left = left;\n *         this.right = right;\n *     }\n * }\n */\nclass Solution {\n    public boolean isValidBST(TreeNode root) {\n        // Your code here\n        return false;\n    }\n}",
                "solutionCode": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode() {}\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val, TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left = left;\n *         this.right = right;\n *     }\n * }\n */\nclass Solution {\n    public boolean isValidBST(TreeNode root) {\n        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);\n    }\n    \n    private boolean validate(TreeNode node, long minVal, long maxVal) {\n        if (node == null) {\n            return true;\n        }\n        \n        if (node.val <= minVal || node.val >= maxVal) {\n            return false;\n        }\n        \n        return validate(node.left, minVal, node.val) && \n               validate(node.right, node.val, maxVal);\n    }\n}",
                "testCases": [
                    {"input": "[2,1,3]", "expected_output": "true", "weight": 0.4, "description": "Valid BST"},
                    {"input": "[5,1,4,null,null,3,6]", "expected_output": "false", "weight": 0.4, "description": "Invalid BST"},
                    {"input": "[1]", "expected_output": "true", "weight": 0.2, "description": "Single node"}
                ]
            },
            {
                "language": "go",
                "starterCode": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc isValidBST(root *TreeNode) bool {\n    // Your code here\n    return false\n}",
                "solutionCode": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc isValidBST(root *TreeNode) bool {\n    return validate(root, math.MinInt64, math.MaxInt64)\n}\n\nfunc validate(node *TreeNode, minVal, maxVal int) bool {\n    if node == nil {\n        return true\n    }\n    \n    if node.Val <= minVal || node.Val >= maxVal {\n        return false\n    }\n    \n    return validate(node.Left, minVal, node.Val) && \n           validate(node.Right, node.Val, maxVal)\n}",
                "testCases": [
                    {"input": "[2,1,3]", "expected_output": "true", "weight": 0.4, "description": "Valid BST"},
                    {"input": "[5,1,4,null,null,3,6]", "expected_output": "false", "weight": 0.4, "description": "Invalid BST"},
                    {"input": "[1]", "expected_output": "true", "weight": 0.2, "description": "Single node"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# Definition for a binary tree node.\n# class TreeNode\n#     attr_accessor :val, :left, :right\n#     def initialize(val = 0, left = nil, right = nil)\n#         @val = val\n#         @left = left\n#         @right = right\n#     end\n# end\n# @param {TreeNode} root\n# @return {Boolean}\ndef is_valid_bst(root)\n    # Your code here\nend",
                "solutionCode": "# Definition for a binary tree node.\n# class TreeNode\n#     attr_accessor :val, :left, :right\n#     def initialize(val = 0, left = nil, right = nil)\n#         @val = val\n#         @left = left\n#         @right = right\n#     end\n# end\n# @param {TreeNode} root\n# @return {Boolean}\ndef is_valid_bst(root)\n    def validate(node, min_val, max_val)\n        return true if node.nil?\n        \n        return false if node.val <= min_val || node.val >= max_val\n        \n        validate(node.left, min_val, node.val) && \n        validate(node.right, node.val, max_val)\n    end\n    \n    validate(root, -Float::INFINITY, Float::INFINITY)\nend",
                "testCases": [
                    {"input": "[2,1,3]", "expected_output": "true", "weight": 0.4, "description": "Valid BST"},
                    {"input": "[5,1,4,null,null,3,6]", "expected_output": "false", "weight": 0.4, "description": "Invalid BST"},
                    {"input": "[1]", "expected_output": "true", "weight": 0.2, "description": "Single node"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution {\npublic:\n    bool isValidBST(TreeNode* root) {\n        // Your code here\n        return false;\n    }\n};",
                "solutionCode": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution {\npublic:\n    bool isValidBST(TreeNode* root) {\n        return validate(root, LLONG_MIN, LLONG_MAX);\n    }\n    \nprivate:\n    bool validate(TreeNode* node, long long minVal, long long maxVal) {\n        if (!node) {\n            return true;\n        }\n        \n        if (node->val <= minVal || node->val >= maxVal) {\n            return false;\n        }\n        \n        return validate(node->left, minVal, node->val) && \n               validate(node->right, node->val, maxVal);\n    }\n};",
                "testCases": [
                    {"input": "[2,1,3]", "expected_output": "true", "weight": 0.4, "description": "Valid BST"},
                    {"input": "[5,1,4,null,null,3,6]", "expected_output": "false", "weight": 0.4, "description": "Invalid BST"},
                    {"input": "[1]", "expected_output": "true", "weight": 0.2, "description": "Single node"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(h)",
            "constraints": ["The number of nodes in the tree is in the range [1, 10^4]", "-2^31 <= Node.val <= 2^31 - 1"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 25,
            "tags": ["tree", "depth-first-search", "binary-search-tree", "binary-tree"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Trees & Graphs"
        }
    })

    # Dynamic Programming - Medium: Coin Change
    questions.append({
        "id": "coin-change",
        "title": "Coin Change",
        "text": "You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.\n\nReturn the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.\n\nYou may assume that you have an infinite number of each kind of coin.\n\n**Example 1:**\nInput: coins = [1,3,4], amount = 6\nOutput: 2\nExplanation: 6 = 3 + 3\n\n**Example 2:**\nInput: coins = [2], amount = 3\nOutput: -1\n\n**Example 3:**\nInput: coins = [1], amount = 0\nOutput: 0",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def coinChange(self, coins, amount):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def coinChange(self, coins, amount):\n        # dp[i] represents the minimum coins needed for amount i\n        dp = [float('inf')] * (amount + 1)\n        dp[0] = 0\n        \n        for i in range(1, amount + 1):\n            for coin in coins:\n                if coin <= i:\n                    dp[i] = min(dp[i], dp[i - coin] + 1)\n        \n        return dp[amount] if dp[amount] != float('inf') else -1",
                "testCases": [
                    {"input": "[1,3,4], 6", "expected_output": "2", "weight": 0.4, "description": "Standard case"},
                    {"input": "[2], 3", "expected_output": "-1", "weight": 0.3, "description": "Impossible case"},
                    {"input": "[1], 0", "expected_output": "0", "weight": 0.3, "description": "Zero amount"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[]} coins\n * @param {number} amount\n * @return {number}\n */\nvar coinChange = function(coins, amount) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[]} coins\n * @param {number} amount\n * @return {number}\n */\nvar coinChange = function(coins, amount) {\n    const dp = new Array(amount + 1).fill(Infinity);\n    dp[0] = 0;\n    \n    for (let i = 1; i <= amount; i++) {\n        for (const coin of coins) {\n            if (coin <= i) {\n                dp[i] = Math.min(dp[i], dp[i - coin] + 1);\n            }\n        }\n    }\n    \n    return dp[amount] === Infinity ? -1 : dp[amount];\n};",
                "testCases": [
                    {"input": "[1,3,4], 6", "expected_output": "2", "weight": 0.4, "description": "Standard case"},
                    {"input": "[2], 3", "expected_output": "-1", "weight": 0.3, "description": "Impossible case"},
                    {"input": "[1], 0", "expected_output": "0", "weight": 0.3, "description": "Zero amount"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int coinChange(int[] coins, int amount) {\n        // Your code here\n        return 0;\n    }\n}",
                "solutionCode": "class Solution {\n    public int coinChange(int[] coins, int amount) {\n        int[] dp = new int[amount + 1];\n        Arrays.fill(dp, Integer.MAX_VALUE);\n        dp[0] = 0;\n        \n        for (int i = 1; i <= amount; i++) {\n            for (int coin : coins) {\n                if (coin <= i && dp[i - coin] != Integer.MAX_VALUE) {\n                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);\n                }\n            }\n        }\n        \n        return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];\n    }\n}",
                "testCases": [
                    {"input": "[1,3,4], 6", "expected_output": "2", "weight": 0.4, "description": "Standard case"},
                    {"input": "[2], 3", "expected_output": "-1", "weight": 0.3, "description": "Impossible case"},
                    {"input": "[1], 0", "expected_output": "0", "weight": 0.3, "description": "Zero amount"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func coinChange(coins []int, amount int) int {\n    // Your code here\n    return 0\n}",
                "solutionCode": "func coinChange(coins []int, amount int) int {\n    dp := make([]int, amount+1)\n    for i := 1; i <= amount; i++ {\n        dp[i] = amount + 1 // Initialize with impossible value\n    }\n    \n    for i := 1; i <= amount; i++ {\n        for _, coin := range coins {\n            if coin <= i {\n                if dp[i-coin]+1 < dp[i] {\n                    dp[i] = dp[i-coin] + 1\n                }\n            }\n        }\n    }\n    \n    if dp[amount] > amount {\n        return -1\n    }\n    return dp[amount]\n}",
                "testCases": [
                    {"input": "[1,3,4], 6", "expected_output": "2", "weight": 0.4, "description": "Standard case"},
                    {"input": "[2], 3", "expected_output": "-1", "weight": 0.3, "description": "Impossible case"},
                    {"input": "[1], 0", "expected_output": "0", "weight": 0.3, "description": "Zero amount"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[]} coins\n# @param {Integer} amount\n# @return {Integer}\ndef coin_change(coins, amount)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[]} coins\n# @param {Integer} amount\n# @return {Integer}\ndef coin_change(coins, amount)\n    dp = Array.new(amount + 1, Float::INFINITY)\n    dp[0] = 0\n    \n    (1..amount).each do |i|\n        coins.each do |coin|\n            if coin <= i\n                dp[i] = [dp[i], dp[i - coin] + 1].min\n            end\n        end\n    end\n    \n    dp[amount] == Float::INFINITY ? -1 : dp[amount]\nend",
                "testCases": [
                    {"input": "[1,3,4], 6", "expected_output": "2", "weight": 0.4, "description": "Standard case"},
                    {"input": "[2], 3", "expected_output": "-1", "weight": 0.3, "description": "Impossible case"},
                    {"input": "[1], 0", "expected_output": "0", "weight": 0.3, "description": "Zero amount"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    int coinChange(vector<int>& coins, int amount) {\n        // Your code here\n        return 0;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    int coinChange(vector<int>& coins, int amount) {\n        vector<int> dp(amount + 1, INT_MAX);\n        dp[0] = 0;\n        \n        for (int i = 1; i <= amount; i++) {\n            for (int coin : coins) {\n                if (coin <= i && dp[i - coin] != INT_MAX) {\n                    dp[i] = min(dp[i], dp[i - coin] + 1);\n                }\n            }\n        }\n        \n        return dp[amount] == INT_MAX ? -1 : dp[amount];\n    }\n};",
                "testCases": [
                    {"input": "[1,3,4], 6", "expected_output": "2", "weight": 0.4, "description": "Standard case"},
                    {"input": "[2], 3", "expected_output": "-1", "weight": 0.3, "description": "Impossible case"},
                    {"input": "[1], 0", "expected_output": "0", "weight": 0.3, "description": "Zero amount"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(amount * coins.length)",
            "spaceComplexity": "O(amount)",
            "constraints": ["1 <= coins.length <= 12", "1 <= coins[i] <= 2^31 - 1", "0 <= amount <= 10^4"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 25,
            "tags": ["array", "dynamic-programming"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Dynamic Programming"
        }
    })

    # Hash Tables - Easy: Valid Anagram
    questions.append({
        "id": "valid-anagram",
        "title": "Valid Anagram",
        "text": "Given two strings s and t, return true if t is an anagram of s, and false otherwise.\n\nAn Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.\n\n**Example 1:**\nInput: s = \"anagram\", t = \"nagaram\"\nOutput: true\n\n**Example 2:**\nInput: s = \"rat\", t = \"car\"\nOutput: false",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def isAnagram(self, s, t):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def isAnagram(self, s, t):\n        if len(s) != len(t):\n            return False\n        \n        char_count = {}\n        \n        # Count characters in s\n        for char in s:\n            char_count[char] = char_count.get(char, 0) + 1\n        \n        # Subtract characters in t\n        for char in t:\n            if char not in char_count:\n                return False\n            char_count[char] -= 1\n            if char_count[char] == 0:\n                del char_count[char]\n        \n        return len(char_count) == 0",
                "testCases": [
                    {"input": "\"anagram\", \"nagaram\"", "expected_output": "True", "weight": 0.5, "description": "Valid anagram"},
                    {"input": "\"rat\", \"car\"", "expected_output": "False", "weight": 0.5, "description": "Not an anagram"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {string} s\n * @param {string} t\n * @return {boolean}\n */\nvar isAnagram = function(s, t) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {string} s\n * @param {string} t\n * @return {boolean}\n */\nvar isAnagram = function(s, t) {\n    if (s.length !== t.length) {\n        return false;\n    }\n    \n    const charCount = {};\n    \n    // Count characters in s\n    for (const char of s) {\n        charCount[char] = (charCount[char] || 0) + 1;\n    }\n    \n    // Subtract characters in t\n    for (const char of t) {\n        if (!charCount[char]) {\n            return false;\n        }\n        charCount[char]--;\n    }\n    \n    return Object.values(charCount).every(count => count === 0);\n};",
                "testCases": [
                    {"input": "\"anagram\", \"nagaram\"", "expected_output": "true", "weight": 0.5, "description": "Valid anagram"},
                    {"input": "\"rat\", \"car\"", "expected_output": "false", "weight": 0.5, "description": "Not an anagram"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public boolean isAnagram(String s, String t) {\n        // Your code here\n        return false;\n    }\n}",
                "solutionCode": "class Solution {\n    public boolean isAnagram(String s, String t) {\n        if (s.length() != t.length()) {\n            return false;\n        }\n        \n        Map<Character, Integer> charCount = new HashMap<>();\n        \n        // Count characters in s\n        for (char c : s.toCharArray()) {\n            charCount.put(c, charCount.getOrDefault(c, 0) + 1);\n        }\n        \n        // Subtract characters in t\n        for (char c : t.toCharArray()) {\n            if (!charCount.containsKey(c)) {\n                return false;\n            }\n            charCount.put(c, charCount.get(c) - 1);\n            if (charCount.get(c) == 0) {\n                charCount.remove(c);\n            }\n        }\n        \n        return charCount.isEmpty();\n    }\n}",
                "testCases": [
                    {"input": "\"anagram\", \"nagaram\"", "expected_output": "true", "weight": 0.5, "description": "Valid anagram"},
                    {"input": "\"rat\", \"car\"", "expected_output": "false", "weight": 0.5, "description": "Not an anagram"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func isAnagram(s string, t string) bool {\n    // Your code here\n    return false\n}",
                "solutionCode": "func isAnagram(s string, t string) bool {\n    if len(s) != len(t) {\n        return false\n    }\n    \n    charCount := make(map[rune]int)\n    \n    // Count characters in s\n    for _, char := range s {\n        charCount[char]++\n    }\n    \n    // Subtract characters in t\n    for _, char := range t {\n        if charCount[char] == 0 {\n            return false\n        }\n        charCount[char]--\n    }\n    \n    // Check if all counts are zero\n    for _, count := range charCount {\n        if count != 0 {\n            return false\n        }\n    }\n    \n    return true\n}",
                "testCases": [
                    {"input": "\"anagram\", \"nagaram\"", "expected_output": "true", "weight": 0.5, "description": "Valid anagram"},
                    {"input": "\"rat\", \"car\"", "expected_output": "false", "weight": 0.5, "description": "Not an anagram"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {String} s\n# @param {String} t\n# @return {Boolean}\ndef is_anagram(s, t)\n    # Your code here\nend",
                "solutionCode": "# @param {String} s\n# @param {String} t\n# @return {Boolean}\ndef is_anagram(s, t)\n    return false if s.length != t.length\n    \n    char_count = Hash.new(0)\n    \n    # Count characters in s\n    s.each_char { |char| char_count[char] += 1 }\n    \n    # Subtract characters in t\n    t.each_char do |char|\n        return false if char_count[char] == 0\n        char_count[char] -= 1\n    end\n    \n    char_count.values.all?(&:zero?)\nend",
                "testCases": [
                    {"input": "\"anagram\", \"nagaram\"", "expected_output": "true", "weight": 0.5, "description": "Valid anagram"},
                    {"input": "\"rat\", \"car\"", "expected_output": "false", "weight": 0.5, "description": "Not an anagram"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    bool isAnagram(string s, string t) {\n        // Your code here\n        return false;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    bool isAnagram(string s, string t) {\n        if (s.length() != t.length()) {\n            return false;\n        }\n        \n        unordered_map<char, int> charCount;\n        \n        // Count characters in s\n        for (char c : s) {\n            charCount[c]++;\n        }\n        \n        // Subtract characters in t\n        for (char c : t) {\n            if (charCount[c] == 0) {\n                return false;\n            }\n            charCount[c]--;\n        }\n        \n        // Check if all counts are zero\n        for (const auto& pair : charCount) {\n            if (pair.second != 0) {\n                return false;\n            }\n        }\n        \n        return true;\n    }\n};",
                "testCases": [
                    {"input": "\"anagram\", \"nagaram\"", "expected_output": "true", "weight": 0.5, "description": "Valid anagram"},
                    {"input": "\"rat\", \"car\"", "expected_output": "false", "weight": 0.5, "description": "Not an anagram"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(1)",
            "constraints": ["1 <= s.length, t.length <= 5 * 10^4", "s and t consist of lowercase English letters"]
        },
        "gradingRules": {
            "testCaseWeight": 0.7,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "EASY",
            "estimatedDuration": 15,
            "tags": ["hash-table", "string", "sorting"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Hash Tables"
        }
    })

    # Two Pointers - Easy: Container With Most Water
    questions.append({
        "id": "container-with-most-water",
        "title": "Container With Most Water",
        "text": "You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).\n\nFind two lines that together with the x-axis form a container that can hold the most water.\n\nReturn the maximum amount of water a container can store.\n\nNotice that you may not slant the container.\n\n**Example 1:**\nInput: height = [1,8,6,2,5,4,8,3,7]\nOutput: 49\nExplanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.\n\n**Example 2:**\nInput: height = [1,1]\nOutput: 1",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def maxArea(self, height):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def maxArea(self, height):\n        left, right = 0, len(height) - 1\n        max_area = 0\n        \n        while left < right:\n            # Calculate current area\n            width = right - left\n            current_height = min(height[left], height[right])\n            current_area = width * current_height\n            max_area = max(max_area, current_area)\n            \n            # Move the pointer with smaller height\n            if height[left] < height[right]:\n                left += 1\n            else:\n                right -= 1\n        \n        return max_area",
                "testCases": [
                    {"input": "[1,8,6,2,5,4,8,3,7]", "expected_output": "49", "weight": 0.6, "description": "Standard case"},
                    {"input": "[1,1]", "expected_output": "1", "weight": 0.4, "description": "Minimum case"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[]} height\n * @return {number}\n */\nvar maxArea = function(height) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[]} height\n * @return {number}\n */\nvar maxArea = function(height) {\n    let left = 0, right = height.length - 1;\n    let maxArea = 0;\n    \n    while (left < right) {\n        const width = right - left;\n        const currentHeight = Math.min(height[left], height[right]);\n        const currentArea = width * currentHeight;\n        maxArea = Math.max(maxArea, currentArea);\n        \n        if (height[left] < height[right]) {\n            left++;\n        } else {\n            right--;\n        }\n    }\n    \n    return maxArea;\n};",
                "testCases": [
                    {"input": "[1,8,6,2,5,4,8,3,7]", "expected_output": "49", "weight": 0.6, "description": "Standard case"},
                    {"input": "[1,1]", "expected_output": "1", "weight": 0.4, "description": "Minimum case"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int maxArea(int[] height) {\n        // Your code here\n        return 0;\n    }\n}",
                "solutionCode": "class Solution {\n    public int maxArea(int[] height) {\n        int left = 0, right = height.length - 1;\n        int maxArea = 0;\n        \n        while (left < right) {\n            int width = right - left;\n            int currentHeight = Math.min(height[left], height[right]);\n            int currentArea = width * currentHeight;\n            maxArea = Math.max(maxArea, currentArea);\n            \n            if (height[left] < height[right]) {\n                left++;\n            } else {\n                right--;\n            }\n        }\n        \n        return maxArea;\n    }\n}",
                "testCases": [
                    {"input": "[1,8,6,2,5,4,8,3,7]", "expected_output": "49", "weight": 0.6, "description": "Standard case"},
                    {"input": "[1,1]", "expected_output": "1", "weight": 0.4, "description": "Minimum case"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func maxArea(height []int) int {\n    // Your code here\n    return 0\n}",
                "solutionCode": "func maxArea(height []int) int {\n    left, right := 0, len(height)-1\n    maxArea := 0\n    \n    for left < right {\n        width := right - left\n        currentHeight := height[left]\n        if height[right] < currentHeight {\n            currentHeight = height[right]\n        }\n        currentArea := width * currentHeight\n        if currentArea > maxArea {\n            maxArea = currentArea\n        }\n        \n        if height[left] < height[right] {\n            left++\n        } else {\n            right--\n        }\n    }\n    \n    return maxArea\n}",
                "testCases": [
                    {"input": "[1,8,6,2,5,4,8,3,7]", "expected_output": "49", "weight": 0.6, "description": "Standard case"},
                    {"input": "[1,1]", "expected_output": "1", "weight": 0.4, "description": "Minimum case"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[]} height\n# @return {Integer}\ndef max_area(height)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[]} height\n# @return {Integer}\ndef max_area(height)\n    left, right = 0, height.length - 1\n    max_area = 0\n    \n    while left < right\n        width = right - left\n        current_height = [height[left], height[right]].min\n        current_area = width * current_height\n        max_area = [max_area, current_area].max\n        \n        if height[left] < height[right]\n            left += 1\n        else\n            right -= 1\n        end\n    end\n    \n    max_area\nend",
                "testCases": [
                    {"input": "[1,8,6,2,5,4,8,3,7]", "expected_output": "49", "weight": 0.6, "description": "Standard case"},
                    {"input": "[1,1]", "expected_output": "1", "weight": 0.4, "description": "Minimum case"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    int maxArea(vector<int>& height) {\n        // Your code here\n        return 0;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    int maxArea(vector<int>& height) {\n        int left = 0, right = height.size() - 1;\n        int maxArea = 0;\n        \n        while (left < right) {\n            int width = right - left;\n            int currentHeight = min(height[left], height[right]);\n            int currentArea = width * currentHeight;\n            maxArea = max(maxArea, currentArea);\n            \n            if (height[left] < height[right]) {\n                left++;\n            } else {\n                right--;\n            }\n        }\n        \n        return maxArea;\n    }\n};",
                "testCases": [
                    {"input": "[1,8,6,2,5,4,8,3,7]", "expected_output": "49", "weight": 0.6, "description": "Standard case"},
                    {"input": "[1,1]", "expected_output": "1", "weight": 0.4, "description": "Minimum case"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(1)",
            "constraints": ["n == height.length", "2 <= n <= 10^5", "0 <= height[i] <= 10^4"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 20,
            "tags": ["array", "two-pointers", "greedy"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Two Pointers"
        }
    })

    # Recursion & Backtracking - Easy: Generate Parentheses
    questions.append({
        "id": "generate-parentheses",
        "title": "Generate Parentheses",
        "text": "Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.\n\n**Example 1:**\nInput: n = 3\nOutput: [\"((()))\",\"(()())\",\"(())()\",\"()(())\",\"()()()\"]\n\n**Example 2:**\nInput: n = 1\nOutput: [\"()\"]",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def generateParenthesis(self, n):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def generateParenthesis(self, n):\n        result = []\n        \n        def backtrack(current, open_count, close_count):\n            # Base case: we've used all n pairs\n            if len(current) == 2 * n:\n                result.append(current)\n                return\n            \n            # Add opening parenthesis if we haven't used all n\n            if open_count < n:\n                backtrack(current + '(', open_count + 1, close_count)\n            \n            # Add closing parenthesis if it won't make string invalid\n            if close_count < open_count:\n                backtrack(current + ')', open_count, close_count + 1)\n        \n        backtrack('', 0, 0)\n        return result",
                "testCases": [
                    {"input": "3", "expected_output": "[\"((()))\",\"(()())\",\"(())()\",\"()(())\",\"()()()\"]", "weight": 0.6, "description": "Standard case n=3"},
                    {"input": "1", "expected_output": "[\"()\"]", "weight": 0.4, "description": "Base case n=1"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number} n\n * @return {string[]}\n */\nvar generateParenthesis = function(n) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number} n\n * @return {string[]}\n */\nvar generateParenthesis = function(n) {\n    const result = [];\n    \n    function backtrack(current, openCount, closeCount) {\n        if (current.length === 2 * n) {\n            result.push(current);\n            return;\n        }\n        \n        if (openCount < n) {\n            backtrack(current + '(', openCount + 1, closeCount);\n        }\n        \n        if (closeCount < openCount) {\n            backtrack(current + ')', openCount, closeCount + 1);\n        }\n    }\n    \n    backtrack('', 0, 0);\n    return result;\n};",
                "testCases": [
                    {"input": "3", "expected_output": "[\"((()))\",\"(()())\",\"(())()\",\"()(())\",\"()()()\"]", "weight": 0.6, "description": "Standard case n=3"},
                    {"input": "1", "expected_output": "[\"()\"]", "weight": 0.4, "description": "Base case n=1"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public List<String> generateParenthesis(int n) {\n        // Your code here\n        return new ArrayList<>();\n    }\n}",
                "solutionCode": "class Solution {\n    public List<String> generateParenthesis(int n) {\n        List<String> result = new ArrayList<>();\n        backtrack(result, \"\", 0, 0, n);\n        return result;\n    }\n    \n    private void backtrack(List<String> result, String current, int openCount, int closeCount, int n) {\n        if (current.length() == 2 * n) {\n            result.add(current);\n            return;\n        }\n        \n        if (openCount < n) {\n            backtrack(result, current + \"(\", openCount + 1, closeCount, n);\n        }\n        \n        if (closeCount < openCount) {\n            backtrack(result, current + \")\", openCount, closeCount + 1, n);\n        }\n    }\n}",
                "testCases": [
                    {"input": "3", "expected_output": "[\"((()))\",\"(()())\",\"(())()\",\"()(())\",\"()()()\"]", "weight": 0.6, "description": "Standard case n=3"},
                    {"input": "1", "expected_output": "[\"()\"]", "weight": 0.4, "description": "Base case n=1"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func generateParenthesis(n int) []string {\n    // Your code here\n    return []string{}\n}",
                "solutionCode": "func generateParenthesis(n int) []string {\n    var result []string\n    \n    var backtrack func(current string, openCount, closeCount int)\n    backtrack = func(current string, openCount, closeCount int) {\n        if len(current) == 2*n {\n            result = append(result, current)\n            return\n        }\n        \n        if openCount < n {\n            backtrack(current+\"(\", openCount+1, closeCount)\n        }\n        \n        if closeCount < openCount {\n            backtrack(current+\")\", openCount, closeCount+1)\n        }\n    }\n    \n    backtrack(\"\", 0, 0)\n    return result\n}",
                "testCases": [
                    {"input": "3", "expected_output": "[\"((()))\",\"(()())\",\"(())()\",\"()(())\",\"()()()\"]", "weight": 0.6, "description": "Standard case n=3"},
                    {"input": "1", "expected_output": "[\"()\"]", "weight": 0.4, "description": "Base case n=1"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer} n\n# @return {String[]}\ndef generate_parenthesis(n)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer} n\n# @return {String[]}\ndef generate_parenthesis(n)\n    result = []\n    \n    def backtrack(current, open_count, close_count, n, result)\n        if current.length == 2 * n\n            result << current\n            return\n        end\n        \n        if open_count < n\n            backtrack(current + '(', open_count + 1, close_count, n, result)\n        end\n        \n        if close_count < open_count\n            backtrack(current + ')', open_count, close_count + 1, n, result)\n        end\n    end\n    \n    backtrack('', 0, 0, n, result)\n    result\nend",
                "testCases": [
                    {"input": "3", "expected_output": "[\"((()))\",\"(()())\",\"(())()\",\"()(())\",\"()()()\"]", "weight": 0.6, "description": "Standard case n=3"},
                    {"input": "1", "expected_output": "[\"()\"]", "weight": 0.4, "description": "Base case n=1"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    vector<string> generateParenthesis(int n) {\n        // Your code here\n        return {};\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    vector<string> generateParenthesis(int n) {\n        vector<string> result;\n        backtrack(result, \"\", 0, 0, n);\n        return result;\n    }\n    \nprivate:\n    void backtrack(vector<string>& result, string current, int openCount, int closeCount, int n) {\n        if (current.length() == 2 * n) {\n            result.push_back(current);\n            return;\n        }\n        \n        if (openCount < n) {\n            backtrack(result, current + \"(\", openCount + 1, closeCount, n);\n        }\n        \n        if (closeCount < openCount) {\n            backtrack(result, current + \")\", openCount, closeCount + 1, n);\n        }\n    }\n};",
                "testCases": [
                    {"input": "3", "expected_output": "[\"((()))\",\"(()())\",\"(())()\",\"()(())\",\"()()()\"]", "weight": 0.6, "description": "Standard case n=3"},
                    {"input": "1", "expected_output": "[\"()\"]", "weight": 0.4, "description": "Base case n=1"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(4^n / sqrt(n))",
            "spaceComplexity": "O(4^n / sqrt(n))",
            "constraints": ["1 <= n <= 8"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 25,
            "tags": ["string", "dynamic-programming", "backtracking"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Recursion & Backtracking"
        }
    })

    # Sliding Window - Easy: Longest Substring Without Repeating Characters
    questions.append({
        "id": "longest-substring-without-repeating-characters",
        "title": "Longest Substring Without Repeating Characters",
        "text": "Given a string s, find the length of the longest substring without repeating characters.\n\n**Example 1:**\nInput: s = \"abcabcbb\"\nOutput: 3\nExplanation: The answer is \"abc\", with the length of 3.\n\n**Example 2:**\nInput: s = \"bbbbb\"\nOutput: 1\nExplanation: The answer is \"b\", with the length of 1.\n\n**Example 3:**\nInput: s = \"pwwkew\"\nOutput: 3\nExplanation: The answer is \"wke\", with the length of 3.\nNotice that the answer must be a substring, \"pwke\" is a subsequence and not a substring.",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def lengthOfLongestSubstring(self, s):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def lengthOfLongestSubstring(self, s):\n        char_set = set()\n        left = 0\n        max_length = 0\n        \n        for right in range(len(s)):\n            # If character is already in set, shrink window from left\n            while s[right] in char_set:\n                char_set.remove(s[left])\n                left += 1\n            \n            # Add current character to set\n            char_set.add(s[right])\n            \n            # Update max length\n            max_length = max(max_length, right - left + 1)\n        \n        return max_length",
                "testCases": [
                    {"input": "\"abcabcbb\"", "expected_output": "3", "weight": 0.4, "description": "Standard case with repeating pattern"},
                    {"input": "\"bbbbb\"", "expected_output": "1", "weight": 0.3, "description": "All same characters"},
                    {"input": "\"pwwkew\"", "expected_output": "3", "weight": 0.3, "description": "Mixed pattern"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {string} s\n * @return {number}\n */\nvar lengthOfLongestSubstring = function(s) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {string} s\n * @return {number}\n */\nvar lengthOfLongestSubstring = function(s) {\n    const charSet = new Set();\n    let left = 0;\n    let maxLength = 0;\n    \n    for (let right = 0; right < s.length; right++) {\n        while (charSet.has(s[right])) {\n            charSet.delete(s[left]);\n            left++;\n        }\n        \n        charSet.add(s[right]);\n        maxLength = Math.max(maxLength, right - left + 1);\n    }\n    \n    return maxLength;\n};",
                "testCases": [
                    {"input": "\"abcabcbb\"", "expected_output": "3", "weight": 0.4, "description": "Standard case with repeating pattern"},
                    {"input": "\"bbbbb\"", "expected_output": "1", "weight": 0.3, "description": "All same characters"},
                    {"input": "\"pwwkew\"", "expected_output": "3", "weight": 0.3, "description": "Mixed pattern"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int lengthOfLongestSubstring(String s) {\n        // Your code here\n        return 0;\n    }\n}",
                "solutionCode": "class Solution {\n    public int lengthOfLongestSubstring(String s) {\n        Set<Character> charSet = new HashSet<>();\n        int left = 0;\n        int maxLength = 0;\n        \n        for (int right = 0; right < s.length(); right++) {\n            while (charSet.contains(s.charAt(right))) {\n                charSet.remove(s.charAt(left));\n                left++;\n            }\n            \n            charSet.add(s.charAt(right));\n            maxLength = Math.max(maxLength, right - left + 1);\n        }\n        \n        return maxLength;\n    }\n}",
                "testCases": [
                    {"input": "\"abcabcbb\"", "expected_output": "3", "weight": 0.4, "description": "Standard case with repeating pattern"},
                    {"input": "\"bbbbb\"", "expected_output": "1", "weight": 0.3, "description": "All same characters"},
                    {"input": "\"pwwkew\"", "expected_output": "3", "weight": 0.3, "description": "Mixed pattern"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func lengthOfLongestSubstring(s string) int {\n    // Your code here\n    return 0\n}",
                "solutionCode": "func lengthOfLongestSubstring(s string) int {\n    charSet := make(map[byte]bool)\n    left := 0\n    maxLength := 0\n    \n    for right := 0; right < len(s); right++ {\n        for charSet[s[right]] {\n            delete(charSet, s[left])\n            left++\n        }\n        \n        charSet[s[right]] = true\n        if right-left+1 > maxLength {\n            maxLength = right - left + 1\n        }\n    }\n    \n    return maxLength\n}",
                "testCases": [
                    {"input": "\"abcabcbb\"", "expected_output": "3", "weight": 0.4, "description": "Standard case with repeating pattern"},
                    {"input": "\"bbbbb\"", "expected_output": "1", "weight": 0.3, "description": "All same characters"},
                    {"input": "\"pwwkew\"", "expected_output": "3", "weight": 0.3, "description": "Mixed pattern"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {String} s\n# @return {Integer}\ndef length_of_longest_substring(s)\n    # Your code here\nend",
                "solutionCode": "# @param {String} s\n# @return {Integer}\ndef length_of_longest_substring(s)\n    char_set = Set.new\n    left = 0\n    max_length = 0\n    \n    (0...s.length).each do |right|\n        while char_set.include?(s[right])\n            char_set.delete(s[left])\n            left += 1\n        end\n        \n        char_set.add(s[right])\n        max_length = [max_length, right - left + 1].max\n    end\n    \n    max_length\nend",
                "testCases": [
                    {"input": "\"abcabcbb\"", "expected_output": "3", "weight": 0.4, "description": "Standard case with repeating pattern"},
                    {"input": "\"bbbbb\"", "expected_output": "1", "weight": 0.3, "description": "All same characters"},
                    {"input": "\"pwwkew\"", "expected_output": "3", "weight": 0.3, "description": "Mixed pattern"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    int lengthOfLongestSubstring(string s) {\n        // Your code here\n        return 0;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    int lengthOfLongestSubstring(string s) {\n        unordered_set<char> charSet;\n        int left = 0;\n        int maxLength = 0;\n        \n        for (int right = 0; right < s.length(); right++) {\n            while (charSet.find(s[right]) != charSet.end()) {\n                charSet.erase(s[left]);\n                left++;\n            }\n            \n            charSet.insert(s[right]);\n            maxLength = max(maxLength, right - left + 1);\n        }\n        \n        return maxLength;\n    }\n};",
                "testCases": [
                    {"input": "\"abcabcbb\"", "expected_output": "3", "weight": 0.4, "description": "Standard case with repeating pattern"},
                    {"input": "\"bbbbb\"", "expected_output": "1", "weight": 0.3, "description": "All same characters"},
                    {"input": "\"pwwkew\"", "expected_output": "3", "weight": 0.3, "description": "Mixed pattern"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(min(m, n))",
            "constraints": ["0 <= s.length <= 5 * 10^4", "s consists of English letters, digits, symbols and spaces"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 20,
            "tags": ["hash-table", "string", "sliding-window"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Sliding Window"
        }
    })

    # Sorting & Searching - Easy: Binary Search
    questions.append({
        "id": "binary-search",
        "title": "Binary Search",
        "text": "Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.\n\nYou must write an algorithm with O(log n) runtime complexity.\n\n**Example 1:**\nInput: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4\nExplanation: 9 exists in nums and its index is 4\n\n**Example 2:**\nInput: nums = [-1,0,3,5,9,12], target = 2\nOutput: -1\nExplanation: 2 does not exist in nums so return -1",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def search(self, nums, target):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def search(self, nums, target):\n        left, right = 0, len(nums) - 1\n        \n        while left <= right:\n            mid = left + (right - left) // 2\n            \n            if nums[mid] == target:\n                return mid\n            elif nums[mid] < target:\n                left = mid + 1\n            else:\n                right = mid - 1\n        \n        return -1",
                "testCases": [
                    {"input": "[-1,0,3,5,9,12], 9", "expected_output": "4", "weight": 0.5, "description": "Target exists"},
                    {"input": "[-1,0,3,5,9,12], 2", "expected_output": "-1", "weight": 0.5, "description": "Target doesn't exist"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[]} nums\n * @param {number} target\n * @return {number}\n */\nvar search = function(nums, target) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[]} nums\n * @param {number} target\n * @return {number}\n */\nvar search = function(nums, target) {\n    let left = 0, right = nums.length - 1;\n    \n    while (left <= right) {\n        const mid = left + Math.floor((right - left) / 2);\n        \n        if (nums[mid] === target) {\n            return mid;\n        } else if (nums[mid] < target) {\n            left = mid + 1;\n        } else {\n            right = mid - 1;\n        }\n    }\n    \n    return -1;\n};",
                "testCases": [
                    {"input": "[-1,0,3,5,9,12], 9", "expected_output": "4", "weight": 0.5, "description": "Target exists"},
                    {"input": "[-1,0,3,5,9,12], 2", "expected_output": "-1", "weight": 0.5, "description": "Target doesn't exist"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int search(int[] nums, int target) {\n        // Your code here\n        return -1;\n    }\n}",
                "solutionCode": "class Solution {\n    public int search(int[] nums, int target) {\n        int left = 0, right = nums.length - 1;\n        \n        while (left <= right) {\n            int mid = left + (right - left) / 2;\n            \n            if (nums[mid] == target) {\n                return mid;\n            } else if (nums[mid] < target) {\n                left = mid + 1;\n            } else {\n                right = mid - 1;\n            }\n        }\n        \n        return -1;\n    }\n}",
                "testCases": [
                    {"input": "[-1,0,3,5,9,12], 9", "expected_output": "4", "weight": 0.5, "description": "Target exists"},
                    {"input": "[-1,0,3,5,9,12], 2", "expected_output": "-1", "weight": 0.5, "description": "Target doesn't exist"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func search(nums []int, target int) int {\n    // Your code here\n    return -1\n}",
                "solutionCode": "func search(nums []int, target int) int {\n    left, right := 0, len(nums)-1\n    \n    for left <= right {\n        mid := left + (right-left)/2\n        \n        if nums[mid] == target {\n            return mid\n        } else if nums[mid] < target {\n            left = mid + 1\n        } else {\n            right = mid - 1\n        }\n    }\n    \n    return -1\n}",
                "testCases": [
                    {"input": "[-1,0,3,5,9,12], 9", "expected_output": "4", "weight": 0.5, "description": "Target exists"},
                    {"input": "[-1,0,3,5,9,12], 2", "expected_output": "-1", "weight": 0.5, "description": "Target doesn't exist"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[]} nums\n# @param {Integer} target\n# @return {Integer}\ndef search(nums, target)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[]} nums\n# @param {Integer} target\n# @return {Integer}\ndef search(nums, target)\n    left, right = 0, nums.length - 1\n    \n    while left <= right\n        mid = left + (right - left) / 2\n        \n        if nums[mid] == target\n            return mid\n        elsif nums[mid] < target\n            left = mid + 1\n        else\n            right = mid - 1\n        end\n    end\n    \n    -1\nend",
                "testCases": [
                    {"input": "[-1,0,3,5,9,12], 9", "expected_output": "4", "weight": 0.5, "description": "Target exists"},
                    {"input": "[-1,0,3,5,9,12], 2", "expected_output": "-1", "weight": 0.5, "description": "Target doesn't exist"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    int search(vector<int>& nums, int target) {\n        // Your code here\n        return -1;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    int search(vector<int>& nums, int target) {\n        int left = 0, right = nums.size() - 1;\n        \n        while (left <= right) {\n            int mid = left + (right - left) / 2;\n            \n            if (nums[mid] == target) {\n                return mid;\n            } else if (nums[mid] < target) {\n                left = mid + 1;\n            } else {\n                right = mid - 1;\n            }\n        }\n        \n        return -1;\n    }\n};",
                "testCases": [
                    {"input": "[-1,0,3,5,9,12], 9", "expected_output": "4", "weight": 0.5, "description": "Target exists"},
                    {"input": "[-1,0,3,5,9,12], 2", "expected_output": "-1", "weight": 0.5, "description": "Target doesn't exist"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(log n)",
            "spaceComplexity": "O(1)",
            "constraints": ["1 <= nums.length <= 10^4", "-10^4 < nums[i], target < 10^4", "All the integers in nums are unique", "nums is sorted in ascending order"]
        },
        "gradingRules": {
            "testCaseWeight": 0.7,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "EASY",
            "estimatedDuration": 15,
            "tags": ["array", "binary-search"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Sorting & Searching"
        }
    })

    # Bit Manipulation - Easy: Single Number
    questions.append({
        "id": "single-number",
        "title": "Single Number",
        "text": "Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.\n\nYou must implement a solution with a linear runtime complexity and use only constant extra space.\n\n**Example 1:**\nInput: nums = [2,2,1]\nOutput: 1\n\n**Example 2:**\nInput: nums = [4,1,2,1,2]\nOutput: 4\n\n**Example 3:**\nInput: nums = [1]\nOutput: 1",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def singleNumber(self, nums):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def singleNumber(self, nums):\n        result = 0\n        for num in nums:\n            result ^= num  # XOR operation\n        return result",
                "testCases": [
                    {"input": "[2,2,1]", "expected_output": "1", "weight": 0.4, "description": "Standard case"},
                    {"input": "[4,1,2,1,2]", "expected_output": "4", "weight": 0.4, "description": "Larger array"},
                    {"input": "[1]", "expected_output": "1", "weight": 0.2, "description": "Single element"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar singleNumber = function(nums) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar singleNumber = function(nums) {\n    let result = 0;\n    for (const num of nums) {\n        result ^= num;\n    }\n    return result;\n};",
                "testCases": [
                    {"input": "[2,2,1]", "expected_output": "1", "weight": 0.4, "description": "Standard case"},
                    {"input": "[4,1,2,1,2]", "expected_output": "4", "weight": 0.4, "description": "Larger array"},
                    {"input": "[1]", "expected_output": "1", "weight": 0.2, "description": "Single element"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int singleNumber(int[] nums) {\n        // Your code here\n        return 0;\n    }\n}",
                "solutionCode": "class Solution {\n    public int singleNumber(int[] nums) {\n        int result = 0;\n        for (int num : nums) {\n            result ^= num;\n        }\n        return result;\n    }\n}",
                "testCases": [
                    {"input": "[2,2,1]", "expected_output": "1", "weight": 0.4, "description": "Standard case"},
                    {"input": "[4,1,2,1,2]", "expected_output": "4", "weight": 0.4, "description": "Larger array"},
                    {"input": "[1]", "expected_output": "1", "weight": 0.2, "description": "Single element"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func singleNumber(nums []int) int {\n    // Your code here\n    return 0\n}",
                "solutionCode": "func singleNumber(nums []int) int {\n    result := 0\n    for _, num := range nums {\n        result ^= num\n    }\n    return result\n}",
                "testCases": [
                    {"input": "[2,2,1]", "expected_output": "1", "weight": 0.4, "description": "Standard case"},
                    {"input": "[4,1,2,1,2]", "expected_output": "4", "weight": 0.4, "description": "Larger array"},
                    {"input": "[1]", "expected_output": "1", "weight": 0.2, "description": "Single element"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[]} nums\n# @return {Integer}\ndef single_number(nums)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[]} nums\n# @return {Integer}\ndef single_number(nums)\n    result = 0\n    nums.each { |num| result ^= num }\n    result\nend",
                "testCases": [
                    {"input": "[2,2,1]", "expected_output": "1", "weight": 0.4, "description": "Standard case"},
                    {"input": "[4,1,2,1,2]", "expected_output": "4", "weight": 0.4, "description": "Larger array"},
                    {"input": "[1]", "expected_output": "1", "weight": 0.2, "description": "Single element"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    int singleNumber(vector<int>& nums) {\n        // Your code here\n        return 0;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    int singleNumber(vector<int>& nums) {\n        int result = 0;\n        for (int num : nums) {\n            result ^= num;\n        }\n        return result;\n    }\n};",
                "testCases": [
                    {"input": "[2,2,1]", "expected_output": "1", "weight": 0.4, "description": "Standard case"},
                    {"input": "[4,1,2,1,2]", "expected_output": "4", "weight": 0.4, "description": "Larger array"},
                    {"input": "[1]", "expected_output": "1", "weight": 0.2, "description": "Single element"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(1)",
            "constraints": ["1 <= nums.length <= 3 * 10^4", "-3 * 10^4 <= nums[i] <= 3 * 10^4", "Each element in the array appears twice except for one element which appears only once"]
        },
        "gradingRules": {
            "testCaseWeight": 0.7,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "EASY",
            "estimatedDuration": 15,
            "tags": ["array", "bit-manipulation"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Bit Manipulation"
        }
    })

    # Trees & Graphs - Medium: Binary Tree Level Order Traversal
    questions.append({
        "id": "binary-tree-level-order-traversal",
        "title": "Binary Tree Level Order Traversal",
        "text": "Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).\n\n**Example 1:**\nInput: root = [3,9,20,null,null,15,7]\nOutput: [[3],[9,20],[15,7]]\n\n**Example 2:**\nInput: root = [1]\nOutput: [[1]]\n\n**Example 3:**\nInput: root = []\nOutput: []",
        "implementations": [
            {
                "language": "python",
                "starterCode": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def levelOrder(self, root):\n        # Your code here\n        pass",
                "solutionCode": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def levelOrder(self, root):\n        if not root:\n            return []\n        \n        result = []\n        queue = [root]\n        \n        while queue:\n            level_size = len(queue)\n            level_values = []\n            \n            for _ in range(level_size):\n                node = queue.pop(0)\n                level_values.append(node.val)\n                \n                if node.left:\n                    queue.append(node.left)\n                if node.right:\n                    queue.append(node.right)\n            \n            result.append(level_values)\n        \n        return result",
                "testCases": [
                    {"input": "[3,9,20,null,null,15,7]", "expected_output": "[[3],[9,20],[15,7]]", "weight": 0.5, "description": "Standard tree"},
                    {"input": "[1]", "expected_output": "[[1]]", "weight": 0.25, "description": "Single node"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.25, "description": "Empty tree"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * Definition for a binary tree node.\n * function TreeNode(val, left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left = (left===undefined ? null : left)\n *     this.right = (right===undefined ? null : right)\n * }\n */\n/**\n * @param {TreeNode} root\n * @return {number[][]}\n */\nvar levelOrder = function(root) {\n    // Your code here\n};",
                "solutionCode": "/**\n * Definition for a binary tree node.\n * function TreeNode(val, left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left = (left===undefined ? null : left)\n *     this.right = (right===undefined ? null : right)\n * }\n */\n/**\n * @param {TreeNode} root\n * @return {number[][]}\n */\nvar levelOrder = function(root) {\n    if (!root) return [];\n    \n    const result = [];\n    const queue = [root];\n    \n    while (queue.length > 0) {\n        const levelSize = queue.length;\n        const levelValues = [];\n        \n        for (let i = 0; i < levelSize; i++) {\n            const node = queue.shift();\n            levelValues.push(node.val);\n            \n            if (node.left) queue.push(node.left);\n            if (node.right) queue.push(node.right);\n        }\n        \n        result.push(levelValues);\n    }\n    \n    return result;\n};",
                "testCases": [
                    {"input": "[3,9,20,null,null,15,7]", "expected_output": "[[3],[9,20],[15,7]]", "weight": 0.5, "description": "Standard tree"},
                    {"input": "[1]", "expected_output": "[[1]]", "weight": 0.25, "description": "Single node"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.25, "description": "Empty tree"}
                ]
            },
            {
                "language": "java",
                "starterCode": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode() {}\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val, TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left = left;\n *         this.right = right;\n *     }\n * }\n */\nclass Solution {\n    public List<List<Integer>> levelOrder(TreeNode root) {\n        // Your code here\n        return new ArrayList<>();\n    }\n}",
                "solutionCode": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode() {}\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val, TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left = left;\n *         this.right = right;\n *     }\n * }\n */\nclass Solution {\n    public List<List<Integer>> levelOrder(TreeNode root) {\n        List<List<Integer>> result = new ArrayList<>();\n        if (root == null) return result;\n        \n        Queue<TreeNode> queue = new LinkedList<>();\n        queue.offer(root);\n        \n        while (!queue.isEmpty()) {\n            int levelSize = queue.size();\n            List<Integer> levelValues = new ArrayList<>();\n            \n            for (int i = 0; i < levelSize; i++) {\n                TreeNode node = queue.poll();\n                levelValues.add(node.val);\n                \n                if (node.left != null) queue.offer(node.left);\n                if (node.right != null) queue.offer(node.right);\n            }\n            \n            result.add(levelValues);\n        }\n        \n        return result;\n    }\n}",
                "testCases": [
                    {"input": "[3,9,20,null,null,15,7]", "expected_output": "[[3],[9,20],[15,7]]", "weight": 0.5, "description": "Standard tree"},
                    {"input": "[1]", "expected_output": "[[1]]", "weight": 0.25, "description": "Single node"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.25, "description": "Empty tree"}
                ]
            },
            {
                "language": "go",
                "starterCode": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc levelOrder(root *TreeNode) [][]int {\n    // Your code here\n    return [][]int{}\n}",
                "solutionCode": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc levelOrder(root *TreeNode) [][]int {\n    if root == nil {\n        return [][]int{}\n    }\n    \n    var result [][]int\n    queue := []*TreeNode{root}\n    \n    for len(queue) > 0 {\n        levelSize := len(queue)\n        var levelValues []int\n        \n        for i := 0; i < levelSize; i++ {\n            node := queue[0]\n            queue = queue[1:]\n            levelValues = append(levelValues, node.Val)\n            \n            if node.Left != nil {\n                queue = append(queue, node.Left)\n            }\n            if node.Right != nil {\n                queue = append(queue, node.Right)\n            }\n        }\n        \n        result = append(result, levelValues)\n    }\n    \n    return result\n}",
                "testCases": [
                    {"input": "[3,9,20,null,null,15,7]", "expected_output": "[[3],[9,20],[15,7]]", "weight": 0.5, "description": "Standard tree"},
                    {"input": "[1]", "expected_output": "[[1]]", "weight": 0.25, "description": "Single node"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.25, "description": "Empty tree"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# Definition for a binary tree node.\n# class TreeNode\n#     attr_accessor :val, :left, :right\n#     def initialize(val = 0, left = nil, right = nil)\n#         @val = val\n#         @left = left\n#         @right = right\n#     end\n# end\n# @param {TreeNode} root\n# @return {Integer[][]}\ndef level_order(root)\n    # Your code here\nend",
                "solutionCode": "# Definition for a binary tree node.\n# class TreeNode\n#     attr_accessor :val, :left, :right\n#     def initialize(val = 0, left = nil, right = nil)\n#         @val = val\n#         @left = left\n#         @right = right\n#     end\n# end\n# @param {TreeNode} root\n# @return {Integer[][]}\ndef level_order(root)\n    return [] if root.nil?\n    \n    result = []\n    queue = [root]\n    \n    while !queue.empty?\n        level_size = queue.length\n        level_values = []\n        \n        level_size.times do\n            node = queue.shift\n            level_values << node.val\n            \n            queue << node.left if node.left\n            queue << node.right if node.right\n        end\n        \n        result << level_values\n    end\n    \n    result\nend",
                "testCases": [
                    {"input": "[3,9,20,null,null,15,7]", "expected_output": "[[3],[9,20],[15,7]]", "weight": 0.5, "description": "Standard tree"},
                    {"input": "[1]", "expected_output": "[[1]]", "weight": 0.25, "description": "Single node"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.25, "description": "Empty tree"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution {\npublic:\n    vector<vector<int>> levelOrder(TreeNode* root) {\n        // Your code here\n        return {};\n    }\n};",
                "solutionCode": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution {\npublic:\n    vector<vector<int>> levelOrder(TreeNode* root) {\n        vector<vector<int>> result;\n        if (!root) return result;\n        \n        queue<TreeNode*> q;\n        q.push(root);\n        \n        while (!q.empty()) {\n            int levelSize = q.size();\n            vector<int> levelValues;\n            \n            for (int i = 0; i < levelSize; i++) {\n                TreeNode* node = q.front();\n                q.pop();\n                levelValues.push_back(node->val);\n                \n                if (node->left) q.push(node->left);\n                if (node->right) q.push(node->right);\n            }\n            \n            result.push_back(levelValues);\n        }\n        \n        return result;\n    }\n};",
                "testCases": [
                    {"input": "[3,9,20,null,null,15,7]", "expected_output": "[[3],[9,20],[15,7]]", "weight": 0.5, "description": "Standard tree"},
                    {"input": "[1]", "expected_output": "[[1]]", "weight": 0.25, "description": "Single node"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.25, "description": "Empty tree"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(n)",
            "constraints": ["The number of nodes in the tree is in the range [0, 2000]", "-1000 <= Node.val <= 1000"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 20,
            "tags": ["tree", "breadth-first-search"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Trees & Graphs"
        }
    })

    # Hash Tables - Hard: LRU Cache
    questions.append({
        "id": "lru-cache",
        "title": "LRU Cache",
        "text": "Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.\n\nImplement the LRUCache class:\n\n- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.\n- int get(int key) Return the value of the key if the key exists, otherwise return -1.\n- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.\n\nThe functions get and put must each run in O(1) average time complexity.\n\n**Example:**\nInput\n[\"LRUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"put\", \"get\", \"get\", \"get\"]\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput\n[null, null, null, 1, null, -1, null, -1, 3, 4]",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class LRUCache:\n\n    def __init__(self, capacity):\n        # Your code here\n        pass\n\n    def get(self, key):\n        # Your code here\n        pass\n\n    def put(self, key, value):\n        # Your code here\n        pass\n\n\n# Your LRUCache object will be instantiated and called as such:\n# obj = LRUCache(capacity)\n# param_1 = obj.get(key)\n# obj.put(key,value)",
                "solutionCode": "class LRUCache:\n    class Node:\n        def __init__(self, key=0, value=0):\n            self.key = key\n            self.value = value\n            self.prev = None\n            self.next = None\n\n    def __init__(self, capacity):\n        self.capacity = capacity\n        self.cache = {}  # key -> node\n        \n        # Create dummy head and tail nodes\n        self.head = self.Node()\n        self.tail = self.Node()\n        self.head.next = self.tail\n        self.tail.prev = self.head\n    \n    def _add_node(self, node):\n        \"\"\"Add node right after head\"\"\"\n        node.prev = self.head\n        node.next = self.head.next\n        \n        self.head.next.prev = node\n        self.head.next = node\n    \n    def _remove_node(self, node):\n        \"\"\"Remove an existing node\"\"\"\n        prev_node = node.prev\n        next_node = node.next\n        \n        prev_node.next = next_node\n        next_node.prev = prev_node\n    \n    def _move_to_head(self, node):\n        \"\"\"Move node to head\"\"\"\n        self._remove_node(node)\n        self._add_node(node)\n    \n    def _pop_tail(self):\n        \"\"\"Pop the last node\"\"\"\n        last_node = self.tail.prev\n        self._remove_node(last_node)\n        return last_node\n\n    def get(self, key):\n        node = self.cache.get(key)\n        \n        if node:\n            # Move to head\n            self._move_to_head(node)\n            return node.value\n        \n        return -1\n\n    def put(self, key, value):\n        node = self.cache.get(key)\n        \n        if node:\n            # Update value and move to head\n            node.value = value\n            self._move_to_head(node)\n        else:\n            new_node = self.Node(key, value)\n            \n            if len(self.cache) >= self.capacity:\n                # Remove tail\n                tail = self._pop_tail()\n                del self.cache[tail.key]\n            \n            self.cache[key] = new_node\n            self._add_node(new_node)",
                "testCases": [
                    {"input": "[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]", "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]", "weight": 1.0, "description": "Standard LRU operations"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number} capacity\n */\nvar LRUCache = function(capacity) {\n    // Your code here\n};\n\n/** \n * @param {number} key\n * @return {number}\n */\nLRUCache.prototype.get = function(key) {\n    // Your code here\n};\n\n/** \n * @param {number} key \n * @param {number} value\n * @return {void}\n */\nLRUCache.prototype.put = function(key, value) {\n    // Your code here\n};\n\n/**\n * Your LRUCache object will be instantiated and called as such:\n * var obj = new LRUCache(capacity);\n * var param_1 = obj.get(key);\n * obj.put(key,value);\n */",
                "solutionCode": "/**\n * @param {number} capacity\n */\nvar LRUCache = function(capacity) {\n    this.capacity = capacity;\n    this.cache = new Map();\n};\n\n/** \n * @param {number} key\n * @return {number}\n */\nLRUCache.prototype.get = function(key) {\n    if (this.cache.has(key)) {\n        const value = this.cache.get(key);\n        // Move to end (most recent)\n        this.cache.delete(key);\n        this.cache.set(key, value);\n        return value;\n    }\n    return -1;\n};\n\n/** \n * @param {number} key \n * @param {number} value\n * @return {void}\n */\nLRUCache.prototype.put = function(key, value) {\n    if (this.cache.has(key)) {\n        // Update existing key\n        this.cache.delete(key);\n    } else if (this.cache.size >= this.capacity) {\n        // Remove least recently used (first item)\n        const firstKey = this.cache.keys().next().value;\n        this.cache.delete(firstKey);\n    }\n    \n    this.cache.set(key, value);\n};",
                "testCases": [
                    {"input": "[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]", "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]", "weight": 1.0, "description": "Standard LRU operations"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class LRUCache {\n\n    public LRUCache(int capacity) {\n        // Your code here\n    }\n    \n    public int get(int key) {\n        // Your code here\n        return -1;\n    }\n    \n    public void put(int key, int value) {\n        // Your code here\n    }\n}\n\n/**\n * Your LRUCache object will be instantiated and called as such:\n * LRUCache obj = new LRUCache(capacity);\n * int param_1 = obj.get(key);\n * obj.put(key,value);\n */",
                "solutionCode": "class LRUCache {\n    private class Node {\n        int key, value;\n        Node prev, next;\n        \n        Node(int key, int value) {\n            this.key = key;\n            this.value = value;\n        }\n    }\n    \n    private int capacity;\n    private Map<Integer, Node> cache;\n    private Node head, tail;\n\n    public LRUCache(int capacity) {\n        this.capacity = capacity;\n        this.cache = new HashMap<>();\n        \n        // Create dummy head and tail\n        this.head = new Node(0, 0);\n        this.tail = new Node(0, 0);\n        head.next = tail;\n        tail.prev = head;\n    }\n    \n    private void addNode(Node node) {\n        node.prev = head;\n        node.next = head.next;\n        \n        head.next.prev = node;\n        head.next = node;\n    }\n    \n    private void removeNode(Node node) {\n        Node prevNode = node.prev;\n        Node nextNode = node.next;\n        \n        prevNode.next = nextNode;\n        nextNode.prev = prevNode;\n    }\n    \n    private void moveToHead(Node node) {\n        removeNode(node);\n        addNode(node);\n    }\n    \n    private Node popTail() {\n        Node lastNode = tail.prev;\n        removeNode(lastNode);\n        return lastNode;\n    }\n    \n    public int get(int key) {\n        Node node = cache.get(key);\n        \n        if (node != null) {\n            moveToHead(node);\n            return node.value;\n        }\n        \n        return -1;\n    }\n    \n    public void put(int key, int value) {\n        Node node = cache.get(key);\n        \n        if (node != null) {\n            node.value = value;\n            moveToHead(node);\n        } else {\n            Node newNode = new Node(key, value);\n            \n            if (cache.size() >= capacity) {\n                Node tail = popTail();\n                cache.remove(tail.key);\n            }\n            \n            cache.put(key, newNode);\n            addNode(newNode);\n        }\n    }\n}",
                "testCases": [
                    {"input": "[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]", "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]", "weight": 1.0, "description": "Standard LRU operations"}
                ]
            },
            {
                "language": "go",
                "starterCode": "type LRUCache struct {\n    // Your code here\n}\n\n\nfunc Constructor(capacity int) LRUCache {\n    // Your code here\n    return LRUCache{}\n}\n\n\nfunc (this *LRUCache) Get(key int) int {\n    // Your code here\n    return -1\n}\n\n\nfunc (this *LRUCache) Put(key int, value int)  {\n    // Your code here\n}\n\n\n/**\n * Your LRUCache object will be instantiated and called as such:\n * obj := Constructor(capacity);\n * param_1 := obj.Get(key);\n * obj.Put(key,value);\n */",
                "solutionCode": "type Node struct {\n    key, value int\n    prev, next *Node\n}\n\ntype LRUCache struct {\n    capacity int\n    cache    map[int]*Node\n    head, tail *Node\n}\n\nfunc Constructor(capacity int) LRUCache {\n    head := &Node{}\n    tail := &Node{}\n    head.next = tail\n    tail.prev = head\n    \n    return LRUCache{\n        capacity: capacity,\n        cache:    make(map[int]*Node),\n        head:     head,\n        tail:     tail,\n    }\n}\n\nfunc (this *LRUCache) addNode(node *Node) {\n    node.prev = this.head\n    node.next = this.head.next\n    \n    this.head.next.prev = node\n    this.head.next = node\n}\n\nfunc (this *LRUCache) removeNode(node *Node) {\n    prevNode := node.prev\n    nextNode := node.next\n    \n    prevNode.next = nextNode\n    nextNode.prev = prevNode\n}\n\nfunc (this *LRUCache) moveToHead(node *Node) {\n    this.removeNode(node)\n    this.addNode(node)\n}\n\nfunc (this *LRUCache) popTail() *Node {\n    lastNode := this.tail.prev\n    this.removeNode(lastNode)\n    return lastNode\n}\n\nfunc (this *LRUCache) Get(key int) int {\n    if node, exists := this.cache[key]; exists {\n        this.moveToHead(node)\n        return node.value\n    }\n    return -1\n}\n\nfunc (this *LRUCache) Put(key int, value int) {\n    if node, exists := this.cache[key]; exists {\n        node.value = value\n        this.moveToHead(node)\n    } else {\n        newNode := &Node{key: key, value: value}\n        \n        if len(this.cache) >= this.capacity {\n            tail := this.popTail()\n            delete(this.cache, tail.key)\n        }\n        \n        this.cache[key] = newNode\n        this.addNode(newNode)\n    }\n}",
                "testCases": [
                    {"input": "[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]", "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]", "weight": 1.0, "description": "Standard LRU operations"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "class LRUCache\n\n=begin\n    :type capacity: Integer\n=end\n    def initialize(capacity)\n        # Your code here\n    end\n\n\n=begin\n    :type key: Integer\n    :rtype: Integer\n=end\n    def get(key)\n        # Your code here\n    end\n\n\n=begin\n    :type key: Integer\n    :type value: Integer\n    :rtype: Void\n=end\n    def put(key, value)\n        # Your code here\n    end\n\n\nend\n\n# Your LRUCache object will be instantiated and called as such:\n# obj = LRUCache.new(capacity)\n# param_1 = obj.get(key)\n# obj.put(key, value)",
                "solutionCode": "class LRUCache\n    def initialize(capacity)\n        @capacity = capacity\n        @cache = {}\n        @order = []\n    end\n\n    def get(key)\n        if @cache.key?(key)\n            # Move to end (most recent)\n            @order.delete(key)\n            @order.push(key)\n            return @cache[key]\n        end\n        -1\n    end\n\n    def put(key, value)\n        if @cache.key?(key)\n            # Update existing key\n            @cache[key] = value\n            @order.delete(key)\n            @order.push(key)\n        else\n            if @cache.size >= @capacity\n                # Remove least recently used\n                lru_key = @order.shift\n                @cache.delete(lru_key)\n            end\n            \n            @cache[key] = value\n            @order.push(key)\n        end\n    end\nend",
                "testCases": [
                    {"input": "[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]", "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]", "weight": 1.0, "description": "Standard LRU operations"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class LRUCache {\npublic:\n    LRUCache(int capacity) {\n        // Your code here\n    }\n    \n    int get(int key) {\n        // Your code here\n        return -1;\n    }\n    \n    void put(int key, int value) {\n        // Your code here\n    }\n};\n\n/**\n * Your LRUCache object will be instantiated and called as such:\n * LRUCache* obj = new LRUCache(capacity);\n * int param_1 = obj->get(key);\n * obj->put(key,value);\n */",
                "solutionCode": "class LRUCache {\nprivate:\n    struct Node {\n        int key, value;\n        Node* prev;\n        Node* next;\n        Node(int k = 0, int v = 0) : key(k), value(v), prev(nullptr), next(nullptr) {}\n    };\n    \n    int capacity;\n    unordered_map<int, Node*> cache;\n    Node* head;\n    Node* tail;\n    \n    void addNode(Node* node) {\n        node->prev = head;\n        node->next = head->next;\n        \n        head->next->prev = node;\n        head->next = node;\n    }\n    \n    void removeNode(Node* node) {\n        Node* prevNode = node->prev;\n        Node* nextNode = node->next;\n        \n        prevNode->next = nextNode;\n        nextNode->prev = prevNode;\n    }\n    \n    void moveToHead(Node* node) {\n        removeNode(node);\n        addNode(node);\n    }\n    \n    Node* popTail() {\n        Node* lastNode = tail->prev;\n        removeNode(lastNode);\n        return lastNode;\n    }\n    \npublic:\n    LRUCache(int capacity) : capacity(capacity) {\n        head = new Node();\n        tail = new Node();\n        head->next = tail;\n        tail->prev = head;\n    }\n    \n    int get(int key) {\n        auto it = cache.find(key);\n        if (it != cache.end()) {\n            Node* node = it->second;\n            moveToHead(node);\n            return node->value;\n        }\n        return -1;\n    }\n    \n    void put(int key, int value) {\n        auto it = cache.find(key);\n        if (it != cache.end()) {\n            Node* node = it->second;\n            node->value = value;\n            moveToHead(node);\n        } else {\n            Node* newNode = new Node(key, value);\n            \n            if (cache.size() >= capacity) {\n                Node* tail = popTail();\n                cache.erase(tail->key);\n                delete tail;\n            }\n            \n            cache[key] = newNode;\n            addNode(newNode);\n        }\n    }\n};",
                "testCases": [
                    {"input": "[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]", "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]", "weight": 1.0, "description": "Standard LRU operations"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(1)",
            "spaceComplexity": "O(capacity)",
            "constraints": ["1 <= capacity <= 3000", "0 <= key <= 10^4", "0 <= value <= 10^5", "At most 2 * 10^5 calls will be made to get and put"]
        },
        "gradingRules": {
            "testCaseWeight": 0.5,
            "codeQualityWeight": 0.3,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "HARD",
            "estimatedDuration": 35,
            "tags": ["hash-table", "linked-list", "design"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn", "Uber"],
            "topic": "Hash Tables"
        }
    })

    # Dynamic Programming - Hard: Edit Distance
    questions.append({
        "id": "edit-distance",
        "title": "Edit Distance",
        "text": "Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.\n\nYou have the following three operations permitted on a word:\n- Insert a character\n- Delete a character\n- Replace a character\n\n**Example 1:**\nInput: word1 = \"horse\", word2 = \"ros\"\nOutput: 3\nExplanation: \nhorse -> rorse (replace 'h' with 'r')\nrorse -> rose (remove 'r')\nrose -> ros (remove 'e')\n\n**Example 2:**\nInput: word1 = \"intention\", word2 = \"execution\"\nOutput: 5\nExplanation: \nintention -> inention (remove 't')\ninention -> enention (replace 'i' with 'e')\nenention -> exention (replace 'n' with 'x')\nexention -> exection (replace 'n' with 'c')\nexection -> execution (insert 'u')",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def minDistance(self, word1, word2):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def minDistance(self, word1, word2):\n        m, n = len(word1), len(word2)\n        \n        # dp[i][j] represents min operations to convert word1[:i] to word2[:j]\n        dp = [[0] * (n + 1) for _ in range(m + 1)]\n        \n        # Initialize base cases\n        for i in range(m + 1):\n            dp[i][0] = i  # Delete all characters from word1\n        for j in range(n + 1):\n            dp[0][j] = j  # Insert all characters to get word2\n        \n        # Fill the dp table\n        for i in range(1, m + 1):\n            for j in range(1, n + 1):\n                if word1[i - 1] == word2[j - 1]:\n                    dp[i][j] = dp[i - 1][j - 1]  # No operation needed\n                else:\n                    dp[i][j] = 1 + min(\n                        dp[i - 1][j],      # Delete\n                        dp[i][j - 1],      # Insert\n                        dp[i - 1][j - 1]   # Replace\n                    )\n        \n        return dp[m][n]",
                "testCases": [
                    {"input": "\"horse\", \"ros\"", "expected_output": "3", "weight": 0.5, "description": "Standard case"},
                    {"input": "\"intention\", \"execution\"", "expected_output": "5", "weight": 0.5, "description": "Complex case"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {string} word1\n * @param {string} word2\n * @return {number}\n */\nvar minDistance = function(word1, word2) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {string} word1\n * @param {string} word2\n * @return {number}\n */\nvar minDistance = function(word1, word2) {\n    const m = word1.length, n = word2.length;\n    \n    const dp = Array(m + 1).fill().map(() => Array(n + 1).fill(0));\n    \n    // Initialize base cases\n    for (let i = 0; i <= m; i++) {\n        dp[i][0] = i;\n    }\n    for (let j = 0; j <= n; j++) {\n        dp[0][j] = j;\n    }\n    \n    // Fill the dp table\n    for (let i = 1; i <= m; i++) {\n        for (let j = 1; j <= n; j++) {\n            if (word1[i - 1] === word2[j - 1]) {\n                dp[i][j] = dp[i - 1][j - 1];\n            } else {\n                dp[i][j] = 1 + Math.min(\n                    dp[i - 1][j],      // Delete\n                    dp[i][j - 1],      // Insert\n                    dp[i - 1][j - 1]   // Replace\n                );\n            }\n        }\n    }\n    \n    return dp[m][n];\n};",
                "testCases": [
                    {"input": "\"horse\", \"ros\"", "expected_output": "3", "weight": 0.5, "description": "Standard case"},
                    {"input": "\"intention\", \"execution\"", "expected_output": "5", "weight": 0.5, "description": "Complex case"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int minDistance(String word1, String word2) {\n        // Your code here\n        return 0;\n    }\n}",
                "solutionCode": "class Solution {\n    public int minDistance(String word1, String word2) {\n        int m = word1.length(), n = word2.length();\n        \n        int[][] dp = new int[m + 1][n + 1];\n        \n        // Initialize base cases\n        for (int i = 0; i <= m; i++) {\n            dp[i][0] = i;\n        }\n        for (int j = 0; j <= n; j++) {\n            dp[0][j] = j;\n        }\n        \n        // Fill the dp table\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {\n                    dp[i][j] = dp[i - 1][j - 1];\n                } else {\n                    dp[i][j] = 1 + Math.min(\n                        Math.min(dp[i - 1][j], dp[i][j - 1]),\n                        dp[i - 1][j - 1]\n                    );\n                }\n            }\n        }\n        \n        return dp[m][n];\n    }\n}",
                "testCases": [
                    {"input": "\"horse\", \"ros\"", "expected_output": "3", "weight": 0.5, "description": "Standard case"},
                    {"input": "\"intention\", \"execution\"", "expected_output": "5", "weight": 0.5, "description": "Complex case"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func minDistance(word1 string, word2 string) int {\n    // Your code here\n    return 0\n}",
                "solutionCode": "func minDistance(word1 string, word2 string) int {\n    m, n := len(word1), len(word2)\n    \n    dp := make([][]int, m+1)\n    for i := range dp {\n        dp[i] = make([]int, n+1)\n    }\n    \n    // Initialize base cases\n    for i := 0; i <= m; i++ {\n        dp[i][0] = i\n    }\n    for j := 0; j <= n; j++ {\n        dp[0][j] = j\n    }\n    \n    // Fill the dp table\n    for i := 1; i <= m; i++ {\n        for j := 1; j <= n; j++ {\n            if word1[i-1] == word2[j-1] {\n                dp[i][j] = dp[i-1][j-1]\n            } else {\n                dp[i][j] = 1 + min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])\n            }\n        }\n    }\n    \n    return dp[m][n]\n}\n\nfunc min(a, b int) int {\n    if a < b {\n        return a\n    }\n    return b\n}",
                "testCases": [
                    {"input": "\"horse\", \"ros\"", "expected_output": "3", "weight": 0.5, "description": "Standard case"},
                    {"input": "\"intention\", \"execution\"", "expected_output": "5", "weight": 0.5, "description": "Complex case"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {String} word1\n# @param {String} word2\n# @return {Integer}\ndef min_distance(word1, word2)\n    # Your code here\nend",
                "solutionCode": "# @param {String} word1\n# @param {String} word2\n# @return {Integer}\ndef min_distance(word1, word2)\n    m, n = word1.length, word2.length\n    \n    dp = Array.new(m + 1) { Array.new(n + 1, 0) }\n    \n    # Initialize base cases\n    (0..m).each { |i| dp[i][0] = i }\n    (0..n).each { |j| dp[0][j] = j }\n    \n    # Fill the dp table\n    (1..m).each do |i|\n        (1..n).each do |j|\n            if word1[i - 1] == word2[j - 1]\n                dp[i][j] = dp[i - 1][j - 1]\n            else\n                dp[i][j] = 1 + [dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]].min\n            end\n        end\n    end\n    \n    dp[m][n]\nend",
                "testCases": [
                    {"input": "\"horse\", \"ros\"", "expected_output": "3", "weight": 0.5, "description": "Standard case"},
                    {"input": "\"intention\", \"execution\"", "expected_output": "5", "weight": 0.5, "description": "Complex case"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    int minDistance(string word1, string word2) {\n        // Your code here\n        return 0;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    int minDistance(string word1, string word2) {\n        int m = word1.length(), n = word2.length();\n        \n        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));\n        \n        // Initialize base cases\n        for (int i = 0; i <= m; i++) {\n            dp[i][0] = i;\n        }\n        for (int j = 0; j <= n; j++) {\n            dp[0][j] = j;\n        }\n        \n        // Fill the dp table\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (word1[i - 1] == word2[j - 1]) {\n                    dp[i][j] = dp[i - 1][j - 1];\n                } else {\n                    dp[i][j] = 1 + min({\n                        dp[i - 1][j],      // Delete\n                        dp[i][j - 1],      // Insert\n                        dp[i - 1][j - 1]   // Replace\n                    });\n                }\n            }\n        }\n        \n        return dp[m][n];\n    }\n};",
                "testCases": [
                    {"input": "\"horse\", \"ros\"", "expected_output": "3", "weight": 0.5, "description": "Standard case"},
                    {"input": "\"intention\", \"execution\"", "expected_output": "5", "weight": 0.5, "description": "Complex case"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(m * n)",
            "spaceComplexity": "O(m * n)",
            "constraints": ["0 <= word1.length, word2.length <= 500", "word1 and word2 consist of lowercase English letters"]
        },
        "gradingRules": {
            "testCaseWeight": 0.5,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.3,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "HARD",
            "estimatedDuration": 30,
            "tags": ["string", "dynamic-programming"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Dynamic Programming"
        }
    })

    # Greedy Algorithms - Easy: Jump Game
    questions.append({
        "id": "jump-game",
        "title": "Jump Game",
        "text": "You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.\n\nReturn true if you can reach the last index, or false otherwise.\n\n**Example 1:**\nInput: nums = [2,3,1,1,4]\nOutput: true\nExplanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.\n\n**Example 2:**\nInput: nums = [3,2,1,0,4]\nOutput: false\nExplanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def canJump(self, nums):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def canJump(self, nums):\n        max_reach = 0\n        \n        for i in range(len(nums)):\n            # If current position is beyond max reach, we can't get here\n            if i > max_reach:\n                return False\n            \n            # Update max reach from current position\n            max_reach = max(max_reach, i + nums[i])\n            \n            # If we can reach or exceed the last index\n            if max_reach >= len(nums) - 1:\n                return True\n        \n        return True",
                "testCases": [
                    {"input": "[2,3,1,1,4]", "expected_output": "True", "weight": 0.5, "description": "Can reach end"},
                    {"input": "[3,2,1,0,4]", "expected_output": "False", "weight": 0.5, "description": "Cannot reach end"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[]} nums\n * @return {boolean}\n */\nvar canJump = function(nums) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[]} nums\n * @return {boolean}\n */\nvar canJump = function(nums) {\n    let maxReach = 0;\n    \n    for (let i = 0; i < nums.length; i++) {\n        if (i > maxReach) {\n            return false;\n        }\n        \n        maxReach = Math.max(maxReach, i + nums[i]);\n        \n        if (maxReach >= nums.length - 1) {\n            return true;\n        }\n    }\n    \n    return true;\n};",
                "testCases": [
                    {"input": "[2,3,1,1,4]", "expected_output": "true", "weight": 0.5, "description": "Can reach end"},
                    {"input": "[3,2,1,0,4]", "expected_output": "false", "weight": 0.5, "description": "Cannot reach end"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public boolean canJump(int[] nums) {\n        // Your code here\n        return false;\n    }\n}",
                "solutionCode": "class Solution {\n    public boolean canJump(int[] nums) {\n        int maxReach = 0;\n        \n        for (int i = 0; i < nums.length; i++) {\n            if (i > maxReach) {\n                return false;\n            }\n            \n            maxReach = Math.max(maxReach, i + nums[i]);\n            \n            if (maxReach >= nums.length - 1) {\n                return true;\n            }\n        }\n        \n        return true;\n    }\n}",
                "testCases": [
                    {"input": "[2,3,1,1,4]", "expected_output": "true", "weight": 0.5, "description": "Can reach end"},
                    {"input": "[3,2,1,0,4]", "expected_output": "false", "weight": 0.5, "description": "Cannot reach end"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func canJump(nums []int) bool {\n    // Your code here\n    return false\n}",
                "solutionCode": "func canJump(nums []int) bool {\n    maxReach := 0\n    \n    for i := 0; i < len(nums); i++ {\n        if i > maxReach {\n            return false\n        }\n        \n        if i+nums[i] > maxReach {\n            maxReach = i + nums[i]\n        }\n        \n        if maxReach >= len(nums)-1 {\n            return true\n        }\n    }\n    \n    return true\n}",
                "testCases": [
                    {"input": "[2,3,1,1,4]", "expected_output": "true", "weight": 0.5, "description": "Can reach end"},
                    {"input": "[3,2,1,0,4]", "expected_output": "false", "weight": 0.5, "description": "Cannot reach end"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[]} nums\n# @return {Boolean}\ndef can_jump(nums)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[]} nums\n# @return {Boolean}\ndef can_jump(nums)\n    max_reach = 0\n    \n    nums.each_with_index do |num, i|\n        return false if i > max_reach\n        \n        max_reach = [max_reach, i + num].max\n        \n        return true if max_reach >= nums.length - 1\n    end\n    \n    true\nend",
                "testCases": [
                    {"input": "[2,3,1,1,4]", "expected_output": "true", "weight": 0.5, "description": "Can reach end"},
                    {"input": "[3,2,1,0,4]", "expected_output": "false", "weight": 0.5, "description": "Cannot reach end"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    bool canJump(vector<int>& nums) {\n        // Your code here\n        return false;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    bool canJump(vector<int>& nums) {\n        int maxReach = 0;\n        \n        for (int i = 0; i < nums.size(); i++) {\n            if (i > maxReach) {\n                return false;\n            }\n            \n            maxReach = max(maxReach, i + nums[i]);\n            \n            if (maxReach >= nums.size() - 1) {\n                return true;\n            }\n        }\n        \n        return true;\n    }\n};",
                "testCases": [
                    {"input": "[2,3,1,1,4]", "expected_output": "true", "weight": 0.5, "description": "Can reach end"},
                    {"input": "[3,2,1,0,4]", "expected_output": "false", "weight": 0.5, "description": "Cannot reach end"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(1)",
            "constraints": ["1 <= nums.length <= 10^4", "0 <= nums[i] <= 10^5"]
        },
        "gradingRules": {
            "testCaseWeight": 0.7,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 20,
            "tags": ["array", "dynamic-programming", "greedy"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Greedy Algorithms"
        }
    })

    # Stack & Queue - Medium: Implement Queue using Stacks
    questions.append({
        "id": "implement-queue-using-stacks",
        "title": "Implement Queue using Stacks",
        "text": "Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).\n\nImplement the MyQueue class:\n\n- void push(int x) Pushes element x to the back of the queue.\n- int pop() Removes the element from the front of the queue and returns it.\n- int peek() Returns the element at the front of the queue.\n- boolean empty() Returns true if the queue is empty, false otherwise.\n\nNotes:\n- You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.\n- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.\n\n**Example:**\nInput\n[\"MyQueue\", \"push\", \"push\", \"peek\", \"pop\", \"empty\"]\n[[], [1], [2], [], [], []]\nOutput\n[null, null, null, 1, 1, false]",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class MyQueue:\n\n    def __init__(self):\n        # Your code here\n        pass\n\n    def push(self, x):\n        # Your code here\n        pass\n\n    def pop(self):\n        # Your code here\n        pass\n\n    def peek(self):\n        # Your code here\n        pass\n\n    def empty(self):\n        # Your code here\n        pass\n\n\n# Your MyQueue object will be instantiated and called as such:\n# obj = MyQueue()\n# obj.push(x)\n# param_2 = obj.pop()\n# param_3 = obj.peek()\n# param_4 = obj.empty()",
                "solutionCode": "class MyQueue:\n\n    def __init__(self):\n        self.input_stack = []\n        self.output_stack = []\n\n    def push(self, x):\n        self.input_stack.append(x)\n\n    def pop(self):\n        self.peek()\n        return self.output_stack.pop()\n\n    def peek(self):\n        if not self.output_stack:\n            while self.input_stack:\n                self.output_stack.append(self.input_stack.pop())\n        return self.output_stack[-1]\n\n    def empty(self):\n        return not self.input_stack and not self.output_stack",
                "testCases": [
                    {"input": "[[\"MyQueue\", \"push\", \"push\", \"peek\", \"pop\", \"empty\"], [[], [1], [2], [], [], []]]", "expected_output": "[null, null, null, 1, 1, false]", "weight": 1.0, "description": "Standard queue operations"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "var MyQueue = function() {\n    // Your code here\n};\n\n/** \n * @param {number} x\n * @return {void}\n */\nMyQueue.prototype.push = function(x) {\n    // Your code here\n};\n\n/**\n * @return {number}\n */\nMyQueue.prototype.pop = function() {\n    // Your code here\n};\n\n/**\n * @return {number}\n */\nMyQueue.prototype.peek = function() {\n    // Your code here\n};\n\n/**\n * @return {boolean}\n */\nMyQueue.prototype.empty = function() {\n    // Your code here\n};\n\n/**\n * Your MyQueue object will be instantiated and called as such:\n * var obj = new MyQueue();\n * obj.push(x);\n * var param_2 = obj.pop();\n * var param_3 = obj.peek();\n * var param_4 = obj.empty();\n */",
                "solutionCode": "var MyQueue = function() {\n    this.inputStack = [];\n    this.outputStack = [];\n};\n\n/** \n * @param {number} x\n * @return {void}\n */\nMyQueue.prototype.push = function(x) {\n    this.inputStack.push(x);\n};\n\n/**\n * @return {number}\n */\nMyQueue.prototype.pop = function() {\n    this.peek();\n    return this.outputStack.pop();\n};\n\n/**\n * @return {number}\n */\nMyQueue.prototype.peek = function() {\n    if (this.outputStack.length === 0) {\n        while (this.inputStack.length > 0) {\n            this.outputStack.push(this.inputStack.pop());\n        }\n    }\n    return this.outputStack[this.outputStack.length - 1];\n};\n\n/**\n * @return {boolean}\n */\nMyQueue.prototype.empty = function() {\n    return this.inputStack.length === 0 && this.outputStack.length === 0;\n};",
                "testCases": [
                    {"input": "[[\"MyQueue\", \"push\", \"push\", \"peek\", \"pop\", \"empty\"], [[], [1], [2], [], [], []]]", "expected_output": "[null, null, null, 1, 1, false]", "weight": 1.0, "description": "Standard queue operations"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class MyQueue {\n\n    public MyQueue() {\n        // Your code here\n    }\n    \n    public void push(int x) {\n        // Your code here\n    }\n    \n    public int pop() {\n        // Your code here\n        return 0;\n    }\n    \n    public int peek() {\n        // Your code here\n        return 0;\n    }\n    \n    public boolean empty() {\n        // Your code here\n        return false;\n    }\n}\n\n/**\n * Your MyQueue object will be instantiated and called as such:\n * MyQueue obj = new MyQueue();\n * obj.push(x);\n * int param_2 = obj.pop();\n * int param_3 = obj.peek();\n * boolean param_4 = obj.empty();\n */",
                "solutionCode": "class MyQueue {\n    private Stack<Integer> inputStack;\n    private Stack<Integer> outputStack;\n\n    public MyQueue() {\n        inputStack = new Stack<>();\n        outputStack = new Stack<>();\n    }\n    \n    public void push(int x) {\n        inputStack.push(x);\n    }\n    \n    public int pop() {\n        peek();\n        return outputStack.pop();\n    }\n    \n    public int peek() {\n        if (outputStack.empty()) {\n            while (!inputStack.empty()) {\n                outputStack.push(inputStack.pop());\n            }\n        }\n        return outputStack.peek();\n    }\n    \n    public boolean empty() {\n        return inputStack.empty() && outputStack.empty();\n    }\n}",
                "testCases": [
                    {"input": "[[\"MyQueue\", \"push\", \"push\", \"peek\", \"pop\", \"empty\"], [[], [1], [2], [], [], []]]", "expected_output": "[null, null, null, 1, 1, false]", "weight": 1.0, "description": "Standard queue operations"}
                ]
            },
            {
                "language": "go",
                "starterCode": "type MyQueue struct {\n    // Your code here\n}\n\n\nfunc Constructor() MyQueue {\n    // Your code here\n    return MyQueue{}\n}\n\n\nfunc (this *MyQueue) Push(x int)  {\n    // Your code here\n}\n\n\nfunc (this *MyQueue) Pop() int {\n    // Your code here\n    return 0\n}\n\n\nfunc (this *MyQueue) Peek() int {\n    // Your code here\n    return 0\n}\n\n\nfunc (this *MyQueue) Empty() bool {\n    // Your code here\n    return false\n}\n\n\n/**\n * Your MyQueue object will be instantiated and called as such:\n * obj := Constructor();\n * obj.Push(x);\n * param_2 := obj.Pop();\n * param_3 := obj.Peek();\n * param_4 := obj.Empty();\n */",
                "solutionCode": "type MyQueue struct {\n    inputStack  []int\n    outputStack []int\n}\n\nfunc Constructor() MyQueue {\n    return MyQueue{\n        inputStack:  []int{},\n        outputStack: []int{},\n    }\n}\n\nfunc (this *MyQueue) Push(x int) {\n    this.inputStack = append(this.inputStack, x)\n}\n\nfunc (this *MyQueue) Pop() int {\n    this.Peek()\n    val := this.outputStack[len(this.outputStack)-1]\n    this.outputStack = this.outputStack[:len(this.outputStack)-1]\n    return val\n}\n\nfunc (this *MyQueue) Peek() int {\n    if len(this.outputStack) == 0 {\n        for len(this.inputStack) > 0 {\n            val := this.inputStack[len(this.inputStack)-1]\n            this.inputStack = this.inputStack[:len(this.inputStack)-1]\n            this.outputStack = append(this.outputStack, val)\n        }\n    }\n    return this.outputStack[len(this.outputStack)-1]\n}\n\nfunc (this *MyQueue) Empty() bool {\n    return len(this.inputStack) == 0 && len(this.outputStack) == 0\n}",
                "testCases": [
                    {"input": "[[\"MyQueue\", \"push\", \"push\", \"peek\", \"pop\", \"empty\"], [[], [1], [2], [], [], []]]", "expected_output": "[null, null, null, 1, 1, false]", "weight": 1.0, "description": "Standard queue operations"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "class MyQueue\n\n=begin\n    Initialize your data structure here.\n=end\n    def initialize()\n        # Your code here\n    end\n\n\n=begin\n    Push element x to the back of queue.\n    :type x: Integer\n    :rtype: Void\n=end\n    def push(x)\n        # Your code here\n    end\n\n\n=begin\n    Removes the element from in front of queue and returns that element.\n    :rtype: Integer\n=end\n    def pop()\n        # Your code here\n    end\n\n\n=begin\n    Get the front element.\n    :rtype: Integer\n=end\n    def peek()\n        # Your code here\n    end\n\n\n=begin\n    Returns whether the queue is empty.\n    :rtype: Boolean\n=end\n    def empty()\n        # Your code here\n    end\n\n\nend\n\n# Your MyQueue object will be instantiated and called as such:\n# obj = MyQueue.new()\n# obj.push(x)\n# param_2 = obj.pop()\n# param_3 = obj.peek()\n# param_4 = obj.empty()",
                "solutionCode": "class MyQueue\n    def initialize()\n        @input_stack = []\n        @output_stack = []\n    end\n\n    def push(x)\n        @input_stack.push(x)\n    end\n\n    def pop()\n        peek\n        @output_stack.pop\n    end\n\n    def peek()\n        if @output_stack.empty?\n            while !@input_stack.empty?\n                @output_stack.push(@input_stack.pop)\n            end\n        end\n        @output_stack.last\n    end\n\n    def empty()\n        @input_stack.empty? && @output_stack.empty?\n    end\nend",
                "testCases": [
                    {"input": "[[\"MyQueue\", \"push\", \"push\", \"peek\", \"pop\", \"empty\"], [[], [1], [2], [], [], []]]", "expected_output": "[null, null, null, 1, 1, false]", "weight": 1.0, "description": "Standard queue operations"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class MyQueue {\npublic:\n    MyQueue() {\n        // Your code here\n    }\n    \n    void push(int x) {\n        // Your code here\n    }\n    \n    int pop() {\n        // Your code here\n        return 0;\n    }\n    \n    int peek() {\n        // Your code here\n        return 0;\n    }\n    \n    bool empty() {\n        // Your code here\n        return false;\n    }\n};\n\n/**\n * Your MyQueue object will be instantiated and called as such:\n * MyQueue* obj = new MyQueue();\n * obj->push(x);\n * int param_2 = obj->pop();\n * int param_3 = obj->peek();\n * bool param_4 = obj->empty();\n */",
                "solutionCode": "class MyQueue {\nprivate:\n    stack<int> inputStack;\n    stack<int> outputStack;\n    \npublic:\n    MyQueue() {\n        \n    }\n    \n    void push(int x) {\n        inputStack.push(x);\n    }\n    \n    int pop() {\n        peek();\n        int val = outputStack.top();\n        outputStack.pop();\n        return val;\n    }\n    \n    int peek() {\n        if (outputStack.empty()) {\n            while (!inputStack.empty()) {\n                outputStack.push(inputStack.top());\n                inputStack.pop();\n            }\n        }\n        return outputStack.top();\n    }\n    \n    bool empty() {\n        return inputStack.empty() && outputStack.empty();\n    }\n};",
                "testCases": [
                    {"input": "[[\"MyQueue\", \"push\", \"push\", \"peek\", \"pop\", \"empty\"], [[], [1], [2], [], [], []]]", "expected_output": "[null, null, null, 1, 1, false]", "weight": 1.0, "description": "Standard queue operations"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(1) amortized",
            "spaceComplexity": "O(n)",
            "constraints": ["1 <= x <= 9", "At most 100 calls will be made to push, pop, peek, and empty", "All the calls to pop and peek are valid"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.3,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "EASY",
            "estimatedDuration": 20,
            "tags": ["stack", "design", "queue"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Stack & Queue"
        }
    })

    # Two Pointers - Medium: 3Sum
    questions.append({
        "id": "three-sum",
        "title": "3Sum",
        "text": "Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.\n\nNotice that the solution set must not contain duplicate triplets.\n\n**Example 1:**\nInput: nums = [-1,0,1,2,-1,-4]\nOutput: [[-1,-1,2],[-1,0,1]]\nExplanation: \nnums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.\nnums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.\nnums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.\nThe distinct triplets are [-1,0,1] and [-1,-1,2].\nNotice that the order of the output and the order of the triplets does not matter.\n\n**Example 2:**\nInput: nums = [0,1,1]\nOutput: []\nExplanation: The only possible triplet does not sum up to 0.\n\n**Example 3:**\nInput: nums = [0,0,0]\nOutput: [[0,0,0]]\nExplanation: The only possible triplet sums up to 0.",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def threeSum(self, nums):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def threeSum(self, nums):\n        nums.sort()\n        result = []\n        \n        for i in range(len(nums) - 2):\n            # Skip duplicates for the first number\n            if i > 0 and nums[i] == nums[i - 1]:\n                continue\n            \n            left, right = i + 1, len(nums) - 1\n            \n            while left < right:\n                current_sum = nums[i] + nums[left] + nums[right]\n                \n                if current_sum == 0:\n                    result.append([nums[i], nums[left], nums[right]])\n                    \n                    # Skip duplicates for left and right pointers\n                    while left < right and nums[left] == nums[left + 1]:\n                        left += 1\n                    while left < right and nums[right] == nums[right - 1]:\n                        right -= 1\n                    \n                    left += 1\n                    right -= 1\n                elif current_sum < 0:\n                    left += 1\n                else:\n                    right -= 1\n        \n        return result",
                "testCases": [
                    {"input": "[-1,0,1,2,-1,-4]", "expected_output": "[[-1,-1,2],[-1,0,1]]", "weight": 0.5, "description": "Standard case with multiple triplets"},
                    {"input": "[0,1,1]", "expected_output": "[]", "weight": 0.25, "description": "No valid triplets"},
                    {"input": "[0,0,0]", "expected_output": "[[0,0,0]]", "weight": 0.25, "description": "All zeros"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[]} nums\n * @return {number[][]}\n */\nvar threeSum = function(nums) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[]} nums\n * @return {number[][]}\n */\nvar threeSum = function(nums) {\n    nums.sort((a, b) => a - b);\n    const result = [];\n    \n    for (let i = 0; i < nums.length - 2; i++) {\n        if (i > 0 && nums[i] === nums[i - 1]) {\n            continue;\n        }\n        \n        let left = i + 1, right = nums.length - 1;\n        \n        while (left < right) {\n            const currentSum = nums[i] + nums[left] + nums[right];\n            \n            if (currentSum === 0) {\n                result.push([nums[i], nums[left], nums[right]]);\n                \n                while (left < right && nums[left] === nums[left + 1]) {\n                    left++;\n                }\n                while (left < right && nums[right] === nums[right - 1]) {\n                    right--;\n                }\n                \n                left++;\n                right--;\n            } else if (currentSum < 0) {\n                left++;\n            } else {\n                right--;\n            }\n        }\n    }\n    \n    return result;\n};",
                "testCases": [
                    {"input": "[-1,0,1,2,-1,-4]", "expected_output": "[[-1,-1,2],[-1,0,1]]", "weight": 0.5, "description": "Standard case with multiple triplets"},
                    {"input": "[0,1,1]", "expected_output": "[]", "weight": 0.25, "description": "No valid triplets"},
                    {"input": "[0,0,0]", "expected_output": "[[0,0,0]]", "weight": 0.25, "description": "All zeros"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public List<List<Integer>> threeSum(int[] nums) {\n        // Your code here\n        return new ArrayList<>();\n    }\n}",
                "solutionCode": "class Solution {\n    public List<List<Integer>> threeSum(int[] nums) {\n        Arrays.sort(nums);\n        List<List<Integer>> result = new ArrayList<>();\n        \n        for (int i = 0; i < nums.length - 2; i++) {\n            if (i > 0 && nums[i] == nums[i - 1]) {\n                continue;\n            }\n            \n            int left = i + 1, right = nums.length - 1;\n            \n            while (left < right) {\n                int currentSum = nums[i] + nums[left] + nums[right];\n                \n                if (currentSum == 0) {\n                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));\n                    \n                    while (left < right && nums[left] == nums[left + 1]) {\n                        left++;\n                    }\n                    while (left < right && nums[right] == nums[right - 1]) {\n                        right--;\n                    }\n                    \n                    left++;\n                    right--;\n                } else if (currentSum < 0) {\n                    left++;\n                } else {\n                    right--;\n                }\n            }\n        }\n        \n        return result;\n    }\n}",
                "testCases": [
                    {"input": "[-1,0,1,2,-1,-4]", "expected_output": "[[-1,-1,2],[-1,0,1]]", "weight": 0.5, "description": "Standard case with multiple triplets"},
                    {"input": "[0,1,1]", "expected_output": "[]", "weight": 0.25, "description": "No valid triplets"},
                    {"input": "[0,0,0]", "expected_output": "[[0,0,0]]", "weight": 0.25, "description": "All zeros"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func threeSum(nums []int) [][]int {\n    // Your code here\n    return [][]int{}\n}",
                "solutionCode": "func threeSum(nums []int) [][]int {\n    sort.Ints(nums)\n    var result [][]int\n    \n    for i := 0; i < len(nums)-2; i++ {\n        if i > 0 && nums[i] == nums[i-1] {\n            continue\n        }\n        \n        left, right := i+1, len(nums)-1\n        \n        for left < right {\n            currentSum := nums[i] + nums[left] + nums[right]\n            \n            if currentSum == 0 {\n                result = append(result, []int{nums[i], nums[left], nums[right]})\n                \n                for left < right && nums[left] == nums[left+1] {\n                    left++\n                }\n                for left < right && nums[right] == nums[right-1] {\n                    right--\n                }\n                \n                left++\n                right--\n            } else if currentSum < 0 {\n                left++\n            } else {\n                right--\n            }\n        }\n    }\n    \n    return result\n}",
                "testCases": [
                    {"input": "[-1,0,1,2,-1,-4]", "expected_output": "[[-1,-1,2],[-1,0,1]]", "weight": 0.5, "description": "Standard case with multiple triplets"},
                    {"input": "[0,1,1]", "expected_output": "[]", "weight": 0.25, "description": "No valid triplets"},
                    {"input": "[0,0,0]", "expected_output": "[[0,0,0]]", "weight": 0.25, "description": "All zeros"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[]} nums\n# @return {Integer[][]}\ndef three_sum(nums)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[]} nums\n# @return {Integer[][]}\ndef three_sum(nums)\n    nums.sort!\n    result = []\n    \n    (0...nums.length - 2).each do |i|\n        next if i > 0 && nums[i] == nums[i - 1]\n        \n        left, right = i + 1, nums.length - 1\n        \n        while left < right\n            current_sum = nums[i] + nums[left] + nums[right]\n            \n            if current_sum == 0\n                result << [nums[i], nums[left], nums[right]]\n                \n                left += 1 while left < right && nums[left] == nums[left - 1]\n                right -= 1 while left < right && nums[right] == nums[right + 1]\n                \n                left += 1\n                right -= 1\n            elsif current_sum < 0\n                left += 1\n            else\n                right -= 1\n            end\n        end\n    end\n    \n    result\nend",
                "testCases": [
                    {"input": "[-1,0,1,2,-1,-4]", "expected_output": "[[-1,-1,2],[-1,0,1]]", "weight": 0.5, "description": "Standard case with multiple triplets"},
                    {"input": "[0,1,1]", "expected_output": "[]", "weight": 0.25, "description": "No valid triplets"},
                    {"input": "[0,0,0]", "expected_output": "[[0,0,0]]", "weight": 0.25, "description": "All zeros"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    vector<vector<int>> threeSum(vector<int>& nums) {\n        // Your code here\n        return {};\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    vector<vector<int>> threeSum(vector<int>& nums) {\n        sort(nums.begin(), nums.end());\n        vector<vector<int>> result;\n        \n        for (int i = 0; i < nums.size() - 2; i++) {\n            if (i > 0 && nums[i] == nums[i - 1]) {\n                continue;\n            }\n            \n            int left = i + 1, right = nums.size() - 1;\n            \n            while (left < right) {\n                int currentSum = nums[i] + nums[left] + nums[right];\n                \n                if (currentSum == 0) {\n                    result.push_back({nums[i], nums[left], nums[right]});\n                    \n                    while (left < right && nums[left] == nums[left + 1]) {\n                        left++;\n                    }\n                    while (left < right && nums[right] == nums[right - 1]) {\n                        right--;\n                    }\n                    \n                    left++;\n                    right--;\n                } else if (currentSum < 0) {\n                    left++;\n                } else {\n                    right--;\n                }\n            }\n        }\n        \n        return result;\n    }\n};",
                "testCases": [
                    {"input": "[-1,0,1,2,-1,-4]", "expected_output": "[[-1,-1,2],[-1,0,1]]", "weight": 0.5, "description": "Standard case with multiple triplets"},
                    {"input": "[0,1,1]", "expected_output": "[]", "weight": 0.25, "description": "No valid triplets"},
                    {"input": "[0,0,0]", "expected_output": "[[0,0,0]]", "weight": 0.25, "description": "All zeros"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n^2)",
            "spaceComplexity": "O(1)",
            "constraints": ["3 <= nums.length <= 3000", "-10^5 <= nums[i] <= 10^5"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 25,
            "tags": ["array", "two-pointers", "sorting"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Two Pointers"
        }
    })

    # Sorting & Searching - Medium: Search in Rotated Sorted Array
    questions.append({
        "id": "search-in-rotated-sorted-array",
        "title": "Search in Rotated Sorted Array",
        "text": "There is an integer array nums sorted in ascending order (with distinct values).\n\nPrior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].\n\nGiven the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.\n\nYou must write an algorithm with O(log n) runtime complexity.\n\n**Example 1:**\nInput: nums = [4,5,6,7,0,1,2], target = 0\nOutput: 4\n\n**Example 2:**\nInput: nums = [4,5,6,7,0,1,2], target = 3\nOutput: -1\n\n**Example 3:**\nInput: nums = [1], target = 0\nOutput: -1",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def search(self, nums, target):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def search(self, nums, target):\n        left, right = 0, len(nums) - 1\n        \n        while left <= right:\n            mid = (left + right) // 2\n            \n            if nums[mid] == target:\n                return mid\n            \n            # Check if left half is sorted\n            if nums[left] <= nums[mid]:\n                # Target is in the left sorted half\n                if nums[left] <= target < nums[mid]:\n                    right = mid - 1\n                else:\n                    left = mid + 1\n            else:\n                # Right half is sorted\n                # Target is in the right sorted half\n                if nums[mid] < target <= nums[right]:\n                    left = mid + 1\n                else:\n                    right = mid - 1\n        \n        return -1",
                "testCases": [
                    {"input": "[4,5,6,7,0,1,2], 0", "expected_output": "4", "weight": 0.4, "description": "Target in rotated part"},
                    {"input": "[4,5,6,7,0,1,2], 3", "expected_output": "-1", "weight": 0.3, "description": "Target not found"},
                    {"input": "[1], 0", "expected_output": "-1", "weight": 0.3, "description": "Single element, not found"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[]} nums\n * @param {number} target\n * @return {number}\n */\nvar search = function(nums, target) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[]} nums\n * @param {number} target\n * @return {number}\n */\nvar search = function(nums, target) {\n    let left = 0, right = nums.length - 1;\n    \n    while (left <= right) {\n        const mid = Math.floor((left + right) / 2);\n        \n        if (nums[mid] === target) {\n            return mid;\n        }\n        \n        // Check if left half is sorted\n        if (nums[left] <= nums[mid]) {\n            // Target is in the left sorted half\n            if (nums[left] <= target && target < nums[mid]) {\n                right = mid - 1;\n            } else {\n                left = mid + 1;\n            }\n        } else {\n            // Right half is sorted\n            // Target is in the right sorted half\n            if (nums[mid] < target && target <= nums[right]) {\n                left = mid + 1;\n            } else {\n                right = mid - 1;\n            }\n        }\n    }\n    \n    return -1;\n};",
                "testCases": [
                    {"input": "[4,5,6,7,0,1,2], 0", "expected_output": "4", "weight": 0.4, "description": "Target in rotated part"},
                    {"input": "[4,5,6,7,0,1,2], 3", "expected_output": "-1", "weight": 0.3, "description": "Target not found"},
                    {"input": "[1], 0", "expected_output": "-1", "weight": 0.3, "description": "Single element, not found"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int search(int[] nums, int target) {\n        // Your code here\n        return -1;\n    }\n}",
                "solutionCode": "class Solution {\n    public int search(int[] nums, int target) {\n        int left = 0, right = nums.length - 1;\n        \n        while (left <= right) {\n            int mid = left + (right - left) / 2;\n            \n            if (nums[mid] == target) {\n                return mid;\n            }\n            \n            // Check if left half is sorted\n            if (nums[left] <= nums[mid]) {\n                // Target is in the left sorted half\n                if (nums[left] <= target && target < nums[mid]) {\n                    right = mid - 1;\n                } else {\n                    left = mid + 1;\n                }\n            } else {\n                // Right half is sorted\n                // Target is in the right sorted half\n                if (nums[mid] < target && target <= nums[right]) {\n                    left = mid + 1;\n                } else {\n                    right = mid - 1;\n                }\n            }\n        }\n        \n        return -1;\n    }\n}",
                "testCases": [
                    {"input": "[4,5,6,7,0,1,2], 0", "expected_output": "4", "weight": 0.4, "description": "Target in rotated part"},
                    {"input": "[4,5,6,7,0,1,2], 3", "expected_output": "-1", "weight": 0.3, "description": "Target not found"},
                    {"input": "[1], 0", "expected_output": "-1", "weight": 0.3, "description": "Single element, not found"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func search(nums []int, target int) int {\n    // Your code here\n    return -1\n}",
                "solutionCode": "func search(nums []int, target int) int {\n    left, right := 0, len(nums)-1\n    \n    for left <= right {\n        mid := left + (right-left)/2\n        \n        if nums[mid] == target {\n            return mid\n        }\n        \n        // Check if left half is sorted\n        if nums[left] <= nums[mid] {\n            // Target is in the left sorted half\n            if nums[left] <= target && target < nums[mid] {\n                right = mid - 1\n            } else {\n                left = mid + 1\n            }\n        } else {\n            // Right half is sorted\n            // Target is in the right sorted half\n            if nums[mid] < target && target <= nums[right] {\n                left = mid + 1\n            } else {\n                right = mid - 1\n            }\n        }\n    }\n    \n    return -1\n}",
                "testCases": [
                    {"input": "[4,5,6,7,0,1,2], 0", "expected_output": "4", "weight": 0.4, "description": "Target in rotated part"},
                    {"input": "[4,5,6,7,0,1,2], 3", "expected_output": "-1", "weight": 0.3, "description": "Target not found"},
                    {"input": "[1], 0", "expected_output": "-1", "weight": 0.3, "description": "Single element, not found"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[]} nums\n# @param {Integer} target\n# @return {Integer}\ndef search(nums, target)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[]} nums\n# @param {Integer} target\n# @return {Integer}\ndef search(nums, target)\n    left, right = 0, nums.length - 1\n    \n    while left <= right\n        mid = left + (right - left) / 2\n        \n        return mid if nums[mid] == target\n        \n        # Check if left half is sorted\n        if nums[left] <= nums[mid]\n            # Target is in the left sorted half\n            if nums[left] <= target && target < nums[mid]\n                right = mid - 1\n            else\n                left = mid + 1\n            end\n        else\n            # Right half is sorted\n            # Target is in the right sorted half\n            if nums[mid] < target && target <= nums[right]\n                left = mid + 1\n            else\n                right = mid - 1\n            end\n        end\n    end\n    \n    -1\nend",
                "testCases": [
                    {"input": "[4,5,6,7,0,1,2], 0", "expected_output": "4", "weight": 0.4, "description": "Target in rotated part"},
                    {"input": "[4,5,6,7,0,1,2], 3", "expected_output": "-1", "weight": 0.3, "description": "Target not found"},
                    {"input": "[1], 0", "expected_output": "-1", "weight": 0.3, "description": "Single element, not found"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    int search(vector<int>& nums, int target) {\n        // Your code here\n        return -1;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    int search(vector<int>& nums, int target) {\n        int left = 0, right = nums.size() - 1;\n        \n        while (left <= right) {\n            int mid = left + (right - left) / 2;\n            \n            if (nums[mid] == target) {\n                return mid;\n            }\n            \n            // Check if left half is sorted\n            if (nums[left] <= nums[mid]) {\n                // Target is in the left sorted half\n                if (nums[left] <= target && target < nums[mid]) {\n                    right = mid - 1;\n                } else {\n                    left = mid + 1;\n                }\n            } else {\n                // Right half is sorted\n                // Target is in the right sorted half\n                if (nums[mid] < target && target <= nums[right]) {\n                    left = mid + 1;\n                } else {\n                    right = mid - 1;\n                }\n            }\n        }\n        \n        return -1;\n    }\n};",
                "testCases": [
                    {"input": "[4,5,6,7,0,1,2], 0", "expected_output": "4", "weight": 0.4, "description": "Target in rotated part"},
                    {"input": "[4,5,6,7,0,1,2], 3", "expected_output": "-1", "weight": 0.3, "description": "Target not found"},
                    {"input": "[1], 0", "expected_output": "-1", "weight": 0.3, "description": "Single element, not found"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(log n)",
            "spaceComplexity": "O(1)",
            "constraints": ["1 <= nums.length <= 5000", "-10^4 <= nums[i] <= 10^4", "All values of nums are unique", "nums is an ascending array that is possibly rotated", "-10^4 <= target <= 10^4"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 25,
            "tags": ["array", "binary-search"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Sorting & Searching"
        }
    })

    # Math & Geometry - Easy: Pow(x, n)
    questions.append({
        "id": "powx-n",
        "title": "Pow(x, n)",
        "text": "Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).\n\n**Example 1:**\nInput: x = 2.00000, n = 10\nOutput: 1024.00000\n\n**Example 2:**\nInput: x = 2.10000, n = 3\nOutput: 9.26100\n\n**Example 3:**\nInput: x = 2.00000, n = -2\nOutput: 0.25000\nExplanation: 2^-2 = 1/2^2 = 1/4 = 0.25",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def myPow(self, x, n):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def myPow(self, x, n):\n        if n == 0:\n            return 1\n        \n        if n < 0:\n            x = 1 / x\n            n = -n\n        \n        result = 1\n        current_power = x\n        \n        while n > 0:\n            if n % 2 == 1:\n                result *= current_power\n            current_power *= current_power\n            n //= 2\n        \n        return result",
                "testCases": [
                    {"input": "2.00000, 10", "expected_output": "1024.00000", "weight": 0.4, "description": "Positive power"},
                    {"input": "2.10000, 3", "expected_output": "9.26100", "weight": 0.3, "description": "Decimal base"},
                    {"input": "2.00000, -2", "expected_output": "0.25000", "weight": 0.3, "description": "Negative power"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number} x\n * @param {number} n\n * @return {number}\n */\nvar myPow = function(x, n) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number} x\n * @param {number} n\n * @return {number}\n */\nvar myPow = function(x, n) {\n    if (n === 0) {\n        return 1;\n    }\n    \n    if (n < 0) {\n        x = 1 / x;\n        n = -n;\n    }\n    \n    let result = 1;\n    let currentPower = x;\n    \n    while (n > 0) {\n        if (n % 2 === 1) {\n            result *= currentPower;\n        }\n        currentPower *= currentPower;\n        n = Math.floor(n / 2);\n    }\n    \n    return result;\n};",
                "testCases": [
                    {"input": "2.00000, 10", "expected_output": "1024.00000", "weight": 0.4, "description": "Positive power"},
                    {"input": "2.10000, 3", "expected_output": "9.26100", "weight": 0.3, "description": "Decimal base"},
                    {"input": "2.00000, -2", "expected_output": "0.25000", "weight": 0.3, "description": "Negative power"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public double myPow(double x, int n) {\n        // Your code here\n        return 0.0;\n    }\n}",
                "solutionCode": "class Solution {\n    public double myPow(double x, int n) {\n        if (n == 0) {\n            return 1;\n        }\n        \n        long longN = n;\n        if (longN < 0) {\n            x = 1 / x;\n            longN = -longN;\n        }\n        \n        double result = 1;\n        double currentPower = x;\n        \n        while (longN > 0) {\n            if (longN % 2 == 1) {\n                result *= currentPower;\n            }\n            currentPower *= currentPower;\n            longN /= 2;\n        }\n        \n        return result;\n    }\n}",
                "testCases": [
                    {"input": "2.00000, 10", "expected_output": "1024.00000", "weight": 0.4, "description": "Positive power"},
                    {"input": "2.10000, 3", "expected_output": "9.26100", "weight": 0.3, "description": "Decimal base"},
                    {"input": "2.00000, -2", "expected_output": "0.25000", "weight": 0.3, "description": "Negative power"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func myPow(x float64, n int) float64 {\n    // Your code here\n    return 0.0\n}",
                "solutionCode": "func myPow(x float64, n int) float64 {\n    if n == 0 {\n        return 1\n    }\n    \n    longN := int64(n)\n    if longN < 0 {\n        x = 1 / x\n        longN = -longN\n    }\n    \n    result := 1.0\n    currentPower := x\n    \n    for longN > 0 {\n        if longN%2 == 1 {\n            result *= currentPower\n        }\n        currentPower *= currentPower\n        longN /= 2\n    }\n    \n    return result\n}",
                "testCases": [
                    {"input": "2.00000, 10", "expected_output": "1024.00000", "weight": 0.4, "description": "Positive power"},
                    {"input": "2.10000, 3", "expected_output": "9.26100", "weight": 0.3, "description": "Decimal base"},
                    {"input": "2.00000, -2", "expected_output": "0.25000", "weight": 0.3, "description": "Negative power"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Float} x\n# @param {Integer} n\n# @return {Float}\ndef my_pow(x, n)\n    # Your code here\nend",
                "solutionCode": "# @param {Float} x\n# @param {Integer} n\n# @return {Float}\ndef my_pow(x, n)\n    return 1 if n == 0\n    \n    if n < 0\n        x = 1.0 / x\n        n = -n\n    end\n    \n    result = 1.0\n    current_power = x\n    \n    while n > 0\n        if n % 2 == 1\n            result *= current_power\n        end\n        current_power *= current_power\n        n /= 2\n    end\n    \n    result\nend",
                "testCases": [
                    {"input": "2.00000, 10", "expected_output": "1024.00000", "weight": 0.4, "description": "Positive power"},
                    {"input": "2.10000, 3", "expected_output": "9.26100", "weight": 0.3, "description": "Decimal base"},
                    {"input": "2.00000, -2", "expected_output": "0.25000", "weight": 0.3, "description": "Negative power"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    double myPow(double x, int n) {\n        // Your code here\n        return 0.0;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    double myPow(double x, int n) {\n        if (n == 0) {\n            return 1;\n        }\n        \n        long long longN = n;\n        if (longN < 0) {\n            x = 1 / x;\n            longN = -longN;\n        }\n        \n        double result = 1;\n        double currentPower = x;\n        \n        while (longN > 0) {\n            if (longN % 2 == 1) {\n                result *= currentPower;\n            }\n            currentPower *= currentPower;\n            longN /= 2;\n        }\n        \n        return result;\n    }\n};",
                "testCases": [
                    {"input": "2.00000, 10", "expected_output": "1024.00000", "weight": 0.4, "description": "Positive power"},
                    {"input": "2.10000, 3", "expected_output": "9.26100", "weight": 0.3, "description": "Decimal base"},
                    {"input": "2.00000, -2", "expected_output": "0.25000", "weight": 0.3, "description": "Negative power"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(log n)",
            "spaceComplexity": "O(1)",
            "constraints": ["-100.0 < x < 100.0", "-2^31 <= n <= 2^31-1", "n is an integer", "-10^4 <= x^n <= 10^4"]
        },
        "gradingRules": {
            "testCaseWeight": 0.7,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 20,
            "tags": ["math", "recursion"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Math & Geometry"
        }
    })

    # Trees & Graphs - Hard: Word Ladder
    questions.append({
        "id": "word-ladder",
        "title": "Word Ladder",
        "text": "A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:\n\n- Every adjacent pair of words differs by a single letter.\n- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.\n- sk == endWord\n\nGiven two words, beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.\n\n**Example 1:**\nInput: beginWord = \"hit\", endWord = \"cog\", wordList = [\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]\nOutput: 5\nExplanation: One shortest transformation sequence is \"hit\" -> \"hot\" -> \"dot\" -> \"dog\" -> \"cog\", which is 5 words long.\n\n**Example 2:**\nInput: beginWord = \"hit\", endWord = \"cog\", wordList = [\"hot\",\"dot\",\"dog\",\"lot\",\"log\"]\nOutput: 0\nExplanation: The endWord \"cog\" is not in wordList, therefore there is no valid transformation sequence.",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def ladderLength(self, beginWord, endWord, wordList):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def ladderLength(self, beginWord, endWord, wordList):\n        if endWord not in wordList:\n            return 0\n        \n        from collections import deque\n        \n        wordSet = set(wordList)\n        queue = deque([(beginWord, 1)])\n        visited = {beginWord}\n        \n        while queue:\n            word, length = queue.popleft()\n            \n            if word == endWord:\n                return length\n            \n            # Try changing each character\n            for i in range(len(word)):\n                for c in 'abcdefghijklmnopqrstuvwxyz':\n                    if c != word[i]:\n                        newWord = word[:i] + c + word[i+1:]\n                        if newWord in wordSet and newWord not in visited:\n                            visited.add(newWord)\n                            queue.append((newWord, length + 1))\n        \n        return 0",
                "testCases": [
                    {"input": "\"hit\", \"cog\", [\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]", "expected_output": "5", "weight": 0.6, "description": "Valid transformation path"},
                    {"input": "\"hit\", \"cog\", [\"hot\",\"dot\",\"dog\",\"lot\",\"log\"]", "expected_output": "0", "weight": 0.4, "description": "No valid path"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {string} beginWord\n * @param {string} endWord\n * @param {string[]} wordList\n * @return {number}\n */\nvar ladderLength = function(beginWord, endWord, wordList) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {string} beginWord\n * @param {string} endWord\n * @param {string[]} wordList\n * @return {number}\n */\nvar ladderLength = function(beginWord, endWord, wordList) {\n    if (!wordList.includes(endWord)) {\n        return 0;\n    }\n    \n    const wordSet = new Set(wordList);\n    const queue = [[beginWord, 1]];\n    const visited = new Set([beginWord]);\n    \n    while (queue.length > 0) {\n        const [word, length] = queue.shift();\n        \n        if (word === endWord) {\n            return length;\n        }\n        \n        for (let i = 0; i < word.length; i++) {\n            for (let c = 97; c <= 122; c++) { // a-z\n                const char = String.fromCharCode(c);\n                if (char !== word[i]) {\n                    const newWord = word.slice(0, i) + char + word.slice(i + 1);\n                    if (wordSet.has(newWord) && !visited.has(newWord)) {\n                        visited.add(newWord);\n                        queue.push([newWord, length + 1]);\n                    }\n                }\n            }\n        }\n    }\n    \n    return 0;\n};",
                "testCases": [
                    {"input": "\"hit\", \"cog\", [\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]", "expected_output": "5", "weight": 0.6, "description": "Valid transformation path"},
                    {"input": "\"hit\", \"cog\", [\"hot\",\"dot\",\"dog\",\"lot\",\"log\"]", "expected_output": "0", "weight": 0.4, "description": "No valid path"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int ladderLength(String beginWord, String endWord, List<String> wordList) {\n        // Your code here\n        return 0;\n    }\n}",
                "solutionCode": "class Solution {\n    public int ladderLength(String beginWord, String endWord, List<String> wordList) {\n        Set<String> wordSet = new HashSet<>(wordList);\n        if (!wordSet.contains(endWord)) {\n            return 0;\n        }\n        \n        Queue<String> queue = new LinkedList<>();\n        Set<String> visited = new HashSet<>();\n        queue.offer(beginWord);\n        visited.add(beginWord);\n        \n        int level = 1;\n        \n        while (!queue.isEmpty()) {\n            int size = queue.size();\n            \n            for (int i = 0; i < size; i++) {\n                String word = queue.poll();\n                \n                if (word.equals(endWord)) {\n                    return level;\n                }\n                \n                char[] chars = word.toCharArray();\n                for (int j = 0; j < chars.length; j++) {\n                    char originalChar = chars[j];\n                    \n                    for (char c = 'a'; c <= 'z'; c++) {\n                        if (c != originalChar) {\n                            chars[j] = c;\n                            String newWord = new String(chars);\n                            \n                            if (wordSet.contains(newWord) && !visited.contains(newWord)) {\n                                visited.add(newWord);\n                                queue.offer(newWord);\n                            }\n                        }\n                    }\n                    \n                    chars[j] = originalChar;\n                }\n            }\n            \n            level++;\n        }\n        \n        return 0;\n    }\n}",
                "testCases": [
                    {"input": "\"hit\", \"cog\", [\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]", "expected_output": "5", "weight": 0.6, "description": "Valid transformation path"},
                    {"input": "\"hit\", \"cog\", [\"hot\",\"dot\",\"dog\",\"lot\",\"log\"]", "expected_output": "0", "weight": 0.4, "description": "No valid path"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func ladderLength(beginWord string, endWord string, wordList []string) int {\n    // Your code here\n    return 0\n}",
                "solutionCode": "func ladderLength(beginWord string, endWord string, wordList []string) int {\n    wordSet := make(map[string]bool)\n    for _, word := range wordList {\n        wordSet[word] = true\n    }\n    \n    if !wordSet[endWord] {\n        return 0\n    }\n    \n    queue := [][]interface{}{{beginWord, 1}}\n    visited := make(map[string]bool)\n    visited[beginWord] = true\n    \n    for len(queue) > 0 {\n        current := queue[0]\n        queue = queue[1:]\n        word := current[0].(string)\n        length := current[1].(int)\n        \n        if word == endWord {\n            return length\n        }\n        \n        for i := 0; i < len(word); i++ {\n            for c := 'a'; c <= 'z'; c++ {\n                if rune(word[i]) != c {\n                    newWord := word[:i] + string(c) + word[i+1:]\n                    if wordSet[newWord] && !visited[newWord] {\n                        visited[newWord] = true\n                        queue = append(queue, []interface{}{newWord, length + 1})\n                    }\n                }\n            }\n        }\n    }\n    \n    return 0\n}",
                "testCases": [
                    {"input": "\"hit\", \"cog\", [\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]", "expected_output": "5", "weight": 0.6, "description": "Valid transformation path"},
                    {"input": "\"hit\", \"cog\", [\"hot\",\"dot\",\"dog\",\"lot\",\"log\"]", "expected_output": "0", "weight": 0.4, "description": "No valid path"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {String} begin_word\n# @param {String} end_word\n# @param {String[]} word_list\n# @return {Integer}\ndef ladder_length(begin_word, end_word, word_list)\n    # Your code here\nend",
                "solutionCode": "# @param {String} begin_word\n# @param {String} end_word\n# @param {String[]} word_list\n# @return {Integer}\ndef ladder_length(begin_word, end_word, word_list)\n    return 0 unless word_list.include?(end_word)\n    \n    word_set = word_list.to_set\n    queue = [[begin_word, 1]]\n    visited = Set.new([begin_word])\n    \n    until queue.empty?\n        word, length = queue.shift\n        \n        return length if word == end_word\n        \n        word.length.times do |i|\n            ('a'..'z').each do |c|\n                next if c == word[i]\n                \n                new_word = word[0...i] + c + word[i+1..-1]\n                if word_set.include?(new_word) && !visited.include?(new_word)\n                    visited.add(new_word)\n                    queue << [new_word, length + 1]\n                end\n            end\n        end\n    end\n    \n    0\nend",
                "testCases": [
                    {"input": "\"hit\", \"cog\", [\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]", "expected_output": "5", "weight": 0.6, "description": "Valid transformation path"},
                    {"input": "\"hit\", \"cog\", [\"hot\",\"dot\",\"dog\",\"lot\",\"log\"]", "expected_output": "0", "weight": 0.4, "description": "No valid path"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {\n        // Your code here\n        return 0;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {\n        unordered_set<string> wordSet(wordList.begin(), wordList.end());\n        if (wordSet.find(endWord) == wordSet.end()) {\n            return 0;\n        }\n        \n        queue<pair<string, int>> q;\n        unordered_set<string> visited;\n        q.push({beginWord, 1});\n        visited.insert(beginWord);\n        \n        while (!q.empty()) {\n            auto [word, length] = q.front();\n            q.pop();\n            \n            if (word == endWord) {\n                return length;\n            }\n            \n            for (int i = 0; i < word.length(); i++) {\n                char originalChar = word[i];\n                \n                for (char c = 'a'; c <= 'z'; c++) {\n                    if (c != originalChar) {\n                        word[i] = c;\n                        \n                        if (wordSet.find(word) != wordSet.end() && \n                            visited.find(word) == visited.end()) {\n                            visited.insert(word);\n                            q.push({word, length + 1});\n                        }\n                    }\n                }\n                \n                word[i] = originalChar;\n            }\n        }\n        \n        return 0;\n    }\n};",
                "testCases": [
                    {"input": "\"hit\", \"cog\", [\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]", "expected_output": "5", "weight": 0.6, "description": "Valid transformation path"},
                    {"input": "\"hit\", \"cog\", [\"hot\",\"dot\",\"dog\",\"lot\",\"log\"]", "expected_output": "0", "weight": 0.4, "description": "No valid path"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(M^2 * N)",
            "spaceComplexity": "O(M * N)",
            "constraints": ["1 <= beginWord.length <= 10", "endWord.length == beginWord.length", "1 <= wordList.length <= 5000", "wordList[i].length == beginWord.length", "beginWord, endWord, and wordList[i] consist of lowercase English letters", "beginWord != endWord", "All the strings in wordList are unique"]
        },
        "gradingRules": {
            "testCaseWeight": 0.5,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.3,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "HARD",
            "estimatedDuration": 35,
            "tags": ["hash-table", "string", "breadth-first-search"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Trees & Graphs"
        }
    })

    # Bit Manipulation - Medium: Counting Bits
    questions.append({
        "id": "counting-bits",
        "title": "Counting Bits",
        "text": "Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.\n\n**Example 1:**\nInput: n = 2\nOutput: [0,1,1]\nExplanation:\n0 --> 0\n1 --> 1\n2 --> 10\n\n**Example 2:**\nInput: n = 5\nOutput: [0,1,1,2,1,2]\nExplanation:\n0 --> 0\n1 --> 1\n2 --> 10\n3 --> 11\n4 --> 100\n5 --> 101",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def countBits(self, n):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def countBits(self, n):\n        dp = [0] * (n + 1)\n        \n        for i in range(1, n + 1):\n            # dp[i] = dp[i >> 1] + (i & 1)\n            # Number of 1s in i = number of 1s in i//2 + (1 if i is odd else 0)\n            dp[i] = dp[i >> 1] + (i & 1)\n        \n        return dp",
                "testCases": [
                    {"input": "2", "expected_output": "[0,1,1]", "weight": 0.5, "description": "Small case"},
                    {"input": "5", "expected_output": "[0,1,1,2,1,2]", "weight": 0.5, "description": "Standard case"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number} n\n * @return {number[]}\n */\nvar countBits = function(n) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number} n\n * @return {number[]}\n */\nvar countBits = function(n) {\n    const dp = new Array(n + 1).fill(0);\n    \n    for (let i = 1; i <= n; i++) {\n        dp[i] = dp[i >> 1] + (i & 1);\n    }\n    \n    return dp;\n};",
                "testCases": [
                    {"input": "2", "expected_output": "[0,1,1]", "weight": 0.5, "description": "Small case"},
                    {"input": "5", "expected_output": "[0,1,1,2,1,2]", "weight": 0.5, "description": "Standard case"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int[] countBits(int n) {\n        // Your code here\n        return new int[0];\n    }\n}",
                "solutionCode": "class Solution {\n    public int[] countBits(int n) {\n        int[] dp = new int[n + 1];\n        \n        for (int i = 1; i <= n; i++) {\n            dp[i] = dp[i >> 1] + (i & 1);\n        }\n        \n        return dp;\n    }\n}",
                "testCases": [
                    {"input": "2", "expected_output": "[0,1,1]", "weight": 0.5, "description": "Small case"},
                    {"input": "5", "expected_output": "[0,1,1,2,1,2]", "weight": 0.5, "description": "Standard case"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func countBits(n int) []int {\n    // Your code here\n    return []int{}\n}",
                "solutionCode": "func countBits(n int) []int {\n    dp := make([]int, n+1)\n    \n    for i := 1; i <= n; i++ {\n        dp[i] = dp[i>>1] + (i&1)\n    }\n    \n    return dp\n}",
                "testCases": [
                    {"input": "2", "expected_output": "[0,1,1]", "weight": 0.5, "description": "Small case"},
                    {"input": "5", "expected_output": "[0,1,1,2,1,2]", "weight": 0.5, "description": "Standard case"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer} n\n# @return {Integer[]}\ndef count_bits(n)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer} n\n# @return {Integer[]}\ndef count_bits(n)\n    dp = Array.new(n + 1, 0)\n    \n    (1..n).each do |i|\n        dp[i] = dp[i >> 1] + (i & 1)\n    end\n    \n    dp\nend",
                "testCases": [
                    {"input": "2", "expected_output": "[0,1,1]", "weight": 0.5, "description": "Small case"},
                    {"input": "5", "expected_output": "[0,1,1,2,1,2]", "weight": 0.5, "description": "Standard case"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    vector<int> countBits(int n) {\n        // Your code here\n        return {};\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    vector<int> countBits(int n) {\n        vector<int> dp(n + 1, 0);\n        \n        for (int i = 1; i <= n; i++) {\n            dp[i] = dp[i >> 1] + (i & 1);\n        }\n        \n        return dp;\n    }\n};",
                "testCases": [
                    {"input": "2", "expected_output": "[0,1,1]", "weight": 0.5, "description": "Small case"},
                    {"input": "5", "expected_output": "[0,1,1,2,1,2]", "weight": 0.5, "description": "Standard case"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(n)",
            "constraints": ["0 <= n <= 10^5"]
        },
        "gradingRules": {
            "testCaseWeight": 0.7,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "EASY",
            "estimatedDuration": 15,
            "tags": ["dynamic-programming", "bit-manipulation"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Bit Manipulation"
        }
    })

    # Recursion & Backtracking - Hard: N-Queens
    questions.append({
        "id": "n-queens",
        "title": "N-Queens",
        "text": "The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.\n\nGiven an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.\n\nEach solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.\n\n**Example 1:**\nInput: n = 4\nOutput: [[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"],[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"]]\nExplanation: There exist two distinct solutions to the 4-queens puzzle as shown above\n\n**Example 2:**\nInput: n = 1\nOutput: [[\"Q\"]]",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def solveNQueens(self, n):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def solveNQueens(self, n):\n        def is_safe(board, row, col):\n            # Check column\n            for i in range(row):\n                if board[i][col] == 'Q':\n                    return False\n            \n            # Check diagonal (top-left to bottom-right)\n            i, j = row - 1, col - 1\n            while i >= 0 and j >= 0:\n                if board[i][j] == 'Q':\n                    return False\n                i -= 1\n                j -= 1\n            \n            # Check diagonal (top-right to bottom-left)\n            i, j = row - 1, col + 1\n            while i >= 0 and j < n:\n                if board[i][j] == 'Q':\n                    return False\n                i -= 1\n                j += 1\n            \n            return True\n        \n        def backtrack(board, row):\n            if row == n:\n                result.append([''.join(row) for row in board])\n                return\n            \n            for col in range(n):\n                if is_safe(board, row, col):\n                    board[row][col] = 'Q'\n                    backtrack(board, row + 1)\n                    board[row][col] = '.'\n        \n        result = []\n        board = [['.' for _ in range(n)] for _ in range(n)]\n        backtrack(board, 0)\n        return result",
                "testCases": [
                    {"input": "4", "expected_output": "[[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"],[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"]]", "weight": 0.7, "description": "Standard 4x4 case"},
                    {"input": "1", "expected_output": "[[\"Q\"]]", "weight": 0.3, "description": "Base case"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number} n\n * @return {string[][]}\n */\nvar solveNQueens = function(n) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number} n\n * @return {string[][]}\n */\nvar solveNQueens = function(n) {\n    function isSafe(board, row, col) {\n        // Check column\n        for (let i = 0; i < row; i++) {\n            if (board[i][col] === 'Q') {\n                return false;\n            }\n        }\n        \n        // Check diagonal (top-left to bottom-right)\n        for (let i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {\n            if (board[i][j] === 'Q') {\n                return false;\n            }\n        }\n        \n        // Check diagonal (top-right to bottom-left)\n        for (let i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {\n            if (board[i][j] === 'Q') {\n                return false;\n            }\n        }\n        \n        return true;\n    }\n    \n    function backtrack(board, row) {\n        if (row === n) {\n            result.push(board.map(row => row.join('')));\n            return;\n        }\n        \n        for (let col = 0; col < n; col++) {\n            if (isSafe(board, row, col)) {\n                board[row][col] = 'Q';\n                backtrack(board, row + 1);\n                board[row][col] = '.';\n            }\n        }\n    }\n    \n    const result = [];\n    const board = Array(n).fill().map(() => Array(n).fill('.'));\n    backtrack(board, 0);\n    return result;\n};",
                "testCases": [
                    {"input": "4", "expected_output": "[[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"],[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"]]", "weight": 0.7, "description": "Standard 4x4 case"},
                    {"input": "1", "expected_output": "[[\"Q\"]]", "weight": 0.3, "description": "Base case"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public List<List<String>> solveNQueens(int n) {\n        // Your code here\n        return new ArrayList<>();\n    }\n}",
                "solutionCode": "class Solution {\n    public List<List<String>> solveNQueens(int n) {\n        List<List<String>> result = new ArrayList<>();\n        char[][] board = new char[n][n];\n        \n        // Initialize board\n        for (int i = 0; i < n; i++) {\n            for (int j = 0; j < n; j++) {\n                board[i][j] = '.';\n            }\n        }\n        \n        backtrack(board, 0, result);\n        return result;\n    }\n    \n    private void backtrack(char[][] board, int row, List<List<String>> result) {\n        if (row == board.length) {\n            List<String> solution = new ArrayList<>();\n            for (char[] r : board) {\n                solution.add(new String(r));\n            }\n            result.add(solution);\n            return;\n        }\n        \n        for (int col = 0; col < board.length; col++) {\n            if (isSafe(board, row, col)) {\n                board[row][col] = 'Q';\n                backtrack(board, row + 1, result);\n                board[row][col] = '.';\n            }\n        }\n    }\n    \n    private boolean isSafe(char[][] board, int row, int col) {\n        int n = board.length;\n        \n        // Check column\n        for (int i = 0; i < row; i++) {\n            if (board[i][col] == 'Q') {\n                return false;\n            }\n        }\n        \n        // Check diagonal (top-left to bottom-right)\n        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {\n            if (board[i][j] == 'Q') {\n                return false;\n            }\n        }\n        \n        // Check diagonal (top-right to bottom-left)\n        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {\n            if (board[i][j] == 'Q') {\n                return false;\n            }\n        }\n        \n        return true;\n    }\n}",
                "testCases": [
                    {"input": "4", "expected_output": "[[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"],[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"]]", "weight": 0.7, "description": "Standard 4x4 case"},
                    {"input": "1", "expected_output": "[[\"Q\"]]", "weight": 0.3, "description": "Base case"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func solveNQueens(n int) [][]string {\n    // Your code here\n    return [][]string{}\n}",
                "solutionCode": "func solveNQueens(n int) [][]string {\n    var result [][]string\n    board := make([][]rune, n)\n    for i := range board {\n        board[i] = make([]rune, n)\n        for j := range board[i] {\n            board[i][j] = '.'\n        }\n    }\n    \n    backtrack(board, 0, &result)\n    return result\n}\n\nfunc backtrack(board [][]rune, row int, result *[][]string) {\n    n := len(board)\n    if row == n {\n        solution := make([]string, n)\n        for i := 0; i < n; i++ {\n            solution[i] = string(board[i])\n        }\n        *result = append(*result, solution)\n        return\n    }\n    \n    for col := 0; col < n; col++ {\n        if isSafe(board, row, col) {\n            board[row][col] = 'Q'\n            backtrack(board, row+1, result)\n            board[row][col] = '.'\n        }\n    }\n}\n\nfunc isSafe(board [][]rune, row, col int) bool {\n    n := len(board)\n    \n    // Check column\n    for i := 0; i < row; i++ {\n        if board[i][col] == 'Q' {\n            return false\n        }\n    }\n    \n    // Check diagonal (top-left to bottom-right)\n    for i, j := row-1, col-1; i >= 0 && j >= 0; i, j = i-1, j-1 {\n        if board[i][j] == 'Q' {\n            return false\n        }\n    }\n    \n    // Check diagonal (top-right to bottom-left)\n    for i, j := row-1, col+1; i >= 0 && j < n; i, j = i-1, j+1 {\n        if board[i][j] == 'Q' {\n            return false\n        }\n    }\n    \n    return true\n}",
                "testCases": [
                    {"input": "4", "expected_output": "[[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"],[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"]]", "weight": 0.7, "description": "Standard 4x4 case"},
                    {"input": "1", "expected_output": "[[\"Q\"]]", "weight": 0.3, "description": "Base case"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer} n\n# @return {String[][]}\ndef solve_n_queens(n)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer} n\n# @return {String[][]}\ndef solve_n_queens(n)\n    def is_safe(board, row, col, n)\n        # Check column\n        (0...row).each do |i|\n            return false if board[i][col] == 'Q'\n        end\n        \n        # Check diagonal (top-left to bottom-right)\n        i, j = row - 1, col - 1\n        while i >= 0 && j >= 0\n            return false if board[i][j] == 'Q'\n            i -= 1\n            j -= 1\n        end\n        \n        # Check diagonal (top-right to bottom-left)\n        i, j = row - 1, col + 1\n        while i >= 0 && j < n\n            return false if board[i][j] == 'Q'\n            i -= 1\n            j += 1\n        end\n        \n        true\n    end\n    \n    def backtrack(board, row, n, result)\n        if row == n\n            result << board.map(&:join)\n            return\n        end\n        \n        (0...n).each do |col|\n            if is_safe(board, row, col, n)\n                board[row][col] = 'Q'\n                backtrack(board, row + 1, n, result)\n                board[row][col] = '.'\n            end\n        end\n    end\n    \n    result = []\n    board = Array.new(n) { Array.new(n, '.') }\n    backtrack(board, 0, n, result)\n    result\nend",
                "testCases": [
                    {"input": "4", "expected_output": "[[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"],[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"]]", "weight": 0.7, "description": "Standard 4x4 case"},
                    {"input": "1", "expected_output": "[[\"Q\"]]", "weight": 0.3, "description": "Base case"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    vector<vector<string>> solveNQueens(int n) {\n        // Your code here\n        return {};\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    vector<vector<string>> solveNQueens(int n) {\n        vector<vector<string>> result;\n        vector<string> board(n, string(n, '.'));\n        backtrack(board, 0, result);\n        return result;\n    }\n    \nprivate:\n    void backtrack(vector<string>& board, int row, vector<vector<string>>& result) {\n        if (row == board.size()) {\n            result.push_back(board);\n            return;\n        }\n        \n        for (int col = 0; col < board.size(); col++) {\n            if (isSafe(board, row, col)) {\n                board[row][col] = 'Q';\n                backtrack(board, row + 1, result);\n                board[row][col] = '.';\n            }\n        }\n    }\n    \n    bool isSafe(vector<string>& board, int row, int col) {\n        int n = board.size();\n        \n        // Check column\n        for (int i = 0; i < row; i++) {\n            if (board[i][col] == 'Q') {\n                return false;\n            }\n        }\n        \n        // Check diagonal (top-left to bottom-right)\n        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {\n            if (board[i][j] == 'Q') {\n                return false;\n            }\n        }\n        \n        // Check diagonal (top-right to bottom-left)\n        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {\n            if (board[i][j] == 'Q') {\n                return false;\n            }\n        }\n        \n        return true;\n    }\n};",
                "testCases": [
                    {"input": "4", "expected_output": "[[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"],[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"]]", "weight": 0.7, "description": "Standard 4x4 case"},
                    {"input": "1", "expected_output": "[[\"Q\"]]", "weight": 0.3, "description": "Base case"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(N!)",
            "spaceComplexity": "O(N^2)",
            "constraints": ["1 <= n <= 9"]
        },
        "gradingRules": {
            "testCaseWeight": 0.5,
            "codeQualityWeight": 0.3,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "HARD",
            "estimatedDuration": 40,
            "tags": ["array", "backtracking"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Recursion & Backtracking"
        }
    })

    # Sliding Window - Hard: Minimum Window Substring
    questions.append({
        "id": "minimum-window-substring-sliding",
        "title": "Minimum Window Substring",
        "text": "Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string \"\".\n\nThe testcases will be generated such that the answer is unique.\n\n**Example 1:**\nInput: s = \"ADOBECODEBANC\", t = \"ABC\"\nOutput: \"BANC\"\nExplanation: The minimum window substring \"BANC\" includes 'A', 'B', and 'C' from string t.\n\n**Example 2:**\nInput: s = \"a\", t = \"a\"\nOutput: \"a\"\nExplanation: The entire string s is the minimum window.\n\n**Example 3:**\nInput: s = \"a\", t = \"aa\"\nOutput: \"\"\nExplanation: Both 'a's from t must be included in the window.\nSince the largest window of s only has one 'a', return empty string.",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def minWindow(self, s, t):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def minWindow(self, s, t):\n        if not s or not t:\n            return \"\"\n        \n        from collections import Counter\n        \n        # Count characters in t\n        t_count = Counter(t)\n        required = len(t_count)\n        \n        # Sliding window variables\n        left = right = 0\n        formed = 0\n        window_counts = {}\n        \n        # Result\n        min_len = float('inf')\n        min_left = 0\n        \n        while right < len(s):\n            # Add character from right to window\n            char = s[right]\n            window_counts[char] = window_counts.get(char, 0) + 1\n            \n            # Check if current character's frequency matches t's frequency\n            if char in t_count and window_counts[char] == t_count[char]:\n                formed += 1\n            \n            # Try to contract window from left\n            while left <= right and formed == required:\n                char = s[left]\n                \n                # Update result if this window is smaller\n                if right - left + 1 < min_len:\n                    min_len = right - left + 1\n                    min_left = left\n                \n                # Remove character from left\n                window_counts[char] -= 1\n                if char in t_count and window_counts[char] < t_count[char]:\n                    formed -= 1\n                \n                left += 1\n            \n            right += 1\n        \n        return \"\" if min_len == float('inf') else s[min_left:min_left + min_len]",
                "testCases": [
                    {"input": "\"ADOBECODEBANC\", \"ABC\"", "expected_output": "\"BANC\"", "weight": 0.5, "description": "Standard case"},
                    {"input": "\"a\", \"a\"", "expected_output": "\"a\"", "weight": 0.25, "description": "Single character"},
                    {"input": "\"a\", \"aa\"", "expected_output": "\"\"", "weight": 0.25, "description": "Impossible case"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {string} s\n * @param {string} t\n * @return {string}\n */\nvar minWindow = function(s, t) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {string} s\n * @param {string} t\n * @return {string}\n */\nvar minWindow = function(s, t) {\n    if (!s || !t) return \"\";\n    \n    const tCount = {};\n    for (const char of t) {\n        tCount[char] = (tCount[char] || 0) + 1;\n    }\n    \n    const required = Object.keys(tCount).length;\n    let left = 0, right = 0;\n    let formed = 0;\n    const windowCounts = {};\n    \n    let minLen = Infinity;\n    let minLeft = 0;\n    \n    while (right < s.length) {\n        const char = s[right];\n        windowCounts[char] = (windowCounts[char] || 0) + 1;\n        \n        if (tCount[char] && windowCounts[char] === tCount[char]) {\n            formed++;\n        }\n        \n        while (left <= right && formed === required) {\n            const leftChar = s[left];\n            \n            if (right - left + 1 < minLen) {\n                minLen = right - left + 1;\n                minLeft = left;\n            }\n            \n            windowCounts[leftChar]--;\n            if (tCount[leftChar] && windowCounts[leftChar] < tCount[leftChar]) {\n                formed--;\n            }\n            \n            left++;\n        }\n        \n        right++;\n    }\n    \n    return minLen === Infinity ? \"\" : s.substring(minLeft, minLeft + minLen);\n};",
                "testCases": [
                    {"input": "\"ADOBECODEBANC\", \"ABC\"", "expected_output": "\"BANC\"", "weight": 0.5, "description": "Standard case"},
                    {"input": "\"a\", \"a\"", "expected_output": "\"a\"", "weight": 0.25, "description": "Single character"},
                    {"input": "\"a\", \"aa\"", "expected_output": "\"\"", "weight": 0.25, "description": "Impossible case"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public String minWindow(String s, String t) {\n        // Your code here\n        return \"\";\n    }\n}",
                "solutionCode": "class Solution {\n    public String minWindow(String s, String t) {\n        if (s.length() == 0 || t.length() == 0) {\n            return \"\";\n        }\n        \n        Map<Character, Integer> tCount = new HashMap<>();\n        for (char c : t.toCharArray()) {\n            tCount.put(c, tCount.getOrDefault(c, 0) + 1);\n        }\n        \n        int required = tCount.size();\n        int left = 0, right = 0;\n        int formed = 0;\n        Map<Character, Integer> windowCounts = new HashMap<>();\n        \n        int minLen = Integer.MAX_VALUE;\n        int minLeft = 0;\n        \n        while (right < s.length()) {\n            char c = s.charAt(right);\n            windowCounts.put(c, windowCounts.getOrDefault(c, 0) + 1);\n            \n            if (tCount.containsKey(c) && windowCounts.get(c).intValue() == tCount.get(c).intValue()) {\n                formed++;\n            }\n            \n            while (left <= right && formed == required) {\n                c = s.charAt(left);\n                \n                if (right - left + 1 < minLen) {\n                    minLen = right - left + 1;\n                    minLeft = left;\n                }\n                \n                windowCounts.put(c, windowCounts.get(c) - 1);\n                if (tCount.containsKey(c) && windowCounts.get(c).intValue() < tCount.get(c).intValue()) {\n                    formed--;\n                }\n                \n                left++;\n            }\n            \n            right++;\n        }\n        \n        return minLen == Integer.MAX_VALUE ? \"\" : s.substring(minLeft, minLeft + minLen);\n    }\n}",
                "testCases": [
                    {"input": "\"ADOBECODEBANC\", \"ABC\"", "expected_output": "\"BANC\"", "weight": 0.5, "description": "Standard case"},
                    {"input": "\"a\", \"a\"", "expected_output": "\"a\"", "weight": 0.25, "description": "Single character"},
                    {"input": "\"a\", \"aa\"", "expected_output": "\"\"", "weight": 0.25, "description": "Impossible case"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func minWindow(s string, t string) string {\n    // Your code here\n    return \"\"\n}",
                "solutionCode": "func minWindow(s string, t string) string {\n    if len(s) == 0 || len(t) == 0 {\n        return \"\"\n    }\n    \n    tCount := make(map[byte]int)\n    for i := 0; i < len(t); i++ {\n        tCount[t[i]]++\n    }\n    \n    required := len(tCount)\n    left, right := 0, 0\n    formed := 0\n    windowCounts := make(map[byte]int)\n    \n    minLen := len(s) + 1\n    minLeft := 0\n    \n    for right < len(s) {\n        c := s[right]\n        windowCounts[c]++\n        \n        if count, exists := tCount[c]; exists && windowCounts[c] == count {\n            formed++\n        }\n        \n        for left <= right && formed == required {\n            c = s[left]\n            \n            if right-left+1 < minLen {\n                minLen = right - left + 1\n                minLeft = left\n            }\n            \n            windowCounts[c]--\n            if count, exists := tCount[c]; exists && windowCounts[c] < count {\n                formed--\n            }\n            \n            left++\n        }\n        \n        right++\n    }\n    \n    if minLen == len(s)+1 {\n        return \"\"\n    }\n    return s[minLeft : minLeft+minLen]\n}",
                "testCases": [
                    {"input": "\"ADOBECODEBANC\", \"ABC\"", "expected_output": "\"BANC\"", "weight": 0.5, "description": "Standard case"},
                    {"input": "\"a\", \"a\"", "expected_output": "\"a\"", "weight": 0.25, "description": "Single character"},
                    {"input": "\"a\", \"aa\"", "expected_output": "\"\"", "weight": 0.25, "description": "Impossible case"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {String} s\n# @param {String} t\n# @return {String}\ndef min_window(s, t)\n    # Your code here\nend",
                "solutionCode": "# @param {String} s\n# @param {String} t\n# @return {String}\ndef min_window(s, t)\n    return \"\" if s.empty? || t.empty?\n    \n    t_count = Hash.new(0)\n    t.each_char { |c| t_count[c] += 1 }\n    \n    required = t_count.size\n    left = right = 0\n    formed = 0\n    window_counts = Hash.new(0)\n    \n    min_len = Float::INFINITY\n    min_left = 0\n    \n    while right < s.length\n        char = s[right]\n        window_counts[char] += 1\n        \n        if t_count.key?(char) && window_counts[char] == t_count[char]\n            formed += 1\n        end\n        \n        while left <= right && formed == required\n            char = s[left]\n            \n            if right - left + 1 < min_len\n                min_len = right - left + 1\n                min_left = left\n            end\n            \n            window_counts[char] -= 1\n            if t_count.key?(char) && window_counts[char] < t_count[char]\n                formed -= 1\n            end\n            \n            left += 1\n        end\n        \n        right += 1\n    end\n    \n    min_len == Float::INFINITY ? \"\" : s[min_left, min_len]\nend",
                "testCases": [
                    {"input": "\"ADOBECODEBANC\", \"ABC\"", "expected_output": "\"BANC\"", "weight": 0.5, "description": "Standard case"},
                    {"input": "\"a\", \"a\"", "expected_output": "\"a\"", "weight": 0.25, "description": "Single character"},
                    {"input": "\"a\", \"aa\"", "expected_output": "\"\"", "weight": 0.25, "description": "Impossible case"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    string minWindow(string s, string t) {\n        // Your code here\n        return \"\";\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    string minWindow(string s, string t) {\n        if (s.empty() || t.empty()) {\n            return \"\";\n        }\n        \n        unordered_map<char, int> tCount;\n        for (char c : t) {\n            tCount[c]++;\n        }\n        \n        int required = tCount.size();\n        int left = 0, right = 0;\n        int formed = 0;\n        unordered_map<char, int> windowCounts;\n        \n        int minLen = INT_MAX;\n        int minLeft = 0;\n        \n        while (right < s.length()) {\n            char c = s[right];\n            windowCounts[c]++;\n            \n            if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) {\n                formed++;\n            }\n            \n            while (left <= right && formed == required) {\n                c = s[left];\n                \n                if (right - left + 1 < minLen) {\n                    minLen = right - left + 1;\n                    minLeft = left;\n                }\n                \n                windowCounts[c]--;\n                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) {\n                    formed--;\n                }\n                \n                left++;\n            }\n            \n            right++;\n        }\n        \n        return minLen == INT_MAX ? \"\" : s.substr(minLeft, minLen);\n    }\n};",
                "testCases": [
                    {"input": "\"ADOBECODEBANC\", \"ABC\"", "expected_output": "\"BANC\"", "weight": 0.5, "description": "Standard case"},
                    {"input": "\"a\", \"a\"", "expected_output": "\"a\"", "weight": 0.25, "description": "Single character"},
                    {"input": "\"a\", \"aa\"", "expected_output": "\"\"", "weight": 0.25, "description": "Impossible case"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(|s| + |t|)",
            "spaceComplexity": "O(|s| + |t|)",
            "constraints": ["m == s.length", "n == t.length", "1 <= m, n <= 10^5", "s and t consist of uppercase and lowercase English letters"]
        },
        "gradingRules": {
            "testCaseWeight": 0.5,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.3,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "HARD",
            "estimatedDuration": 35,
            "tags": ["hash-table", "string", "sliding-window"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Sliding Window"
        }
    })

    # Greedy Algorithms - Medium: Meeting Rooms II
    questions.append({
        "id": "meeting-rooms-ii",
        "title": "Meeting Rooms II",
        "text": "Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.\n\n**Example 1:**\nInput: intervals = [[0,30],[5,10],[15,20]]\nOutput: 2\nExplanation: We need two meeting rooms:\n- Room 1: [0,30]\n- Room 2: [5,10], [15,20]\n\n**Example 2:**\nInput: intervals = [[7,10],[2,4]]\nOutput: 1\nExplanation: Only one meeting room is needed.",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def minMeetingRooms(self, intervals):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def minMeetingRooms(self, intervals):\n        if not intervals:\n            return 0\n        \n        import heapq\n        \n        # Sort intervals by start time\n        intervals.sort(key=lambda x: x[0])\n        \n        # Min heap to track end times of meetings\n        heap = []\n        \n        for interval in intervals:\n            start, end = interval\n            \n            # If the earliest ending meeting has ended, remove it\n            if heap and heap[0] <= start:\n                heapq.heappop(heap)\n            \n            # Add current meeting's end time\n            heapq.heappush(heap, end)\n        \n        # The size of heap is the number of rooms needed\n        return len(heap)",
                "testCases": [
                    {"input": "[[0,30],[5,10],[15,20]]", "expected_output": "2", "weight": 0.6, "description": "Overlapping meetings"},
                    {"input": "[[7,10],[2,4]]", "expected_output": "1", "weight": 0.4, "description": "Non-overlapping meetings"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[][]} intervals\n * @return {number}\n */\nvar minMeetingRooms = function(intervals) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[][]} intervals\n * @return {number}\n */\nvar minMeetingRooms = function(intervals) {\n    if (intervals.length === 0) {\n        return 0;\n    }\n    \n    // Sort intervals by start time\n    intervals.sort((a, b) => a[0] - b[0]);\n    \n    // Min heap to track end times\n    const heap = [];\n    \n    for (const interval of intervals) {\n        const [start, end] = interval;\n        \n        // If the earliest ending meeting has ended, remove it\n        if (heap.length > 0 && heap[0] <= start) {\n            heap.shift();\n            // Re-heapify after removal\n            heap.sort((a, b) => a - b);\n        }\n        \n        // Add current meeting's end time\n        heap.push(end);\n        heap.sort((a, b) => a - b);\n    }\n    \n    return heap.length;\n};",
                "testCases": [
                    {"input": "[[0,30],[5,10],[15,20]]", "expected_output": "2", "weight": 0.6, "description": "Overlapping meetings"},
                    {"input": "[[7,10],[2,4]]", "expected_output": "1", "weight": 0.4, "description": "Non-overlapping meetings"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int minMeetingRooms(int[][] intervals) {\n        // Your code here\n        return 0;\n    }\n}",
                "solutionCode": "class Solution {\n    public int minMeetingRooms(int[][] intervals) {\n        if (intervals.length == 0) {\n            return 0;\n        }\n        \n        // Sort intervals by start time\n        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);\n        \n        // Min heap to track end times\n        PriorityQueue<Integer> heap = new PriorityQueue<>();\n        \n        for (int[] interval : intervals) {\n            int start = interval[0];\n            int end = interval[1];\n            \n            // If the earliest ending meeting has ended, remove it\n            if (!heap.isEmpty() && heap.peek() <= start) {\n                heap.poll();\n            }\n            \n            // Add current meeting's end time\n            heap.offer(end);\n        }\n        \n        return heap.size();\n    }\n}",
                "testCases": [
                    {"input": "[[0,30],[5,10],[15,20]]", "expected_output": "2", "weight": 0.6, "description": "Overlapping meetings"},
                    {"input": "[[7,10],[2,4]]", "expected_output": "1", "weight": 0.4, "description": "Non-overlapping meetings"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func minMeetingRooms(intervals [][]int) int {\n    // Your code here\n    return 0\n}",
                "solutionCode": "import (\n    \"container/heap\"\n    \"sort\"\n)\n\ntype IntHeap []int\n\nfunc (h IntHeap) Len() int           { return len(h) }\nfunc (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }\nfunc (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }\n\nfunc (h *IntHeap) Push(x interface{}) {\n    *h = append(*h, x.(int))\n}\n\nfunc (h *IntHeap) Pop() interface{} {\n    old := *h\n    n := len(old)\n    x := old[n-1]\n    *h = old[0 : n-1]\n    return x\n}\n\nfunc minMeetingRooms(intervals [][]int) int {\n    if len(intervals) == 0 {\n        return 0\n    }\n    \n    // Sort intervals by start time\n    sort.Slice(intervals, func(i, j int) bool {\n        return intervals[i][0] < intervals[j][0]\n    })\n    \n    // Min heap to track end times\n    h := &IntHeap{}\n    heap.Init(h)\n    \n    for _, interval := range intervals {\n        start, end := interval[0], interval[1]\n        \n        // If the earliest ending meeting has ended, remove it\n        if h.Len() > 0 && (*h)[0] <= start {\n            heap.Pop(h)\n        }\n        \n        // Add current meeting's end time\n        heap.Push(h, end)\n    }\n    \n    return h.Len()\n}",
                "testCases": [
                    {"input": "[[0,30],[5,10],[15,20]]", "expected_output": "2", "weight": 0.6, "description": "Overlapping meetings"},
                    {"input": "[[7,10],[2,4]]", "expected_output": "1", "weight": 0.4, "description": "Non-overlapping meetings"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[][]} intervals\n# @return {Integer}\ndef min_meeting_rooms(intervals)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[][]} intervals\n# @return {Integer}\ndef min_meeting_rooms(intervals)\n    return 0 if intervals.empty?\n    \n    # Sort intervals by start time\n    intervals.sort_by! { |interval| interval[0] }\n    \n    # Array to track end times (simulating min heap)\n    heap = []\n    \n    intervals.each do |interval|\n        start, end_time = interval\n        \n        # If the earliest ending meeting has ended, remove it\n        if !heap.empty? && heap.min <= start\n            heap.delete(heap.min)\n        end\n        \n        # Add current meeting's end time\n        heap << end_time\n    end\n    \n    heap.length\nend",
                "testCases": [
                    {"input": "[[0,30],[5,10],[15,20]]", "expected_output": "2", "weight": 0.6, "description": "Overlapping meetings"},
                    {"input": "[[7,10],[2,4]]", "expected_output": "1", "weight": 0.4, "description": "Non-overlapping meetings"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    int minMeetingRooms(vector<vector<int>>& intervals) {\n        // Your code here\n        return 0;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    int minMeetingRooms(vector<vector<int>>& intervals) {\n        if (intervals.empty()) {\n            return 0;\n        }\n        \n        // Sort intervals by start time\n        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {\n            return a[0] < b[0];\n        });\n        \n        // Min heap to track end times\n        priority_queue<int, vector<int>, greater<int>> heap;\n        \n        for (const auto& interval : intervals) {\n            int start = interval[0];\n            int end = interval[1];\n            \n            // If the earliest ending meeting has ended, remove it\n            if (!heap.empty() && heap.top() <= start) {\n                heap.pop();\n            }\n            \n            // Add current meeting's end time\n            heap.push(end);\n        }\n        \n        return heap.size();\n    }\n};",
                "testCases": [
                    {"input": "[[0,30],[5,10],[15,20]]", "expected_output": "2", "weight": 0.6, "description": "Overlapping meetings"},
                    {"input": "[[7,10],[2,4]]", "expected_output": "1", "weight": 0.4, "description": "Non-overlapping meetings"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n log n)",
            "spaceComplexity": "O(n)",
            "constraints": ["1 <= intervals.length <= 10^4", "0 <= starti < endi <= 10^6"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 25,
            "tags": ["array", "two-pointers", "greedy", "sorting", "heap"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Greedy Algorithms"
        }
    })

    # Math & Geometry - Medium: Rotate Image
    questions.append({
        "id": "rotate-image",
        "title": "Rotate Image",
        "text": "You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).\n\nYou have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.\n\n**Example 1:**\nInput: matrix = [[1,2,3],[4,5,6],[7,8,9]]\nOutput: [[7,4,1],[8,5,2],[9,6,3]]\n\n**Example 2:**\nInput: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\nOutput: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def rotate(self, matrix):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def rotate(self, matrix):\n        n = len(matrix)\n        \n        # Step 1: Transpose the matrix\n        for i in range(n):\n            for j in range(i, n):\n                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]\n        \n        # Step 2: Reverse each row\n        for i in range(n):\n            matrix[i].reverse()",
                "testCases": [
                    {"input": "[[1,2,3],[4,5,6],[7,8,9]]", "expected_output": "[[7,4,1],[8,5,2],[9,6,3]]", "weight": 0.5, "description": "3x3 matrix"},
                    {"input": "[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]", "expected_output": "[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]", "weight": 0.5, "description": "4x4 matrix"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[][]} matrix\n * @return {void} Do not return anything, modify matrix in-place instead.\n */\nvar rotate = function(matrix) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[][]} matrix\n * @return {void} Do not return anything, modify matrix in-place instead.\n */\nvar rotate = function(matrix) {\n    const n = matrix.length;\n    \n    // Step 1: Transpose the matrix\n    for (let i = 0; i < n; i++) {\n        for (let j = i; j < n; j++) {\n            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];\n        }\n    }\n    \n    // Step 2: Reverse each row\n    for (let i = 0; i < n; i++) {\n        matrix[i].reverse();\n    }\n};",
                "testCases": [
                    {"input": "[[1,2,3],[4,5,6],[7,8,9]]", "expected_output": "[[7,4,1],[8,5,2],[9,6,3]]", "weight": 0.5, "description": "3x3 matrix"},
                    {"input": "[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]", "expected_output": "[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]", "weight": 0.5, "description": "4x4 matrix"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public void rotate(int[][] matrix) {\n        // Your code here\n    }\n}",
                "solutionCode": "class Solution {\n    public void rotate(int[][] matrix) {\n        int n = matrix.length;\n        \n        // Step 1: Transpose the matrix\n        for (int i = 0; i < n; i++) {\n            for (int j = i; j < n; j++) {\n                int temp = matrix[i][j];\n                matrix[i][j] = matrix[j][i];\n                matrix[j][i] = temp;\n            }\n        }\n        \n        // Step 2: Reverse each row\n        for (int i = 0; i < n; i++) {\n            int left = 0, right = n - 1;\n            while (left < right) {\n                int temp = matrix[i][left];\n                matrix[i][left] = matrix[i][right];\n                matrix[i][right] = temp;\n                left++;\n                right--;\n            }\n        }\n    }\n}",
                "testCases": [
                    {"input": "[[1,2,3],[4,5,6],[7,8,9]]", "expected_output": "[[7,4,1],[8,5,2],[9,6,3]]", "weight": 0.5, "description": "3x3 matrix"},
                    {"input": "[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]", "expected_output": "[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]", "weight": 0.5, "description": "4x4 matrix"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func rotate(matrix [][]int)  {\n    // Your code here\n}",
                "solutionCode": "func rotate(matrix [][]int) {\n    n := len(matrix)\n    \n    // Step 1: Transpose the matrix\n    for i := 0; i < n; i++ {\n        for j := i; j < n; j++ {\n            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]\n        }\n    }\n    \n    // Step 2: Reverse each row\n    for i := 0; i < n; i++ {\n        left, right := 0, n-1\n        for left < right {\n            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]\n            left++\n            right--\n        }\n    }\n}",
                "testCases": [
                    {"input": "[[1,2,3],[4,5,6],[7,8,9]]", "expected_output": "[[7,4,1],[8,5,2],[9,6,3]]", "weight": 0.5, "description": "3x3 matrix"},
                    {"input": "[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]", "expected_output": "[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]", "weight": 0.5, "description": "4x4 matrix"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[][]} matrix\n# @return {Void} Do not return anything, modify matrix in-place instead.\ndef rotate(matrix)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[][]} matrix\n# @return {Void} Do not return anything, modify matrix in-place instead.\ndef rotate(matrix)\n    n = matrix.length\n    \n    # Step 1: Transpose the matrix\n    (0...n).each do |i|\n        (i...n).each do |j|\n            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]\n        end\n    end\n    \n    # Step 2: Reverse each row\n    (0...n).each do |i|\n        matrix[i].reverse!\n    end\nend",
                "testCases": [
                    {"input": "[[1,2,3],[4,5,6],[7,8,9]]", "expected_output": "[[7,4,1],[8,5,2],[9,6,3]]", "weight": 0.5, "description": "3x3 matrix"},
                    {"input": "[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]", "expected_output": "[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]", "weight": 0.5, "description": "4x4 matrix"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    void rotate(vector<vector<int>>& matrix) {\n        // Your code here\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    void rotate(vector<vector<int>>& matrix) {\n        int n = matrix.size();\n        \n        // Step 1: Transpose the matrix\n        for (int i = 0; i < n; i++) {\n            for (int j = i; j < n; j++) {\n                swap(matrix[i][j], matrix[j][i]);\n            }\n        }\n        \n        // Step 2: Reverse each row\n        for (int i = 0; i < n; i++) {\n            reverse(matrix[i].begin(), matrix[i].end());\n        }\n    }\n};",
                "testCases": [
                    {"input": "[[1,2,3],[4,5,6],[7,8,9]]", "expected_output": "[[7,4,1],[8,5,2],[9,6,3]]", "weight": 0.5, "description": "3x3 matrix"},
                    {"input": "[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]", "expected_output": "[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]", "weight": 0.5, "description": "4x4 matrix"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n^2)",
            "spaceComplexity": "O(1)",
            "constraints": ["n == matrix.length == matrix[i].length", "1 <= n <= 20", "-1000 <= matrix[i][j] <= 1000"]
        },
        "gradingRules": {
            "testCaseWeight": 0.7,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 20,
            "tags": ["array", "math", "matrix"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Math & Geometry"
        }
    })

    # Arrays & Strings - Medium: Group Anagrams
    questions.append({
        "id": "group-anagrams-v2",
        "title": "Group Anagrams",
        "text": "Given an array of strings strs, group the anagrams together. You can return the answer in any order.\n\nAn Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.\n\n**Example 1:**\nInput: strs = [\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]\nOutput: [[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]\n\n**Example 2:**\nInput: strs = [\"\"]\nOutput: [[\"\"]]\n\n**Example 3:**\nInput: strs = [\"a\"]\nOutput: [[\"a\"]]",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def groupAnagrams(self, strs):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def groupAnagrams(self, strs):\n        from collections import defaultdict\n        \n        anagram_groups = defaultdict(list)\n        \n        for s in strs:\n            # Sort the string to create a key\n            key = ''.join(sorted(s))\n            anagram_groups[key].append(s)\n        \n        return list(anagram_groups.values())",
                "testCases": [
                    {"input": "[\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]", "expected_output": "[[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]", "weight": 0.6, "description": "Multiple anagram groups"},
                    {"input": "[\"\"]", "expected_output": "[[\"\"]]", "weight": 0.2, "description": "Empty string"},
                    {"input": "[\"a\"]", "expected_output": "[[\"a\"]]", "weight": 0.2, "description": "Single character"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {string[]} strs\n * @return {string[][]}\n */\nvar groupAnagrams = function(strs) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {string[]} strs\n * @return {string[][]}\n */\nvar groupAnagrams = function(strs) {\n    const anagramGroups = new Map();\n    \n    for (const s of strs) {\n        // Sort the string to create a key\n        const key = s.split('').sort().join('');\n        \n        if (!anagramGroups.has(key)) {\n            anagramGroups.set(key, []);\n        }\n        anagramGroups.get(key).push(s);\n    }\n    \n    return Array.from(anagramGroups.values());\n};",
                "testCases": [
                    {"input": "[\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]", "expected_output": "[[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]", "weight": 0.6, "description": "Multiple anagram groups"},
                    {"input": "[\"\"]", "expected_output": "[[\"\"]]", "weight": 0.2, "description": "Empty string"},
                    {"input": "[\"a\"]", "expected_output": "[[\"a\"]]", "weight": 0.2, "description": "Single character"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public List<List<String>> groupAnagrams(String[] strs) {\n        // Your code here\n        return new ArrayList<>();\n    }\n}",
                "solutionCode": "class Solution {\n    public List<List<String>> groupAnagrams(String[] strs) {\n        Map<String, List<String>> anagramGroups = new HashMap<>();\n        \n        for (String s : strs) {\n            // Sort the string to create a key\n            char[] chars = s.toCharArray();\n            Arrays.sort(chars);\n            String key = new String(chars);\n            \n            anagramGroups.computeIfAbsent(key, k -> new ArrayList<>()).add(s);\n        }\n        \n        return new ArrayList<>(anagramGroups.values());\n    }\n}",
                "testCases": [
                    {"input": "[\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]", "expected_output": "[[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]", "weight": 0.6, "description": "Multiple anagram groups"},
                    {"input": "[\"\"]", "expected_output": "[[\"\"]]", "weight": 0.2, "description": "Empty string"},
                    {"input": "[\"a\"]", "expected_output": "[[\"a\"]]", "weight": 0.2, "description": "Single character"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func groupAnagrams(strs []string) [][]string {\n    // Your code here\n    return [][]string{}\n}",
                "solutionCode": "import (\n    \"sort\"\n    \"strings\"\n)\n\nfunc groupAnagrams(strs []string) [][]string {\n    anagramGroups := make(map[string][]string)\n    \n    for _, s := range strs {\n        // Sort the string to create a key\n        chars := strings.Split(s, \"\")\n        sort.Strings(chars)\n        key := strings.Join(chars, \"\")\n        \n        anagramGroups[key] = append(anagramGroups[key], s)\n    }\n    \n    result := make([][]string, 0, len(anagramGroups))\n    for _, group := range anagramGroups {\n        result = append(result, group)\n    }\n    \n    return result\n}",
                "testCases": [
                    {"input": "[\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]", "expected_output": "[[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]", "weight": 0.6, "description": "Multiple anagram groups"},
                    {"input": "[\"\"]", "expected_output": "[[\"\"]]", "weight": 0.2, "description": "Empty string"},
                    {"input": "[\"a\"]", "expected_output": "[[\"a\"]]", "weight": 0.2, "description": "Single character"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {String[]} strs\n# @return {String[][]}\ndef group_anagrams(strs)\n    # Your code here\nend",
                "solutionCode": "# @param {String[]} strs\n# @return {String[][]}\ndef group_anagrams(strs)\n    anagram_groups = Hash.new { |h, k| h[k] = [] }\n    \n    strs.each do |s|\n        # Sort the string to create a key\n        key = s.chars.sort.join\n        anagram_groups[key] << s\n    end\n    \n    anagram_groups.values\nend",
                "testCases": [
                    {"input": "[\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]", "expected_output": "[[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]", "weight": 0.6, "description": "Multiple anagram groups"},
                    {"input": "[\"\"]", "expected_output": "[[\"\"]]", "weight": 0.2, "description": "Empty string"},
                    {"input": "[\"a\"]", "expected_output": "[[\"a\"]]", "weight": 0.2, "description": "Single character"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    vector<vector<string>> groupAnagrams(vector<string>& strs) {\n        // Your code here\n        return {};\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    vector<vector<string>> groupAnagrams(vector<string>& strs) {\n        unordered_map<string, vector<string>> anagramGroups;\n        \n        for (const string& s : strs) {\n            // Sort the string to create a key\n            string key = s;\n            sort(key.begin(), key.end());\n            \n            anagramGroups[key].push_back(s);\n        }\n        \n        vector<vector<string>> result;\n        for (const auto& pair : anagramGroups) {\n            result.push_back(pair.second);\n        }\n        \n        return result;\n    }\n};",
                "testCases": [
                    {"input": "[\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]", "expected_output": "[[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]", "weight": 0.6, "description": "Multiple anagram groups"},
                    {"input": "[\"\"]", "expected_output": "[[\"\"]]", "weight": 0.2, "description": "Empty string"},
                    {"input": "[\"a\"]", "expected_output": "[[\"a\"]]", "weight": 0.2, "description": "Single character"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n * k log k)",
            "spaceComplexity": "O(n * k)",
            "constraints": ["1 <= strs.length <= 10^4", "0 <= strs[i].length <= 100", "strs[i] consists of lowercase English letters"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 20,
            "tags": ["array", "hash-table", "string", "sorting"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Arrays & Strings"
        }
    })

    # Linked Lists - Hard: Merge k Sorted Lists
    questions.append({
        "id": "merge-k-sorted-lists-v2",
        "title": "Merge k Sorted Lists",
        "text": "You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.\n\nMerge all the linked-lists into one sorted linked-list and return it.\n\n**Example 1:**\nInput: lists = [[1,4,5],[1,3,4],[2,6]]\nOutput: [1,1,2,3,4,4,5,6]\nExplanation: The linked-lists are:\n[\n  1->4->5,\n  1->3->4,\n  2->6\n]\nmerging them into one sorted list:\n1->1->2->3->4->4->5->6\n\n**Example 2:**\nInput: lists = []\nOutput: []\n\n**Example 3:**\nInput: lists = [[]]\nOutput: []",
        "implementations": [
            {
                "language": "python",
                "starterCode": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def mergeKLists(self, lists):\n        # Your code here\n        pass",
                "solutionCode": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def mergeKLists(self, lists):\n        import heapq\n        \n        if not lists:\n            return None\n        \n        # Min heap to store (value, index, node)\n        heap = []\n        \n        # Initialize heap with first node from each list\n        for i, head in enumerate(lists):\n            if head:\n                heapq.heappush(heap, (head.val, i, head))\n        \n        dummy = ListNode(0)\n        current = dummy\n        \n        while heap:\n            val, i, node = heapq.heappop(heap)\n            current.next = node\n            current = current.next\n            \n            # Add next node from the same list\n            if node.next:\n                heapq.heappush(heap, (node.next.val, i, node.next))\n        \n        return dummy.next",
                "testCases": [
                    {"input": "[[1,4,5],[1,3,4],[2,6]]", "expected_output": "[1,1,2,3,4,4,5,6]", "weight": 0.6, "description": "Multiple sorted lists"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.2, "description": "Empty input"},
                    {"input": "[[]]", "expected_output": "[]", "weight": 0.2, "description": "Single empty list"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n/**\n * @param {ListNode[]} lists\n * @return {ListNode}\n */\nvar mergeKLists = function(lists) {\n    // Your code here\n};",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n/**\n * @param {ListNode[]} lists\n * @return {ListNode}\n */\nvar mergeKLists = function(lists) {\n    if (!lists || lists.length === 0) {\n        return null;\n    }\n    \n    function mergeTwoLists(l1, l2) {\n        const dummy = new ListNode(0);\n        let current = dummy;\n        \n        while (l1 && l2) {\n            if (l1.val <= l2.val) {\n                current.next = l1;\n                l1 = l1.next;\n            } else {\n                current.next = l2;\n                l2 = l2.next;\n            }\n            current = current.next;\n        }\n        \n        current.next = l1 || l2;\n        return dummy.next;\n    }\n    \n    // Divide and conquer approach\n    while (lists.length > 1) {\n        const mergedLists = [];\n        \n        for (let i = 0; i < lists.length; i += 2) {\n            const l1 = lists[i];\n            const l2 = i + 1 < lists.length ? lists[i + 1] : null;\n            mergedLists.push(mergeTwoLists(l1, l2));\n        }\n        \n        lists = mergedLists;\n    }\n    \n    return lists[0];\n};",
                "testCases": [
                    {"input": "[[1,4,5],[1,3,4],[2,6]]", "expected_output": "[1,1,2,3,4,4,5,6]", "weight": 0.6, "description": "Multiple sorted lists"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.2, "description": "Empty input"},
                    {"input": "[[]]", "expected_output": "[]", "weight": 0.2, "description": "Single empty list"}
                ]
            },
            {
                "language": "java",
                "starterCode": "/**\n * Definition for singly-linked list.\n * public class ListNode {\n *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n * }\n */\nclass Solution {\n    public ListNode mergeKLists(ListNode[] lists) {\n        // Your code here\n        return null;\n    }\n}",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * public class ListNode {\n *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n * }\n */\nclass Solution {\n    public ListNode mergeKLists(ListNode[] lists) {\n        if (lists == null || lists.length == 0) {\n            return null;\n        }\n        \n        PriorityQueue<ListNode> heap = new PriorityQueue<>((a, b) -> a.val - b.val);\n        \n        // Add first node from each list to heap\n        for (ListNode head : lists) {\n            if (head != null) {\n                heap.offer(head);\n            }\n        }\n        \n        ListNode dummy = new ListNode(0);\n        ListNode current = dummy;\n        \n        while (!heap.isEmpty()) {\n            ListNode node = heap.poll();\n            current.next = node;\n            current = current.next;\n            \n            if (node.next != null) {\n                heap.offer(node.next);\n            }\n        }\n        \n        return dummy.next;\n    }\n}",
                "testCases": [
                    {"input": "[[1,4,5],[1,3,4],[2,6]]", "expected_output": "[1,1,2,3,4,4,5,6]", "weight": 0.6, "description": "Multiple sorted lists"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.2, "description": "Empty input"},
                    {"input": "[[]]", "expected_output": "[]", "weight": 0.2, "description": "Single empty list"}
                ]
            },
            {
                "language": "go",
                "starterCode": "/**\n * Definition for singly-linked list.\n * type ListNode struct {\n *     Val int\n *     Next *ListNode\n * }\n */\nfunc mergeKLists(lists []*ListNode) *ListNode {\n    // Your code here\n    return nil\n}",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * type ListNode struct {\n *     Val int\n *     Next *ListNode\n * }\n */\nfunc mergeKLists(lists []*ListNode) *ListNode {\n    if len(lists) == 0 {\n        return nil\n    }\n    \n    for len(lists) > 1 {\n        var mergedLists []*ListNode\n        \n        for i := 0; i < len(lists); i += 2 {\n            l1 := lists[i]\n            var l2 *ListNode\n            if i+1 < len(lists) {\n                l2 = lists[i+1]\n            }\n            mergedLists = append(mergedLists, mergeTwoLists(l1, l2))\n        }\n        \n        lists = mergedLists\n    }\n    \n    return lists[0]\n}\n\nfunc mergeTwoLists(l1, l2 *ListNode) *ListNode {\n    dummy := &ListNode{}\n    current := dummy\n    \n    for l1 != nil && l2 != nil {\n        if l1.Val <= l2.Val {\n            current.Next = l1\n            l1 = l1.Next\n        } else {\n            current.Next = l2\n            l2 = l2.Next\n        }\n        current = current.Next\n    }\n    \n    if l1 != nil {\n        current.Next = l1\n    } else {\n        current.Next = l2\n    }\n    \n    return dummy.Next\n}",
                "testCases": [
                    {"input": "[[1,4,5],[1,3,4],[2,6]]", "expected_output": "[1,1,2,3,4,4,5,6]", "weight": 0.6, "description": "Multiple sorted lists"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.2, "description": "Empty input"},
                    {"input": "[[]]", "expected_output": "[]", "weight": 0.2, "description": "Single empty list"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# Definition for singly-linked list.\n# class ListNode\n#     attr_accessor :val, :next\n#     def initialize(val = 0, _next = nil)\n#         @val = val\n#         @next = _next\n#     end\n# end\n# @param {ListNode[]} lists\n# @return {ListNode}\ndef merge_k_lists(lists)\n    # Your code here\nend",
                "solutionCode": "# Definition for singly-linked list.\n# class ListNode\n#     attr_accessor :val, :next\n#     def initialize(val = 0, _next = nil)\n#         @val = val\n#         @next = _next\n#     end\n# end\n# @param {ListNode[]} lists\n# @return {ListNode}\ndef merge_k_lists(lists)\n    return nil if lists.nil? || lists.empty?\n    \n    def merge_two_lists(l1, l2)\n        dummy = ListNode.new(0)\n        current = dummy\n        \n        while l1 && l2\n            if l1.val <= l2.val\n                current.next = l1\n                l1 = l1.next\n            else\n                current.next = l2\n                l2 = l2.next\n            end\n            current = current.next\n        end\n        \n        current.next = l1 || l2\n        dummy.next\n    end\n    \n    # Divide and conquer approach\n    while lists.length > 1\n        merged_lists = []\n        \n        (0...lists.length).step(2) do |i|\n            l1 = lists[i]\n            l2 = i + 1 < lists.length ? lists[i + 1] : nil\n            merged_lists << merge_two_lists(l1, l2)\n        end\n        \n        lists = merged_lists\n    end\n    \n    lists[0]\nend",
                "testCases": [
                    {"input": "[[1,4,5],[1,3,4],[2,6]]", "expected_output": "[1,1,2,3,4,4,5,6]", "weight": 0.6, "description": "Multiple sorted lists"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.2, "description": "Empty input"},
                    {"input": "[[]]", "expected_output": "[]", "weight": 0.2, "description": "Single empty list"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr) {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\npublic:\n    ListNode* mergeKLists(vector<ListNode*>& lists) {\n        // Your code here\n        return nullptr;\n    }\n};",
                "solutionCode": "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr) {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\npublic:\n    ListNode* mergeKLists(vector<ListNode*>& lists) {\n        if (lists.empty()) {\n            return nullptr;\n        }\n        \n        auto compare = [](ListNode* a, ListNode* b) {\n            return a->val > b->val;\n        };\n        \n        priority_queue<ListNode*, vector<ListNode*>, decltype(compare)> heap(compare);\n        \n        // Add first node from each list to heap\n        for (ListNode* head : lists) {\n            if (head) {\n                heap.push(head);\n            }\n        }\n        \n        ListNode dummy(0);\n        ListNode* current = &dummy;\n        \n        while (!heap.empty()) {\n            ListNode* node = heap.top();\n            heap.pop();\n            \n            current->next = node;\n            current = current->next;\n            \n            if (node->next) {\n                heap.push(node->next);\n            }\n        }\n        \n        return dummy.next;\n    }\n};",
                "testCases": [
                    {"input": "[[1,4,5],[1,3,4],[2,6]]", "expected_output": "[1,1,2,3,4,4,5,6]", "weight": 0.6, "description": "Multiple sorted lists"},
                    {"input": "[]", "expected_output": "[]", "weight": 0.2, "description": "Empty input"},
                    {"input": "[[]]", "expected_output": "[]", "weight": 0.2, "description": "Single empty list"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n log k)",
            "spaceComplexity": "O(k)",
            "constraints": ["k == lists.length", "0 <= k <= 10^4", "0 <= lists[i].length <= 500", "-10^4 <= lists[i][j] <= 10^4", "lists[i] is sorted in ascending order", "The sum of lists[i].length will not exceed 10^4"]
        },
        "gradingRules": {
            "testCaseWeight": 0.5,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.3,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "HARD",
            "estimatedDuration": 30,
            "tags": ["linked-list", "divide-and-conquer", "heap", "merge-sort"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Linked Lists"
        }
    })

    # Dynamic Programming - Medium: Longest Increasing Subsequence
    questions.append({
        "id": "longest-increasing-subsequence",
        "title": "Longest Increasing Subsequence",
        "text": "Given an integer array nums, return the length of the longest strictly increasing subsequence.\n\n**Example 1:**\nInput: nums = [10,9,2,5,3,7,101,18]\nOutput: 4\nExplanation: The longest increasing subsequence is [2,3,7,18], therefore the length is 4.\n\n**Example 2:**\nInput: nums = [0,1,0,3,2,3]\nOutput: 4\n\n**Example 3:**\nInput: nums = [7,7,7,7,7,7,7]\nOutput: 1",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def lengthOfLIS(self, nums):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def lengthOfLIS(self, nums):\n        if not nums:\n            return 0\n        \n        dp = [1] * len(nums)\n        \n        for i in range(1, len(nums)):\n            for j in range(i):\n                if nums[j] < nums[i]:\n                    dp[i] = max(dp[i], dp[j] + 1)\n        \n        return max(dp)",
                "testCases": [
                    {"input": "[10,9,2,5,3,7,101,18]", "expected_output": "4", "weight": 0.4, "description": "Standard case"},
                    {"input": "[0,1,0,3,2,3]", "expected_output": "4", "weight": 0.3, "description": "Mixed sequence"},
                    {"input": "[7,7,7,7,7,7,7]", "expected_output": "1", "weight": 0.3, "description": "All same elements"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar lengthOfLIS = function(nums) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar lengthOfLIS = function(nums) {\n    if (nums.length === 0) {\n        return 0;\n    }\n    \n    const dp = new Array(nums.length).fill(1);\n    \n    for (let i = 1; i < nums.length; i++) {\n        for (let j = 0; j < i; j++) {\n            if (nums[j] < nums[i]) {\n                dp[i] = Math.max(dp[i], dp[j] + 1);\n            }\n        }\n    }\n    \n    return Math.max(...dp);\n};",
                "testCases": [
                    {"input": "[10,9,2,5,3,7,101,18]", "expected_output": "4", "weight": 0.4, "description": "Standard case"},
                    {"input": "[0,1,0,3,2,3]", "expected_output": "4", "weight": 0.3, "description": "Mixed sequence"},
                    {"input": "[7,7,7,7,7,7,7]", "expected_output": "1", "weight": 0.3, "description": "All same elements"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int lengthOfLIS(int[] nums) {\n        // Your code here\n        return 0;\n    }\n}",
                "solutionCode": "class Solution {\n    public int lengthOfLIS(int[] nums) {\n        if (nums.length == 0) {\n            return 0;\n        }\n        \n        int[] dp = new int[nums.length];\n        Arrays.fill(dp, 1);\n        \n        for (int i = 1; i < nums.length; i++) {\n            for (int j = 0; j < i; j++) {\n                if (nums[j] < nums[i]) {\n                    dp[i] = Math.max(dp[i], dp[j] + 1);\n                }\n            }\n        }\n        \n        int maxLength = 0;\n        for (int length : dp) {\n            maxLength = Math.max(maxLength, length);\n        }\n        \n        return maxLength;\n    }\n}",
                "testCases": [
                    {"input": "[10,9,2,5,3,7,101,18]", "expected_output": "4", "weight": 0.4, "description": "Standard case"},
                    {"input": "[0,1,0,3,2,3]", "expected_output": "4", "weight": 0.3, "description": "Mixed sequence"},
                    {"input": "[7,7,7,7,7,7,7]", "expected_output": "1", "weight": 0.3, "description": "All same elements"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func lengthOfLIS(nums []int) int {\n    // Your code here\n    return 0\n}",
                "solutionCode": "func lengthOfLIS(nums []int) int {\n    if len(nums) == 0 {\n        return 0\n    }\n    \n    dp := make([]int, len(nums))\n    for i := range dp {\n        dp[i] = 1\n    }\n    \n    for i := 1; i < len(nums); i++ {\n        for j := 0; j < i; j++ {\n            if nums[j] < nums[i] {\n                if dp[j]+1 > dp[i] {\n                    dp[i] = dp[j] + 1\n                }\n            }\n        }\n    }\n    \n    maxLength := 0\n    for _, length := range dp {\n        if length > maxLength {\n            maxLength = length\n        }\n    }\n    \n    return maxLength\n}",
                "testCases": [
                    {"input": "[10,9,2,5,3,7,101,18]", "expected_output": "4", "weight": 0.4, "description": "Standard case"},
                    {"input": "[0,1,0,3,2,3]", "expected_output": "4", "weight": 0.3, "description": "Mixed sequence"},
                    {"input": "[7,7,7,7,7,7,7]", "expected_output": "1", "weight": 0.3, "description": "All same elements"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[]} nums\n# @return {Integer}\ndef length_of_lis(nums)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[]} nums\n# @return {Integer}\ndef length_of_lis(nums)\n    return 0 if nums.empty?\n    \n    dp = Array.new(nums.length, 1)\n    \n    (1...nums.length).each do |i|\n        (0...i).each do |j|\n            if nums[j] < nums[i]\n                dp[i] = [dp[i], dp[j] + 1].max\n            end\n        end\n    end\n    \n    dp.max\nend",
                "testCases": [
                    {"input": "[10,9,2,5,3,7,101,18]", "expected_output": "4", "weight": 0.4, "description": "Standard case"},
                    {"input": "[0,1,0,3,2,3]", "expected_output": "4", "weight": 0.3, "description": "Mixed sequence"},
                    {"input": "[7,7,7,7,7,7,7]", "expected_output": "1", "weight": 0.3, "description": "All same elements"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    int lengthOfLIS(vector<int>& nums) {\n        // Your code here\n        return 0;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    int lengthOfLIS(vector<int>& nums) {\n        if (nums.empty()) {\n            return 0;\n        }\n        \n        vector<int> dp(nums.size(), 1);\n        \n        for (int i = 1; i < nums.size(); i++) {\n            for (int j = 0; j < i; j++) {\n                if (nums[j] < nums[i]) {\n                    dp[i] = max(dp[i], dp[j] + 1);\n                }\n            }\n        }\n        \n        return *max_element(dp.begin(), dp.end());\n    }\n};",
                "testCases": [
                    {"input": "[10,9,2,5,3,7,101,18]", "expected_output": "4", "weight": 0.4, "description": "Standard case"},
                    {"input": "[0,1,0,3,2,3]", "expected_output": "4", "weight": 0.3, "description": "Mixed sequence"},
                    {"input": "[7,7,7,7,7,7,7]", "expected_output": "1", "weight": 0.3, "description": "All same elements"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n^2)",
            "spaceComplexity": "O(n)",
            "constraints": ["1 <= nums.length <= 2500", "-10^4 <= nums[i] <= 10^4"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 25,
            "tags": ["array", "binary-search", "dynamic-programming"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Dynamic Programming"
        }
    })

    # Arrays & Strings - Hard: Trapping Rain Water
    questions.append({
        "id": "trapping-rain-water",
        "title": "Trapping Rain Water",
        "text": "Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.\n\n**Example 1:**\nInput: height = [0,1,0,2,1,0,1,3,2,1,2,1]\nOutput: 6\nExplanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.\n\n**Example 2:**\nInput: height = [4,2,0,3,2,5]\nOutput: 9",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def trap(self, height):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def trap(self, height):\n        if not height:\n            return 0\n        \n        left, right = 0, len(height) - 1\n        left_max = right_max = 0\n        water = 0\n        \n        while left < right:\n            if height[left] < height[right]:\n                if height[left] >= left_max:\n                    left_max = height[left]\n                else:\n                    water += left_max - height[left]\n                left += 1\n            else:\n                if height[right] >= right_max:\n                    right_max = height[right]\n                else:\n                    water += right_max - height[right]\n                right -= 1\n        \n        return water",
                "testCases": [
                    {"input": "[0,1,0,2,1,0,1,3,2,1,2,1]", "expected_output": "6", "weight": 0.6, "description": "Standard case"},
                    {"input": "[4,2,0,3,2,5]", "expected_output": "9", "weight": 0.4, "description": "Another case"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[]} height\n * @return {number}\n */\nvar trap = function(height) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[]} height\n * @return {number}\n */\nvar trap = function(height) {\n    if (height.length === 0) {\n        return 0;\n    }\n    \n    let left = 0, right = height.length - 1;\n    let leftMax = 0, rightMax = 0;\n    let water = 0;\n    \n    while (left < right) {\n        if (height[left] < height[right]) {\n            if (height[left] >= leftMax) {\n                leftMax = height[left];\n            } else {\n                water += leftMax - height[left];\n            }\n            left++;\n        } else {\n            if (height[right] >= rightMax) {\n                rightMax = height[right];\n            } else {\n                water += rightMax - height[right];\n            }\n            right--;\n        }\n    }\n    \n    return water;\n};",
                "testCases": [
                    {"input": "[0,1,0,2,1,0,1,3,2,1,2,1]", "expected_output": "6", "weight": 0.6, "description": "Standard case"},
                    {"input": "[4,2,0,3,2,5]", "expected_output": "9", "weight": 0.4, "description": "Another case"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int trap(int[] height) {\n        // Your code here\n        return 0;\n    }\n}",
                "solutionCode": "class Solution {\n    public int trap(int[] height) {\n        if (height.length == 0) {\n            return 0;\n        }\n        \n        int left = 0, right = height.length - 1;\n        int leftMax = 0, rightMax = 0;\n        int water = 0;\n        \n        while (left < right) {\n            if (height[left] < height[right]) {\n                if (height[left] >= leftMax) {\n                    leftMax = height[left];\n                } else {\n                    water += leftMax - height[left];\n                }\n                left++;\n            } else {\n                if (height[right] >= rightMax) {\n                    rightMax = height[right];\n                } else {\n                    water += rightMax - height[right];\n                }\n                right--;\n            }\n        }\n        \n        return water;\n    }\n}",
                "testCases": [
                    {"input": "[0,1,0,2,1,0,1,3,2,1,2,1]", "expected_output": "6", "weight": 0.6, "description": "Standard case"},
                    {"input": "[4,2,0,3,2,5]", "expected_output": "9", "weight": 0.4, "description": "Another case"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func trap(height []int) int {\n    // Your code here\n    return 0\n}",
                "solutionCode": "func trap(height []int) int {\n    if len(height) == 0 {\n        return 0\n    }\n    \n    left, right := 0, len(height)-1\n    leftMax, rightMax := 0, 0\n    water := 0\n    \n    for left < right {\n        if height[left] < height[right] {\n            if height[left] >= leftMax {\n                leftMax = height[left]\n            } else {\n                water += leftMax - height[left]\n            }\n            left++\n        } else {\n            if height[right] >= rightMax {\n                rightMax = height[right]\n            } else {\n                water += rightMax - height[right]\n            }\n            right--\n        }\n    }\n    \n    return water\n}",
                "testCases": [
                    {"input": "[0,1,0,2,1,0,1,3,2,1,2,1]", "expected_output": "6", "weight": 0.6, "description": "Standard case"},
                    {"input": "[4,2,0,3,2,5]", "expected_output": "9", "weight": 0.4, "description": "Another case"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[]} height\n# @return {Integer}\ndef trap(height)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[]} height\n# @return {Integer}\ndef trap(height)\n    return 0 if height.empty?\n    \n    left, right = 0, height.length - 1\n    left_max = right_max = 0\n    water = 0\n    \n    while left < right\n        if height[left] < height[right]\n            if height[left] >= left_max\n                left_max = height[left]\n            else\n                water += left_max - height[left]\n            end\n            left += 1\n        else\n            if height[right] >= right_max\n                right_max = height[right]\n            else\n                water += right_max - height[right]\n            end\n            right -= 1\n        end\n    end\n    \n    water\nend",
                "testCases": [
                    {"input": "[0,1,0,2,1,0,1,3,2,1,2,1]", "expected_output": "6", "weight": 0.6, "description": "Standard case"},
                    {"input": "[4,2,0,3,2,5]", "expected_output": "9", "weight": 0.4, "description": "Another case"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    int trap(vector<int>& height) {\n        // Your code here\n        return 0;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    int trap(vector<int>& height) {\n        if (height.empty()) {\n            return 0;\n        }\n        \n        int left = 0, right = height.size() - 1;\n        int leftMax = 0, rightMax = 0;\n        int water = 0;\n        \n        while (left < right) {\n            if (height[left] < height[right]) {\n                if (height[left] >= leftMax) {\n                    leftMax = height[left];\n                } else {\n                    water += leftMax - height[left];\n                }\n                left++;\n            } else {\n                if (height[right] >= rightMax) {\n                    rightMax = height[right];\n                } else {\n                    water += rightMax - height[right];\n                }\n                right--;\n            }\n        }\n        \n        return water;\n    }\n};",
                "testCases": [
                    {"input": "[0,1,0,2,1,0,1,3,2,1,2,1]", "expected_output": "6", "weight": 0.6, "description": "Standard case"},
                    {"input": "[4,2,0,3,2,5]", "expected_output": "9", "weight": 0.4, "description": "Another case"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(1)",
            "constraints": ["n == height.length", "1 <= n <= 2 * 10^4", "0 <= height[i] <= 3 * 10^4"]
        },
        "gradingRules": {
            "testCaseWeight": 0.5,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.3,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "HARD",
            "estimatedDuration": 30,
            "tags": ["array", "two-pointers", "dynamic-programming", "stack", "monotonic-stack"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Arrays & Strings"
        }
    })

    # Intervals - Medium: Merge Intervals
    questions.append({
        "id": "merge-intervals",
        "title": "Merge Intervals",
        "text": "Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.\n\n**Example 1:**\nInput: intervals = [[1,3],[2,6],[8,10],[15,18]]\nOutput: [[1,6],[8,10],[15,18]]\nExplanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].\n\n**Example 2:**\nInput: intervals = [[1,4],[4,5]]\nOutput: [[1,5]]\nExplanation: Intervals [1,4] and [4,5] are considered overlapping.",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def merge(self, intervals):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def merge(self, intervals):\n        if not intervals:\n            return []\n        \n        # Sort intervals by start time\n        intervals.sort(key=lambda x: x[0])\n        \n        merged = [intervals[0]]\n        \n        for current in intervals[1:]:\n            last = merged[-1]\n            \n            # If current interval overlaps with the last merged interval\n            if current[0] <= last[1]:\n                # Merge them by updating the end time\n                last[1] = max(last[1], current[1])\n            else:\n                # No overlap, add current interval\n                merged.append(current)\n        \n        return merged",
                "testCases": [
                    {"input": "[[1,3],[2,6],[8,10],[15,18]]", "expected_output": "[[1,6],[8,10],[15,18]]", "weight": 0.6, "description": "Multiple overlapping intervals"},
                    {"input": "[[1,4],[4,5]]", "expected_output": "[[1,5]]", "weight": 0.4, "description": "Adjacent intervals"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[][]} intervals\n * @return {number[][]}\n */\nvar merge = function(intervals) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[][]} intervals\n * @return {number[][]}\n */\nvar merge = function(intervals) {\n    if (intervals.length === 0) {\n        return [];\n    }\n    \n    // Sort intervals by start time\n    intervals.sort((a, b) => a[0] - b[0]);\n    \n    const merged = [intervals[0]];\n    \n    for (let i = 1; i < intervals.length; i++) {\n        const current = intervals[i];\n        const last = merged[merged.length - 1];\n        \n        // If current interval overlaps with the last merged interval\n        if (current[0] <= last[1]) {\n            // Merge them by updating the end time\n            last[1] = Math.max(last[1], current[1]);\n        } else {\n            // No overlap, add current interval\n            merged.push(current);\n        }\n    }\n    \n    return merged;\n};",
                "testCases": [
                    {"input": "[[1,3],[2,6],[8,10],[15,18]]", "expected_output": "[[1,6],[8,10],[15,18]]", "weight": 0.6, "description": "Multiple overlapping intervals"},
                    {"input": "[[1,4],[4,5]]", "expected_output": "[[1,5]]", "weight": 0.4, "description": "Adjacent intervals"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int[][] merge(int[][] intervals) {\n        // Your code here\n        return new int[0][];\n    }\n}",
                "solutionCode": "class Solution {\n    public int[][] merge(int[][] intervals) {\n        if (intervals.length == 0) {\n            return new int[0][];\n        }\n        \n        // Sort intervals by start time\n        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);\n        \n        List<int[]> merged = new ArrayList<>();\n        merged.add(intervals[0]);\n        \n        for (int i = 1; i < intervals.length; i++) {\n            int[] current = intervals[i];\n            int[] last = merged.get(merged.size() - 1);\n            \n            // If current interval overlaps with the last merged interval\n            if (current[0] <= last[1]) {\n                // Merge them by updating the end time\n                last[1] = Math.max(last[1], current[1]);\n            } else {\n                // No overlap, add current interval\n                merged.add(current);\n            }\n        }\n        \n        return merged.toArray(new int[merged.size()][]);\n    }\n}",
                "testCases": [
                    {"input": "[[1,3],[2,6],[8,10],[15,18]]", "expected_output": "[[1,6],[8,10],[15,18]]", "weight": 0.6, "description": "Multiple overlapping intervals"},
                    {"input": "[[1,4],[4,5]]", "expected_output": "[[1,5]]", "weight": 0.4, "description": "Adjacent intervals"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func merge(intervals [][]int) [][]int {\n    // Your code here\n    return [][]int{}\n}",
                "solutionCode": "import \"sort\"\n\nfunc merge(intervals [][]int) [][]int {\n    if len(intervals) == 0 {\n        return [][]int{}\n    }\n    \n    // Sort intervals by start time\n    sort.Slice(intervals, func(i, j int) bool {\n        return intervals[i][0] < intervals[j][0]\n    })\n    \n    merged := [][]int{intervals[0]}\n    \n    for i := 1; i < len(intervals); i++ {\n        current := intervals[i]\n        last := merged[len(merged)-1]\n        \n        // If current interval overlaps with the last merged interval\n        if current[0] <= last[1] {\n            // Merge them by updating the end time\n            if current[1] > last[1] {\n                last[1] = current[1]\n            }\n        } else {\n            // No overlap, add current interval\n            merged = append(merged, current)\n        }\n    }\n    \n    return merged\n}",
                "testCases": [
                    {"input": "[[1,3],[2,6],[8,10],[15,18]]", "expected_output": "[[1,6],[8,10],[15,18]]", "weight": 0.6, "description": "Multiple overlapping intervals"},
                    {"input": "[[1,4],[4,5]]", "expected_output": "[[1,5]]", "weight": 0.4, "description": "Adjacent intervals"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[][]} intervals\n# @return {Integer[][]}\ndef merge(intervals)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[][]} intervals\n# @return {Integer[][]}\ndef merge(intervals)\n    return [] if intervals.empty?\n    \n    # Sort intervals by start time\n    intervals.sort_by! { |interval| interval[0] }\n    \n    merged = [intervals[0]]\n    \n    intervals[1..-1].each do |current|\n        last = merged[-1]\n        \n        # If current interval overlaps with the last merged interval\n        if current[0] <= last[1]\n            # Merge them by updating the end time\n            last[1] = [last[1], current[1]].max\n        else\n            # No overlap, add current interval\n            merged << current\n        end\n    end\n    \n    merged\nend",
                "testCases": [
                    {"input": "[[1,3],[2,6],[8,10],[15,18]]", "expected_output": "[[1,6],[8,10],[15,18]]", "weight": 0.6, "description": "Multiple overlapping intervals"},
                    {"input": "[[1,4],[4,5]]", "expected_output": "[[1,5]]", "weight": 0.4, "description": "Adjacent intervals"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    vector<vector<int>> merge(vector<vector<int>>& intervals) {\n        // Your code here\n        return {};\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    vector<vector<int>> merge(vector<vector<int>>& intervals) {\n        if (intervals.empty()) {\n            return {};\n        }\n        \n        // Sort intervals by start time\n        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {\n            return a[0] < b[0];\n        });\n        \n        vector<vector<int>> merged;\n        merged.push_back(intervals[0]);\n        \n        for (int i = 1; i < intervals.size(); i++) {\n            vector<int>& current = intervals[i];\n            vector<int>& last = merged.back();\n            \n            // If current interval overlaps with the last merged interval\n            if (current[0] <= last[1]) {\n                // Merge them by updating the end time\n                last[1] = max(last[1], current[1]);\n            } else {\n                // No overlap, add current interval\n                merged.push_back(current);\n            }\n        }\n        \n        return merged;\n    }\n};",
                "testCases": [
                    {"input": "[[1,3],[2,6],[8,10],[15,18]]", "expected_output": "[[1,6],[8,10],[15,18]]", "weight": 0.6, "description": "Multiple overlapping intervals"},
                    {"input": "[[1,4],[4,5]]", "expected_output": "[[1,5]]", "weight": 0.4, "description": "Adjacent intervals"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n log n)",
            "spaceComplexity": "O(log n)",
            "constraints": ["1 <= intervals.length <= 10^4", "intervals[i].length == 2", "0 <= starti <= endi <= 10^4"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 20,
            "tags": ["array", "sorting"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Intervals"
        }
    })

    # Bit Manipulation - Hard: Number of 1 Bits
    questions.append({
        "id": "number-of-1-bits",
        "title": "Number of 1 Bits",
        "text": "Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).\n\nNote:\n- Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.\n- In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer -3.\n\n**Example 1:**\nInput: n = 00000000000000000000000000001011\nOutput: 3\nExplanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.\n\n**Example 2:**\nInput: n = 00000000000000000000000010000000\nOutput: 1\nExplanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.\n\n**Example 3:**\nInput: n = 11111111111111111111111111111101\nOutput: 31\nExplanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def hammingWeight(self, n):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def hammingWeight(self, n):\n        count = 0\n        while n:\n            count += n & 1\n            n >>= 1\n        return count",
                "testCases": [
                    {"input": "11", "expected_output": "3", "weight": 0.4, "description": "Binary: 1011"},
                    {"input": "128", "expected_output": "1", "weight": 0.3, "description": "Binary: 10000000"},
                    {"input": "4294967293", "expected_output": "31", "weight": 0.3, "description": "Binary: 11111111111111111111111111111101"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number} n - a positive integer\n * @return {number}\n */\nvar hammingWeight = function(n) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number} n - a positive integer\n * @return {number}\n */\nvar hammingWeight = function(n) {\n    let count = 0;\n    while (n !== 0) {\n        count += n & 1;\n        n >>>= 1; // Unsigned right shift\n    }\n    return count;\n};",
                "testCases": [
                    {"input": "11", "expected_output": "3", "weight": 0.4, "description": "Binary: 1011"},
                    {"input": "128", "expected_output": "1", "weight": 0.3, "description": "Binary: 10000000"},
                    {"input": "4294967293", "expected_output": "31", "weight": 0.3, "description": "Binary: 11111111111111111111111111111101"}
                ]
            },
            {
                "language": "java",
                "starterCode": "public class Solution {\n    // you need to treat n as an unsigned value\n    public int hammingWeight(int n) {\n        // Your code here\n        return 0;\n    }\n}",
                "solutionCode": "public class Solution {\n    // you need to treat n as an unsigned value\n    public int hammingWeight(int n) {\n        int count = 0;\n        while (n != 0) {\n            count += n & 1;\n            n >>>= 1; // Unsigned right shift\n        }\n        return count;\n    }\n}",
                "testCases": [
                    {"input": "11", "expected_output": "3", "weight": 0.4, "description": "Binary: 1011"},
                    {"input": "128", "expected_output": "1", "weight": 0.3, "description": "Binary: 10000000"},
                    {"input": "-3", "expected_output": "31", "weight": 0.3, "description": "Binary: 11111111111111111111111111111101"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func hammingWeight(num uint32) int {\n    // Your code here\n    return 0\n}",
                "solutionCode": "func hammingWeight(num uint32) int {\n    count := 0\n    for num != 0 {\n        count += int(num & 1)\n        num >>= 1\n    }\n    return count\n}",
                "testCases": [
                    {"input": "11", "expected_output": "3", "weight": 0.4, "description": "Binary: 1011"},
                    {"input": "128", "expected_output": "1", "weight": 0.3, "description": "Binary: 10000000"},
                    {"input": "4294967293", "expected_output": "31", "weight": 0.3, "description": "Binary: 11111111111111111111111111111101"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer} n\n# @return {Integer}\ndef hamming_weight(n)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer} n\n# @return {Integer}\ndef hamming_weight(n)\n    count = 0\n    while n != 0\n        count += n & 1\n        n >>= 1\n    end\n    count\nend",
                "testCases": [
                    {"input": "11", "expected_output": "3", "weight": 0.4, "description": "Binary: 1011"},
                    {"input": "128", "expected_output": "1", "weight": 0.3, "description": "Binary: 10000000"},
                    {"input": "4294967293", "expected_output": "31", "weight": 0.3, "description": "Binary: 11111111111111111111111111111101"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    int hammingWeight(uint32_t n) {\n        // Your code here\n        return 0;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    int hammingWeight(uint32_t n) {\n        int count = 0;\n        while (n != 0) {\n            count += n & 1;\n            n >>= 1;\n        }\n        return count;\n    }\n};",
                "testCases": [
                    {"input": "11", "expected_output": "3", "weight": 0.4, "description": "Binary: 1011"},
                    {"input": "128", "expected_output": "1", "weight": 0.3, "description": "Binary: 10000000"},
                    {"input": "4294967293", "expected_output": "31", "weight": 0.3, "description": "Binary: 11111111111111111111111111111101"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(1)",
            "spaceComplexity": "O(1)",
            "constraints": ["The input must be a binary string of length 32"]
        },
        "gradingRules": {
            "testCaseWeight": 0.7,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.1,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "EASY",
            "estimatedDuration": 15,
            "tags": ["divide-and-conquer", "bit-manipulation"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Bit Manipulation"
        }
    })

    # Stack & Queue - Hard: Largest Rectangle in Histogram
    questions.append({
        "id": "largest-rectangle-in-histogram",
        "title": "Largest Rectangle in Histogram",
        "text": "Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.\n\n**Example 1:**\nInput: heights = [2,1,5,6,2,3]\nOutput: 10\nExplanation: The above is a histogram where width of each bar is 1.\nThe largest rectangle is shown in the red area, which has an area = 10 units.\n\n**Example 2:**\nInput: heights = [2,4]\nOutput: 4",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def largestRectangleArea(self, heights):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def largestRectangleArea(self, heights):\n        stack = []\n        max_area = 0\n        \n        for i, h in enumerate(heights):\n            while stack and heights[stack[-1]] > h:\n                height = heights[stack.pop()]\n                width = i if not stack else i - stack[-1] - 1\n                max_area = max(max_area, height * width)\n            stack.append(i)\n        \n        while stack:\n            height = heights[stack.pop()]\n            width = len(heights) if not stack else len(heights) - stack[-1] - 1\n            max_area = max(max_area, height * width)\n        \n        return max_area",
                "testCases": [
                    {"input": "[2,1,5,6,2,3]", "expected_output": "10", "weight": 0.6, "description": "Standard histogram"},
                    {"input": "[2,4]", "expected_output": "4", "weight": 0.4, "description": "Simple case"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[]} heights\n * @return {number}\n */\nvar largestRectangleArea = function(heights) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[]} heights\n * @return {number}\n */\nvar largestRectangleArea = function(heights) {\n    const stack = [];\n    let maxArea = 0;\n    \n    for (let i = 0; i < heights.length; i++) {\n        while (stack.length > 0 && heights[stack[stack.length - 1]] > heights[i]) {\n            const height = heights[stack.pop()];\n            const width = stack.length === 0 ? i : i - stack[stack.length - 1] - 1;\n            maxArea = Math.max(maxArea, height * width);\n        }\n        stack.push(i);\n    }\n    \n    while (stack.length > 0) {\n        const height = heights[stack.pop()];\n        const width = stack.length === 0 ? heights.length : heights.length - stack[stack.length - 1] - 1;\n        maxArea = Math.max(maxArea, height * width);\n    }\n    \n    return maxArea;\n};",
                "testCases": [
                    {"input": "[2,1,5,6,2,3]", "expected_output": "10", "weight": 0.6, "description": "Standard histogram"},
                    {"input": "[2,4]", "expected_output": "4", "weight": 0.4, "description": "Simple case"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int largestRectangleArea(int[] heights) {\n        // Your code here\n        return 0;\n    }\n}",
                "solutionCode": "class Solution {\n    public int largestRectangleArea(int[] heights) {\n        Stack<Integer> stack = new Stack<>();\n        int maxArea = 0;\n        \n        for (int i = 0; i < heights.length; i++) {\n            while (!stack.isEmpty() && heights[stack.peek()] > heights[i]) {\n                int height = heights[stack.pop()];\n                int width = stack.isEmpty() ? i : i - stack.peek() - 1;\n                maxArea = Math.max(maxArea, height * width);\n            }\n            stack.push(i);\n        }\n        \n        while (!stack.isEmpty()) {\n            int height = heights[stack.pop()];\n            int width = stack.isEmpty() ? heights.length : heights.length - stack.peek() - 1;\n            maxArea = Math.max(maxArea, height * width);\n        }\n        \n        return maxArea;\n    }\n}",
                "testCases": [
                    {"input": "[2,1,5,6,2,3]", "expected_output": "10", "weight": 0.6, "description": "Standard histogram"},
                    {"input": "[2,4]", "expected_output": "4", "weight": 0.4, "description": "Simple case"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func largestRectangleArea(heights []int) int {\n    // Your code here\n    return 0\n}",
                "solutionCode": "func largestRectangleArea(heights []int) int {\n    stack := []int{}\n    maxArea := 0\n    \n    for i, h := range heights {\n        for len(stack) > 0 && heights[stack[len(stack)-1]] > h {\n            height := heights[stack[len(stack)-1]]\n            stack = stack[:len(stack)-1]\n            \n            var width int\n            if len(stack) == 0 {\n                width = i\n            } else {\n                width = i - stack[len(stack)-1] - 1\n            }\n            \n            if height*width > maxArea {\n                maxArea = height * width\n            }\n        }\n        stack = append(stack, i)\n    }\n    \n    for len(stack) > 0 {\n        height := heights[stack[len(stack)-1]]\n        stack = stack[:len(stack)-1]\n        \n        var width int\n        if len(stack) == 0 {\n            width = len(heights)\n        } else {\n            width = len(heights) - stack[len(stack)-1] - 1\n        }\n        \n        if height*width > maxArea {\n            maxArea = height * width\n        }\n    }\n    \n    return maxArea\n}",
                "testCases": [
                    {"input": "[2,1,5,6,2,3]", "expected_output": "10", "weight": 0.6, "description": "Standard histogram"},
                    {"input": "[2,4]", "expected_output": "4", "weight": 0.4, "description": "Simple case"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[]} heights\n# @return {Integer}\ndef largest_rectangle_area(heights)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[]} heights\n# @return {Integer}\ndef largest_rectangle_area(heights)\n    stack = []\n    max_area = 0\n    \n    heights.each_with_index do |h, i|\n        while !stack.empty? && heights[stack[-1]] > h\n            height = heights[stack.pop]\n            width = stack.empty? ? i : i - stack[-1] - 1\n            max_area = [max_area, height * width].max\n        end\n        stack << i\n    end\n    \n    while !stack.empty?\n        height = heights[stack.pop]\n        width = stack.empty? ? heights.length : heights.length - stack[-1] - 1\n        max_area = [max_area, height * width].max\n    end\n    \n    max_area\nend",
                "testCases": [
                    {"input": "[2,1,5,6,2,3]", "expected_output": "10", "weight": 0.6, "description": "Standard histogram"},
                    {"input": "[2,4]", "expected_output": "4", "weight": 0.4, "description": "Simple case"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    int largestRectangleArea(vector<int>& heights) {\n        // Your code here\n        return 0;\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    int largestRectangleArea(vector<int>& heights) {\n        stack<int> st;\n        int maxArea = 0;\n        \n        for (int i = 0; i < heights.size(); i++) {\n            while (!st.empty() && heights[st.top()] > heights[i]) {\n                int height = heights[st.top()];\n                st.pop();\n                int width = st.empty() ? i : i - st.top() - 1;\n                maxArea = max(maxArea, height * width);\n            }\n            st.push(i);\n        }\n        \n        while (!st.empty()) {\n            int height = heights[st.top()];\n            st.pop();\n            int width = st.empty() ? heights.size() : heights.size() - st.top() - 1;\n            maxArea = max(maxArea, height * width);\n        }\n        \n        return maxArea;\n    }\n};",
                "testCases": [
                    {"input": "[2,1,5,6,2,3]", "expected_output": "10", "weight": 0.6, "description": "Standard histogram"},
                    {"input": "[2,4]", "expected_output": "4", "weight": 0.4, "description": "Simple case"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(n)",
            "constraints": ["1 <= heights.length <= 10^5", "0 <= heights[i] <= 10^4"]
        },
        "gradingRules": {
            "testCaseWeight": 0.5,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.3,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "HARD",
            "estimatedDuration": 35,
            "tags": ["array", "stack", "monotonic-stack"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Stack & Queue"
        }
    })

    # Math & Geometry - Hard: Spiral Matrix
    questions.append({
        "id": "spiral-matrix",
        "title": "Spiral Matrix",
        "text": "Given an m x n matrix, return all elements of the matrix in spiral order.\n\n**Example 1:**\nInput: matrix = [[1,2,3],[4,5,6],[7,8,9]]\nOutput: [1,2,3,6,9,8,7,4,5]\n\n**Example 2:**\nInput: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\nOutput: [1,2,3,4,8,12,11,10,9,5,6,7]",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def spiralOrder(self, matrix):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def spiralOrder(self, matrix):\n        if not matrix or not matrix[0]:\n            return []\n        \n        result = []\n        top, bottom = 0, len(matrix) - 1\n        left, right = 0, len(matrix[0]) - 1\n        \n        while top <= bottom and left <= right:\n            # Traverse right\n            for col in range(left, right + 1):\n                result.append(matrix[top][col])\n            top += 1\n            \n            # Traverse down\n            for row in range(top, bottom + 1):\n                result.append(matrix[row][right])\n            right -= 1\n            \n            # Traverse left (if we still have rows)\n            if top <= bottom:\n                for col in range(right, left - 1, -1):\n                    result.append(matrix[bottom][col])\n                bottom -= 1\n            \n            # Traverse up (if we still have columns)\n            if left <= right:\n                for row in range(bottom, top - 1, -1):\n                    result.append(matrix[row][left])\n                left += 1\n        \n        return result",
                "testCases": [
                    {"input": "[[1,2,3],[4,5,6],[7,8,9]]", "expected_output": "[1,2,3,6,9,8,7,4,5]", "weight": 0.6, "description": "3x3 matrix"},
                    {"input": "[[1,2,3,4],[5,6,7,8],[9,10,11,12]]", "expected_output": "[1,2,3,4,8,12,11,10,9,5,6,7]", "weight": 0.4, "description": "3x4 matrix"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[][]} matrix\n * @return {number[]}\n */\nvar spiralOrder = function(matrix) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[][]} matrix\n * @return {number[]}\n */\nvar spiralOrder = function(matrix) {\n    if (matrix.length === 0 || matrix[0].length === 0) {\n        return [];\n    }\n    \n    const result = [];\n    let top = 0, bottom = matrix.length - 1;\n    let left = 0, right = matrix[0].length - 1;\n    \n    while (top <= bottom && left <= right) {\n        // Traverse right\n        for (let col = left; col <= right; col++) {\n            result.push(matrix[top][col]);\n        }\n        top++;\n        \n        // Traverse down\n        for (let row = top; row <= bottom; row++) {\n            result.push(matrix[row][right]);\n        }\n        right--;\n        \n        // Traverse left (if we still have rows)\n        if (top <= bottom) {\n            for (let col = right; col >= left; col--) {\n                result.push(matrix[bottom][col]);\n            }\n            bottom--;\n        }\n        \n        // Traverse up (if we still have columns)\n        if (left <= right) {\n            for (let row = bottom; row >= top; row--) {\n                result.push(matrix[row][left]);\n            }\n            left++;\n        }\n    }\n    \n    return result;\n};",
                "testCases": [
                    {"input": "[[1,2,3],[4,5,6],[7,8,9]]", "expected_output": "[1,2,3,6,9,8,7,4,5]", "weight": 0.6, "description": "3x3 matrix"},
                    {"input": "[[1,2,3,4],[5,6,7,8],[9,10,11,12]]", "expected_output": "[1,2,3,4,8,12,11,10,9,5,6,7]", "weight": 0.4, "description": "3x4 matrix"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public List<Integer> spiralOrder(int[][] matrix) {\n        // Your code here\n        return new ArrayList<>();\n    }\n}",
                "solutionCode": "class Solution {\n    public List<Integer> spiralOrder(int[][] matrix) {\n        List<Integer> result = new ArrayList<>();\n        if (matrix.length == 0 || matrix[0].length == 0) {\n            return result;\n        }\n        \n        int top = 0, bottom = matrix.length - 1;\n        int left = 0, right = matrix[0].length - 1;\n        \n        while (top <= bottom && left <= right) {\n            // Traverse right\n            for (int col = left; col <= right; col++) {\n                result.add(matrix[top][col]);\n            }\n            top++;\n            \n            // Traverse down\n            for (int row = top; row <= bottom; row++) {\n                result.add(matrix[row][right]);\n            }\n            right--;\n            \n            // Traverse left (if we still have rows)\n            if (top <= bottom) {\n                for (int col = right; col >= left; col--) {\n                    result.add(matrix[bottom][col]);\n                }\n                bottom--;\n            }\n            \n            // Traverse up (if we still have columns)\n            if (left <= right) {\n                for (int row = bottom; row >= top; row--) {\n                    result.add(matrix[row][left]);\n                }\n                left++;\n            }\n        }\n        \n        return result;\n    }\n}",
                "testCases": [
                    {"input": "[[1,2,3],[4,5,6],[7,8,9]]", "expected_output": "[1,2,3,6,9,8,7,4,5]", "weight": 0.6, "description": "3x3 matrix"},
                    {"input": "[[1,2,3,4],[5,6,7,8],[9,10,11,12]]", "expected_output": "[1,2,3,4,8,12,11,10,9,5,6,7]", "weight": 0.4, "description": "3x4 matrix"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func spiralOrder(matrix [][]int) []int {\n    // Your code here\n    return []int{}\n}",
                "solutionCode": "func spiralOrder(matrix [][]int) []int {\n    if len(matrix) == 0 || len(matrix[0]) == 0 {\n        return []int{}\n    }\n    \n    var result []int\n    top, bottom := 0, len(matrix)-1\n    left, right := 0, len(matrix[0])-1\n    \n    for top <= bottom && left <= right {\n        // Traverse right\n        for col := left; col <= right; col++ {\n            result = append(result, matrix[top][col])\n        }\n        top++\n        \n        // Traverse down\n        for row := top; row <= bottom; row++ {\n            result = append(result, matrix[row][right])\n        }\n        right--\n        \n        // Traverse left (if we still have rows)\n        if top <= bottom {\n            for col := right; col >= left; col-- {\n                result = append(result, matrix[bottom][col])\n            }\n            bottom--\n        }\n        \n        // Traverse up (if we still have columns)\n        if left <= right {\n            for row := bottom; row >= top; row-- {\n                result = append(result, matrix[row][left])\n            }\n            left++\n        }\n    }\n    \n    return result\n}",
                "testCases": [
                    {"input": "[[1,2,3],[4,5,6],[7,8,9]]", "expected_output": "[1,2,3,6,9,8,7,4,5]", "weight": 0.6, "description": "3x3 matrix"},
                    {"input": "[[1,2,3,4],[5,6,7,8],[9,10,11,12]]", "expected_output": "[1,2,3,4,8,12,11,10,9,5,6,7]", "weight": 0.4, "description": "3x4 matrix"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[][]} matrix\n# @return {Integer[]}\ndef spiral_order(matrix)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[][]} matrix\n# @return {Integer[]}\ndef spiral_order(matrix)\n    return [] if matrix.empty? || matrix[0].empty?\n    \n    result = []\n    top, bottom = 0, matrix.length - 1\n    left, right = 0, matrix[0].length - 1\n    \n    while top <= bottom && left <= right\n        # Traverse right\n        (left..right).each { |col| result << matrix[top][col] }\n        top += 1\n        \n        # Traverse down\n        (top..bottom).each { |row| result << matrix[row][right] }\n        right -= 1\n        \n        # Traverse left (if we still have rows)\n        if top <= bottom\n            right.downto(left) { |col| result << matrix[bottom][col] }\n            bottom -= 1\n        end\n        \n        # Traverse up (if we still have columns)\n        if left <= right\n            bottom.downto(top) { |row| result << matrix[row][left] }\n            left += 1\n        end\n    end\n    \n    result\nend",
                "testCases": [
                    {"input": "[[1,2,3],[4,5,6],[7,8,9]]", "expected_output": "[1,2,3,6,9,8,7,4,5]", "weight": 0.6, "description": "3x3 matrix"},
                    {"input": "[[1,2,3,4],[5,6,7,8],[9,10,11,12]]", "expected_output": "[1,2,3,4,8,12,11,10,9,5,6,7]", "weight": 0.4, "description": "3x4 matrix"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    vector<int> spiralOrder(vector<vector<int>>& matrix) {\n        // Your code here\n        return {};\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    vector<int> spiralOrder(vector<vector<int>>& matrix) {\n        vector<int> result;\n        if (matrix.empty() || matrix[0].empty()) {\n            return result;\n        }\n        \n        int top = 0, bottom = matrix.size() - 1;\n        int left = 0, right = matrix[0].size() - 1;\n        \n        while (top <= bottom && left <= right) {\n            // Traverse right\n            for (int col = left; col <= right; col++) {\n                result.push_back(matrix[top][col]);\n            }\n            top++;\n            \n            // Traverse down\n            for (int row = top; row <= bottom; row++) {\n                result.push_back(matrix[row][right]);\n            }\n            right--;\n            \n            // Traverse left (if we still have rows)\n            if (top <= bottom) {\n                for (int col = right; col >= left; col--) {\n                    result.push_back(matrix[bottom][col]);\n                }\n                bottom--;\n            }\n            \n            // Traverse up (if we still have columns)\n            if (left <= right) {\n                for (int row = bottom; row >= top; row--) {\n                    result.push_back(matrix[row][left]);\n                }\n                left++;\n            }\n        }\n        \n        return result;\n    }\n};",
                "testCases": [
                    {"input": "[[1,2,3],[4,5,6],[7,8,9]]", "expected_output": "[1,2,3,6,9,8,7,4,5]", "weight": 0.6, "description": "3x3 matrix"},
                    {"input": "[[1,2,3,4],[5,6,7,8],[9,10,11,12]]", "expected_output": "[1,2,3,4,8,12,11,10,9,5,6,7]", "weight": 0.4, "description": "3x4 matrix"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(m * n)",
            "spaceComplexity": "O(1)",
            "constraints": ["m == matrix.length", "n == matrix[i].length", "1 <= m, n <= 10", "-100 <= matrix[i][j] <= 100"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 25,
            "tags": ["array", "matrix", "simulation"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
            "topic": "Math & Geometry"
        }
    })

    # Arrays & Strings - Easy: Product of Array Except Self
    questions.append({
        "id": "product-of-array-except-self",
        "title": "Product of Array Except Self",
        "text": "Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].\n\nThe product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.\n\nYou must write an algorithm that runs in O(n) time and without using the division operation.\n\n**Example 1:**\nInput: nums = [1,2,3,4]\nOutput: [24,12,8,6]\n\n**Example 2:**\nInput: nums = [-1,1,0,-3,3]\nOutput: [0,0,9,0,0]",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def productExceptSelf(self, nums):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def productExceptSelf(self, nums):\n        n = len(nums)\n        result = [1] * n\n        \n        # Calculate left products\n        for i in range(1, n):\n            result[i] = result[i - 1] * nums[i - 1]\n        \n        # Calculate right products and multiply with left products\n        right_product = 1\n        for i in range(n - 1, -1, -1):\n            result[i] *= right_product\n            right_product *= nums[i]\n        \n        return result",
                "testCases": [
                    {"input": "[1,2,3,4]", "expected_output": "[24,12,8,6]", "weight": 0.6, "description": "Standard case"},
                    {"input": "[-1,1,0,-3,3]", "expected_output": "[0,0,9,0,0]", "weight": 0.4, "description": "With zero"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar productExceptSelf = function(nums) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar productExceptSelf = function(nums) {\n    const n = nums.length;\n    const result = new Array(n).fill(1);\n    \n    // Calculate left products\n    for (let i = 1; i < n; i++) {\n        result[i] = result[i - 1] * nums[i - 1];\n    }\n    \n    // Calculate right products and multiply with left products\n    let rightProduct = 1;\n    for (let i = n - 1; i >= 0; i--) {\n        result[i] *= rightProduct;\n        rightProduct *= nums[i];\n    }\n    \n    return result;\n};",
                "testCases": [
                    {"input": "[1,2,3,4]", "expected_output": "[24,12,8,6]", "weight": 0.6, "description": "Standard case"},
                    {"input": "[-1,1,0,-3,3]", "expected_output": "[0,0,9,0,0]", "weight": 0.4, "description": "With zero"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int[] productExceptSelf(int[] nums) {\n        // Your code here\n        return new int[0];\n    }\n}",
                "solutionCode": "class Solution {\n    public int[] productExceptSelf(int[] nums) {\n        int n = nums.length;\n        int[] result = new int[n];\n        \n        // Initialize result array with 1s\n        Arrays.fill(result, 1);\n        \n        // Calculate left products\n        for (int i = 1; i < n; i++) {\n            result[i] = result[i - 1] * nums[i - 1];\n        }\n        \n        // Calculate right products and multiply with left products\n        int rightProduct = 1;\n        for (int i = n - 1; i >= 0; i--) {\n            result[i] *= rightProduct;\n            rightProduct *= nums[i];\n        }\n        \n        return result;\n    }\n}",
                "testCases": [
                    {"input": "[1,2,3,4]", "expected_output": "[24,12,8,6]", "weight": 0.6, "description": "Standard case"},
                    {"input": "[-1,1,0,-3,3]", "expected_output": "[0,0,9,0,0]", "weight": 0.4, "description": "With zero"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func productExceptSelf(nums []int) []int {\n    // Your code here\n    return []int{}\n}",
                "solutionCode": "func productExceptSelf(nums []int) []int {\n    n := len(nums)\n    result := make([]int, n)\n    \n    // Initialize result array with 1s\n    for i := range result {\n        result[i] = 1\n    }\n    \n    // Calculate left products\n    for i := 1; i < n; i++ {\n        result[i] = result[i-1] * nums[i-1]\n    }\n    \n    // Calculate right products and multiply with left products\n    rightProduct := 1\n    for i := n - 1; i >= 0; i-- {\n        result[i] *= rightProduct\n        rightProduct *= nums[i]\n    }\n    \n    return result\n}",
                "testCases": [
                    {"input": "[1,2,3,4]", "expected_output": "[24,12,8,6]", "weight": 0.6, "description": "Standard case"},
                    {"input": "[-1,1,0,-3,3]", "expected_output": "[0,0,9,0,0]", "weight": 0.4, "description": "With zero"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer[]} nums\n# @return {Integer[]}\ndef product_except_self(nums)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer[]} nums\n# @return {Integer[]}\ndef product_except_self(nums)\n    n = nums.length\n    result = Array.new(n, 1)\n    \n    # Calculate left products\n    (1...n).each do |i|\n        result[i] = result[i - 1] * nums[i - 1]\n    end\n    \n    # Calculate right products and multiply with left products\n    right_product = 1\n    (n - 1).downto(0) do |i|\n        result[i] *= right_product\n        right_product *= nums[i]\n    end\n    \n    result\nend",
                "testCases": [
                    {"input": "[1,2,3,4]", "expected_output": "[24,12,8,6]", "weight": 0.6, "description": "Standard case"},
                    {"input": "[-1,1,0,-3,3]", "expected_output": "[0,0,9,0,0]", "weight": 0.4, "description": "With zero"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    vector<int> productExceptSelf(vector<int>& nums) {\n        // Your code here\n        return {};\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    vector<int> productExceptSelf(vector<int>& nums) {\n        int n = nums.size();\n        vector<int> result(n, 1);\n        \n        // Calculate left products\n        for (int i = 1; i < n; i++) {\n            result[i] = result[i - 1] * nums[i - 1];\n        }\n        \n        // Calculate right products and multiply with left products\n        int rightProduct = 1;\n        for (int i = n - 1; i >= 0; i--) {\n            result[i] *= rightProduct;\n            rightProduct *= nums[i];\n        }\n        \n        return result;\n    }\n};",
                "testCases": [
                    {"input": "[1,2,3,4]", "expected_output": "[24,12,8,6]", "weight": 0.6, "description": "Standard case"},
                    {"input": "[-1,1,0,-3,3]", "expected_output": "[0,0,9,0,0]", "weight": 0.4, "description": "With zero"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(n)",
            "spaceComplexity": "O(1)",
            "constraints": ["2 <= nums.length <= 10^5", "-30 <= nums[i] <= 30", "The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer"]
        },
        "gradingRules": {
            "testCaseWeight": 0.6,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.2,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 20,
            "tags": ["array", "prefix-sum"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Arrays & Strings"
        }
    })

    # Graph Algorithms - Hard: Course Schedule II
    questions.append({
        "id": "course-schedule-ii",
        "title": "Course Schedule II",
        "text": "There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.\n\nFor example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.\n\nReturn the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.\n\n**Example 1:**\nInput: numCourses = 2, prerequisites = [[1,0]]\nOutput: [0,1]\nExplanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].\n\n**Example 2:**\nInput: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]\nOutput: [0,2,1,3]\nExplanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.\nSo one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].\n\n**Example 3:**\nInput: numCourses = 1, prerequisites = []\nOutput: [0]",
        "implementations": [
            {
                "language": "python",
                "starterCode": "class Solution:\n    def findOrder(self, numCourses, prerequisites):\n        # Your code here\n        pass",
                "solutionCode": "class Solution:\n    def findOrder(self, numCourses, prerequisites):\n        from collections import defaultdict, deque\n        \n        # Build adjacency list and in-degree count\n        graph = defaultdict(list)\n        in_degree = [0] * numCourses\n        \n        for course, prereq in prerequisites:\n            graph[prereq].append(course)\n            in_degree[course] += 1\n        \n        # Find all courses with no prerequisites\n        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])\n        result = []\n        \n        while queue:\n            course = queue.popleft()\n            result.append(course)\n            \n            # Remove this course and update in-degrees\n            for next_course in graph[course]:\n                in_degree[next_course] -= 1\n                if in_degree[next_course] == 0:\n                    queue.append(next_course)\n        \n        # Check if all courses can be taken (no cycle)\n        return result if len(result) == numCourses else []",
                "testCases": [
                    {"input": "2, [[1,0]]", "expected_output": "[0,1]", "weight": 0.4, "description": "Simple case"},
                    {"input": "4, [[1,0],[2,0],[3,1],[3,2]]", "expected_output": "[0,2,1,3]", "weight": 0.4, "description": "Complex dependencies"},
                    {"input": "1, []", "expected_output": "[0]", "weight": 0.2, "description": "Single course"}
                ]
            },
            {
                "language": "javascript",
                "starterCode": "/**\n * @param {number} numCourses\n * @param {number[][]} prerequisites\n * @return {number[]}\n */\nvar findOrder = function(numCourses, prerequisites) {\n    // Your code here\n};",
                "solutionCode": "/**\n * @param {number} numCourses\n * @param {number[][]} prerequisites\n * @return {number[]}\n */\nvar findOrder = function(numCourses, prerequisites) {\n    const graph = Array(numCourses).fill().map(() => []);\n    const inDegree = new Array(numCourses).fill(0);\n    \n    // Build graph and in-degree count\n    for (const [course, prereq] of prerequisites) {\n        graph[prereq].push(course);\n        inDegree[course]++;\n    }\n    \n    // Find courses with no prerequisites\n    const queue = [];\n    for (let i = 0; i < numCourses; i++) {\n        if (inDegree[i] === 0) {\n            queue.push(i);\n        }\n    }\n    \n    const result = [];\n    \n    while (queue.length > 0) {\n        const course = queue.shift();\n        result.push(course);\n        \n        // Remove this course and update in-degrees\n        for (const nextCourse of graph[course]) {\n            inDegree[nextCourse]--;\n            if (inDegree[nextCourse] === 0) {\n                queue.push(nextCourse);\n            }\n        }\n    }\n    \n    return result.length === numCourses ? result : [];\n};",
                "testCases": [
                    {"input": "2, [[1,0]]", "expected_output": "[0,1]", "weight": 0.4, "description": "Simple case"},
                    {"input": "4, [[1,0],[2,0],[3,1],[3,2]]", "expected_output": "[0,2,1,3]", "weight": 0.4, "description": "Complex dependencies"},
                    {"input": "1, []", "expected_output": "[0]", "weight": 0.2, "description": "Single course"}
                ]
            },
            {
                "language": "java",
                "starterCode": "class Solution {\n    public int[] findOrder(int numCourses, int[][] prerequisites) {\n        // Your code here\n        return new int[0];\n    }\n}",
                "solutionCode": "class Solution {\n    public int[] findOrder(int numCourses, int[][] prerequisites) {\n        List<List<Integer>> graph = new ArrayList<>();\n        int[] inDegree = new int[numCourses];\n        \n        // Initialize graph\n        for (int i = 0; i < numCourses; i++) {\n            graph.add(new ArrayList<>());\n        }\n        \n        // Build graph and in-degree count\n        for (int[] prereq : prerequisites) {\n            int course = prereq[0];\n            int pre = prereq[1];\n            graph.get(pre).add(course);\n            inDegree[course]++;\n        }\n        \n        // Find courses with no prerequisites\n        Queue<Integer> queue = new LinkedList<>();\n        for (int i = 0; i < numCourses; i++) {\n            if (inDegree[i] == 0) {\n                queue.offer(i);\n            }\n        }\n        \n        List<Integer> result = new ArrayList<>();\n        \n        while (!queue.isEmpty()) {\n            int course = queue.poll();\n            result.add(course);\n            \n            // Remove this course and update in-degrees\n            for (int nextCourse : graph.get(course)) {\n                inDegree[nextCourse]--;\n                if (inDegree[nextCourse] == 0) {\n                    queue.offer(nextCourse);\n                }\n            }\n        }\n        \n        if (result.size() == numCourses) {\n            return result.stream().mapToInt(i -> i).toArray();\n        } else {\n            return new int[0];\n        }\n    }\n}",
                "testCases": [
                    {"input": "2, [[1,0]]", "expected_output": "[0,1]", "weight": 0.4, "description": "Simple case"},
                    {"input": "4, [[1,0],[2,0],[3,1],[3,2]]", "expected_output": "[0,2,1,3]", "weight": 0.4, "description": "Complex dependencies"},
                    {"input": "1, []", "expected_output": "[0]", "weight": 0.2, "description": "Single course"}
                ]
            },
            {
                "language": "go",
                "starterCode": "func findOrder(numCourses int, prerequisites [][]int) []int {\n    // Your code here\n    return []int{}\n}",
                "solutionCode": "func findOrder(numCourses int, prerequisites [][]int) []int {\n    graph := make([][]int, numCourses)\n    inDegree := make([]int, numCourses)\n    \n    // Build graph and in-degree count\n    for _, prereq := range prerequisites {\n        course, pre := prereq[0], prereq[1]\n        graph[pre] = append(graph[pre], course)\n        inDegree[course]++\n    }\n    \n    // Find courses with no prerequisites\n    var queue []int\n    for i := 0; i < numCourses; i++ {\n        if inDegree[i] == 0 {\n            queue = append(queue, i)\n        }\n    }\n    \n    var result []int\n    \n    for len(queue) > 0 {\n        course := queue[0]\n        queue = queue[1:]\n        result = append(result, course)\n        \n        // Remove this course and update in-degrees\n        for _, nextCourse := range graph[course] {\n            inDegree[nextCourse]--\n            if inDegree[nextCourse] == 0 {\n                queue = append(queue, nextCourse)\n            }\n        }\n    }\n    \n    if len(result) == numCourses {\n        return result\n    }\n    return []int{}\n}",
                "testCases": [
                    {"input": "2, [[1,0]]", "expected_output": "[0,1]", "weight": 0.4, "description": "Simple case"},
                    {"input": "4, [[1,0],[2,0],[3,1],[3,2]]", "expected_output": "[0,2,1,3]", "weight": 0.4, "description": "Complex dependencies"},
                    {"input": "1, []", "expected_output": "[0]", "weight": 0.2, "description": "Single course"}
                ]
            },
            {
                "language": "ruby",
                "starterCode": "# @param {Integer} num_courses\n# @param {Integer[][]} prerequisites\n# @return {Integer[]}\ndef find_order(num_courses, prerequisites)\n    # Your code here\nend",
                "solutionCode": "# @param {Integer} num_courses\n# @param {Integer[][]} prerequisites\n# @return {Integer[]}\ndef find_order(num_courses, prerequisites)\n    graph = Array.new(num_courses) { [] }\n    in_degree = Array.new(num_courses, 0)\n    \n    # Build graph and in-degree count\n    prerequisites.each do |course, prereq|\n        graph[prereq] << course\n        in_degree[course] += 1\n    end\n    \n    # Find courses with no prerequisites\n    queue = []\n    (0...num_courses).each do |i|\n        queue << i if in_degree[i] == 0\n    end\n    \n    result = []\n    \n    until queue.empty?\n        course = queue.shift\n        result << course\n        \n        # Remove this course and update in-degrees\n        graph[course].each do |next_course|\n            in_degree[next_course] -= 1\n            queue << next_course if in_degree[next_course] == 0\n        end\n    end\n    \n    result.length == num_courses ? result : []\nend",
                "testCases": [
                    {"input": "2, [[1,0]]", "expected_output": "[0,1]", "weight": 0.4, "description": "Simple case"},
                    {"input": "4, [[1,0],[2,0],[3,1],[3,2]]", "expected_output": "[0,2,1,3]", "weight": 0.4, "description": "Complex dependencies"},
                    {"input": "1, []", "expected_output": "[0]", "weight": 0.2, "description": "Single course"}
                ]
            },
            {
                "language": "cpp",
                "starterCode": "class Solution {\npublic:\n    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {\n        // Your code here\n        return {};\n    }\n};",
                "solutionCode": "class Solution {\npublic:\n    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {\n        vector<vector<int>> graph(numCourses);\n        vector<int> inDegree(numCourses, 0);\n        \n        // Build graph and in-degree count\n        for (const auto& prereq : prerequisites) {\n            int course = prereq[0];\n            int pre = prereq[1];\n            graph[pre].push_back(course);\n            inDegree[course]++;\n        }\n        \n        // Find courses with no prerequisites\n        queue<int> q;\n        for (int i = 0; i < numCourses; i++) {\n            if (inDegree[i] == 0) {\n                q.push(i);\n            }\n        }\n        \n        vector<int> result;\n        \n        while (!q.empty()) {\n            int course = q.front();\n            q.pop();\n            result.push_back(course);\n            \n            // Remove this course and update in-degrees\n            for (int nextCourse : graph[course]) {\n                inDegree[nextCourse]--;\n                if (inDegree[nextCourse] == 0) {\n                    q.push(nextCourse);\n                }\n            }\n        }\n        \n        return result.size() == numCourses ? result : vector<int>();\n    }\n};",
                "testCases": [
                    {"input": "2, [[1,0]]", "expected_output": "[0,1]", "weight": 0.4, "description": "Simple case"},
                    {"input": "4, [[1,0],[2,0],[3,1],[3,2]]", "expected_output": "[0,2,1,3]", "weight": 0.4, "description": "Complex dependencies"},
                    {"input": "1, []", "expected_output": "[0]", "weight": 0.2, "description": "Single course"}
                ]
            }
        ],
        "evaluationCriteria": {
            "timeComplexity": "O(V + E)",
            "spaceComplexity": "O(V + E)",
            "constraints": ["1 <= numCourses <= 2000", "0 <= prerequisites.length <= numCourses * (numCourses - 1)", "prerequisites[i].length == 2", "0 <= ai, bi < numCourses", "ai != bi", "All the pairs [ai, bi] are distinct"]
        },
        "gradingRules": {
            "testCaseWeight": 0.5,
            "codeQualityWeight": 0.2,
            "efficiencyWeight": 0.3,
            "partialCredit": True
        },
        "metadata": {
            "difficulty": "MEDIUM",
            "estimatedDuration": 30,
            "tags": ["depth-first-search", "breadth-first-search", "graph", "topological-sort"],
            "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple", "LinkedIn"],
            "topic": "Trees & Graphs"
        }
    })

    return questions
