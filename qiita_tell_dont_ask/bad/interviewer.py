class Interviewer:
    """ 面接官
    """
    __MIN_HP: int = 0
    __MAX_HP: int = 100

    def __init__(self) -> None:
        self.__hp = self.__MAX_HP

    def get_min_hp(self) -> int:
        return self.__MIN_HP

    def get_max_hp(self) -> int:
        return self.__MAX_HP

    def get_hp(self) -> int:
        return self.__hp

    def set_hp(self, hp: int) -> None:
        self.__hp = hp
