import factorial #importing the factorial module
import tkinter as tk
from tkinter import messagebox

class UserInterface:

    def __init__(self):
        #Set Application Window
        self.root = tk.Tk()
        self.root.geometry("500x300")
        self.root.title("Technical Assessment")
        
        self.label =tk.Label(self.root,text ="PRIME AND FACTORIAL", font=('Arial', 18))
        self.label.pack(padx=20,pady=20)

        #User input textbox
        self.textbox = tk.Entry(self.root,font=('Arial', 20))
        self.textbox.pack()

        #Button to call the checking function
        self.button = tk.Button(self.root,text="CHECK", command=self.checking)
        self.button.pack(padx=10,pady=10)

        #The Output to display prime and factorial value
        self.prime_output = tk.Label(self.root,text="",font=('Arial', 15))
        self.prime_output.pack(padx=10,pady=10)

        self.factorial_output = tk.Label(self.root,text="",font=('Arial', 15))
        self.factorial_output.pack()


        self.root.mainloop()
    
           
    #Button Function to check if number is prime and calculate the factorial
    def checking(self):
        
        try:
            givenNum = int(self.textbox.get())

            #call the function on factorial module and set as variable
            factorial_num = factorial.factorialvalue(givenNum) 

            #call the function on factorial module and set as variable
            prime_num = factorial.primevalue(givenNum)

            if prime_num == False:
                 self.prime_output.config(text=f"{givenNum} is not a prime number")
                 self.factorial_output.config(text= f"Factorial: {factorial_num}")
            else:
                 self.prime_output.config(text=f"{givenNum} is a prime number")
                 self.factorial_output.config(text= f"Factorial: {factorial_num}")
                         
        except ValueError:
            messagebox.showerror("Error:", "Please enter valid numbers")


if __name__=="__main__":
    UserInterface()

    
