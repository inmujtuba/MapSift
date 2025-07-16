import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import re
import pandas as pd

class DataExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MapSift")
        self.root.configure(bg="orange")

        # Make the window resizable
        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)

        # Heading
        heading = tk.Label(root, text="MapSift", font=("Georgia", 20, "bold"), bg="orange", fg="black")
        heading.grid(row=0, column=0, pady=10, sticky="n")

        # Text area for raw data (smaller height)
        self.text_area = tk.Text(root, wrap=tk.WORD, height=12, width=100, bg="#FFD580", fg="black", font=("Trebuchet MS", 11))
        self.text_area.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        # Buttons
        frame = tk.Frame(root, bg="orange")
        frame.grid(row=2, column=0, pady=5, sticky="ew")

        self.process_btn = tk.Button(
            frame,
            text="Process Data",
            command=self.process_data,
            bg="red",
            fg="white",
            font=("Trebuchet MS", 10, "bold")
        )
        self.process_btn.pack(side=tk.LEFT, padx=5)

        self.export_btn = tk.Button(
            frame,
            text="Export to Excel",
            command=self.export_excel,
            state=tk.DISABLED,
            bg="red",
            fg="white",
            font=("Trebuchet MS", 10, "bold")
        )
        self.export_btn.pack(side=tk.LEFT, padx=5)

        # Treeview to display results (default styling)
        self.tree = ttk.Treeview(
            root,
            columns=("Name", "Address", "Phone"),
            show="headings"
        )
        self.tree.heading("Name", text="Company Name", anchor="w")
        self.tree.heading("Address", text="Address", anchor="w")
        self.tree.heading("Phone", text="Phone Number", anchor="w")
        self.tree.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        # Allow Treeview to expand
        self.root.rowconfigure(3, weight=1)

        self.data = []

    def process_data(self):
        raw_text = self.text_area.get("1.0", tk.END)
        lines = raw_text.strip().split("\n")

        results = []
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line and i + 1 < len(lines) and re.search(r"\(\d+\)", lines[i + 1]):
                name = line
                j = i + 2
                address = ""
                while j < len(lines):
                    addr_line = lines[j].strip()
                    if addr_line:
                        address = addr_line
                        break
                    j += 1
                phone = ""
                for k in range(j, min(j + 10, len(lines))):
                    phone_match = re.search(r"(\+?\d[\d\s\-\(\)]{6,})", lines[k])
                    if phone_match:
                        raw_phone = phone_match.group(1).strip()
                        digits = re.sub(r"\D", "", raw_phone)
                        if raw_phone.startswith("+"):
                            cc_match = re.match(r"\+(\d+)", raw_phone)
                            if cc_match:
                                cc = cc_match.group(1)
                                rest_digits = digits[len(cc):]
                                phone = cc + rest_digits
                            else:
                                phone = digits
                        else:
                            phone = digits
                        break
                results.append((name, address, phone))
                i = j + 1
            else:
                i += 1

        for row in self.tree.get_children():
            self.tree.delete(row)

        for item in results:
            self.tree.insert("", tk.END, values=item)

        self.data = results

        if results:
            self.export_btn.config(state=tk.NORMAL)
            messagebox.showinfo("Success", f"Extracted {len(results)} records.")
        else:
            messagebox.showwarning("No Data", "No companies found in the input.")

    def export_excel(self):
        if not self.data:
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                 filetypes=[("Excel Files", "*.xlsx")])
        if file_path:
            df = pd.DataFrame(self.data, columns=["Company Name", "Address", "Phone Number"])
            df.to_excel(file_path, index=False)
            messagebox.showinfo("Exported", f"Data exported to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataExtractorApp(root)
    root.mainloop()
