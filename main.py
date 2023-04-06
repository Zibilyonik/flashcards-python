# Write your code here
# python3
import random
import os
from contextlib import redirect_stdout


class FlashCard:
    all_cards = []

    def __init__(self, front, back, wrong=0):
        self.front = front
        self.back = back
        self.all_cards.append(self)
        self.wrong = wrong

    def __str__(self):
        return f"Front: {self.front}, Back: {self.back}"

    def check_unique(self):
        if not self.all_cards:
            return True
        for card in self.all_cards[:-1]:
            if card.front == self.front or card.back == self.back:
                return False
        return True

    def remove_card(self):
        self.all_cards.remove(self)


def printer(text, solo=False):
    with open('temp.txt', 'a') as f:
        if not solo:
            print(text)
        with redirect_stdout(f):
            print(text)


def add_card(card_number):
    new_card = FlashCard("", "")
    printer(f"The term for card #{card_number}:")
    while True:
        new_card_front = input()
        printer(new_card_front, True)
        new_card.front = new_card_front
        if not new_card.check_unique():
            printer(f"The term \"{new_card.front}\" already exists. Try again:")
            new_card.front = ""
            continue
        break
    printer(f"The definition for card #{card_number}:")
    while True:
        new_card_back = input()
        printer(new_card_back, True)
        new_card.back = new_card_back
        if not new_card.check_unique():
            printer(f"The definition \"{new_card.back}\" already exists. Try again:")
            new_card.back = ""
            continue
        break
    printer(f"The pair (\"{new_card_front}\":\"{new_card_back}\") has been added.")


def remove_card():
    printer("Which card?")
    card_to_remove = input()
    printer(card_to_remove, True)
    for card in FlashCard.all_cards:
        if card.front == card_to_remove:
            card.remove_card()
            printer("The card has been removed.")
            return
    printer(f"Can't remove \"{card_to_remove}\": there is no such card.")


def check_answer(card):
    printer(f"Print the definition of \"{card.front}\"):")
    answer = str(input())
    printer(answer, True)
    if answer == card.back:
        printer("Correct!")
    elif answer in [card.back for card in FlashCard.all_cards]:
        card.wrong += 1
        printer(
            f"Wrong. The right answer is \"{card.back}\", but your definition is correct for \"{[card.front for card in FlashCard.all_cards if card.back == answer][0]}\".")
    else:
        card.wrong += 1
        printer(f"Wrong. The right answer is \"{card.back}\".")


def ask_cards():
    random_card = random.choice(FlashCard.all_cards)
    check_answer(random_card)


def import_cards():
    printer("File name:")
    file_name = input()
    printer(file_name, True)
    counter = 0
    try:
        with open(file_name, "r") as file:
            for line in file:
                card_list = line.split("|")
                for card in card_list[:-1]:
                    front, back, wrongs = card.split(":")
                    counter += 1
                    for card in FlashCard.all_cards:
                        if card.front == front:
                            card.remove_card()
                    FlashCard(front, back, wrongs)
        printer(f"{counter} cards have been loaded.")
    except FileNotFoundError:
        printer("File not found.")


def export_cards():
    printer("File name:")
    file_name = input()
    printer(file_name, True)
    with open(file_name, "w") as file:
        for card in FlashCard.all_cards:
            file.write(f"{card.front}:{card.back}:{card.wrong}|")
    printer(f"{len(FlashCard.all_cards)} cards have been saved.")


def log(records):
    printer("File name:")
    file_name = input()
    printer(file_name, True)
    with open(file_name, "w") as file:
        for record in records:
            print(record, file=file)
    printer("The log has been saved.")


def hardest_card():
    hardest_cards = [card for card in FlashCard.all_cards if
                     card.wrong == max(card.wrong for card in FlashCard.all_cards)]

    if not hardest_cards or hardest_cards[-1].wrong == 0:
        printer("There are no cards with errors.")
        return
    if len(hardest_cards) == 1:
        printer(
            f"The hardest card is \"{hardest_cards[0].front}\". You have {hardest_cards[0].wrong} errors answering it.")
    else:
        hardest_cards_str = ", ".join([f"\"{card.front}\"" for card in hardest_cards])
        printer(f"The hardest cards are {hardest_cards_str}. You have {hardest_cards[0].wrong} errors answering it.")


def print_menu():
    printer("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):")
    answer = input()
    printer(answer, True)
    match answer:
        case "add":
            add_card(len(FlashCard.all_cards) + 1)
        case "remove":
            remove_card()
        case "import":
            import_cards()
        case "export":
            export_cards()
        case "list":
            for card in FlashCard.all_cards:
                printer(card)
        case "ask":
            printer("How many times to ask?")
            count = input()
            printer(count, True)
            for _ in range(int(count)):
                ask_cards()
        case "exit":
            printer("Bye bye!")
            os.remove("temp.txt")
            return False
        case "log":
            with open("temp.txt", "r") as file:
                log(file.readlines())

        case "hardest card":
            hardest_card()
        case "reset stats":
            for card in FlashCard.all_cards:
                card.wrong = 0
            printer("Card statistics have been reset.")

    return True


def main():
    while True:
        if not print_menu():
            break


if __name__ == "__main__":
    main()
