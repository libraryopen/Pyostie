import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # Here is the module name.
    name="Pyostie",

    # version of the module
    version="1.0",

    # Name of Author
    author="Anirudh Palaparthi",

    # your Email address
    author_email="anirudhpalaparthi@gmail.com",

    # Small Description about module
    description="A python package to OCR data and extract text with insights too.",

    long_description=long_description,

    # Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",

    # Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/anirudhpnbb/Pyostie",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["cv2", "numpy", "pandas", "PyPDF2", "pdfplumber", "xlrd", "docx2text", "pytesseract", "PIL"],
    # classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
