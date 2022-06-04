class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Convert to lower
        # Remove all non-alphanumeric characters
        forward = ""
        for char in s.lower():
            if char.isalnum():
                forward+=char

        # Read all chars backwards as forward
        backward = ""
        for char in range(len(forward)-1, -1, -1):
            backward += forward[char]

        # Check if backward is equal to forward
        if backward == forward:
            return True
        return False
        