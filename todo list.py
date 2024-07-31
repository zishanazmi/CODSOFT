import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("550x450")
        self.root.configure(bg="#E8F0F2")  # Soft light blue background
        
        self.task_list = []
        
        # Frame for the entry and add button
        self.frame = tk.Frame(self.root, bg="#E8F0F2")
        self.frame.pack(pady=20)
        
        # Entry widget to input tasks
        self.task_entry = tk.Entry(self.frame, width=31, font=("Helvetica", 14), bg="#FFFFFF", fg="#333333", relief=tk.FLAT, bd=5)
        self.task_entry.pack(side=tk.LEFT, padx=10)
        self.task_entry.bind("<Return>", lambda event: self.add_task())
        
        # Add Task button
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task, bg="#5BC8AC", fg="#FFFFFF", font=("Helvetica", 12, "bold"), relief=tk.FLAT)
        self.add_button.pack(side=tk.LEFT, padx=10)
        
        # Listbox to display tasks
        self.listbox = tk.Listbox(self.root, font=("Helvetica", 12), width=50, height=10, bg="#FFFFFF", fg="#333333", selectbackground="#5BC8AC", selectforeground="#FFFFFF", relief=tk.FLAT, bd=5)
        self.listbox.pack(pady=20)
        
        # Frame for action buttons
        self.button_frame = tk.Frame(self.root, bg="#E8F0F2")
        self.button_frame.pack(pady=10)
        
        # Mark as Done button
        self.done_button = tk.Button(self.button_frame, text="Mark as Done", command=self.mark_as_done, bg="#FFD166", fg="#333333", font=("Helvetica", 12, "bold"), relief=tk.FLAT)
        self.done_button.pack(side=tk.LEFT, padx=10)
        
        # Update Task button
        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task, bg="#118AB2", fg="#FFFFFF", font=("Helvetica", 12, "bold"), relief=tk.FLAT)
        self.update_button.pack(side=tk.LEFT, padx=10)
        
        # Delete Task button
        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task, bg="#EF476F", fg="#FFFFFF", font=("Helvetica", 12, "bold"), relief=tk.FLAT)
        self.delete_button.pack(side=tk.LEFT, padx=10)
        
        # Clear List button
        self.clear_button = tk.Button(self.button_frame, text="Clear List", command=self.clear_list, bg="#EF476F", fg="#FFFFFF", font=("Helvetica", 12, "bold"), relief=tk.FLAT)
        self.clear_button.pack(side=tk.LEFT, padx=10)
        
    def add_task(self):
        task = self.task_entry.get()
        if task.strip():
            self.task_list.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")
        
    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            del self.task_list[selected_task_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Delete Error", "Please select a task to delete.")
        
    def clear_list(self):
        self.task_list = []
        self.update_listbox()
        
    def mark_as_done(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.task_list[selected_task_index] = f"{self.task_list[selected_task_index]}✅"
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Mark Error", "Please select a task to mark as done.")
        
    def update_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task.strip():
                self.task_list[selected_task_index] = new_task
                self.update_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a new task description.")
        except IndexError:
            messagebox.showwarning("Update Error", "Please select a task to update.")
        
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.task_list:
            self.listbox.insert(tk.END, task)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
