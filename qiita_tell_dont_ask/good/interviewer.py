class Interviewer:
    """ 面接官
    """
    __MIN_HP = 0
    __MAX_HP = 100

    @property
    def hp(self) -> int:
        return self.__hp

    def __init__(self) -> None:
        self.__hp = self.__MAX_HP

    def take_damage(self, attack_power: int) -> None:

        damaged_hp = self.__hp - attack_power

        if self.__MIN_HP > damaged_hp:
            self.__hp = self.__MIN_HP
            return

        if self.__MAX_HP < damaged_hp:
            self.__hp = self.__MAX_HP
            return

        self.__hp = damaged_hp
