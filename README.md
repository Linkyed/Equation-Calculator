# Equation-Calculator
Python scripts to calculate first and second degree equations

# Day 3: 
I lost what i already write about this project, then i will start writing here on GITHUB README, ok les't start.
The project's that i thougt start to working but it was really bad, i writed a lot of code to only do simple thing like plus and minus operations, then i throw away everthing and start from zero for the second time :).

Now the project look a lot better, i alreaty have a totally function numbers calculator (Only rest to implement the order when the equation has parentheses). The logic is a bit strange but when you understand it will be more easy to read. I divided a equation between two part first, Left side and Right side, after that i divided again between the numbers and operations. Then in the final the program have 4 lists,
two to save the numbers and operation of the left side and the other 2 to save the numbers and operations of the right side. With that the program can calculate in the math order, all the operations with all the numbers and get the final result. How the program do that it's using on object that store the operation and the location that it is in the equation, and with a list of al this objects one function can calculate in the math order everting. I write one simple equation and one more complicated in the program, to you understand all of i said it's really important to open my code an ready all the comments :). See you next day! 

# Day 4:
Today i finished the script that can calculate a sequence of numbers and operations, now it can do the math counts and at the same time it make a .txt doccument that store all the steps to solve all the math. And the script can solve the final math count when you get the value of the left equation and pass to the right side with oposite signal. To finish that completly i just need one way to get the equation and the X that the program will have to calculate, to do that i already decided to creat one simple GUI on python, just to finish the program and have a usefull tool

I finally decided the library that i will use to creat the GUI, i choose the TKINTER because i already used it one year ago an i am more confident to relearn this library. I already created some window with a bunch of basic buttons to create one equation but i need to complete them and i get them in the right position. I also discovery a library called CustomTkinter that has a more beautiful things to show in the GUI, tomorrow i will decide if i will use that library or not

# Day 5:
Today i upgraded the visual of the GUI, i start using the library CUSTOM TKINTER developed by Tom Schimansky and you can find it here on github. This library is a lot more beatiful that normal tkinter then i restructure the code and change almost every thing to this library.

And for the the logic, today i changed the way that the program can get the numbers, now it will be a TextBox that you can type any integer number and after typing you can click on the Save button and the number will go to the equation. It can already save the numbers in one list that in the future will be used in the second code to calculate all the operations. It's it for today, tomorrow i will readd the backspace button that doest work with the textbox and start to figure out how i will add the X in the equation, have a nice day!
