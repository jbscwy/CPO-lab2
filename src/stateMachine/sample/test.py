import unittest

from src.stateMachine.sample import start_transitions
from src.stateMachine.sample.start_transitions import python_state_transitions, is_state_transitions, \
    not_state_transitions
from src.stateMachine.sample.stateMachine import StateMachine


class DiscreteEventTest(unittest.TestCase):
    def test_stateMachine(self):
        m = StateMachine()
        m.add_state("Start", start_transitions)  # 添加初始状态
        m.add_state("Python_state", python_state_transitions)
        m.add_state("is_state", is_state_transitions)
        m.add_state("not_state", not_state_transitions)
        m.add_state("neg_state", None, end_state=1)  # 添加最终状态
        m.add_state("pos_state", None, end_state=1)
        m.add_state("error_state", None, end_state=1)

        m.set_start("Start")  # 设置开始状态
        # m.run("Python is great")
        # m.run("Python is not fun")
        # m.run("Perl is ugly")
        # m.run("Pythoniseasy")
        self.assertEqual(m.set_start("Start"),None)
        # m.run("Python is great")



if __name__ == '__main__':
  unittest.main()
