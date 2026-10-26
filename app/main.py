lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}


def sort_func(args_list: list) -> dict:
    sorted_variables = {}
    immutable_list = []
    mutable_list = []

    for item in args_list:
        if isinstance(item, (list, dict, set)):
            mutable_list.append(item)
        else:
            immutable_list.append(item)

    sorted_variables["immutable"] = immutable_list
    sorted_variables["mutable"] = mutable_list

    return sorted_variables


result = sort_func([
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins
])
print(result)
