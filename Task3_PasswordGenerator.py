#Password Generator Source Code!

#importing requires modules
import random
import string
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

#function that generates and return a password of random characters of desired length
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

#function to get the user input(desired length), validate it and prints the output on the console
def main():
    print("\nWelcome to the Password Generator!\n")

    try:
        password_length = int(input("Enter the desired length of the password: "))
        if password_length <= 0:        #to check whether the entered value is positive number or not
            print("Please enter a valid positive length.")
            return
    except ValueError:      #to check whether the entered length is integer or not
        print("Please enter a valid integer for the length.")
        return

    password = generate_password(password_length)
    print(f"\nGenerated Password: {password}\n")
    print("\nNow see the simple demonstration of the PassWord Application! If a new window didn't pop up, check that out in your task bar!\n")

if __name__ == "__main__":
    main()


#This is a sample application build using the above source code.
#Please note that the application can be modified. This is the simplest model of the application
#A window may or may not open, but you will find a new icon opened in your task bar. Check that out
    

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        master.geometry("400x250")
        master.resizable(False, False)
        master.configure(bg='#f0f0f0')

        self.label = Label(master, text="Enter the desired length of the password:", font=('Arial', 12), bg='#f0f0f0')
        self.label.pack(pady=10)

        self.length_entry = Entry(master, font=('Arial', 12), bd=2, relief=tk.GROOVE)
        self.length_entry.pack(pady=10)

        self.generate_button = Button(master, text="Generate Password", command=self.generate_password, bg='#4CAF50', fg='white', font=('Arial', 12), relief=tk.GROOVE)
        self.generate_button.pack(pady=20)

        self.result_label = Label(master, text="", font=('Arial', 14), bg='#f0f0f0')
        self.result_label.pack()

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
            if password_length <= 0:
                messagebox.showerror("Error", "Please enter a valid positive length.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for the length.")
            return

        password = self._generate_password(password_length)
        self.result_label.config(text=f"Generated Password:\n{password}")

    def _generate_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()


