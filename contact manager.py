import tkinter as tk
from tkinter import messagebox, simpledialog
import shelve

# Initialize the contact storage
contact_storage = shelve.open("contacts_db")

# Function to add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter contact name:")
    phone = simpledialog.askstring("Input", "Enter contact phone number:")
    email = simpledialog.askstring("Input", "Enter contact email:")
    address = simpledialog.askstring("Input", "Enter contact address:")
    
    if name and phone:
        contact_id = f"{name.lower()}_{phone}"
        contact_storage[contact_id] = {"name": name, "phone": phone, "email": email, "address": address}
        messagebox.showinfo("Success", "Contact added successfully!")
        update_contact_list()
    else:
        messagebox.showwarning("Input Error", "Name and phone number are required!")

# Function to view the contact list
def view_contacts():
    update_contact_list()

# Function to search for a contact
def search_contact():
    search_term = simpledialog.askstring("Search", "Enter name or phone number to search:")
    if search_term:
        search_results = [f"{data['name']} - {data['phone']} - {data['email']} - {data['address']}" 
                          for key, data in contact_storage.items() 
                          if search_term.lower() in data['name'].lower() or search_term in data['phone']]
        contact_list.delete(0, tk.END)
        for result in search_results:
            contact_list.insert(tk.END, result)
    else:
        messagebox.showwarning("Input Error", "Search term cannot be empty!")

# Function to update a contact
def update_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        contact_info = contact_list.get(selected_contact[0])
        name, phone, email, address = contact_info.split(" - ")
        contact_id = f"{name.lower()}_{phone}"
        
        new_name = simpledialog.askstring("Update", "Enter new contact name:", initialvalue=name)
        new_phone = simpledialog.askstring("Update", "Enter new contact phone number:", initialvalue=phone)
        new_email = simpledialog.askstring("Update", "Enter new contact email:", initialvalue=email)
        new_address = simpledialog.askstring("Update", "Enter new contact address:", initialvalue=address)
        
        if new_name and new_phone:
            new_contact_id = f"{new_name.lower()}_{new_phone}"
            contact_storage[new_contact_id] = {"name": new_name, "phone": new_phone, "email": new_email, "address": new_address}
            if new_contact_id != contact_id:
                del contact_storage[contact_id]
            messagebox.showinfo("Success", "Contact updated successfully!")
            update_contact_list()
        else:
            messagebox.showwarning("Input Error", "Name and phone number are required!")
    else:
        messagebox.showwarning("Selection Error", "No contact selected!")

# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        contact_info = contact_list.get(selected_contact[0])
        name, phone, *_ = contact_info.split(" - ")
        contact_id = f"{name.lower()}_{phone}"
        del contact_storage[contact_id]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        update_contact_list()
    else:
        messagebox.showwarning("Selection Error", "No contact selected!")

# Function to update the contact list display
def update_contact_list():
    contact_list.delete(0, tk.END)
    for key, data in contact_storage.items():
        contact_list.insert(tk.END, f"{data['name']} - {data['phone']} - {data['email']} - {data['address']}")

# Create the main window
root = tk.Tk()
root.title("Contact Management System")

# Set the window size and position
root.geometry("620x400")
root.configure(bg="#F0F4F8")

# Define custom font
custom_font = ("Helvetica", 12)

# Style and layout for buttons
button_style = {
    'font': custom_font,
    'bg': "#A1C4FD",
    'fg': "#34495E",
    'activebackground': "#B6E1FC",
    'activeforeground': "#34495E",
    'bd': 0,
    'relief': 'flat',
    'width': 20,
    'pady': 10
}

# Style for listbox
listbox_style = {
    'font': ("Helvetica", 10),
    'bg': "#FFFFFF",
    'fg': "#34495E",
    'selectbackground': "#A1C4FD",
    'selectforeground': "#34495E"
}

# Create and place widgets
button_add = tk.Button(root, text="Add Contact", command=add_contact, **button_style)
button_view = tk.Button(root, text="View Contacts", command=view_contacts, **button_style)
button_search = tk.Button(root, text="Search Contact", command=search_contact, **button_style)
button_update = tk.Button(root, text="Update Contact", command=update_contact, **button_style)
button_delete = tk.Button(root, text="Delete Contact", command=delete_contact, **button_style)
contact_list = tk.Listbox(root, **listbox_style, width=80, height=10)

# Place the buttons and listbox in the grid
button_add.grid(row=0, column=0, padx=10, pady=10)
button_view.grid(row=0, column=1, padx=10, pady=10)
button_search.grid(row=0, column=2, padx=10, pady=10)
button_update.grid(row=1, column=0, padx=10, pady=10)
button_delete.grid(row=1, column=1, padx=10, pady=10)
contact_list.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Populate the contact list initially
update_contact_list()

# Run the application
root.mainloop()

# Close the contact storage when the program ends
contact_storage.close()


