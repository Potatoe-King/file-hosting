import os
import qrcode
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox

def generate_qr_code(file_url, save_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(file_url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(save_path)
    messagebox.showinfo("Success", f"QR Code saved as {save_path}")

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = os.path.basename(file_path)
        file_url = f"https://your-username.github.io/repository-name/{file_name}"
        
        # Generate QR code
        qr_save_path = f"{file_name}.png"
        generate_qr_code(file_url, qr_save_path)

def main():
    root = Tk()
    root.title("QR Code Generator for GitHub Pages")

    Label(root, text="Upload File to GitHub Pages and Generate QR Code").pack(pady=10)
    Button(root, text="Upload File", command=upload_file).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
