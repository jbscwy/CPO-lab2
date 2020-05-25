import unittest

from src.stateMachine.trafficSignal.FSM import StateMachine
from src.stateMachine.trafficSignal.trafficSignal import red_tran, yellow_tran, green_tran


class EventTest(unittest.TestCase):
    def test_stateMachine(self):
        m = StateMachine()
        m.add_state('red', red_tran, 0)
        m.add_state('yellow', yellow_tran, 0)
        m.add_state('green', green_tran, 0)
        m.add_state('RUN', None, 1)
        m.add_state('WAIT', None, 1)
        m.add_state('RUN　OR WAIT', None, 1)
        m.add_state('error', None, 1)

        # The first state is red,40 seconds later,the light is green,you can run
        m.set_start('red')
        # m.run([40])
        self.assertEqual(m.run([40]),'RUN')

        # The first state is green,40 seconds later,the light is yellow,you can run or wait
        m.set_start('green')
        # m.run([40])
        self.assertEqual(m.run([40]), 'RUN　OR WAIT')
        # The first state is yellow,40 seconds later,the light is red,you can wait
        m.set_start('yellow')
        # m.run([40])
        self.assertEqual(m.run([40]), 'WAIT')


if __name__ == '__main__':
  unittest.main()