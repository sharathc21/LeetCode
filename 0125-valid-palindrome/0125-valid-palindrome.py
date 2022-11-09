class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = re.sub("[^A-Za-z0-9]+", "", s).lower()
        s1_reverse = s1[ : : -1]
        print(s1)
        print(s1_reverse)
        if (s1==s1_reverse):
            return True
        return False
    