from qiita_tell_dont_ask.good.interviewer import Interviewer


class Wai:
    """ ワイ
    """
    __ATTACK_POWER = 999

    @property
    def attack_power(self) -> int:
        return self.__ATTACK_POWER

    def attack(self, interviewer: Interviewer) -> None:
        interviewer.take_damage(self.__ATTACK_POWER)
