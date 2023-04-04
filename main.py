#python3

class FlashCard:
    all_cards = []
    def __init__(self, front, back):
        self.front = front
        self.back = back
        self.all_cards.append(self)

    def __str__(self):
        return f"Front: {self.front}, Back: {self.back}"


def add_card(cards_list, card_number):
    print(f"The term for card #{card_number}:")
    front = str(input())
    print(f"The definition for card #{card_number}:")
    back = str(input())
    cards_list[front] = back

def ask_cards(cards_list):
    for i in cards_list:
        print(f"print the definition of \"{i}\"):")
        answer = str(input())
        if answer == cards_list[i]:
            print("Correct!")
        else:
            print(f"Wrong. The right answer is \"{cards_list[i]}\".")
            
def main():
    cards_list = {}
    print("Input the number of cards:")
    count = input()
    for i in range(int(count)):
        add_card(cards_list, i + 1)
    ask_cards(cards_list)

if __name__ == "__main__":
    main()
