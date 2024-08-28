import random

# Define the questions, options, and correct answers
quiz_data = {
    "What is a function in Python?": {
        "options": ["A piece of code that only runs once", "A block of code that executes repeatedly", "A block of code that only runs when it is called", "A type of variable"],
        "answer": "A block of code that only runs when it is called"
    },
    "Which keyword is used to define a function in Python?": {
        "options": ["function", "define", "def", "func"],
        "answer": "def"
    },
    "What is the purpose of the 'return' statement in a Python function?": {
        "options": ["To stop the function from executing", "To output a value from the function", "To define a function", "To pass an argument to the function"],
        "answer": "To output a value from the function"
    },
    "How do you call a function named 'my_function' in Python?": {
        "options": ["call my_function", "my_function()", "execute my_function", "run my_function"],
        "answer": "my_function()"
    },
    "What will 'print(my_function())' do if 'my_function' has no 'return' statement?": {
        "options": ["Print 'None'", "Print an empty string", "Cause an error", "Print the function name"],
        "answer": "Print 'None'"
    },
    "Can a Python function return multiple values?": {
        "options": ["Yes, using a tuple", "No", "Yes, using multiple return statements", "Yes, but only if they are integers"],
        "answer": "Yes, using a tuple"
    },
    "What is the purpose of 'args' and 'kwargs' in Python functions?": {
        "options": ["To pass variable length arguments", "To pass only keyword arguments", "To pass only positional arguments", "To define local variables"],
        "answer": "To pass variable length arguments"
    },
    "What is a lambda function in Python?": {
        "options": ["A function that takes no arguments", "A function that always returns 'None'", "An anonymous function", "A built-in Python function"],
        "answer": "An anonymous function"
    },
    "How do you pass a default value to a parameter in Python?": {
        "options": ["Using the 'default' keyword", "Using the '=' operator", "Using the 'const' keyword", "You cannot assign default values"],
        "answer": "Using the '=' operator"
    },
    "What does the 'global' keyword do in a Python function?": {
        "options": ["It makes a local variable global", "It restricts the function to be called only once", "It is used to define global constants", "It does nothing"],
        "answer": "It makes a local variable global"
    },
    "What is a recursive function in Python?": {
        "options": ["A function that calls itself", "A function that returns the same value every time", "A function that is defined within another function", "A function that does not return any value"],
        "answer": "A function that calls itself"
    },
    "How can you specify that a parameter is optional in a Python function?": {
        "options": ["Using the 'optional' keyword", "Using the '=' operator with a default value", "Using the '?' operator", "Using the 'None' keyword"],
        "answer": "Using the '=' operator with a default value"
    },
    "What will 'my_function(2, 3)' return if 'my_function' is defined as 'def my_function(a, b=5): return a + b'?": {
        "options": ["5", "7", "10", "8"],
        "answer": "5"
    },
    "Can you define a function inside another function in Python?": {
        "options": ["Yes", "No", "Only in classes", "Only in modules"],
        "answer": "Yes"
    },
    "What is the scope of a variable defined inside a function?": {
        "options": ["Global", "Local", "Both", "Universal"],
        "answer": "Local"
    },
    "What does the 'nonlocal' keyword do in a Python function?": {
        "options": ["It makes a variable local", "It restricts the function to access only global variables", "It is used to declare variables outside any function", "It allows you to assign a value to a variable in an outer function"],
        "answer": "It allows you to assign a value to a variable in an outer function"
    },
    "What will the following code print? \n```def my_function(x, y): return x * y\nprint(my_function(2, 3))```": {
        "options": ["5", "6", "2", "3"],
        "answer": "6"
    },
    "How do you document a Python function?": {
        "options": ["Using the '#' symbol", "Using a docstring", "Using a comment", "Using a 'note' function"],
        "answer": "Using a docstring"
    },
    "What happens if you define two functions with the same name in Python?": {
        "options": ["An error is thrown", "The program crashes", "The second function definition overwrites the first one", "Both functions are called"],
        "answer": "The second function definition overwrites the first one"
    },
    "How can you ensure a function only accepts integer arguments?": {
        "options": ["Using the 'int' keyword", "Using type hints and runtime checks", "It is automatically done by Python", "Using the 'check' function"],
        "answer": "Using type hints and runtime checks"
    },
     "What will the following code print? \n```def my_function(a, b=2, c=3): return a + b + c\nprint(my_function(5))```": {
        "options": ["10", "8", "5", "None"],
        "answer": "10"
    },
    "What is the purpose of a 'decorator' in Python?": {
        "options": ["To decorate strings", "To modify the behavior of a function", "To format the output of a function", "To create a new function"],
        "answer": "To modify the behavior of a function"
    },
    "What will happen if you call a function that takes two arguments, but you only pass one?": {
        "options": ["An error occurs", "The second argument is set to 'None'", "The function uses a default value for the second argument", "The function returns an empty string"],
        "answer": "An error occurs"
    },
    "What keyword is used to import a module into a Python script?": {
        "options": ["include", "require", "import", "use"],
        "answer": "import"
    },
    "What is the difference between a parameter and an argument in Python?": {
        "options": ["They are the same", "A parameter is a variable in the function definition; an argument is the value passed to the function", "An argument is defined in the function, while a parameter is passed to the function", "Parameters are optional, arguments are required"],
        "answer": "A parameter is a variable in the function definition; an argument is the value passed to the function"
    },
    "How do you specify that a Python function does not return any value?": {
        "options": ["Use the 'void' keyword", "Use the 'return' statement without any value", "Don't use the 'return' statement", "Use 'return None' explicitly"],
        "answer": "Use 'return None' explicitly"
    },
    "Can a Python function modify a global variable?": {
        "options": ["No", "Yes, but only if declared with the 'global' keyword", "Yes, by default", "Only if the function is defined in the global scope"],
        "answer": "Yes, but only if declared with the 'global' keyword"
    },
    "What is a 'docstring' in Python?": {
        "options": ["A string that documents the function", "A string that is ignored by the interpreter", "A string that is printed by the function", "A special variable type"],
        "answer": "A string that documents the function"
    },
    "What will the following code print? \n```def my_function(x):\n    if x > 0:\n        return 'Positive'\n    else:\n        return 'Non-Positive'\nprint(my_function(-1))```": {
        "options": ["Positive", "Non-Positive", "None", "Error"],
        "answer": "Non-Positive"
    },
    "What is the purpose of the 'assert' statement in a Python function?": {
        "options": ["To raise an error if a condition is false", "To define a function", "To return a value from the function", "To create a loop in the function"],
        "answer": "To raise an error if a condition is false"
    },
    "What does the 'pass' statement do in a Python function?": {
        "options": ["Terminates the function", "Does nothing and allows you to write empty functions", "Returns a default value", "Calls the function"],
        "answer": "Does nothing and allows you to write empty functions"
    },
    "How can you prevent a Python function from being called when the module is imported?": {
        "options": ["By not defining the function", "By using the 'if __name__ == \"__main__\":' construct", "By using the 'private' keyword", "By defining the function after the import statement"],
        "answer": "By using the 'if __name__ == \"__main__\":' construct"
    },
    "What will the following code output? \n```def func(x=[]):\n    x.append(1)\n    return x\nprint(func())\nprint(func())```": {
        "options": ["[1] [1]", "[1] [1, 1]", "[1, 1] [1]", "[1, 1] [1, 1]"],
        "answer": "[1] [1, 1]"
    },
    "What is the difference between 'args' and 'kwargs' in a Python function?": {
        "options": ["'args' is used for positional arguments, 'kwargs' for keyword arguments", "'args' is for required arguments, 'kwargs' for optional arguments", "'args' is a list, 'kwargs' is a dictionary", "There is no difference"],
        "answer": "'args' is used for positional arguments, 'kwargs' for keyword arguments"
    },
    "What does the following code do? \n```def my_function():\n    pass\n```": {
        "options": ["Defines an empty function", "Causes an error", "Defines a function that does nothing", "Both A and C"],
        "answer": "Both A and C"
    },
    "How do you specify a keyword argument in a Python function call?": {
        "options": ["Using the '=' operator", "Using the ':' operator", "Using the '->' operator", "Using the '=>' operator"],
        "answer": "Using the '=' operator"
    },
    "What will happen if you use the 'return' statement outside a function?": {
        "options": ["It will cause a syntax error", "It will return None", "It will return a default value", "It will pass control to the calling code"],
        "answer": "It will cause a syntax error"
    },
    "Can a Python function be assigned to a variable?": {
        "options": ["Yes, functions are first-class objects in Python", "No, functions cannot be treated as variables", "Yes, but only if the function is static", "Only if the function is a lambda function"],
        "answer": "Yes, functions are first-class objects in Python"
    },
    "What is the purpose of a function signature in Python?": {
        "options": ["To define the structure of the function", "To define the data types of arguments", "To provide a description of the function", "To specify the arguments and return type"],
        "answer": "To specify the arguments and return type"
    },
    "What will the following code print? \n```def my_function(x, y=4): return x * y\nprint(my_function(2))```": {
        "options": ["4", "8", "2", "Error"],
        "answer": "8"
    },
    "What is a dictionary in Python?": {
        "options": ["A list of key-value pairs", "A list of integers", "A collection of unordered items", "A sequence of elements"],
        "answer": "A list of key-value pairs"
    },
    "How do you create an empty dictionary in Python?": {
        "options": ["[]", "{}", "()", "set()"],
        "answer": "{}"
    },
    "How can you access the value associated with a specific key in a dictionary?": {
        "options": ["dict[key]", "dict.get(key)", "dict.key", "dict.value"],
        "answer": "dict[key]"
    },
    "What will dict.get(key) return if the key is not found?": {
        "options": ["None", "A default value, or None if not specified", "KeyError", "False"],
        "answer": "A default value, or None if not specified"
    },
    "How do you add a new key-value pair to a dictionary?": {
        "options": ["dict.add(key, value)", "dict.insert(key, value)", "dict[key] = value", "dict.append(key, value)"],
        "answer": "dict[key] = value"
    },
    "What will the following code print?\n\nd = {'a': 1, 'b': 2}\nprint(d['c'])": {
        "options": ["KeyError", "None", "2", "0"],
        "answer": "KeyError"
    },
    "How can you check if a key exists in a dictionary?": {
        "options": ["key in dict.keys()", "key in dict", "dict.contains(key)", "key.exists(dict)"],
        "answer": "key in dict"
    },
    "Which of the following methods removes a key from a dictionary and returns its value?": {
        "options": ["dict.delete(key)", "dict.pop(key)", "dict.remove(key)", "dict.popitem(key)"],
        "answer": "dict.pop(key)"
    },
    "What will dict.popitem() do?": {
        "options": ["Remove and return the first key-value pair", "Return the first key-value pair without removing it", "Remove and return an arbitrary key-value pair", "Raise a KeyError"],
        "answer": "Remove and return an arbitrary key-value pair"
    },
    "How can you merge two dictionaries in Python 3.9+?": {
        "options": ["dict1.update(dict2)", "dict3 = dict1 | dict2", "dict3 = dict1 & dict2", "dict1 += dict2"],
        "answer": "dict3 = dict1 | dict2"
    },
    "What will len(dict) return?": {
        "options": ["The number of values in the dictionary", "The number of key-value pairs in the dictionary", "The total number of keys in the dictionary", "The size of the dictionary in bytes"],
        "answer": "The number of key-value pairs in the dictionary"
    },
    "How can you get all the keys from a dictionary?": {
        "options": ["dict.keys()", "dict.values()", "dict.getkeys()", "dict.items()"],
        "answer": "dict.keys()"
    },
    "What does the clear() method do in a dictionary?": {
        "options": ["Deletes the first key-value pair", "Removes all key-value pairs from the dictionary", "Removes a specific key-value pair", "Resets the dictionary to its default values"],
        "answer": "Removes all key-value pairs from the dictionary"
    },
    "What is the output of the following code?\n\nd = {'a': 1, 'b': 2}\nprint(d.get('c', 3))": {
        "options": ["None", "3", "KeyError", "2"],
        "answer": "3"
    },
    "Can dictionary keys be of different data types?": {
        "options": ["Yes", "No", "Only if they are strings", "Only if they are numbers"],
        "answer": "Yes"
    },
    "What is the output of the following code?\n\nd = {'a': 1, 'b': 2}\nd['c'] = d['a'] + d['b']\nprint(d)": {
        "options": ["{'a': 1, 'b': 2}", "{'a': 1, 'b': 2, 'c': 3}", "{'c': 3}", "{'a': 1, 'b': 2, 'c': '12'}"],
        "answer": "{'a': 1, 'b': 2, 'c': 3}"
    },
    "Which method would you use to copy a dictionary?": {
        "options": ["dict.duplicate()", "dict.copy()", "dict.clone()", "dict.replicate()"],
        "answer": "dict.copy()"
    },
    "Can dictionary values be of different data types?": {
        "options": ["Yes", "No", "Only if they are strings", "Only if they are numbers"],
        "answer": "Yes"
    },
    "What is the output of the following code?\n\nd = {'a': 1, 'b': 2}\nd.update({'b': 3, 'c': 4})\nprint(d)": {
        "options": ["{'a': 1, 'b': 2}", "{'a': 1, 'b': 3, 'c': 4}", "{'b': 3, 'c': 4}", "{'a': 1, 'b': 2, 'c': 4}"],
        "answer": "{'a': 1, 'b': 3, 'c': 4}"
    },
    "Which of the following can be used as a dictionary key?": {
        "options": ["A list", "A tuple", "A set", "A dictionary"],
        "answer": "A tuple"
    },
     
    " What is the main difference between a tuple and a list in Python?": {
        "options": ["Lists are mutable, and tuples are immutable", "Tuples are mutable, and lists are immutable", "Both are mutable", "Both are immutable"],
        "answer": "Lists are mutable, and tuples are immutable"
    },
    " Which method is used to add an element to a list in Python?": {
        "options": [".append()", ".insert()", ".add()", ".extend()"],
        "answer": ".append()"
    },
    " How can you convert a list into a tuple?": {
        "options": ["tuple(list)", "list(tuple)", "convert(list, tuple)", "list_to_tuple(list)"],
        "answer": "tuple(list)"
    },
    " Which of the following methods can be used to remove an element from a list?": {
        "options": [".remove()", ".pop()", "del", "All of the above"],
        "answer": "All of the above"
    },
    " Which of the following operations will raise an error for tuples?": {
        "options": ["Adding elements", "Accessing elements", "Indexing elements", "Slicing elements"],
        "answer": "Adding elements"
    },
    " What is the correct way to create an empty tuple?": {
        "options": ["()", "[]", "{}", "tuple([])"],
        "answer": "()"
    },
    " How do you get the length of a list or tuple in Python?": {
        "options": ["len()", "length()", "size()", "count()"],
        "answer": "len()"
    },
    " Which of the following can a tuple contain?": {
        "options": ["Only strings", "Only integers", "Only lists", "Elements of any data type"],
        "answer": "Elements of any data type"
    },
    " Which method is used to insert an element at a specific position in a list?": {
        "options": [".insert()", ".append()", ".add()", ".extend()"],
        "answer": ".insert()"
    },
    " Can a tuple contain duplicate elements?": {
        "options": ["Yes", "No", "Only strings can be duplicated", "Only integers can be duplicated"],
        "answer": "Yes"
    },
    " Which of the following is a valid way to declare a tuple with a single element?": {
        "options": ["(element,)", "(element)", "[element]", "{element}"],
        "answer": "(element,)"
    },
    " Which method removes the last element from a list?": {
        "options": [".remove()", ".pop()", ".delete()", ".discard()"],
        "answer": ".pop()"
    },
    " Can lists contain elements of different data types?": {
        "options": ["Yes", "No", "Only strings and integers", "Only numbers"],
        "answer": "Yes"
    },
    " What is the result of the expression len([(1,2), (3,4)])?": {
        "options": ["4", "2", "1", "Error"],
        "answer": "2"
    },
    "Which method can be used to extend a list by adding all elements from another list?": {
        "options": [".extend()", ".append()", ".insert()", ".add()"],
        "answer": ".extend()"
    },
    "How can you access the second element of a tuple named tup?": {
        "options": ["tup[1]", "tup(1)", "tup[2]", "tup{1}"],
        "answer": "tup[1]"
    },
    " Can tuples be nested inside lists?": {
        "options": ["Yes", "No", "Only in dictionaries", "Only with strings"],
        "answer": "Yes"
    },
    " Which method reverses the elements of a list in place?": {
        "options": [".reverse()", ".reversed()", ".flip()", ".invert()"],
        "answer": ".reverse()"
    },
    " Can you sort the elements of a tuple?": {
        "options": ["No, tuples are immutable", "Yes, using .sort()", "Yes, using sorted()", "Only for integers"],
        "answer": "No, tuples are immutable"
    },
    " What will be the output of the expression list('abc')?": {
        "options": ["['abc']", "['a', 'b', 'c']", "['a', 'bc']", "Error"],
        "answer": "['a', 'b', 'c']"
    }
}
def ask_question(question, options, correct_answer):
    """Ask the question with options and return if the user's choice is correct."""
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    try:
        user_choice = int(input("Choose the correct option (1-4): "))
        return options[user_choice - 1].strip().lower() == correct_answer.strip().lower()
    except (ValueError, IndexError):
        print("Invalid choice. Please choose a number between 1 and 4.")
        return False

def run_quiz(quiz_data, num_questions=5):
    """Run the quiz game."""
    score = 0
    questions = list(quiz_data.keys())
    random.shuffle(questions)  # Randomize the order of questions
    
    for i in range(min(num_questions, len(quiz_data))):
        question = questions[i]
        options = quiz_data[question]["options"]
        correct_answer = quiz_data[question]["answer"]
        correct = ask_question(question, options, correct_answer)
        if correct:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: {correct_answer}\n")

    print(f"Your final score is: {score}/{num_questions}")
    
    # Display a message based on the score
    if score == num_questions:
        print("VERY GOOD KEEP IT UP")
    else:
        print("WELL TRIED!! GOOD LUCK FOR NEXT TIME")

# Example usage:
print("Welcome to the .py Quiz Game!")
print(f"Total questions {len(quiz_data)}")
num_questions = int(input("How many questions would you like to answer? "))
run_quiz(quiz_data, num_questions)
