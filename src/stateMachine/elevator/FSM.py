from typing import TypeVar

import graphviz
from typing import TypeVar


# V = TypeVar(str, list, NontType)

# Parameter check
RESULT=[]
def ParamCheck(*ty2):
    def common(fun):
        def deal(*fun_x):
            ty = map(to_check_fun, ty2)
            if ty:
                x_list = [a for a in fun_x]
                x_list_it = iter(x_list)
                RESULT.clear()
                for t_check in ty:
                    r = t_check(x_list_it.__next__())
                    if r is False:
                        RESULT.append('false property')
                        return 'false property'
                RESULT.append('true property')
            return fun(*fun_x)
        return deal
    return common


def to_check_fun(t):

    return lambda x:isinstance(x,t)

#Used for parameter type detection unit test
@ParamCheck(int,int,str)
def param_check_test(a,b,c):
    return RESULT


class StateMachine:
    def __init__(self):
        self.handlers = {}  # State transfer function dictionary
        self.startState = None  # initial state
        self.endStates = []  # Final state list
        self.runResult = 0  # The result of function run
        self.state = []  # To collect all state
        self.trans = {}  # Transfer process information
        self.trans_to = {} # "Key" state can be transferred to "value" state

    @ParamCheck(object,str,object,(list,type(None)),int)
    def add_state(self, name, handler, trans_to, end_state=0):
        '''
        Function introduction:Add state
        :param name:Name of the added state
        :param handler:State transition function of the state
        :param trans_to:The next state that this state allows to move to
        :param end_state:Is the state final state or not.
        :return:
        '''
        self.handlers[name] = handler
        self.state.append(name)
        self.trans_to[name] = trans_to
        if end_state:
            self.endStates.append(name)

    def add_trans_status(self, state, move):
        '''
        Function introduction:Add state transition information
        :param state:State name.
        :param move:Actions performed in this state/
        :return:
        '''
        self.trans[state] = move

    @ParamCheck(object,str)
    def set_start(self, name):
        '''
        Function introduction:Set start state.
        :param name:State name.
        :return:
        '''
        self.startState = name


    @ParamCheck(object,list)
    def run(self, cargo):
        '''
        Function introduction:Running FSM.
        :param cargo:Input action list.
        :return:
        '''
        try:
            handler = self.handlers[self.startState]
        except:
            self.runResult ="must call .set_start() before .run()"
            raise InitializationError("must call .set_start() before .run()")
        if not self.endStates:
            self.runResult ="at least one state must be an end_state"
            raise InitializationError("at least one state must be an end_state")

        # Start running from "Start state"
        flag = 0
        for input_data in cargo:
            new_state = handler(input_data)  # Transform to a new state after a state transition function
            if new_state in self.endStates:  # If it transitions to the end state, print the state and end the loop
                self.runResult = "arrived "+new_state
                print(self.runResult)
                flag = 1
                break
            else:  # Otherwise, switch the transfer function to the transfer function in the new state
                handler = self.handlers[new_state]
        if flag is 0:
            self.runResult = "not arrive end state"
            print(self.runResult)

    @ParamCheck(object)
    def visualize(self):
        '''
        Function introduction:Create dot code for graphviz.
        :return:
        '''
        res = []
        res.append("digraph G {")
        res.append("  rankdir=LR;")
        for v in self.state:
            res.append("  {}[];".format(v))


        for v in self.state:
            if self.handlers[v] is not None:
                for value in self.trans_to[v]:
                    res.append('  {} -> {}[label="{}"];'.format(v, value, self.trans[value]))


        res.append("}")

        return "\n".join(res)

def trace(f):
    def traced(*args, **kwargs):
        print("{}(*{}, **{}) START".format(f.__name__, args, kwargs))
        try:
            return f(*args, **kwargs)
        finally:
            print("{} FINISH".format(f.__name__))
    return traced



class InitializationError(Exception):
    def __init__(self,arg):
        self.arg = arg

    def __str__(self):
        print(self.arg)



if __name__ =="__main__":

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


    m = StateMachine()



    m.add_state('MOVE', move_tran,['MOVE','OPEN','ERROR'],0)
    m.add_state('START', start_tran,['MOVE','OPEN','ERROR'],0)
    m.add_state('OPEN', open_tran,['MOVE','OPEN','STATIC'],0)
    m.add_state('STATIC', None,None, 1)
    m.add_state('ERROR', None,None, 1)

    m.add_trans_status('MOVE','rise or down/0',)
    m.add_trans_status('OPEN', 'open/0' )
    m.add_trans_status('ERROR', 'none/0' )
    m.add_trans_status('STATIC', 'none/1' )

    m.set_start('START')

    m.run(['down','none'])#use "down" action to transfer state from "start" to "move",then use none action to transfer state from "action" to "static"
    # ,because the rule says we cant tranfer state from "action" to "static",so transfer to "error" state
    m.run(['down','down','open','down'])#dont arrive at final state
    m.run(['down', 'down', 'open', 'none'])#arrive at the final state "STATIC"

    dot = m.visualize()

    f = open('fsm.dot','w')

    f.write(dot)

    f.close()

    with open("fsm.dot") as f:

        dot_graph = f.read()

    dot = graphviz.Source(dot_graph)

    dot.view()