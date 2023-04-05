# python3

class FlashCard:
    all_cards = []

    def __init__(self, front, back):
        self.front = front
        self.back = back
        self.all_cards.append(self)

    def __str__(self):
        return f"Front: {self.front}, Back: {self.back}"

    # def ask(self):
    #     print(self.front)
    #     answer = input()
    #     if answer == self.back:
    #         print("Correct!")
    #     else:
    #         print(f"Your answer was wrong. Correct answer is {self.back}")

    def check_unique(self):
        if self.all_cards == []:
            return True
        for card in self.all_cards[:-1]:
            if card.front == self.front or card.back == self.back:
                return False
        return True

    def list(self):
        for card in self.all_cards:
            print(f"Term: {card.front}")
            print(f"Definition: {card.back}")

    def remove(self):
        for card in self.all_cards:
            if card.front == self.front:
                self.all_cards.remove(card)
                print("The card has been removed.")
                break
        else:
            print(f"Can't remove \"{self.front}\": there is no such card.")


def add_card(card_number):
    new_card = FlashCard("", "")
    while True:
        print(f"The term for card #{card_number}:")
        new_card_front = input()
        new_card.front = new_card_front
        if not new_card.check_unique():
            print(f"The term \"{new_card.front}\" already exists. Try again:")
            new_card.front = ""
            continue
        break
    while True:
        print("Input the definition")
        new_card_back = input()
        new_card.back = new_card_back
        if not new_card.check_unique():
            print(
                f"The definition \"{new_card.back}\" already exists. Try again:")
            new_card.back = ""
            continue
        break


def check_answer(card):
    print(f"Print the definition of \"{card.front}\"):")
    answer = str(input())
    if answer == card.back:
        print("Correct!")
    elif answer in [card.back for card in FlashCard.all_cards]:
        print(
            f"Wrong. The right answer is \"{card.back}\", but your definition is correct for \"{[card.front for card in FlashCard.all_cards if card.back == answer][0]}\".")
    else:
        print(f"Wrong. The right answer is \"{card.back}\".")


def ask_cards(cards_list):
    for i in cards_list:
        check_answer(i)


def main():
    print("Input the number of cards:")
    count = input()
    for i in range(int(count)):
        add_card(i + 1)
    ask_cards(FlashCard.all_cards)


if __name__ == "__main__":
    main()
