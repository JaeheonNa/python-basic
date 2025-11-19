class Character:
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERY_STRONG = 30

    def __init__(self):
        self.__hp = Character.NORMAL

    def levelUp(self):
        self.__hp = Character.STRONG

    def damage(self):
        self.__hp = Character.WEAK

    def __str__(self):
        return "HP: %d" % self.__hp