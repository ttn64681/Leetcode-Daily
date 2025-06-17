class Solution:
    def isPalindrome(s: str) -> bool:
        string = s.lower().replace(" ", "")
        print(string)
        for c in string:
            if not c.isalpha():
                string = string.replace(c, "")
        print(string)
        return string == string[::-1]

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama?"
    print(Solution.isPalindrome(s))