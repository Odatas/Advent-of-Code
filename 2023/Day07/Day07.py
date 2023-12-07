


class CharCounter:
    def __init__(self):
        # Initialize an empty dictionary to store the counts of each character
        self.char_counts = {}

    def add_letter(self, letter):
        # Increment the count of the given letter
        if letter in self.char_counts:
            self.char_counts[letter] += 1
        else:
            self.char_counts[letter] = 1

    def get_counts(self):
        # Return a list of tuples sorted by count in descending order
        return sorted(self.char_counts.items(), key=lambda item: item[1], reverse=True)

    def get_counts_joker_rule(self):
        joker = None
        sorted_char_count = sorted(self.char_counts.items(), key=lambda item: item[1], reverse=True)
        for i, tuple in enumerate(sorted_char_count):
            if tuple[0] == "J":
                joker = sorted_char_count.pop(i)
                break
        # Case only Joker we transfert to highest hand.
        if joker:
            if not sorted_char_count:
                sorted_char_count.append(("A",joker[1]))
                return sorted_char_count
        # If we have joker and still items
            if len(sorted_char_count) == 1:
                sorted_char_count[0] += (sorted_char_count[0][0], sorted_char_count[0][1] + joker[1])
                return sorted_char_count
            if sorted_char_count:
                addindex = 0
                count = sorted_char_count[0][1]

                for i in range(1,len(sorted_char_count)):
                    if card_values[sorted_char_count[i][0]] > card_values[sorted_char_count[addindex][0]] and sorted_char_count[i][1]==count:
                        addindex = i

                sorted_char_count[addindex] = (sorted_char_count[addindex][0],sorted_char_count[addindex][1]+joker[1])
        return sorted_char_count






def card_is_higher(card, check_card):
    for i in range(len(card[0])):
        if card_values[card[0][i]] > card_values[check_card[0][i]]:
            return True
        if card_values[card[0][i]] < card_values[check_card[0][i]]:
            return False

def sort_card_hands(list_of_cards):
    sorted_list = []
    # Sort every hand
    for hand in list_of_cards:
        # Add the first
        if len(sorted_list) == 0:
            sorted_list.append(hand)
        else:
            # For every card in the sorted list.
            for i, sorted_hand in enumerate(sorted_list):
                if card_is_higher(hand, sorted_hand):
                    sorted_list.insert(i,hand)
                    break
                if i == len(sorted_list)-1:
                    sorted_list.append(hand)
                    break
    return sorted_list


card_values = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}



with open("input.txt", mode = "r") as file:
    puzzel_input = file.readlines()
    puzzel_input = [x.strip().split(" ") for x in puzzel_input]

def do_it_all(Joker_rule = False):
    Five_of_a_kind = []
    Four_of_a_kind =[]
    Full_house = []
    Three_of_a_kind = []
    Two_pair = []
    One_pair = []
    High_card = []


    for entry in puzzel_input:
        hand = entry[0]
        counter = CharCounter()
        for card in hand:
            counter.add_letter(card)
        if Joker_rule:
            hand_counted = counter.get_counts_joker_rule()
        else:
            hand_counted = counter.get_counts()

        # a=5
        if len(hand_counted) == 1:
            Five_of_a_kind.append(entry)
            #print("Five of a kind")
        # a=4, b=1| a=3,b=2
        elif len(hand_counted) == 2:
            if hand_counted[0][1]==4:
                Four_of_a_kind.append(entry)
                #print("Four of a kind")
            else:
                Full_house.append(entry)
                #print("Full House")
        # a=3,b=1,c=1|a=2,b=2,c=1
        elif len(hand_counted) == 3:
            if hand_counted[0][1] ==3:
                Three_of_a_kind.append(entry)
                #print("three of a kind")
            else:
                Two_pair.append(entry)
                #print("Two pairs")
        elif len(hand_counted) == 4:
            One_pair.append(entry)
            #print("One Pair")
        else:
            High_card.append(entry)
            #print("High Card")



    Five_of_a_kind = sort_card_hands(Five_of_a_kind)
    Four_of_a_kind =sort_card_hands(Four_of_a_kind)
    Full_house = sort_card_hands(Full_house)
    Three_of_a_kind = sort_card_hands(Three_of_a_kind)
    Two_pair = sort_card_hands(Two_pair)
    One_pair = sort_card_hands(One_pair)
    High_card = sort_card_hands(High_card)

    masterlist = Five_of_a_kind + Four_of_a_kind + Full_house + Three_of_a_kind + Two_pair + One_pair + High_card

    multiplier = 0
    sum = 0
    for hand in reversed(masterlist):
        multiplier += 1
        sum += int(hand[1]) * multiplier
    return sum



print("Part 1: ", do_it_all())


card_values["J"] = 1

print("Part 2: ", do_it_all(Joker_rule=True))









