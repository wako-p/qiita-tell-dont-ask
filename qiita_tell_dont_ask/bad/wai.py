from qiita_tell_dont_ask.bad.interviewer import Interviewer


class Wai:
    """ ワイ
    """
    __ATTACK_POWER = 999

    @property
    def attack_power(self) -> int:
        return self.__ATTACK_POWER

    def attack(self, interviewer: Interviewer) -> None:

        current_hp = interviewer.get_hp()
        damaged_hp = current_hp - self.__ATTACK_POWER

        min_hp = interviewer.get_min_hp()
        if min_hp > damaged_hp:
            interviewer.set_hp(min_hp)
            return

        max_hp = interviewer.get_max_hp()
        if max_hp < damaged_hp:
            interviewer.set_hp(max_hp)
            return

        interviewer.set_hp(damaged_hp)
