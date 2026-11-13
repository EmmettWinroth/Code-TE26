bag = []
mem = ""
spot = 0
action = ""
while True:
    print("\033[0m-------------------------------------------")
    action = input(f"\033[93m[C] Check inventory    \033[0mSize ({len(bag)}/10)\n"
    "\033[92m[A] Add to Inventory\n"
    "\033[94m[S] Search Inventory\n"
    "\033[91m[R] Remove\n"
    "\033[90m[Q] Quit\n\033[0m").lower()
    if action == "c":
        print("\033[93m",bag,"\033[0m")
    elif action == "r":
        mem = input("\033[91mWhat you want to remove: ")
        if mem.lower() in bag:
            spot = bag.index(mem.lower())
            bag.pop(spot)
            print(f"{mem} Removed.\033[0m")
    elif action == "a" and len(bag) < 10:
        mem = input("\033[92mWhat would you like to add: \033[0m")
        bag.append(mem.lower())
        mem = ""
    elif action == "s":
        mem = input("\033[94mWhat are you looking for: ")
        if mem.lower() in bag:
            spot = bag.index(mem.lower())
            print(f"{mem} found at index: {spot}")
        else:
            print(f"Could not find: {mem}\033[0m")
    elif action == "q":
        print("\033[90mQuitting...\033[0m")
        break
    else:        
        print("\033[91mNot valid action.")
    if len(bag) > 10:
        print("\033[96mBag is full!")        