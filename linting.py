def count(sequence, item):
    y = 0
    for n in sequence:
        if n == item:
            y += 1
    return y


int_list = [1,2,3,2,4,2,5]
int_item = 2
int_count = count(int_list, int_item)
assert int_count == 3, f"Expected count of {int_item} is 3, but got {int_count}"

str_list = ["apple", "banana", "cherry", "strawberry"]
str_item = "banana"
str_count = count(str_list, str_item)
assert str_count == 1, f"Expected count of {str_item} is 3, but got {str_count}"

print("Tests passed!")