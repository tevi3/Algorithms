# my_solution
class Solution:
    def reverse_string(self, s: list[str]) -> None:

        reversed_list = s[::-1]

        for num in range(len(s)):
            s[num] = reversed_list[num]


# other_solution

# def reverse_string(s: list[str]) -> None:
#
#     left, right = 0, len(s) - 1
#
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1

# def reverse_string(s: list[str]) -> None:
#
#     s[:] = s[::-1]
