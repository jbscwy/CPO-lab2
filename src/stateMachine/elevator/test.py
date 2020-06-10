import unittest

from src.stateMachine.elevator.FSM import StateMachine, param_check_test, trace


# Add state transition function for elevator control
def start_tran(input):
    if input is 'rise' or input is 'down':
        new_state = 'MOVE'
    elif input is 'open':
        new_state = 'OPEN'
    elif input is 'none':
        new_state = 'ERROR'  # The initial state "START" cannot be directly converted to the final state "Static" by "none" action
    else:
        new_state = "ERROR"
    return new_state

def move_tran(input):
    if input is 'rise' or input is 'down':
        new_state = 'MOVE'
    elif input is 'open':
        new_state = 'OPEN'
    elif input is 'none':  # The elevator can only enter the final state "STAIC" through the "none" action when the door is open
        new_state = 'ERROR'
    else:
        new_state = "ERROR"
    return new_state

def open_tran(input):
    if input is 'rise' or input is 'down':
        new_state = 'MOVE'
    elif input is 'open':
        new_state = 'OPEN'
    elif input is 'none':
        new_state = 'STATIC'
        print("final state")
    else:
        new_state = 'ERROR'
    return new_state


class EventTest(unittest.TestCase):

    def test_set_start(self):
        st = StateMachine()
        st.set_start("START")
        self.assertEqual(st.startState, 'START')

    def test_add(self):

        m = StateMachine()
        m = StateMachine()
        m.add_state('MOVE', move_tran, ['MOVE', 'OPEN', 'ERROR'], 0)
        m.add_state('START', start_tran, ['MOVE', 'OPEN', 'ERROR'], 0)
        m.add_state('OPEN', open_tran, ['MOVE', 'OPEN', 'STATIC'], 0)
        m.add_state('STATIC', None, None, 1)
        m.add_state('ERROR', None, None, 1)
        self.assertEqual(m.handlers, {'MOVE':move_tran,'START':start_tran,'OPEN':open_tran,'STATIC': None,'ERROR': None})


    def test_run(self):
        m = StateMachine()
        m.add_state('MOVE', move_tran, ['MOVE', 'OPEN', 'ERROR'], 0)
        m.add_state('START', start_tran, ['MOVE', 'OPEN', 'ERROR'], 0)
        m.add_state('OPEN', open_tran, ['MOVE', 'OPEN', 'STATIC'], 0)
        m.add_state('STATIC', None, None, 1)
        m.add_state('ERROR', None, None, 1)

        m.add_trans_status('MOVE', 'rise or down/0', )
        m.add_trans_status('OPEN', 'open/0')
        m.add_trans_status('ERROR', 'none/0')
        m.add_trans_status('STATIC', 'none/1')

        m.set_start('START')
        m.run(['down', 'none'])
        self.assertEqual(m.runResult,"arrived ERROR" )
        m.run(['down', 'down', 'open', 'down'])  # dont arrive at final state
        self.assertEqual(m.runResult, "not arrive end state")
        m.run(['down', 'down', 'open', 'none'])  # arrive at the final state "STATIC"
        self.assertEqual(m.runResult, "arrived STATIC")


    def test_param(self):
        #Type test the input parameters, execute the function if the type is correct, otherwise output 'false property'
        #the corret input parameter type was found in the previous test
        m=StateMachine()
        self.assertEqual(m.add_state('STATIC', None, None,'1'),'false property')
        self.assertEqual(m.set_start(0), 'false property')
        self.assertEqual(m.run('down'), 'false property')


if __name__ == '__main__':
  unittest.main()