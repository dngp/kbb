import numpy as np 


def string_to_cards(cards:str) -> list[list[int]]:
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
                case "Q": out[i].append(12)
                case "K": out[i].append(13)
                case "A": out[i].append(14)
                case _: out[i].append(int(letter))
        
        out[i].sort(reverse=True)
    return out


def cardlist_to_strings(cards:list[list[int]]) -> list[str]:
    out = []
    for suit in cards:
        suitstr = ""
        if suit == []:
            out.append(suitstr)
        else:
            for val in suit:
                match val:
                    case 14: suitstr += "A"
                    case 13: suitstr += "K"
                    case 12: suitstr += "Q"
                    case 11: suitstr += "J"
                    case 10: suitstr += "10"
                    case _: suitstr += f"{val}"
            out.append(suitstr)

    return out


def return_bid_value(level:int,letter:str) -> int:
    match letter:
        case "c": return 1 + 10*(level-1)
        case "d": return 2 + 10*(level-1)
        case "h": return 3 + 10*(level-1)
        case "s": return 4 + 10*(level-1)
        case "n": return 5 + 10*(level-1)
        case _: raise ValueError("return_bid_value cannot assign a bid.")


def string_to_bids(bids:str) -> list[int]:
    """
    Given a string of the bids made, represent it as
    a list of integers. Bids always begin with declarer.
    Redouble is denoted 'r' and notrump 'n'.
    Example input: "p1c1sxp2hppp"
    and ouput: []
    """
    bids = ''.join(bids.split())
    out = []
    for i, letter in enumerate(bids):
        match letter:
            case ("c" | "d" | "h" | "s" | "n"): continue
            case "p": out.append(0)
            case "1": out.append(return_bid_value(1,bids[i+1]))
            case "2": out.append(return_bid_value(2,bids[i+1]))
            case "3": out.append(return_bid_value(3,bids[i+1]))
            case "4": out.append(return_bid_value(4,bids[i+1]))
            case "5": out.append(return_bid_value(5,bids[i+1]))
            case "6": out.append(return_bid_value(6,bids[i+1]))
            case "7": out.append(return_bid_value(7,bids[i+1]))
            case "x": out.append(-1)
            case "r": out.append(-2)

    return out

SUITS = ["\u2663", "\u2666", "\u2665", "\u2660"]
CLUB = SUITS[0]
DIAMOND = SUITS[1]
HEART = SUITS[2]
SPADE = SUITS[3]



def display_deal(info:list, cards:list, bids:list, playernames:list[str]=["West","North","East","South"]) -> None:
    """
    Given the board, bids and cards,
    represent them in a terminal board interface.
    Info: [board nr, vul 0-NS, 1-EW, decl "w", "n", "e", "s"]
    """
    boardnr = str(info[0]).zfill(3)

    if info[1] == 0: 
        vulns = "V"
        vulew = "n"
    elif info[1] == 1:
        vulns = "n"
        vulew = "V"
    else:
        raise ValueError("Incorrect vulnerability option.")

    cardstrs_west = cardlist_to_strings(cards[0])
    cardstrs_north = cardlist_to_strings(cards[1])
    cardstrs_east = cardlist_to_strings(cards[2])
    cardstrs_south = cardlist_to_strings(cards[3])

    lines = []
    lines.append(f"""      {"D" if info[2]=="n" else " "}      """)
    lines.append(f"""      {vulns}      """)
    lines.append(f""" {"D" if info[2]=="w" else " "} {vulew} {boardnr} {vulew} {"D" if info[2]=="e" else " "} """)
    lines.append(f"""      {vulns}      """)
    lines.append(f"""      {"D" if info[2]=="s" else " "}      """)
    
    lines.append("W " + playernames[0])
    lines.append(SPADE + " " + cardstrs_west[0])
    lines.append(HEART + " " + cardstrs_west[1])
    lines.append(DIAMOND + " " + cardstrs_west[2])
    lines.append(CLUB + " " + cardstrs_west[3])

    lines.append(f"""             """)
    lines.append(f"""             """)
    lines.append(f"""             """)
    lines.append(f"""             """)
    lines.append(f"""             """)

    lines[0] += "N " + playernames[1]
    lines[1] += SPADE + " " + cardstrs_north[0]
    lines[2] += HEART + " " + cardstrs_north[1]
    lines[3] += DIAMOND + " " + cardstrs_north[2]
    lines[4] += CLUB + " " + cardstrs_north[3]
    
    lines[10] += "S " + playernames[3]
    lines[11] += SPADE + " " + cardstrs_south[0]
    lines[12] += HEART + " " + cardstrs_south[1]
    lines[13] += DIAMOND + " " + cardstrs_south[2]
    lines[14] += CLUB + " " + cardstrs_south[3]

    for lstr in lines:
        print(lstr)



def main():
    ...

if __name__ == "__main__":
    cards = string_to_cards("KQJ109 AQ - 876543")
    string_to_bids("ppp1c p 1d xr1nppp")


    display_deal(
            [1, 0, "w"],
            [cards, cards, cards, cards],
            []
            )





