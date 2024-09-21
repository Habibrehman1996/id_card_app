import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageOps

# Function to generate ID card
def generate_id_card():
    name = entry_name.get()
    roll_no = entry_roll_no.get()
    distance_learning = entry_distance_learning.get()
    city = entry_city.get()
    center = entry_center.get()
    campus = entry_campus.get()
    time = entry_time.get()
    batch = entry_batch.get()

    if not name or not roll_no or not distance_learning or not city or not center or not campus or not time or not batch or not img_path:
        messagebox.showerror("Error", "All fields and image must be provided")
        return

    # Create a blank ID card template
    card = Image.new('RGBA', (600, 350), color=(255, 255, 255, 255))  # RGBA for transparency
    draw = ImageDraw.Draw(card)

    # Load fonts
    font_title = ImageFont.truetype("arial.ttf", 24)
    font_normal = ImageFont.truetype("arial.ttf", 18)
    font_small = ImageFont.truetype("arial.ttf", 14)

    # Load and add watermark image
    watermark = Image.open("piaic logo.png").convert("RGBA")  # Make sure you have this image
    watermark = watermark.resize((300, 300))  # Resize watermark if necessary

    # Make watermark semi-transparent
    watermark_with_transparency = Image.new('RGBA', watermark.size)
    for x in range(watermark.width):
        for y in range(watermark.height):
            r, g, b, a = watermark.getpixel((x, y))
            watermark_with_transparency.putpixel((x, y), (r, g, b, int(a * 0.2)))  # Adjust alpha for transparency

    # Paste watermark on the card (centered and semi-transparent)
    card.alpha_composite(watermark_with_transparency, (150, 25))

    # Add the green header line
    draw.line((0, 10, 600, 10), fill=(0, 128, 0), width=4)

    # Add the ID card title
    draw.text((20, 20), "ID CARD", fill=(0, 128, 0), font=font_title)

    # Add text fields (labels in green)
    draw.text((20, 60), "Name:", fill=(0, 128, 0), font=font_normal)
    draw.text((20, 90), "Roll No:", fill=(0, 128, 0), font=font_normal)
    draw.text((20, 120), "Distance learning:", fill=(0, 128, 0), font=font_normal)
    draw.text((20, 150), "City:", fill=(0, 128, 0), font=font_normal)
    draw.text((20, 180), "Center:", fill=(0, 128, 0), font=font_normal)
    draw.text((20, 210), "Campus:", fill=(0, 128, 0), font=font_normal)
    draw.text((20, 240), "Days / Time:", fill=(0, 128, 0), font=font_normal)
    draw.text((20, 270), "Batch:", fill=(0, 128, 0), font=font_normal)

    # Add provided data (in black)
    draw.text((120, 60), name, fill="black", font=font_normal)
    draw.text((120, 90), roll_no, fill="black", font=font_normal)
    draw.text((180, 120), distance_learning, fill="black", font=font_normal)
    draw.text((80, 150), city, fill="black", font=font_normal)
    draw.text((100, 180), center, fill="black", font=font_normal)
    draw.text((100, 210), campus, fill="black", font=font_normal)
    draw.text((120, 240), time, fill="black", font=font_normal)
    draw.text((80, 270), batch, fill="black", font=font_normal)

    # Add the uploaded image (resized to fit)
    img = Image.open(img_path)
    img = img.resize((120, 140))
    card.paste(img, (450, 60))  # Adjusted position

    # Adjust the signature area (line and text slightly down)
    draw.line((450, 290, 580, 290), fill="black", width=2)  # Adjusted Y position for line
    draw.text((450, 300), "Authorized Signature", fill=(0, 128, 0), font=font_small)  # Adjusted Y position for text

    # Add bottom colored bars with text
    draw.rectangle([(20, 300), (100, 330)], fill=(255, 0, 0))  # Red bar
    draw.text((40, 305), "Q1", fill="white", font=font_normal)  # Add "Q1" in the red box

    draw.rectangle([(100, 300), (180, 330)], fill=(0, 255, 0))  # Green bar
    draw.text((120, 305), "WMD", fill="white", font=font_normal)  # Add "WMD" in the green box

    # Save the card (convert to RGB before saving as PNG doesn't need alpha)
    final_card = card.convert("RGB")
    final_card.save(f'{name}_id_card.png')

    messagebox.showinfo("Success", f"ID card for {name} generated successfully!")

# Function to upload image
def upload_image():
    global img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
    if img_path:
        label_image.config(text="Image Uploaded")

# GUI setup
root = tk.Tk()
root.title("ID Card Generator")
root.geometry("400x500")

# Labels and entry fields
label_name = tk.Label(root, text="Name:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_roll_no = tk.Label(root, text="Roll No:")
label_roll_no.pack()
entry_roll_no = tk.Entry(root)
entry_roll_no.pack()

label_distance_learning = tk.Label(root, text="Distance Learning:")
label_distance_learning.pack()
entry_distance_learning = tk.Entry(root)
entry_distance_learning.pack()

label_city = tk.Label(root, text="City:")
label_city.pack()
entry_city = tk.Entry(root)
entry_city.pack()

label_center = tk.Label(root, text="Center:")
label_center.pack()
entry_center = tk.Entry(root)
entry_center.pack()

label_campus = tk.Label(root, text="Campus:")
label_campus.pack()
entry_campus = tk.Entry(root)
entry_campus.pack()

label_time = tk.Label(root, text="Days / Time:")
label_time.pack()
entry_time = tk.Entry(root)
entry_time.pack()

label_batch = tk.Label(root, text="Batch:")
label_batch.pack()
entry_batch = tk.Entry(root)
entry_batch.pack()

# Button to upload image
label_image = tk.Label(root, text="Upload Image:")
label_image.pack()
button_upload = tk.Button(root, text="Upload Image", command=upload_image)
button_upload.pack()

# Button to generate ID card
button_generate = tk.Button(root, text="Generate ID Card", command=generate_id_card)
button_generate.pack()

img_path = None  # Global variable to store image path

root.mainloop()
