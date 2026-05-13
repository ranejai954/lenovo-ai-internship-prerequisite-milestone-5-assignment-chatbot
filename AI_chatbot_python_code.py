import tkinter as tk
from tkinter import scrolledtext

def process_choice(choice):
    # Clear the text box before inserting new information
    chat_display.config(state=tk.NORMAL)
    chat_display.delete('1.0', tk.END)
    
    if choice == 1:
        output_text = (
            "==========================================\n"
            "📝 [ADMISSIONS INFO]:\n"
            "==========================================\n"
            "• Entry Criteria: Minimum aggregate of 60% in high school.\n"
            "• Fee Deadline: The portal closes on the 15th of next month.\n"
            "• Status: Portals open for registration."
        )
    elif choice == 2:
        output_text = (
            "==========================================\n"
            "🏢 [CAMPUS FACILITIES]:\n"
            "==========================================\n"
            "• Central Library: Open daily from 8:00 AM to 9:00 PM.\n"
            "• Hostels: Student blocks are located on the North and South wings.\n"
            "• Wi-Fi: Available across campus for registered students."
        )
    elif choice == 3:
        output_text = (
            "==========================================\n"
            "📞 [EMERGENCY CONTACTS]:\n"
            "==========================================\n"
            "• Administrative Helpline: Call 022-245678.\n"
            "• Medical Emergency: Dial extension 104 on campus.\n"
            "• Security Desk: Available 24/7 at the front gates."
        )
    elif choice == 4:
        output_text = (
            "==========================================\n"
            "👋 CHATBOT TERMINATED\n"
            "==========================================\n"
            "Thank you for using Campus Buddy! Have a great day ahead! 🚀"
        )
        # Disable buttons upon exiting the chat app
        btn1.config(state=tk.DISABLED)
        btn2.config(state=tk.DISABLED)
        btn3.config(state=tk.DISABLED)
        btn4.config(state=tk.DISABLED)
        
    chat_display.insert(tk.END, output_text)
    chat_display.config(state=tk.DISABLED)

# Initialize Window Layout
window = tk.Tk()
window.title("Campus Buddy AI Chatbot")
window.geometry("500x450")
window.configure(bg="#1e1e2e")

# Title Header
title_label = tk.Label(window, text="🎓 Campus Buddy Assistant", font=("Arial", 16, "bold"), bg="#1e1e2e", fg="#cdd6f4")
title_label.pack(pady=10)

# Welcome Sub-label
welcome_label = tk.Label(window, text="Hello! Click an option below to navigate your first days on campus.", font=("Arial", 10), bg="#1e1e2e", fg="#a6adc8")
welcome_label.pack(pady=5)

# Scrollable Output Display Panel
chat_display = scrolledtext.ScrolledText(window, width=55, height=12, font=("Courier New", 10), bg="#313244", fg="#a6e3a1", wrap=tk.WORD)
chat_display.insert(tk.END, "System Ready. Please select a panel below...")
chat_display.config(state=tk.DISABLED)
chat_display.pack(pady=10)

# Frame container for control options buttons
button_frame = tk.Frame(window, bg="#1e1e2e")
button_frame.pack(pady=10)

# Button Styling Array Configurations
btn_style = {"font": ("Arial", 10, "bold"), "bg": "#89b4fa", "fg": "#11111b", "width": 20, "pady": 5, "bd": 0, "activebackground": "#b4befe"}

btn1 = tk.Button(button_frame, text="1. Admissions Info", **btn_style, command=lambda: process_choice(1))
btn1.grid(row=0, column=0, padx=5, pady=5)

btn2 = tk.Button(button_frame, text="2. Campus Facilities", **btn_style, command=lambda: process_choice(2))
btn2.grid(row=0, column=1, padx=5, pady=5)

btn3 = tk.Button(button_frame, text="3. Emergency Contacts", **btn_style, command=lambda: process_choice(3))
btn3.grid(row=1, column=0, padx=5, pady=5)

btn4 = tk.Button(button_frame, text="4. Exit Assistant", font=("Arial", 10, "bold"), bg="#f38ba8", fg="#11111b", width=20, pady=5, bd=0, activebackground="#f5e0dc", command=lambda: process_choice(4))
btn4.grid(row=1, column=1, padx=5, pady=5)

# Keep application window operational
window.mainloop()
import tkinter as tk
from tkinter import scrolledtext

def process_choice(choice):
    # Clear the text box before inserting new information
    chat_display.config(state=tk.NORMAL)
    chat_display.delete('1.0', tk.END)
    
    if choice == 1:
        output_text = (
            "==========================================\n"
            "📝 [ADMISSIONS INFO]:\n"
            "==========================================\n"
            "• Entry Criteria: Minimum aggregate of 60% in high school.\n"
            "• Fee Deadline: The portal closes on the 15th of next month.\n"
            "• Status: Portals open for registration."
        )
    elif choice == 2:
        output_text = (
            "==========================================\n"
            "🏢 [CAMPUS FACILITIES]:\n"
            "==========================================\n"
            "• Central Library: Open daily from 8:00 AM to 9:00 PM.\n"
            "• Hostels: Student blocks are located on the North and South wings.\n"
            "• Wi-Fi: Available across campus for registered students."
        )
    elif choice == 3:
        output_text = (
            "==========================================\n"
            "📞 [EMERGENCY CONTACTS]:\n"
            "==========================================\n"
            "• Administrative Helpline: Call 022-245678.\n"
            "• Medical Emergency: Dial extension 104 on campus.\n"
            "• Security Desk: Available 24/7 at the front gates."
        )
    elif choice == 4:
        output_text = (
            "==========================================\n"
            "👋 CHATBOT TERMINATED\n"
            "==========================================\n"
            "Thank you for using Campus Buddy! Have a great day ahead! 🚀"
        )
        # Disable buttons upon exiting the chat app
        btn1.config(state=tk.DISABLED)
        btn2.config(state=tk.DISABLED)
        btn3.config(state=tk.DISABLED)
        btn4.config(state=tk.DISABLED)
        
    chat_display.insert(tk.END, output_text)
    chat_display.config(state=tk.DISABLED)

# Initialize Window Layout
window = tk.Tk()
window.title("Campus Buddy AI Chatbot")
window.geometry("500x450")
window.configure(bg="#1e1e2e")

# Title Header
title_label = tk.Label(window, text="🎓 Campus Buddy Assistant", font=("Arial", 16, "bold"), bg="#1e1e2e", fg="#cdd6f4")
title_label.pack(pady=10)

# Welcome Sub-label
welcome_label = tk.Label(window, text="Hello! Click an option below to navigate your first days on campus.", font=("Arial", 10), bg="#1e1e2e", fg="#a6adc8")
welcome_label.pack(pady=5)

# Scrollable Output Display Panel
chat_display = scrolledtext.ScrolledText(window, width=55, height=12, font=("Courier New", 10), bg="#313244", fg="#a6e3a1", wrap=tk.WORD)
chat_display.insert(tk.END, "System Ready. Please select a panel below...")
chat_display.config(state=tk.DISABLED)
chat_display.pack(pady=10)

# Frame container for control options buttons
button_frame = tk.Frame(window, bg="#1e1e2e")
button_frame.pack(pady=10)

# Button Styling Array Configurations
btn_style = {"font": ("Arial", 10, "bold"), "bg": "#89b4fa", "fg": "#11111b", "width": 20, "pady": 5, "bd": 0, "activebackground": "#b4befe"}

btn1 = tk.Button(button_frame, text="1. Admissions Info", **btn_style, command=lambda: process_choice(1))
btn1.grid(row=0, column=0, padx=5, pady=5)

btn2 = tk.Button(button_frame, text="2. Campus Facilities", **btn_style, command=lambda: process_choice(2))
btn2.grid(row=0, column=1, padx=5, pady=5)

btn3 = tk.Button(button_frame, text="3. Emergency Contacts", **btn_style, command=lambda: process_choice(3))
btn3.grid(row=1, column=0, padx=5, pady=5)

btn4 = tk.Button(button_frame, text="4. Exit Assistant", font=("Arial", 10, "bold"), bg="#f38ba8", fg="#11111b", width=20, pady=5, bd=0, activebackground="#f5e0dc", command=lambda: process_choice(4))
btn4.grid(row=1, column=1, padx=5, pady=5)

# Keep application window operational
window.mainloop()
