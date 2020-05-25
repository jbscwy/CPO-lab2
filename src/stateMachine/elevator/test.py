import unittest

from src.stateMachine.elevator.FSM import StateMachine
from src.stateMachine.elevator.elevator import move_tran, start_tran, open_tran


class EventTest(unittest.TestCase):
    def test_stateMachine(self):
        m = StateMachine()
        m.add_state('MOVE', move_tran, 0)
        m.add_state('START', start_tran, 0)
        m.add_state('OPEN', open_tran, 0)
        m.add_state('STATIC', None, 1)
        m.add_state('ERROR', None, 1)

        m.set_start('START')
        self.assertEqual(m.set_start('START'),None)

        m.set_start('MOVE')
        self.assertEqual(m.set_start('START'),None)
        # m.run(['down', 'none'])  # 开始状态，进入move状态，然后想none，进入error状态
        # self.assertEqual(m.run(['down', 'none']), 'Input error!')
        #
        # m.run(['down', 'down', 'open', 'down'])  # 输出没到达最终状态
        # self.assertEqual(m.run(['down', 'down', 'open', 'down']), 'Input error!')
        # m.run(['down', 'down', 'open', 'none'])  # 进入static状态
        # self.assertEqual(m.run(['down', 'down', 'open', 'none']), 'Input error!')


if __name__ == '__main__':
  unittest.main()