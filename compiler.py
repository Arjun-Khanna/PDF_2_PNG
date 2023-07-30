import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_png_to_pdf(input_folder, output_pdf=None):
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]

    if not image_files:
        print("No PNG files found in the input folder.")
        return

    temp_image_files = []
    images = []
    for file in image_files:
        image_path = os.path.join(input_folder, file)
        temp_image_files.append(image_path)
        images.append(Image.open(image_path))

    c = canvas.Canvas(output_pdf, pagesize=letter) if output_pdf else canvas.Canvas(pagesize=letter)
    for image, image_path in zip(images, temp_image_files):
        img_width, img_height = image.size
        aspect_ratio = img_width / img_height

        
        pdf_width, pdf_height = 500, 500 / aspect_ratio

        c.drawImage(image_path, 50, 750 - pdf_height, width=pdf_width, height=pdf_height)
        c.showPage()

    c.save()

    # Close all opened images
    for image in images:
        image.close()

    if output_pdf:
        print(f"PDF file '{output_pdf}' created successfully.")
    else:
        print("PDF file created successfully.")

if __name__ == "__main__":
    # Set the input folder path
    input_folder = r"C:\Users\Arjun Khanna\Desktop\Berserk\Berserk v03 (2004) (Digital) (Cyborgzx-repack)"  # Replace with the path to your folder containing PNG files

    # Set the output PDF path
    output_pdf = r"C:\Users\Arjun Khanna\Desktop\Berserk\Berserk v03 (2004) (Digital) (Cyborgzx-repack)\output.pdf"  # Replace with the desired output PDF filename or set to None

    convert_png_to_pdf(input_folder, output_pdf)
