# my_solution
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


# other_solution

# def check_palindrome(s: str) -> bool:
#     strs = collections.deque()
#
#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
#
#     while len(strs) > 1:
#         if strs.popleft() != strs.pop():
#             return False
#
#     return True


# def check_palindrome(s: str) -> bool:
#     s = s.lower()
#     s = re.sub('[^a-z0-9]', '', s)
#
#     return s == s[::-1]
