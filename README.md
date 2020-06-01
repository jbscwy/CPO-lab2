# CPO-lab2

## list of group members:

192050214 Mu Yuankai 
192050208 Jia Yuebin

## variant description:

eDSL for finite state machine (Mealy).

## synopsis:

Display as a state graph (GraphViz dots) or table (ASCII).

Provide a complex example, such as the controller of an elevator, a traffic light at an intersection, and so on.After modification, delete the example of the traffic light at the intersection, the main example is the controller of the elevator



## To work together:

Complete the FSM class together
## Personal work：
Mu Yuankai finished FSM.py  code module writing.
Jia Yuebin completed the  test modules and collected relevant data.



## Code Introduction:

#### src/stateMachine/elevator/FSM.py:

class StateMachineis a class of finite state machine . 

member variables:

```python
self.handlers = {}  # State transfer function dictionary
self.startState = None  # initial state
self.endStates = []  # Final state list
self.runResult = 0  # The result of function run
self.state = []  # To collect all state
self.trans = {}  # Transfer process information
self.trans_to = {} # "Key" state can be transferred to "value" state
```

member methods:

```python
def add_state(self, name, handler, trans_to, end_state=0):
    '''
    Function introduction:Add state
    :param name:Name of the added state
    :param handler:State transition function of the state
    :param trans_to:The next state that this state allows to move to
    :param end_state:Is the state final state or not.
    :return:
    '''
```

```python
def add_trans_status(self, state, move):
    '''
    Function introduction:Add state transition information
    :param state:State name.
    :param move:Actions performed in this state/
    :return:
    '''
```

```python
def set_start(self, name):
    '''
    Function introduction:Set start state.
    :param name:State name.
    :return:
    '''
```

```python
def run(self, cargo):
    '''
    Function introduction:Running FSM.
    :param cargo:Input action list.
    :return:
    '''
```

```python
def visualize(self):
    '''
    Function introduction:Create dot code for graphviz.
    :return:
    '''
```



#### The elevator case

The state transition generation diagram is under src/stateMachine/elevator.

The initial state is "START", and the final state is "STATIC" or "ERROR".You can draw the transition rules from the state transition diagram.



## conclusion:

According to the elevator example, different actions are performed by entering different values through the state machine.Understand the basic purpose of a finite state machine: to "run" in response to a series of events

