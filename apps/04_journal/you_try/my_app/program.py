import journal

def main():
    print_header()
    run_event_loop()


def list_entries(data):
    for indx, entry in enumerate(data):
        print("Entry {0} is '{1}'.".format(indx + 1, entry))

def add_entry(data):
    entry = input("Type your entry, and press <Enter> to exit. ")
    journal.add_entry(entry, data)


def run_event_loop():
    print("What do you want to do with your journal?")

    journal_name = "Default"
    journal_data = journal.load_journal(journal_name)
    cmd = "x"
    while cmd.lower() != "e":
        user_cmd = input("[L]ist entries, [A]dd entries, [E]xit? ")
        cmd = user_cmd.lower().strip()

        if cmd == "l":
            list_entries(journal_data)
        elif cmd == "a":
            add_entry(journal_data)

        elif cmd == "e":
            print("Goodbye!")
            journal.save_journal(journal_name, journal_data)
        else:
            print("Sorry, we didn't understand the input '{}.'".format(user_cmd))


def print_header():
    print("----------------------------------")
    print("         JOURNAL APP              ")
    print("----------------------------------")


if __name__ == '__main__':
    main()