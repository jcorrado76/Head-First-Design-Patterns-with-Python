if __name__ == "__main__":
    from character_classes import King, Queen, Knight, Troll, SwordBehavior

    for character in [King(), Queen(), Knight(), Troll()]:
        character.display()
        character.fight()
        print("\n")

    victorious_troll = Troll()
    victorious_troll.display()
    victorious_troll.fight()
    print("I have killed the Queen's Knight! I will take this sword as my reward!")
    victorious_troll.setWeapon(SwordBehavior())
    victorious_troll.fight()
