def best_score(a_dictionary):
    sum1 = 0
    if a_dictionary == None:
        return None
    else:
        for x in a_dictionary:
            if a_dictionary[x] > sum1:
                sum1 = a_dictionary[x]
                sum2 = x
        return sum2
