
from unittest import TestCase

from qiita_tell_dont_ask.bad.interviewer import Interviewer


class TestNew(TestCase):

    def test_面接官はHPが100で生成される(self) -> None:
        # when:
        interviewer = Interviewer()

        # then:
        self.assertEqual(100, interviewer.get_hp())


class TestGetMinHp(TestCase):

    def test_最小HPを取得できる(self) -> None:
        # given:
        interviewer = Interviewer()

        # when:
        min_hp = interviewer.get_min_hp()

        # then:
        self.assertEqual(0, min_hp)


class TestGetMaxHp(TestCase):

    def test_最大HPを取得できる(self) -> None:
        # given:
        interviewer = Interviewer()

        # when:
        max_hp = interviewer.get_max_hp()

        # then:
        self.assertEqual(100, max_hp)


class TestGetHp(TestCase):

    def test_HPを取得できる(self) -> None:
        # given:
        interviewer = Interviewer()

        # when:
        hp = interviewer.get_hp()

        # then:
        self.assertEqual(100, hp)


class TestSetHp(TestCase):

    def test_HPを設定できる(self) -> None:
        # given:
        interviewer = Interviewer()

        # when:
        interviewer.set_hp(50)

        # then:
        self.assertEqual(50, interviewer.get_hp())
