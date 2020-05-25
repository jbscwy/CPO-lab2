class StateMachine:
    def __init__(self):
        self.handlers = {}  # 状态转移函数字典
        self.startState = None  # 初始状态
        self.endStates = []  # 最终状态集合

    # def arg_zero(f):
    #     def arg_zerod(self, *args, **kwargs):
    #         # print("{}(*{}, **{}) START".format(f.__name__, args, kwargs))
    #         if len(args) == 0:
    #             return f(self, *args, **kwargs)
    #         else:
    #             print('Input error!')
    #             return 'Input error!'
    #     return arg_zerod

    # @arg_zero
    # 参数name为状态名,handler为状态转移函数,end_state表明是否为最终状态
    def add_state(self, name, handler, end_state=0):
        name = name # 转换为大写
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    # @arg_zero
    def set_start(self, name):
        self.startState = name


    # def run(self, cargo):
    #     try:
    #         handler = self.handlers[self.startState]
    #     except:
    #         raise InitializationError("must call .set_start() before .run()")
    #     if not self.endStates:
    #         raise InitializationError("at least one state must be an end_state")
    #
    #     # 从Start状态开始进行处理
    #     while True:
    #         (newState, cargo) = handler(cargo)  # 经过状态转移函数变换到新状态
    #         if newState.upper() in self.endStates:  # 如果跳到终止状态,则打印状态并结束循环
    #             print("reached ", newState)
    #             break
    #         else:  # 否则将转移函数切换为新状态下的转移函数
    #             handler = self.handlers[newState.upper()]

    # 修改了一下，输入cargo为list
    # @arg_zero
    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("must call .set_start() before .run()")
        if not self.endStates:
            raise InitializationError("at least one state must be an end_state")

        # 从Start状态开始进行处理
        flag = 0
        for input_data in cargo:
            new_state = handler(input_data)  # 经过状态转移函数变换到新状态
            if new_state in self.endStates:  # 如果跳到终止状态,则打印状态并结束循环
                print("{} second later,You can {} ".format(input_data,new_state))
                flag = 1
                return new_state
                break
            else:  # 否则将转移函数切换为新状态下的转移函数
                handler = self.handlers[new_state]
        if flag is 0:
            print("not arrive end state")

    def visualize(self):

        res = []
        res.append("digraph G {")
        res.append(" rankdir=LR;")
        for v in self.inputs:
            res.append(" {}[shape=rarrow];".format(v))
        for v in self.outputs:
            res.append(" {}[shape=rarrow];".format(v))
        for i, n in enumerate(self.nodes):
            res.append(' n_{}[label="{}"];'.format(i, n.name))
        for i, n in enumerate(self.nodes):
            for v in n.inputs:
                if v in self.inputs:
                    res.append(' {} -> n_{};'.format(v, i))
        for j, n2 in enumerate(self.nodes):
            if i == j: continue
        for v in n.inputs:
            if v in n2.outputs:
                res.append(' n_{} -> n_{}[label="{}"];'.format(j, i, v))
        for v in n.outputs:
            if v in self.outputs:
                res.append(' n_{} -> {};'.format(i, v))
        res.append("}")
        return "\n".join(res)

class InitializationError(Exception):
    def __init__(self,arg):
        self.arg = arg

    def __str__(self):
        print(self.arg)