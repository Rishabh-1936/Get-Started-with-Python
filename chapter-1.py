import time
import sys

def print_slow(str):
    
    for letter in str:
        if letter=="*": 
            sleep=0.8
        else:
            sleep=0.1
            sys.stdout.write(letter)
            sys.stdout.flush()
        time.sleep(sleep)
print('Hi')
print_slow("Hi this is the testing string")


para1='''
Hello Everyone, in today’s class we are going to talk about what the Python is? Basically, in today's class we get the basic idea of what is Programming Language, Syntax, Semantics, Python and its scope and usage.
So without wasting your much time in introduction, let's get started with today's interation.
*
As we know for interacting with anyone we need a language just like that, with the computer systems that language is called Programming Language. So, in short we can say that a programming language is the set of instructions through which humans interact with computers.
*
'''
para2='''
There are many programming languages like C, C++, Java, Python and many more. Today we are discussing about the Python. Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
Python's simple and easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reusability.
And because of such advantages it is widely used for automation and quite popular too.
*
'''

para3='''
Python is one of the general purpose scripting language that is widely used for scripting and automation .An automation is the process of replacing a manual step with one that happens automatically.Like
Sending an E-Mail to a same set of users can be done using scripting,task scheduling,etc.
*
As we discussed earlier that python is an interpereted language so what it means? An interpreted language is a type of programming language for which most of its implementations execute instructions directly and freely, without previously compiling a program into machine-language instructions.
I means in interepreted language interpreter compiles the instructions one-by-one not in one go.
*
While the another type of language is compiled language in which the whole implementation i.e source code is compiled into machine-language instruction in one go.
*
As we discussed that python is a high-level programming language.So what is it? An high level language is a programming language which has strong abstraction level it means it is more close to human understandable language than machine understandable low level language which is assembly language or binary language i.e 0/1.
For example ,for printing anything on the screen there is a command in python i.e ‘print’ which tells the operating system to display the charater over the screen , so we need not to worry about how to call operating system and how to command it for displaying the character over the screen ,it’s all infer from the ‘print’ command.  
*
Everything in python (lists, dictionaries, classes and so forth) is an object; high-level: it means that the syntax of the code is easier to interpret by humans.
*
Now let’s talk about syntax and semantics before discussing the dynamic semantics.
So, Syntax is about the structure or the grammar of the language. It answers the question: how do I construct a valid sentence? All languages, even English and other human (aka "natural") languages have grammars, that is, rules that define whether or not the sentence is properly constructed.
*
Here are some syntax rules in Python:
1.	There should be proper indentation to define the scope of the block like function,class.
2.	Comments must be started with ‘#’.
3.	Python is case sensitive. This means, Variable and variable are not the same.
4.	there is no command terminator, which means no semicolon ; or anything else.
*
Semantics is about the meaning of the sentence. It answers the questions: is this sentence valid? If so, what does the sentence mean? For example:
A=5;	-> statement 1
X+Y=Z;	-> statement 2
*
Above both statements are syntactically correct but the second statement is semantically incorrect. According to statement 2, it means that assign the sum of ‘X’ and ‘Y’ to ‘Z’ but in actual what we want ?
We want to store the sum of ‘X’ and ‘Y’ in ‘Z’. So this statement does not give any error as it is syntactically correct but leads to inconsistent result.
*
So writing code, using correct syntax is super important. Even a small typo, like a missing parentheses or an extra comma, can cause a syntax error and the code won't execute at all.
If your code results in an error or an exception, pay close attention to syntax and watch out for minor mistakes.
If your syntax is correct, but the script has unexpected behavior or output, this may be due to a semantic problem. Remember that syntax is the rules of how code is constructed, while semantics are the overall effect the code has. 
It is possible to have syntactically correct code that runs successfully, but doesn't do what we want it to do.
*
So now understand what is dynamically typed or semantic language. Whenever in any language if we want to use any variable we need to define it’s type i.e what type of value it will hold, 
which tells the compiler to allocate that much amount of space into the memory which happens in static language but in dynamically typed language the type of the variable is unknown until the code is run.
So declaration is of no use. What it does is, it stores that value at some memory location and then binds that variable name to that memory container. And thus makes the contents of the container accessible through that variable name. 
So the data type does not matter. As it will get to know the type of the value which the variable holds at run-time only.
*
For example:
Python:							C++:
    X=5								int x=5;
    Print(x)						cout<<x;
    X='hello'						string str="hello";
    Print(x) 						cout<<str;
*
'''

para4='''
Today we get to know a lot of stuff about python but before diving deep into the python we need to know some of the termologies:
*
-> Program:     It has complex structure of code and has various other dependent or linked programs or scripts.
-> Script:      It is a simple piece of code which generally written to perform a single and independent task.
-> Tokens:      The basic building blocks in a programming language. Constants, Keywords, Identifier, Operators all are the tokens as they cannot be sub-divided into more simpler form.
-> Keywords:    They are the reserved words in Python.We cannot use a keyword as a variable name, function name or any other identifier. They are used to define the syntax and structure of the Python language.
                In Python, keywords are case sensitive and there are 33 keywords for example, for, while, if,else, elif ,.. We discuss each one of them in subsequent classes.
-> Identifiers: An identifier is a name given to entities like class, functions, variables, etc. It helps to differentiate one entity from another.
*
Rules for writing identifiers
1.	Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore _. Names like myClass, var_1 and print_this_to_screen, all are valid example.
2.	An identifier cannot start with a digit. 1variable is invalid, but variable1 is a valid name.
3.	Keywords cannot be used as identifiers.
4.	We cannot use special symbols like !, @, #, $, % etc. in our identifier.
5.	An identifier can be of any length.
*

'''

print_slow(para1)
print_slow(para2)
print_slow(para3)
print_slow(para4)