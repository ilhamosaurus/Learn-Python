# var_arr = [1, 2, 3, 4, 5]

# for i in range(len(var_arr)):
#     current_element = var_arr[i]
#     next_index = i + 1

#     if next_index < len(var_arr):
#         next_element = var_arr[next_index]
#     else:
#         next_element = None

#     print(f"Current element: {current_element}, next element: {next_element}")


var_arr = [i for i in range(101)]
total = sum(var_arr)
jumlah = len(var_arr)
result = total / jumlah

print(
    f"array memiliki total sebesar {total} dengan jumlah elemen sebanyak {jumlah} dan rata - rata sebesar {result}"
)
