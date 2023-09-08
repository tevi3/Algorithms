class Solution:
    def check_palindrome(self, check_case: str) -> bool:

        check_list = []

        for char in check_case.lower():
            if char.isalnum():
                check_list.append(char)

        if check_list == check_list[::-1]:
            return True
        else:
            return False
