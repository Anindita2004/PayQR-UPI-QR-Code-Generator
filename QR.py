import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox, ttk
#function to generate QR
def generate_qr():
    upi_id = upi_entry.get().strip()
    name = name_entry.get().strip()
    amount = amount_entry.get().strip()
    note = note_entry.get().strip()
#validation
    if not upi_id or not name or not amount:
        messagebox.showerror("Input Error", "Please fill in all required fields (*)")
        return

    try:
        payment_url = f'upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR&tn={note}'
        
        #create QR code
        qr = qrcode.QRCode(box_size=15, border=2)  #if u want to increse size of qr code box
        qr.add_data(payment_url)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color="black", back_color="white")
        #save and display
        img_qr.save("upi_qr.png")
        img_display = Image.open("upi_qr.png").resize((300, 300))  # if u want to increse size of display size
        img_tk = ImageTk.PhotoImage(img_display)
        
        qr_label.config(image=img_tk)
        qr_label.image = img_tk
        status_label.config(text="QR Code Generated Successfully!", foreground="green")
        
    except Exception as e:
        messagebox.showerror("System Error", f"An error occurred: {e}")

#all GUI hereee 
root = tk.Tk()
root.title("Professional UPI Generator")
root.geometry("450x750")  # if u want to increase window size
root.configure(bg="#ffffff")
style = ttk.Style()
style.configure("TButton", font=("Arial", 10, "bold"), padding=10)
style.configure("TLabel", background="#ffffff", font=("Arial", 10))

#header
header_frame = tk.Frame(root, bg="#4CAF50", height=80)
header_frame.pack(fill="x")
tk.Label(header_frame, text="UPI PAYMENTS",
         font=("Arial", 16, "bold"),
         bg="#4CAF50",
         fg="white").pack(pady=20)

#Main input container
main_frame = tk.Frame(root, bg="#ffffff", padx=30, pady=20)
main_frame.pack(fill="both", expand=True)

def create_input(label_text):
    lbl = ttk.Label(main_frame, text=label_text)
    lbl.pack(anchor="w", pady=(10, 2))
    entry = ttk.Entry(main_frame, width=40)
    entry.pack(fill="x", ipady=5)
    return entry

upi_entry = create_input("UPI ID (e.g., name@okaxis) *")
name_entry = create_input("Recipient Name *")
amount_entry = create_input("Amount (INR) *")
note_entry = create_input("Note (Optional)")
ttk.Label(main_frame, text="").pack() 
generate_btn = ttk.Button(main_frame,
                          text="GENERATE SECURE QR",
                          command=generate_qr)
generate_btn.pack(fill="x", pady=20)
#Display
qr_label = tk.Label(main_frame,
                    bg="#f9f9f9",
                    relief="groove",
                    bd=1)
qr_label.pack(pady=10, ipadx=10, ipady=10)

status_label = ttk.Label(main_frame,
                         text="Enter details and click generate",
                         font=("Arial", 9, "italic"))
status_label.pack()
root.mainloop()
