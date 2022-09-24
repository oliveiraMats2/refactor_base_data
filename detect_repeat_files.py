from open_header_dicom import OpenHeaderDicom
from compare_files import CompareFiles
from unzip_files import UnzipFiles

absolut_path = 'data_test'
file_path_1 = f'{absolut_path}/2010-03-27-14-55-CLEONICE_AP__DE_SOUZA_ALENCAR-VVBM_6min_SENSE-ENH-0040'
file_path_2 = f'{absolut_path}/2010-03-29-13-26-DANIELA_ALVES_FERNANDES-Reg__DTI_high_iso20_SENSE-ENH-4620'
file_path_3 = f'{absolut_path}/2010-03-29-13-26-DANIELA_ALVES_FERNANDES-Reg__DTI_high_iso20_SENSE-ENH-4620 (cópia)'

open_header_dicom = OpenHeaderDicom()
compare_files = CompareFiles()
unzip_files = UnzipFiles()

#dataset = open_header_dicom.open_just_header(file_path_1)
unzip_files.open_zip_and_save()
unzip_files.open_dicom_and_save()
