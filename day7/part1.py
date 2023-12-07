import re

_card_val_dict = {"A" : 20,
                  "K" : 13,
                  "Q" : 12,
                  "J" : 11,
                  "T" : 10,
                  "9" : 9,
                  "8" : 8,
                  "7" : 7,
                  "6" : 6,
                  "5" : 5,
                  "4" : 4,
                  "3" : 3,
                  "2" : 2}

_hand_type_dict = {"high_card" : 1,
                   "one_pair" : 2,
                   "two_pair" : 3,
                   "three_of_a_kind": 4,
                   "full_house" : 5,
                   "four_of_a_kind" : 6,
                   "five_of_a_kind" : 7}

def convert_cards_str(cards_str):
    return [_card_val_dict[c] for c in cards_str]

def get_sublists_with_size(mlist, lsize):
    index_increment = len(mlist) - lsize
    sublists = []
    for i in range(index_increment + 1):
        sublists.append(mlist[i:len(mlist) - (index_increment - i)])
    return sublists

def all_elements_in_list_equal(list_):
    return all(e == list_[0] for e in list_)

def determine_hand_type(cards):
    if all_elements_in_list_equal(cards):
        return "five_of_a_kind"

    cards = sorted(cards)

    for sublist in get_sublists_with_size(cards, 4):
        if all_elements_in_list_equal(sublist):
            return "four_of_a_kind"

    has_three_of_a_kind = False
    for sublist in get_sublists_with_size(cards, 3):
        if all_elements_in_list_equal(sublist):
            has_three_of_a_kind = True
            break
    two_of_a_kind_count = 0
    for sublist in get_sublists_with_size(cards, 2):
        if all_elements_in_list_equal(sublist):
            two_of_a_kind_count += 1
    
    if has_three_of_a_kind and two_of_a_kind_count == 3:
        return "full_house"

    if has_three_of_a_kind:
        return "three_of_a_kind"

    if two_of_a_kind_count == 2:
        return "two_pair"

    if two_of_a_kind_count == 1:
        return "one_pair"

    return "high_card"

class Hand:
    def __init__(self, cards_str, bid):
        self.cards = convert_cards_str(cards_str)
        self.cards_str = cards_str
        self.bid = bid
        self.hand_type_str = determine_hand_type(self.cards)
        self.hand_type = _hand_type_dict[self.hand_type_str]

    def __eq__(self, other):
        if self.hand_type != other.hand_type:
            return False
        return self.cards == other.cards

    def __lt__(self, other):
        if self.hand_type < other.hand_type:
            return True
        if self.hand_type > other.hand_type:
            return False

        for i in range(len(self.cards)):
            if self.cards[i] == other.cards[i]:
                continue
            return self.cards[i] < other.cards[i]

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]

    hands = []
    for line in lines:
        match = re.match("^([^\s]+)\s+(\d+)", line)
        hands.append(Hand(match.group(1), int(match.group(2))))
    hands.sort()
    result = 0
    for i in range(len(hands)):
        result += (i + 1)*hands[i].bid
    print(result)
