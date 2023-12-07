

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


def card_is_higher(card, check_card):
    for i in range(len(card[0])):
        if card_values[card[0][i]] > card_values[check_card[0][i]]:
            return True
        if card_values[card[0][i]] < card_values[check_card[0][i]]:
            return False


def calculate_all_permutation(hand_info, index=0, current_hand=None, all_hands=None):
    if hand_info[0] == "JJJJJ":
        return [["AAAAA", hand_info[1]]]
    if hand_info[0].count("J") == 4:
        for i in hand_info[0]:
            if i != "J":
                return_string = ""
                for j in range(5):
                    return_string += i
                return [[return_string, hand_info[1]]]
    # Extract the hand string and the number from the input list
    hand = hand_info[0]
    number = hand_info[1]

    # Define the set of all possible cards
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    # Initialize the current hand and all hands list
    if current_hand is None:
        current_hand = list(hand)
    if all_hands is None:
        all_hands = []

    # Base case: No more Js to replace
    if index >= len(current_hand):
        all_hands.append([''.join(current_hand), number])
        return

    # Recursive case: Replace the J and move to the next card
    if current_hand[index] == 'J':
        for card in cards:
            new_hand = current_hand.copy()
            new_hand[index] = card
            calculate_all_permutation([new_hand, number], index + 1, new_hand, all_hands)
    else:
        calculate_all_permutation([current_hand, number], index + 1, current_hand, all_hands)

    return all_hands


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
                    sorted_list.insert(i, hand)
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


with open("example.txt", mode="r") as file:
    puzzel_input = file.readlines()
    puzzel_input = [x.strip().split(" ") for x in puzzel_input]


def do_it_all(puzzel, Joker_rule=False):
    if len(puzzel) == 1:
        print(puzzel[0])
        return 0, puzzel[0]
    Five_of_a_kind = []
    Four_of_a_kind = []
    Full_house = []
    Three_of_a_kind = []
    Two_pair = []
    One_pair = []
    High_card = []

    for entry in puzzel:
        if Joker_rule:
            print("Start with", entry)
        line = entry

        if Joker_rule and "J" in line[0]:
            highest_permutation = calculate_all_permutation(entry)
            _, line = do_it_all(highest_permutation)
        hand = line[0]
        counter = CharCounter()
        for card in hand:
            counter.add_letter(card)
        hand_counted = counter.get_counts()
        if Joker_rule:
            print("Got now", entry)
        # a=5
        if len(hand_counted) == 1:
            Five_of_a_kind.append(line)
            # print("Five of a kind")
        # a=4, b=1| a=3,b=2
        elif len(hand_counted) == 2:
            if hand_counted[0][1] == 4:
                Four_of_a_kind.append(line)
                # print("Four of a kind")
            else:
                Full_house.append(line)
                # print("Full House")
        # a=3,b=1,c=1|a=2,b=2,c=1
        elif len(hand_counted) == 3:
            if hand_counted[0][1] == 3:
                Three_of_a_kind.append(line)
                # print("three of a kind")
            else:
                Two_pair.append(line)
                # print("Two pairs")
        elif len(hand_counted) == 4:
            One_pair.append(line)
            # print("One Pair")
        else:
            High_card.append(line)
            # print("High Card")

    Five_of_a_kind = sort_card_hands(Five_of_a_kind)
    Four_of_a_kind = sort_card_hands(Four_of_a_kind)
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
        try:
            sum += int(hand[1]) * multiplier
        except ValueError:
            print(hand)
            exit
    return sum, masterlist[0]


print("Part 1: ", do_it_all(puzzel_input))


card_values["J"] = 1

print("Part 2: ", do_it_all(puzzel_input, Joker_rule=True))
