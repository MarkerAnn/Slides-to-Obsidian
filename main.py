import os
from pathlib import Path
import fitz  # PyMuPDF
from PIL import Image
import re


class PDFProcessor:
    def process_pdf(self, pdf_path, output_dir):
        """Process all slides in the PDF"""
        print("\nProcessing PDF slides...")
        processed_slides = []

        try:
            pdf_document = fitz.open(pdf_path)

            for page_num in range(len(pdf_document)):
                page = pdf_document[page_num]

                # Get slide number or section number
                page_text = page.get_text()
                slide_number = self._extract_slide_number(page_text, page_num + 1)

                # Get page dimensions
                zoom = 4  # higher zoom for better quality
                mat = fitz.Matrix(zoom, zoom)
                rect = page.rect  # page rectangle

                # Create high-quality image from page
                pix = page.get_pixmap(matrix=mat, alpha=False)

                # Convert to PIL Image
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                # Save image with high quality
                image_filename = f"slide_{slide_number}.png"
                image_path = os.path.join(output_dir, image_filename)
                img.save(image_path, "PNG", quality=100, optimize=False)

                processed_slides.append((image_path, slide_number))
                print(f"Processed slide {slide_number}")

            pdf_document.close()
            return sorted(processed_slides, key=lambda x: self._sort_key(x[1]))

        except Exception as e:
            raise Exception(f"Error processing PDF: {str(e)}")

    def _extract_slide_number(self, page_text, default_num):
        """Extract slide number from page text or section number"""
        section_match = re.search(r"\d+\.\d+", page_text)
        if section_match:
            return section_match.group(0)
        return str(default_num)

    def _sort_key(self, slide_num):
        """Create sort key for slide numbers"""
        parts = slide_num.split(".")
        if len(parts) == 2:
            return (int(parts[0]), int(parts[1]))
        return (int(parts[0]), 0)


class FileManager:
    def setup_image_directory(self, images_base_path, folder_name):
        """Create directory for images"""
        image_dir = Path(images_base_path) / folder_name
        image_dir.mkdir(parents=True, exist_ok=True)
        return str(image_dir)

    def create_note_file(self, notes_path, note_name):
        """Create note file at specified path"""
        note_path = Path(notes_path) / f"{note_name}.md"
        note_path.parent.mkdir(parents=True, exist_ok=True)
        note_path.touch()
        return str(note_path)


def main():
    print("Welcome to the PDF to Markdown Converter!")

    # Get user inputs
    notes_path = input("Enter the path where the note file should be saved: ").strip()
    note_name = input("Enter the name for the note file (without .md): ").strip()
    images_base_path = input(
        "Enter the base path where images should be stored: "
    ).strip()
    image_folder_name = input("Enter the name for the images folder: ").strip()
    pdf_path = input("Enter the path to your PDF file: ").strip()

    # Remove quotes if present in paths
    notes_path = notes_path.strip("\"'")
    images_base_path = images_base_path.strip("\"'")
    pdf_path = pdf_path.strip("\"'")

    # Initialize classes
    file_manager = FileManager()
    pdf_processor = PDFProcessor()

    try:
        # Validate PDF exists
        if not os.path.exists(pdf_path):
            raise ValueError(f"PDF file not found: {pdf_path}")

        # Setup image directory
        print("\nSetting up image directory...")
        images_dir = file_manager.setup_image_directory(
            images_base_path, image_folder_name
        )
        print(f"Created image directory at: {images_dir}")

        # Process all slides from PDF
        slides = pdf_processor.process_pdf(pdf_path, images_dir)

        if not slides:
            raise ValueError(
                "No slides were processed from the PDF. Please check the PDF file."
            )

        print(f"\nProcessed {len(slides)} slides from PDF")

        # Create note file
        note_path = file_manager.create_note_file(notes_path, note_name)
        print(f"\nCreated note file at: {note_path}")

        # Write markdown file with images and headers
        print("\nCreating markdown file...")
        with open(note_path, "w", encoding="utf-8") as note_file:
            for image_path, slide_number in slides:
                # Add header
                note_file.write(f"### Slide {slide_number}\n\n")

                # Add image reference
                note_file.write(f"![[{os.path.basename(image_path)}]]\n\n")

                # Add extra space for notes
                note_file.write("\n\n\n")

        print("\nProcess completed successfully!")
        print(f"Images saved in: {images_dir}")
        print(f"Note file created at: {note_path}")

    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
