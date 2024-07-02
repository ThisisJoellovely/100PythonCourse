import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking App")

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.watermark_entry = tk.Entry(root, width=40)
        self.watermark_entry.insert(0, "Enter watermark text")
        self.watermark_entry.pack(pady=10)

        self.add_watermark_button = tk.Button(root, text="Add Watermark", command=self.add_watermark)
        self.add_watermark_button.pack(pady=10)

        self.image_path = None
        self.watermarked_image = None

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            messagebox.showinfo("Image Upload", "Image uploaded successfully!")

    def add_watermark(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please upload an image first!")
            return

        watermark_text = self.watermark_entry.get()
        if not watermark_text or watermark_text == "Enter watermark text":
            messagebox.showerror("Error", "Please enter a valid watermark text!")
            return

        # Open the image
        with Image.open(self.image_path) as im:
            width, height = im.size
            draw = ImageDraw.Draw(im)

            # Use a truetype font
            try:
                font = ImageFont.truetype("arial.ttf", 36)
            except IOError:
                font = ImageFont.load_default()

            # Position the watermark at the bottom right corner
            text_width, text_height = draw.textsize(watermark_text, font)
            x = width - text_width - 10
            y = height - text_height - 10

            # Add the watermark
            draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))  # White text with opacity

            # Save the watermarked image
            self.watermarked_image = im.copy()
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
            if save_path:
                self.watermarked_image.save(save_path)
                messagebox.showinfo("Success", f"Watermarked image saved to {save_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
