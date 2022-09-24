from open_header_dicom import OpenHeaderDicom

class CompareFiles:
    def __init__(self):
        self.open_header_dicom = OpenHeaderDicom()

    def compare_two_files(self, file_1, file_2):
        data_1 = self.open_header_dicom.open_just_header(file_1)
        data_2 = self.open_header_dicom.open_just_header(file_2)

        info_1 = (self.open_header_dicom.view_date(data_1),
                  self.open_header_dicom.view_id(data_1))

        info_2 = (self.open_header_dicom.view_date(data_2),
                  self.open_header_dicom.view_id(data_2))

        if info_1 == info_2:
            print(info_1)
            print(info_2)

