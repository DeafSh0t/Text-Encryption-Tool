import code
import tkinter as tk
from tkinter import messagebox
import base64
import os
root = tk.Tk()

root.geometry("500x600")
root.title("Cryptographer")

code= tk.StringVar()
tk.Entry(textvariable=code,font=("arial",18),show="*")


def encrypt():
    message = textbox1.get("1.0", tk.END).strip()
    secret_key = textbox2.get("1.0", tk.END).strip()
    if not message or not secret_key:
        messagebox.showwarning("Input Error", "Please enter both message and secret key.")
        return
    
    encoded_chars = []
    for i in range(len(message)):
        key_c = secret_key[i % len(secret_key)]
        encoded_c = chr(ord(message[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = base64.urlsafe_b64encode("".join(encoded_chars).encode()).decode()
    
    textbox3.delete(1.0, tk.END)
    textbox3.insert(tk.END, encoded_string)

def decrypt():
    encoded_message = textbox1.get("1.0", tk.END).strip()
    secret_key = textbox2.get("1.0", tk.END).strip()
    if not encoded_message or not secret_key:
        messagebox.showwarning("Input Error", "Please enter both encoded message and secret key.")
        return
    
    decoded_message = base64.urlsafe_b64decode(encoded_message).decode()
    decoded_chars = []
    for i in range(len(decoded_message)):
        key_c = secret_key[i % len(secret_key)]
        decoded_c = chr((256 + ord(decoded_message[i]) - ord(key_c)) % 256)
        decoded_chars.append(decoded_c)
    decoded_string = "".join(decoded_chars)
    
    textbox3.delete(1.0, tk.END)
    textbox3.insert(tk.END, decoded_string)

def reset():
    textbox1.delete(1.0, tk.END)
    textbox2.delete(1.0, tk.END)
    textbox3.delete(1.0,tk.END)

#def swap():
 #textbox1.delete(1.0,tk.END)
 #textbox1.insert(tk.END,textbox3)
 

label = tk.Label (root,text="Enter text you want to Encrypt or Decrypt", font=('verdana', 16,))
label.pack (padx=5)

textbox1 = tk.Text(root, height=3,font=('arial',16))
textbox1.pack(padx=5,pady=5)

label = tk.Label (root,text="Enter secret key For Encyption or Decryption", font=('verdana', 16,))
label.pack (padx=5,pady=5)

textbox2 = tk.Text(root, height=1.5, font=('arial',16))
textbox2.pack(padx=5,pady=5)

button=tk.Button(root, text="Encypt", bg='red', font=('arial',18),command=encrypt)
button.pack(pady=5,padx=5)

button2=tk.Button(root, text="Decypt",bg='green', font=('arial',18),command=decrypt)
button2.pack(padx=5,pady=5)

button=tk.Button(root, text="Reset",bg='cyan', font=('arial',18),command=reset)
button.pack(padx=5,pady=5)

#button=tk.Button(root, text="Swap",bg='cyan', font=('arial',18), command=swap)
#button.pack(padx=5,pady=5)

label = tk.Label (root,text="Output", font=('verdana', 16,))
label.pack (padx=5,pady=5)

textbox3 = tk.Text(root, height=1.5, font=('arial',16))
textbox3.pack(padx=5,pady=5)




root.mainloop()


