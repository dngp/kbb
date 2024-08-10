import numpy as np 


def string_to_cards(cards:str) -> list[int]:
    """
    Given as input the cards of a player, written as 
        "AQ75 KJ109 762 AKQ"
        "KQJ10987 - 954 AK2"
    in order S, H, D, C, and where - denotes void,
    outputs them as the primary data type -- a list 
    of integers. J=11, Q=12, K=13, A=14.
    """
    cards_in_suits = cards.split(" ")
    out = [[], [], [], []]
    for i in range(4):
        if cards_in_suits[i] == "-":
            continue
        for letter in cards_in_suits[i]:
            match letter:
                case "0": continue
                case "1": out[i].append(10)
                case "J": out[i].append(11)
                case "K": out[i].append(12)
                case "Q": out[i].append(13)
                case "A": out[i].append(14)
                case _: out[i].append(int(letter))

    return out 






def display_deal(info:list, cards:list, bids:list) -> None:
    """
    Given the board, bids and cards,
    represent them in a terminal board interface.
    """
    



def main():
    ...

if __name__ == "__main__":
    main()
