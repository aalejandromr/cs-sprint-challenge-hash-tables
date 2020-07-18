# Plan

# Creo todos los reminders, con la siguiente forma
        # store{ 4: (17, 0), 6: (15, 1) }
        # donde index es weight y value es (reminder, index)
        # traverse por todo el array de nuevo, still O(n)
        # para 4, el reminder es 17, hay algun index 17?
        # # i - limit in store? no, next
        # para 6, el reminder es 15, hay algun index 15?
        # # i - limit in store? yes,
        # # # Get the value and get i as well, get both index and order asc

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    store = {}
    # Need a temp store since I can't hold duplicate keys on the same data structure
    dup_keys = {}

    for index in range(len(weights)):
        if weights[index] not in store:
            store[weights[index]] = (limit - weights[index], index)
        elif len(store) <= 1:
            dup_keys[weights[index]] = (limit - weights[index], index)

    for index in range(len(weights)):
        if store[weights[index]][0] in store:
            # If there is duplicates, answer should be in looking at dub and store for the same key
            if len(dup_keys) > 0:
                return (dup_keys[dup_keys[weights[index]][0]][1], store[weights[index]][1])
            return (store[store[weights[index]][0]][1], store[weights[index]][1])

    return None

# weights_2 = [4, 4]
# print(get_indices_of_item_weights(weights_2, 2, 8))