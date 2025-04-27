import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from PIL import Image, ImageTk
import os

# Main CRANEX App Class
class CranexApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRANEX - FOR LIFE")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)  # Fixed size for consistent look
        
        # In-memory data storage
        self.vitals_records = []
        self.symptoms_records = []
        self.chat_history = ["AI: Welcome! How can I assist you today?"]
        self.logged_in_user = None
        
        # Background image (default None, can be set later)
        self.bg_image = None
        
        # Start with login screen
        self.setup_login()

    # Setup Login Screen
    def setup_login(self):
        self.clear_window()
        self.login_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.login_frame.pack(fill="both", expand=True)
        
        # Gradient header for login
        header = tk.Label(self.login_frame, text="CRANEX - FOR LIFE", font=("Segoe UI", 28, "bold"),
                          bg="#1e90ff", fg="white", pady=20)
        header.pack(fill="x")
        
        # Login fields
        tk.Label(self.login_frame, text="Username", font=("Segoe UI", 14), bg="#f0f8ff").pack(pady=10)
        self.username_entry = tk.Entry(self.login_frame, font=("Segoe UI", 12), width=25)
        self.username_entry.pack()
        
        tk.Label(self.login_frame, text="Password", font=("Segoe UI", 14), bg="#f0f8ff").pack(pady=10)
        self.password_entry = tk.Entry(self.login_frame, show="*", font=("Segoe UI", 12), width=25)
        self.password_entry.pack()
        
        # Buttons with hover effect
        login_btn = self.create_styled_button("Login", self.login)
        login_btn.pack(pady=20)
        
        register_btn = self.create_styled_button("Register", self.register)
        register_btn.pack(pady=5)

    # Clear the window for new content
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Login Logic (basic placeholder)
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            self.logged_in_user = username
            self.setup_main_interface()
            messagebox.showinfo("Success", f"Welcome, {username}!")
        else:
            messagebox.showerror("Error", "Please enter username and password!")

    # Register Logic (basic placeholder)
    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            messagebox.showinfo("Success", "Registration successful! Please login.")
        else:
            messagebox.showerror("Error", "Please enter username and password!")

    # Setup Main Interface
    def setup_main_interface(self):
        self.clear_window()
        
        # Main frame with background image support
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)
        
        # Canvas for background image
        self.canvas = tk.Canvas(self.main_frame, width=1000, height=700)
        self.canvas.pack(fill="both", expand=True)
        self.set_default_background()  # Set default gradient or load image
        
        # Sidebar
        self.setup_sidebar()
        
        # Content area
        self.content_frame = tk.Frame(self.canvas, bg="white")
        self.canvas.create_window(300, 100, window=self.content_frame, anchor="nw")
        
        # Initial content (Vitals by default)
        self.show_vitals()

    # Set default background (gradient if no image)
    def set_default_background(self):
        if self.bg_image:
            self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        else:
            # Simple gradient effect
            for i in range(700):
                color = f"#{(255 - i//3):02x}{(206 - i//5):02x}{(235 - i//10):02x}"
                self.canvas.create_line(0, i, 1000, i, fill=color)

    # Load custom background image
    def load_background_image(self):
        try:
            file_path = tk.filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
            if file_path:
                img = Image.open(file_path)
                img = img.resize((1000, 700), Image.Resampling.LANCZOS)  # Resize to fit window
                self.bg_image = ImageTk.PhotoImage(img)
                self.canvas.delete("all")  # Clear previous background
                self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
                self.setup_sidebar()  # Redraw sidebar over new background
                self.content_frame.lift()  # Ensure content stays on top
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")

    # Setup Sidebar
    def setup_sidebar(self):
        self.sidebar = tk.Frame(self.canvas, bg="#e6f0ff", width=200, height=700)
        self.canvas.create_window(0, 0, window=self.sidebar, anchor="nw")
        
        # Sidebar header
        tk.Label(self.sidebar, text="Menu", font=("Segoe UI", 18, "bold"), bg="#1e90ff", fg="white",
                 width=200, pady=20).pack(fill="x")
        
        # Sidebar buttons
        options = [
            ("Vitals Tracking", self.show_vitals),
            ("Symptoms", self.show_symptoms),
            ("AI Chatbot", self.show_chatbot),
            ("Health Records", self.show_records),
            ("Consultation", self.show_consultation),
            ("Set Background", self.load_background_image)
        ]
        
        for text, command in options:
            btn = self.create_styled_button(text, command, bg="#e6f0ff", fg="#1e90ff")
            btn.pack(fill="x", pady=5, padx=10)

    # Create styled button with hover effect
    def create_styled_button(self, text, command, bg="#1e90ff", fg="white"):
        btn = tk.Button(self.root, text=text, command=command, font=("Segoe UI", 12, "bold"),
                        bg=bg, fg=fg, relief="flat", padx=10, pady=10)
        
        def on_enter(e):
            btn.config(bg="#4169e1" if bg == "#1e90ff" else "#d0e0ff")
        
        def on_leave(e):
            btn.config(bg=bg)
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        return btn

    # Show Vitals Panel
    def show_vitals(self):
        self.clear_content()
        self.content_frame.config(bg="white", width=700, height=550)
        
        tk.Label(self.content_frame, text="Track Your Vitals", font=("Segoe UI", 20, "bold"),
                 bg="white", fg="#1e90ff").pack(pady=10)
        
        fields_frame = tk.Frame(self.content_frame, bg="white")
        fields_frame.pack(pady=10)
        
        self.hr_entry = self.create_entry(fields_frame, "Heart Rate (bpm)", 0)
        self.bp_sys_entry = self.create_entry(fields_frame, "BP Systolic (mmHg)", 1)
        self.bp_dia_entry = self.create_entry(fields_frame, "BP Diastolic (mmHg)", 2)
        self.sugar_entry = self.create_entry(fields_frame, "Blood Sugar (mg/dL)", 3)
        self.temp_entry = self.create_entry(fields_frame, "Temperature (°C)", 4)
        
        submit_btn = self.create_styled_button("Submit Vitals", self.submit_vitals)
        submit_btn.pack(pady=20)

    # Create labeled entry field
    def create_entry(self, parent, label_text, row):
        tk.Label(parent, text=label_text, font=("Segoe UI", 12), bg="white").grid(row=row, column=0, padx=10, pady=5)
        entry = tk.Entry(parent, font=("Segoe UI", 12), width=20)
        entry.grid(row=row, column=1, padx=10, pady=5)
        return entry

    # Submit Vitals
    def submit_vitals(self):
        hr = self.hr_entry.get()
        bp_sys = self.bp_sys_entry.get()
        bp_dia = self.bp_dia_entry.get()
        sugar = self.sugar_entry.get()
        temp = self.temp_entry.get()
        record = f"HR: {hr} bpm, BP: {bp_sys}/{bp_dia} mmHg, Sugar: {sugar} mg/dL, Temp: {temp}°C"
        self.vitals_records.append(record)
        messagebox.showinfo("Vitals", f"Vitals recorded: {record}")

    # Show Symptoms Panel
    def show_symptoms(self):
        self.clear_content()
        self.content_frame.config(bg="white", width=700, height=550)
        
        tk.Label(self.content_frame, text="Log Your Symptoms", font=("Segoe UI", 20, "bold"),
                 bg="white", fg="#1e90ff").pack(pady=10)
        
        self.symptoms_area = scrolledtext.ScrolledText(self.content_frame, font=("Segoe UI", 12),
                                                       width=50, height=15, wrap=tk.WORD)
        self.symptoms_area.pack(pady=10)
        
        submit_btn = self.create_styled_button("Submit Symptoms", self.submit_symptoms)
        submit_btn.pack(pady=20)

    # Submit Symptoms
    def submit_symptoms(self):
        symptoms = self.symptoms_area.get("1.0", tk.END).strip()
        if symptoms:
            self.symptoms_records.append(symptoms)
            messagebox.showinfo("Symptoms", f"Symptoms logged: {symptoms}")
            self.symptoms_area.delete("1.0", tk.END)

    # Show Chatbot Panel
    def show_chatbot(self):
        self.clear_content()
        self.content_frame.config(bg="white", width=700, height=550)
        
        tk.Label(self.content_frame, text="CRANEX AI Chatbot", font=("Segoe UI", 20, "bold"),
                 bg="white", fg="#1e90ff").pack(pady=10)
        
        self.chat_display = scrolledtext.ScrolledText(self.content_frame, font=("Segoe UI", 12),
                                                      width=50, height=15, wrap=tk.WORD)
        self.chat_display.pack(pady=10)
        self.update_chat()
        
        self.chat_entry = tk.Entry(self.content_frame, font=("Segoe UI", 12), width=40)
        self.chat_entry.pack(pady=5)
        
        send_btn = self.create_styled_button("Send", self.send_chat)
        send_btn.pack(pady=10)

    # Send Chat Message
    def send_chat(self):
        message = self.chat_entry.get().strip()
        if message:
            self.chat_history.append(f"You: {message}")
            self.chat_history.append("AI: This is a basic response. How can I help?")
            self.update_chat()
            self.chat_entry.delete(0, tk.END)

    # Update Chat Display
    def update_chat(self):
        self.chat_display.delete("1.0", tk.END)
        for line in self.chat_history:
            self.chat_display.insert(tk.END, line + "\n")

    # Show Records Panel
    def show_records(self):
        self.clear_content()
        self.content_frame.config(bg="white", width=700, height=550)
        
        tk.Label(self.content_frame, text="Digital Health Records", font=("Segoe UI", 20, "bold"),
                 bg="white", fg="#1e90ff").pack(pady=10)
        
        self.records_display = scrolledtext.ScrolledText(self.content_frame, font=("Segoe UI", 12),
                                                         width=50, height=15, wrap=tk.WORD)
        self.records_display.pack(pady=10)
        self.update_records()
        
        refresh_btn = self.create_styled_button("Refresh Records", self.update_records)
        refresh_btn.pack(pady=20)

    # Update Records Display
    def update_records(self):
        self.records_display.delete("1.0", tk.END)
        self.records_display.insert(tk.END, "=== Vitals Records ===\n")
        for record in self.vitals_records:
            self.records_display.insert(tk.END, record + "\n")
        self.records_display.insert(tk.END, "\n=== Symptoms Records ===\n")
        for record in self.symptoms_records:
            self.records_display.insert(tk.END, record + "\n")

    # Show Consultation Panel
    def show_consultation(self):
        self.clear_content()
        self.content_frame.config(bg="white", width=700, height=550)
        
        tk.Label(self.content_frame, text="Request Doctor Consultation", font=("Segoe UI", 20, "bold"),
                 bg="white", fg="#1e90ff").pack(pady=10)
        
        self.consult_area = scrolledtext.ScrolledText(self.content_frame, font=("Segoe UI", 12),
                                                      width=50, height=15, wrap=tk.WORD)
        self.consult_area.pack(pady=10)
        
        submit_btn = self.create_styled_button("Submit Request", self.submit_consultation)
        submit_btn.pack(pady=20)

    # Submit Consultation Request
    def submit_consultation(self):
        request = self.consult_area.get("1.0", tk.END).strip()
        if request:
            messagebox.showinfo("Consultation", f"Request sent: {request}")
            self.consult_area.delete("1.0", tk.END)

    # Clear Content Frame
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

# Run the App
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = CranexApp(root)
        root.mainloop()
    except Exception as e:
        print(f"Error starting app: {e}")