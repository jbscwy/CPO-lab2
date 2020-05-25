from src.stateMachine.trafficSignal.FSM import StateMachine


def start_tran(input):
    if input is 'red':
        new_state = 'WAIT'
    elif input is 'green':
        new_state = 'RUN'
    elif input is 'yellow':
        new_state = 'RUN　OR WAIT'
    else:
        new_state = "error"
    return new_state

def red_tran(time):
    Time=time%70
    if  Time <=30:
        new_state = 'WAIT'
    elif 30<Time<=60:
        new_state = 'RUN'
    elif 60<Time<=70:
        new_state = 'RUN　OR WAIT'
    else:
        new_state = "error"
    return new_state


def green_tran(time):
    Time=time%70
    if  Time <=30:
        new_state = 'RUN'
    elif 30<Time<=40:
        new_state = 'RUN　OR WAIT'
    elif 40<Time<=70:
        new_state = 'WAIT'
    else:
        new_state = "error"
    return new_state

def yellow_tran(time):
    Time=time%70
    if  Time <=10:
        new_state = 'RUN　OR WAIT'
    elif 10<Time<=40:
        new_state = 'WAIT'
    elif 40<Time<=70:
        new_state = 'RUN'
    else:
        new_state = "error"
    return new_state




if __name__== "__main__":
    m = StateMachine()
    m.add_state('red', red_tran,0)
    m.add_state('yellow', yellow_tran,0)
    m.add_state('green', green_tran,0)
    m.add_state('RUN', None, 1)
    m.add_state('WAIT', None, 1)
    m.add_state('RUN　OR WAIT', None, 1)
    m.add_state('error', None, 1)

# The first state is red,40 seconds later,the light is green,you can run
    m.set_start('red')
    m.run([40])

# The first state is green,40 seconds later,the light is yellow,you can run or wait
    m.set_start('green')
    m.run([40])

# The first state is yellow,40 seconds later,the light is red,you can wait
    m.set_start('yellow')
    m.run([40])




