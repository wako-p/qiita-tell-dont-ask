
from unittest import TestCase
from parameterized import parameterized

from qiita_tell_dont_ask.good.interviewer import Interviewer


class TestNew(TestCase):

    def test_面接官はHPが100で生成される(self) -> None:
        # when:
        interviewer = Interviewer()

        # then:
        self.assertEqual(100, interviewer.hp)


class TestTakeDamage(TestCase):

    @parameterized.expand([
        [0, 100],
        [1, 99],
        [50, 50],
        [99, 1],
        [100, 0],
    ])
    def test_引数に指定した攻撃力の値だけHPが減少する(self, attack_power: int, expected: int) -> None:
        # given:
        interviewer = Interviewer()

        # when:
        interviewer.take_damage(attack_power)

        # then:
        self.assertEqual(expected, interviewer.hp)

    @parameterized.expand([
        [101],
        [102],
        [999],
    ])
    def test_引数に指定した攻撃力がHPを超える場合は0で制限される(self, attack_power: int) -> None:
        # given:
        interviewer = Interviewer()

        # when:
        interviewer.take_damage(attack_power)

        # then:
        self.assertEqual(0, interviewer.hp)
