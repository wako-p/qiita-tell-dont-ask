from qiita_tell_dont_ask.good.interviewer import Interviewer


class MannerInstructor:
    """ マナー講師
    """
    __ATTACK_POWER = 1

    @property
    def attack_power(self) -> int:
        return self.__ATTACK_POWER

    def attack(self, interviewer: Interviewer) -> None:
        interviewer.take_damage(self.__ATTACK_POWER)
