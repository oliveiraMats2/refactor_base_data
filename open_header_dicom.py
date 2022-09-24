from datetime import date

import pydicom


class OpenHeaderDicom:
    def __init__(self):
        self.anonnymate_date = str(date.today())

    def open_just_header(self, dicom_file):
        dataset = pydicom.read_file(dicom_file)

        if int(dataset[(0x0008, 0x002a)].value[:4]) > 0:
            date_acquisition = dataset[(0x0008, 0x002a)].value
        else:
            date_acquisition = dataset[(0x0008, 0x0022)].value

        return date_acquisition, dataset

    def view_date(self, data_acquisition):

        year = int(data_acquisition[:4])
        month = int(data_acquisition[4:6])
        day = int(data_acquisition[6:8])

        date_acquisition2 = date(year,
                                 month,
                                 day)
        return date_acquisition2

    def view_id(self, data_acquisition):
        id_sub = str(data_acquisition[(0x0010, 0x0020)].value)
        id_sub = id_sub.replace('-', '')
        return id_sub


if __name__ == '__main__':
    absolut_path = 'data_test'
    file_path = '2010-03-27-14-55-CLEONICE_AP__DE_SOUZA_ALENCAR-VVBM_6min_SENSE-ENH-0040'
    open_header_dicom = OpenHeaderDicom()
    date_acquisition, dataset = open_header_dicom.open_just_header(f'{absolut_path}/{file_path}')

    print(open_header_dicom.view_date(date_acquisition))
    print(open_header_dicom.view_id(dataset))
