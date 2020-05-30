class StateMachine:
    def __init__(self):
        self.handlers = {}  # State transition function dictionary
        self.startState = None  # The initial state
        self.endStates = []  # Final set of states

    # The parameter name is the state name,handler is the state transfer function, and end_state indicates whether it is the final state
    def add_state(self, name, handler, end_state=0):
        name = name # Convert to uppercase
        self.handlers[name] = handler
        if end_state:
          self.endStates.append(name)


    def set_start(self, name):
        self.startState = name


    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("must call .set_start() before .run()")
        if not self.endStates:
            raise InitializationError("at least one state must be an end_state")

        # Start processing from the Start state
        flag = 0
        for input_data in cargo:
            new_state = handler(input_data)  # It goes through the state transfer function to the new state
            if new_state in self.endStates:  # If you jump to the termination state, print the state and end the loop
                print("{} second later,You can {} ".format(input_data,new_state))
                flag = 1
                return new_state
                break
            else:  # Otherwise, switch the transition function to the transition function in the new state
                handler = self.handlers[new_state]
        if flag is 0:
            print("not arrive end state")


class InitializationError(Exception):
    def __init__(self,arg):
        self.arg = arg

    def __str__(self):
        print(self.arg)