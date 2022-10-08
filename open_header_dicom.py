from datetime import date

import pydicom, os


class OpenHeaderDicom:
    def __init__(self):
        self.anonnymate_date = str(date.today())

    def open_just_header(self, dicom_file):
        dataset = pydicom.read_file(dicom_file)

        return dataset

    def view_date(self, dataset):
        try:
            if int(dataset[(0x0008, 0x002a)].value[:4]) > 0:
                date_acquisition = dataset[(0x0008, 0x002a)].value
            else:
                date_acquisition = dataset[(0x0008, 0x0022)].value

        except:
            date_acquisition = dataset[(0x0008, 0x0022)].value


        year = int(date_acquisition[:4])
        month = int(date_acquisition[4:6])
        day = int(date_acquisition[6:8])

        return day, month, year

    def view_id(self, dataset):
        id_sub = str(dataset[(0x0010, 0x0020)].value)
        id_sub = id_sub.replace('-', '')
        return id_sub

    def view_image_type(self, dataset) -> str:
        modality = dataset[(0x0008, 0x0008)].value[2]
        return modality

    def view_study_description(self, dataset) -> str:
        modality = dataset[(0x0008, 0x1030)].value
        return modality

    def view_size_file(self, file):
        return os.stat(file).st_size
