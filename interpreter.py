class Interpreter:
        def __init__(self):
                self.stack = []
                self.environment = {}

        def LOAD_VALUE(self, number):
                self.stack.append(number)

        def PRINT_ANSWER(self):
                answer = self.stack.pop()
                print(answer)

        def ADD_TWO_VALUES(self):
                first_num = self.stack.pop()
                second_num = self.stack.pop()
                total = first_num + second_num
                self.stack.append(total)

        def STORE_NAME(self, name):
                val = self.stack.pop()
                self.environmentp[name] = val

        def LOAD_NAME(self, name):
                val = self.environment[name]
                self.stack.append()

        def parse_argument(self, instruction, argument, what_to_execute):
                numbers = ["LOAD_VALUE"]  
                names = ["LOAD_NAME", "STORE_NAME"]

                if instruction in numbers:
                    argument = what_to_execute["numbers"][argument]
                elif instruction in names:
                    argument = what_to_execute["names"][argument]

                return argument

        def run_code(self, what_to_execute):
                instructions = what_to_execute["instructions"]
                numbers = what_to_execute["numbers"]
                for each_step in instructions:
                        instruction, argument = each_step
                        if instruction == "LOAD_VALUE":
                                number = numbers[argument]
                                self.LOAD_VALUE(number)
                        elif instruction == "ADD_TWO_VALUES":
                                self.ADD_TWO_VALUES()
                        elif instruction == "PRINT_ANSWER":
                                self.PRINT_ANSWER()
                        elif instruction == "STORE_NAME":
                                self.STORE_NAME(argument)
                        elif instruction == "LOAD_NAME":
                                self.LOAD_NAME(argument)
        
        def execute(self, what_to_execute):
                instructions = what_to_execute["instructions"]
                for each_step in instructions:
                        instruction, argument = each_step
                        argument = self.parse_argument(instruction, argument, what_to_execute)
                        bytecode_method = getattr(self, instruction)
                        if argument is None:
                                bytecode_method()
                        else:
                                bytecode_method(argument)

