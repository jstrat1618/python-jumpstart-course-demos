def main():
    #print header
    print_header()
    #run game loop
    game_loop()


def print_header():
    print("------------------------------------------")
    print("               WIZARD GAME APP ")
    print("------------------------------------------")

def game_loop():
    while True:
        cmd = input("Do you [a]ttack, [r]un away, [l]ook around or [e]xit? ")
        if cmd.strip().lower() == 'a':
            print('a')
        elif cmd == 'r':
            print('r')
        elif cmd == 'l':
            print("l")
        elif cmd == 'e':
            break
        else:
            print("Sorry, we didn't understand that command")




if __name__ == '__main__':
    main()