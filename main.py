from interpreter import Interpreter

what_to_execute = {
	"instructions": [
			("LOAD_VALUE", 0), 
			("LOAD_VALUE", 1), 
			("ADD_TWO_VALUES", None), 
			("PRINT_ANSWER", None) 
			],
	"numbers": [7, 5]
}

interpreter = Interpreter()
interpreter.run_code(what_to_execute)
