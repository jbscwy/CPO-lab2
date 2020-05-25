

#input is of type list
from src.stateMachine.elevator.FSM import StateMachine


def start_tran(input):
    if input is 'rise' or input is 'down':
        new_state = 'MOVE'
    elif input is 'open':
        new_state = 'OPEN'
    elif input is 'none':
        new_state = 'ERROR' #初试状态不可以直接通过none动作转换为最终的静止状态
    else:
        new_state = "ERROR"
    return new_state


def move_tran(input):
    if input is 'rise' or input is 'down':
        new_state = 'MOVE'
    elif input is 'open':
        new_state = 'OPEN'
    elif input is 'none':  #电梯在开门状态时才可以通过none动作进入精致状态
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



if __name__== "__main__":
    m = StateMachine()
    m.add_state('MOVE', move_tran,0)
    m.add_state('START', start_tran,0)
    m.add_state('OPEN', open_tran,0)
    m.add_state('STATIC', None, 1)
    m.add_state('ERROR', None, 1)

    m.set_start('START')

    m.run(['down','none']) #开始状态，进入move状态，然后想none，进入error状态
    m.run(['down','down','open','down'])#输出没到达最终状态
    m.run(['down', 'down', 'open', 'none'])#进入static状态

#规则
# 四种动作：rise,down,open,none。none动作表示进入静止状态，只有在开门状态后才能进none，因为运动状态必须先进入开门状态才能进入静止停业状态
# 五种状态：开始状态，移动状态，开门状态，静止状态（最终状态），错误状态（最终状态）
# 具体个状态下的转移，看转移函数
# 到达最终状态会跳出输出结果