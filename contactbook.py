from tkinter import *
from tkinter import messagebox

class ContactBook:
    def _init(self, root):  # fixed __init_
        self.root = root
        self.root.title("Contact Book (OOP Version)")
        self.root.geometry("550x530")
        self.root.config(bg="lightyellow")
        
        self.contacts = []
        
        self.country_codes = {
            "🇮🇳 +91": "+91",
            "🇺🇸 +1": "+1",
            "🇬🇧 +44": "+44",
            "🇨🇦 +1": "+1",
            "🇦🇺 +61": "+61",
            "🇩🇪 +49": "+49",
            "🇯🇵 +81": "+81",
            "🇨🇳 +86": "+86",
            "🇵🇰 +92": "+92",
            "🇮🇩 +62": "+62"
        }

        self.create_widgets()

    def create_widgets(self):
        Label(self.root, text="Name:", bg="lightyellow").place(x=30, y=30)
        self.name_entry = Entry(self.root, width=40)
        self.name_entry.place(x=100, y=30)

        Label(self.root, text="Phone:", bg="lightyellow").place(x=30, y=70)

        self.country_code_var = StringVar(self.root)
        self.country_code_var.set("🇮🇳 +91")
        OptionMenu(self.root, self.country_code_var, *self.country_codes.keys()).place(x=100, y=65)

        self.phone_entry = Entry(self.root, width=25)
        self.phone_entry.place(x=200, y=70)

        Label(self.root, text="Email:", bg="lightyellow").place(x=30, y=110)
        self.email_entry = Entry(self.root, width=40)
        self.email_entry.place(x=100, y=110)

        Button(self.root, text="Add Contact", width=15, command=self.add_contact).place(x=50, y=150)
        Button(self.root, text="Delete Selected", width=15, command=self.delete_contact).place(x=200, y=150)

        Label(self.root, text="Search Name:", bg="lightyellow").place(x=30, y=200)
        self.search_entry = Entry(self.root, width=25)
        self.search_entry.place(x=130, y=200)
        Button(self.root, text="Search", command=self.search_contact).place(x=320, y=197)

        self.contact_list = Listbox(self.root, width=70, height=15)
        self.contact_list.place(x=30, y=250)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        code = self.country_code_var.get()

        if name == "" or phone == "":
            messagebox.showwarning("Input Error", "Name and Phone are required!")
            return

        full_phone = f"{self.country_codes[code]} {phone}"
        self.contacts.append({'name': name, 'phone': full_phone, 'email': email})
        self.update_listbox()
        self.clear_entries()

    def update_listbox(self):
        self.contact_list.delete(0, END)
        for contact in self.contacts:
            self.contact_list.insert(END, f"{contact['name']} - {contact['phone']} - {contact['email']}")

    def clear_entries(self):
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)

    def search_contact(self):
        search_term = self.search_entry.get().strip().lower()
        self.contact_list.delete(0, END)
        for contact in self.contacts:
            if search_term in contact['name'].lower():
                self.contact_list.insert(END, f"{contact['name']} - {contact['phone']} - {contact['email']}")

    def delete_contact(self):
        selected = self.contact_list.curselection()
        if not selected:
            messagebox.showwarning("Delete Error", "No contact selected.")
            return
        index = selected[0]
        del self.contacts[index]
        self.update_listbox()

if _name_ == "_main":  # fixed __name_
    root = Tk()
    app = ContactBook(root)
    root.mainloop()
