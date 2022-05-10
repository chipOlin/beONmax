# def check_sequence(list_values):
#     if len(list_values) >= 2:
#         i = 0
#         tflist = []
#         for v in list_values:
#             i += 1
#             if i < len(list_values):
#                 tflist.append(v < list_values[i])
#         if all(tflist):
#             print(1)
#         elif any(tflist):
#             print(0)
#         else:
#             print(-1)
#     else:
#         print("list too small")
#
def check_sequence(lst):
    if sorted(set(lst)) == lst:
        return 1
    elif sorted(set(lst), reverse=True) == lst:
        return -1
    else:
        return 0


print(check_sequence([1, 2, 3]))
print(check_sequence([3, 2, 1]))
print(check_sequence([1, 1, 2]))
