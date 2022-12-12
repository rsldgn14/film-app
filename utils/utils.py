import requests


def unique(list1):
    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


print(requests.get(
    "https://m.media-amazon.com/images/M/MV5BMTAzOTBhNTAtMzY5MS00YjcwLWIzYWItNWI1NzQ4YjcxY2E2XkEyXkFqcGdeQXVyNTI4MjkwNjA@._V1_SX300.jpg").content)
