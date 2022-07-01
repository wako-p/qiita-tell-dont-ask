from unittest import TestCase

from qiita_tell_dont_ask.bad.interviewer import Interviewer
from qiita_tell_dont_ask.bad.wai import Wai


class TestNew(TestCase):

    def test_ワイは攻撃力が999で生成される(self) -> None:
        # when:
        wai = Wai()

        # then:
        self.assertEqual(999, wai.attack_power)


class TestAttack(TestCase):

    def test_ワイは面接官に攻撃することができ面接官のHPは0となる(self) -> None:
        # given:
        wai = Wai()
        interviewer = Interviewer()

        # when:
        wai.attack(interviewer)

        # then:
        self.assertEqual(0, interviewer.get_hp())
