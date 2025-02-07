from pyostie.parsers import *
from pyostie.insights_ext import *
from pyostie.convert import *
from pyostie.utils import *


class extract:

    def __init__(self, filename, insights=False, tess_path=None, extension=None):
        """
        :param filename:
        :param insights:
        :param tess_path:
        :param extension:

        :return:
        """
        self.file = filename
        self.insights = insights
        self.path = tess_path
        self.ext = extension

    # noinspection PyBroadException
    def start(self):
        """

        :return: Main function to start the process.
        """
        @extension_type_check(self.ext, str)
        def ext_type_check(extnsn):
            return extnsn
        ext = ext_type_check(self.ext)
        print(ext)

        if ext.upper() == "PDF":
            if isinstance(self.file, str):
                try:
                    pdf = PDFParser(self.file, insights=self.insights)
                    output = pdf.extract_pypdf2()
                    return output
                except Exception:
                    try:
                        pdf = PDFParser(self.file)
                        output = pdf.extract_pdfplumber()
                        return output
                    except Exception as ex:
                        raise ex

        elif ext == "CSV":
            if isinstance(self.file, str):
                csv_output = CSVParser(self.file)
                output = csv_output.extract_csv()
                return output

        elif ext == "TXT":
            if isinstance(self.file, str):
                txt = TXTParser(self.file)
                output = txt.extract_txt()
                return output

        elif ext == "XLSX":
            if isinstance(self.file, str):
                excel = XLSXParser(self.file)
                output = excel.extract_xlsx()
                return output

        elif ext == "DOCX":
            if isinstance(self.file, str):
                docx = DOCXParser(self.file)
                output = docx.extract_docx()
                return output

        elif ext == "JPG":
            if self.insights:
                image = generate_insights(self.file, df)
                output_df = image.generate_df()
                image = ImageParser(self.file)
                output = image.extract_image()
                return output_df, output

            elif not self.insights:
                image = ImageParser(self.file)
                output = image.extract_image()
                return output

        elif ext == "PPTX":
            pptx = PPTXParser(self.file)
            output = pptx.extract_pptx()
            return output
