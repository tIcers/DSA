"""125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters."""


class Solution:
    def alphanum(self, char):
        return (ord('A')<= ord(char) <= ord('Z') or
        ord('a')<= ord(char) <= ord('z') or
        ord('0')<= ord(char) <= ord('9'))

    def isPalindrome(self, s):
        left_pointer, right_pointer = 0, len(s)-1

        while left_pointer < right_pointer:
            while left_pointer < right_pointer and not self.alphanum(s[left_pointer]):
                left_pointer += 1
            while left_pointer < right_pointer and not self.alphanum(s[right_pointer]):
                right_pointer -= 1
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            left_pointer += 1
            right_pointer -= 1
        return True
