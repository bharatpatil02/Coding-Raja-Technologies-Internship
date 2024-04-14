from tkinter import * #import function (tix is not library)

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do-List')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-Do-List-App', font='arial 25 bold', width=10, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task', font='arial 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks', font='arial 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=15, bd=5, width=40, font="arial 12 bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='arial 10 bold')
        self.text.place(x=20, y=120)

        # Add task
        def add(): #naming convention 
            content = self.text.get(1.0, END)
            if content != '\n':  # Check if the content is not empty
                self.main_text.insert(END, content)
                with open('data.txt', 'a') as file:
                    file.write(content + '\n')  # Write the content with a newline character
                self.text.delete(1.0, END)

        # Delete task
        def delete():
            delete_item = self.main_text.curselection()
            if delete_item:  # Check if an item is selected
                look = self.main_text.get(delete_item)
                with open('data.txt', 'r') as file:
                    lines = file.readlines()  # Read all lines into a list
                with open('data.txt', 'w') as file:
                    for line in lines:
                        if line.strip('\n') != look:  # Compare without the newline character
                            file.write(line)  # Write the line back, excluding the deleted item
                self.main_text.delete(delete_item)

        self.button = Button(self.root, text="Add", font='arial 20 bold italic', width=10, bd=5, bg='orange', fg='black', command=add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font='arial 20 bold italic', width=10, bd=5, bg='orange', fg='black', command=delete)
        self.button2.place(x=30, y=280)

        # Load tasks from the file
        with open('data.txt', 'r') as file:
            tasks = file.readlines()
            for task in tasks:
                self.main_text.insert(END, task.strip('\n'))

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    