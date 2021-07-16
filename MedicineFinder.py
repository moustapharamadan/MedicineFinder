from tkinter import *
from MedicineFinderDatabase import createTable, dbSubmit, dbQuery, dbUpdate, dbDelete


def submitClick(medicineNameText, medicineDetailsText, fullNameText, addressText, phoneNumberText):
    dbSubmit(medicineNameText.get(), medicineDetailsText.get(),
             fullNameText.get(), addressText.get(), phoneNumberText.get())
    medicineNameText.delete(0, END)
    medicineDetailsText.delete(0, END)
    fullNameText.delete(0, END)
    addressText.delete(0, END)
    phoneNumberText.delete(0, END)


def deleteClick(editDeleteIdText):
    recordId = editDeleteIdText.get()
    records = dbQuery(recordId)
    if(len(records) == 0):
        return
    dbDelete(recordId)
    editDeleteIdText.delete(0, END)


def edit(editDeleteIdText):
    record_id = editDeleteIdText.get()
    records = dbQuery(record_id)
    if(len(records) != 1):
        return

    editor = Tk()
    editor.title('Update A Record')
    editor.geometry("400x300")

    # Create Text Boxes
    medicineNameText_editor = Entry(editor, width=30)
    medicineNameText_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    medicineDetailsText_editor = Entry(editor, width=30)
    medicineDetailsText_editor.grid(row=1, column=1)
    fullNameText_editor = Entry(editor, width=30)
    fullNameText_editor.grid(row=2, column=1)
    addressText_editor = Entry(editor, width=30)
    addressText_editor.grid(row=3, column=1)
    phoneNumberText_editor = Entry(editor, width=30)
    phoneNumberText_editor.grid(row=4, column=1)

    # Create Text Box Labels
    medicineNameLabel_editor = Label(editor, text="Medicine Name")
    medicineNameLabel_editor.grid(row=0, column=0, pady=(10, 0))
    medicineDetailsLabel_editor = Label(editor, text="Medicine Details")
    medicineDetailsLabel_editor.grid(row=1, column=0)
    fullNameLabel_editor = Label(editor, text="Full Name")
    fullNameLabel_editor.grid(row=2, column=0)
    addressLabel_editor = Label(editor, text="Address")
    addressLabel_editor.grid(row=3, column=0)
    phoneNumberLabel_editor = Label(editor, text="Phone Number")
    phoneNumberLabel_editor.grid(row=4, column=0)

    # Loop thru results
    for record in records:
        medicineNameText_editor.insert(0, record[0])
        medicineDetailsText_editor.insert(0, record[1])
        fullNameText_editor.insert(0, record[2])
        addressText_editor.insert(0, record[3])
        phoneNumberText_editor.insert(0, record[4])

    def updateClick(editDeleteIdText):
        dbUpdate(medicineNameText_editor.get(), medicineDetailsText_editor.get(),
                 fullNameText_editor.get(), addressText_editor.get(), phoneNumberText_editor.get(), editDeleteIdText.get())
        editor.destroy()
        editDeleteIdText.delete(0, END)
    # Create a Save Button To Save edited record
    edit_btn = Button(editor, text="Save Record",
                      command=lambda: updateClick(editDeleteIdText))
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)


def queryClick(recordTable):
    for widget in recordTable.winfo_children():
        widget.destroy()
    records = dbQuery()
    Table(recordTable, records)


class Table:
    def __init__(self, rootWindow, records):
        recordList = [('Medicine Name', 'Medicine Details',
                      'Full Name', 'Address', 'Phone Number', 'ID')]
        recordList += records
        for i in range(len(recordList)):
            for j in range(len(recordList[i])):
                self.e = Label(rootWindow, text=recordList[i][j])
                self.e.grid(row=i, column=j)


def main():
    createTable()

    root = Tk()
    root.title('Medicine Request')
    root.geometry("400x600")
    # Create Text Boxes
    medicineNameText = Entry(root, width=30)
    medicineNameText.grid(row=0, column=1, padx=20, pady=(10, 0))
    medicineDetailsText = Entry(root, width=30)
    medicineDetailsText.grid(row=1, column=1)
    fullNameText = Entry(root, width=30)
    fullNameText.grid(row=2, column=1)
    addressText = Entry(root, width=30)
    addressText.grid(row=3, column=1)
    phoneNumberText = Entry(root, width=30)
    phoneNumberText.grid(row=4, column=1)
    editDeleteIdText = Entry(root, width=30)
    editDeleteIdText.grid(row=9, column=1, pady=5)

    # Create Text Box Labels
    medicineNameLabel = Label(root, text="Medicine Name")
    medicineNameLabel.grid(row=0, column=0, pady=(10, 0))
    medicineDetailsLabel = Label(root, text="Medicine Details")
    medicineDetailsLabel.grid(row=1, column=0)
    fullNameLabel = Label(root, text="Full Name")
    fullNameLabel.grid(row=2, column=0)
    addressLabel = Label(root, text="Address")
    addressLabel.grid(row=3, column=0)
    phoneNumberLabel = Label(root, text="Phone Number")
    phoneNumberLabel.grid(row=4, column=0)
    editDeleteIdLabel = Label(root, text="Select ID")
    editDeleteIdLabel.grid(row=9, column=0, pady=5)

    # Create Submit Button
    submit_btn = Button(root, text="Submit",
                        command=lambda: submitClick(medicineNameText, medicineDetailsText, fullNameText, addressText, phoneNumberText))
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # Create a Query Button
    record_table = Frame(root)
    record_table.grid(row=12, columnspan=3)
    query_btn = Button(root, text="Show Records",
                       command=lambda: queryClick(record_table))
    query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    # Create A Delete Button
    delete_btn = Button(root, text="Delete Record",
                        command=lambda: deleteClick(editDeleteIdText))
    delete_btn.grid(row=10, column=0, columnspan=2,
                    pady=10, padx=10, ipadx=136)

    # Create an Update Button
    edit_btn = Button(root, text="Edit Record",
                      command=lambda: edit(editDeleteIdText))
    edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

    root.mainloop()


if __name__ == '__main__':
    main()
