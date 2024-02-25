def playing_domino(cards, deck):
    matching_card = [my_card for my_card in cards if any(num in my_card for num in deck)]

    if matching_card:
        max_num_card = max(matching_card, key=lambda x:sum(x))
        return max_num_card
    else:
        return []


if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []