from pprint import pprint

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def lcs(strA, strB):
    if len(strA) == 0 or len(strB) == 0:
        return 0
    elif strA[-1] == strB[-1]: # if the last characters match
        return 1 + lcs(strA[:-1], strB[:-1])
    else: # if the last characters don't match
        return max(lcs(strA[:-1], strB), lcs(strA, strB[:-1]))


def lcs_dp(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    rows = len(strA) + 1
    cols = len(strB) + 1

    dp_table = [[0 for j in range(cols)] for i in range(rows)]


    for string_a_current_char in range(rows):
        for string_b_current_char in range(cols):

            
            if string_a_current_char == 0 or string_b_current_char == 0:
                dp_table[string_a_current_char][string_b_current_char] = 0


            elif strA[string_a_current_char - 1] == strB[string_b_current_char - 1]:
                dp_table[string_a_current_char][string_b_current_char] = dp_table[string_a_current_char - 1][string_b_current_char - 1] + 1


            else:
                above_option = dp_table[string_a_current_char - 1][string_b_current_char]
                left_option = dp_table[string_a_current_char][string_b_current_char - 1]

                dp_table[string_a_current_char][string_b_current_char] = max(left_option, above_option)

    # TODO: Fill in the table using a nested for loop.
    return dp_table[rows-1][cols-1]

def knapsack(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    if len(items) == 0 or capacity <= 0:
        return 0


    value_without = knapsack(items[1:], capacity)

    if capacity < items[0][1]:
        return value_without
    else:
        value_with = items[0][2] + knapsack(items[1:], capacity - items[0][1])
        return max(value_with, value_without)


def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # TODO: Fill in the table using a nested for loop.
    for current_num_items in range(rows):
            for current_capacity in range(cols):
                if current_num_items == 0 or current_capacity == 0:
                    dp_table[current_num_items][current_capacity] = 0
                    continue


                elif items[current_num_items - 1][1] > current_capacity:
                    dp_table[current_num_items][current_capacity] = dp_table[current_num_items-1][current_capacity]

                else:
                    value_with = items[current_num_items-1][2] + dp_table[current_num_items-1][current_capacity - items[current_num_items-1][1]]
                    value_without = dp_table[current_num_items-1][current_capacity]
                    dp_table[current_num_items][current_capacity] = max(value_with, value_without)
    return dp_table[rows-1][cols-1]
    
def edit_distance(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)




    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[:-1])


    else:
        insert_call = edit_distance(str1, str2[:-1])
        delete_call = edit_distance(str1[:-1], str2)
        replace_call = edit_distance(str1[:-1], str2[:-1])



    return min(insert_call, delete_call, replace_call) + 1

def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # TODO: Fill in the table using a nested for loop.
    for string1_current_char in range(rows):
        for string2_current_char in range(cols):

            if string1_current_char == 0  or string2_current_char == 0:
                dp_table[string1_current_char][string2_current_char] = max(string1_current_char, string2_current_char)

            if str1[string1_current_char - 1] == str2[string2_current_char - 1]:
                dp_table[string1_current_char][string2_current_char] = dp_table[string1_current_char - 1][string2_current_char -  1]

            else:
                insert_call = dp_table[string1_current_char][string2_current_char - 1]
                delete_call = dp_table[string1_current_char - 1][string2_current_char]
                replace_call = dp_table[string1_current_char - 1][string2_current_char - 1]

                dp_table[string1_current_char][string2_current_char] = min(insert_call, delete_call, replace_call) + 1
    return dp_table[rows-1][cols-1]
