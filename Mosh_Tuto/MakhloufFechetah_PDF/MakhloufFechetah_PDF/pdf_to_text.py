# ==============================
# DOCSTRINGS
# ==============================

# A docstring is a special string used to document:
# - functions
# - classes
# - modules
#
# It is written using triple quotes:
# """ """
#
# Docstrings explain:
# - what the code does
# - parameters
# - return values
# - usage

class PDFConverter:
    """
    A class used for PDF conversions.

    Supports:
    - PDF to text
    - PDF to images
    """

    def convert(pdf_path, output_path=None):
        """
        Extract text from a PDF file.

        Parameters:
            pdf_path (str):
                Path to the PDF file.

            output_path (str, optional):
                Path where the extracted text
                will be saved.

        Returns:
            str:
                Extracted text from the PDF.

        Raises:
            FileNotFoundError:
                If the PDF file does not exist.

        Example:
            pdf_to_text("book.pdf", "book.txt")
        """

        # Example processing
        extracted_text = "Example PDF text"

        # Save extracted text if output path exists
        if output_path:
            with open(output_path, "w") as file:
                file.write(extracted_text)

        # Return extracted text
        return extracted_text


# ==============================
# BEST PRACTICES
# ==============================

# Good docstrings should:
# - be clear
# - explain purpose
# - explain parameters
# - explain return values
# - include examples for complex functions


# ==============================
# COMMON CONVENTION
# ==============================

# Most Python developers use:
#
# Google Style
# or
# NumPy Style
#
# for writing professional docstrings
