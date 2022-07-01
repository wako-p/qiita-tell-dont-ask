from unittest import TestCase

from qiita_tell_dont_ask.good.interviewer import Interviewer
from qiita_tell_dont_ask.good.manner_instructor import MannerInstructor


class TestNew(TestCase):

    def test_マナー講師は攻撃力が1で生成される(self) -> None:
        # when:
        manner_instructor = MannerInstructor()

        # then:
        self.assertEqual(1, manner_instructor.attack_power)


class TestAttack(TestCase):

    def test_マナー講師は面接官に攻撃することができ面接官のHPは99となる(self) -> None:
        # given:
        manner_instructor = MannerInstructor()
        interviewer = Interviewer()

        # when:
        manner_instructor.attack(interviewer)

        # then:
        self.assertEqual(99, interviewer.hp)
