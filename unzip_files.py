import zipfile
import os
from open_header_dicom import OpenHeaderDicom
from tqdm import tqdm
import pandas as pd


class UnzipFiles:
    def __init__(self):
        self.open_header_dicom = OpenHeaderDicom()
        self.dict_data_frame = {'name_file_zip': [],
                                'name_file_in_zip': [],
                                'size_file': [],
                                'date': [],
                                'id': [],
                                'image_type': []}

    def unzip_file(self, path_to_zip_file, directory_to_extract_to='/media/miclab/35c55d58-b4bf-4acf-a411-306032b6ca77/Originais/tmp_zip/'):
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall(directory_to_extract_to)

    def open_dicom_and_save(self, dir_data='/media/miclab/35c55d58-b4bf-4acf-a411-306032b6ca77/Originais/'):
        list_dir_data = os.listdir(dir_data)
        list_dir_data_filter = [x for x in list_dir_data if '.zip' not in x]

        for file_dicom in tqdm(list_dir_data_filter):
            try:
                dir_file_dicom = f'{dir_data}{file_dicom}'
                #print(dir_file_dicom)

                dataset = self.open_header_dicom.open_just_header(dir_file_dicom)

                size_file = self.open_header_dicom.view_size_file(dir_file_dicom)
                date = self.open_header_dicom.view_date(dataset)
                id = self.open_header_dicom.view_id(dataset)
                image_type = self.open_header_dicom.view_image_type(dataset)

                self.dict_data_frame['name_file_zip'].append(dir_file_dicom)
                self.dict_data_frame['size_file'].append(size_file)
                self.dict_data_frame['date'].append(date)
                self.dict_data_frame['id'].append(id)
                self.dict_data_frame['image_type'].append(image_type)
            except:
                print(f'is not possible to open {dir_file_dicom}')

        df = pd.DataFrame(self.dict_data_frame, columns=self.dict_data_frame.keys())
        df.to_csv('data_dicom_compare_dicom.csv', index=False)

    def open_zip_and_save(self, dir_data='/media/miclab/35c55d58-b4bf-4acf-a411-306032b6ca77/Originais/'):
        list_dir_data = os.listdir(dir_data)
        list_dir_data_filter = [x for x in list_dir_data if '.zip' in x]

        for file_zip in tqdm(list_dir_data_filter):

            name_file_zip = f'{dir_data}{file_zip}'
            self.unzip_file(name_file_zip, f'{dir_data}tmp_zip/')

            sub_name_file_zip = f'{dir_data}tmp_zip/'
            list_tmp_data = os.listdir(sub_name_file_zip)
                
            for file_dicom in list_tmp_data:
                try:
                    name_file_dicom = f'{dir_data}tmp_zip/{file_dicom}'

                    dataset = self.open_header_dicom.open_just_header(name_file_dicom)

                    size_file = self.open_header_dicom.view_size_file(name_file_dicom)

                    date = self.open_header_dicom.view_date(dataset)
                    id = self.open_header_dicom.view_id(dataset)
                    image_type = self.open_header_dicom.view_image_type(dataset)

                    self.dict_data_frame['name_file_zip'].append(name_file_zip)
                    self.dict_data_frame['name_file_in_zip'].append(name_file_dicom)
                    self.dict_data_frame['size_file'].append(size_file)
                    self.dict_data_frame['date'].append(date)
                    self.dict_data_frame['id'].append(id)
                    self.dict_data_frame['image_type'].append(image_type)
                    os.remove(name_file_dicom)

                #name_file_dicom = f'{dir_data}tmp_zip/{file_zip}'
                #name_file_dicom = name_file_dicom.replace(".zip", ".dcm")

                #name_file_dicom = name_file_dicom.replace(dir_data, 'unzip_dicom/')

                #dataset = self.open_header_dicom.open_just_header(name_file_dicom)

                #size_file = self.open_header_dicom.view_size_file(name_file_dicom)
                #date = self.open_header_dicom.view_date(dataset)
                #id = self.open_header_dicom.view_id(dataset)
                #image_type = self.open_header_dicom.view_image_type(dataset)

                #self.dict_data_frame['name_file_zip'].append(name_file_zip)
                #self.dict_data_frame['size_file'].append(size_file)
                #self.dict_data_frame['date'].append(date)
                #self.dict_data_frame['id'].append(id)
                #self.dict_data_frame['image_type'].append(image_type)
                #os.remove(name_file_dicom)
                except Exception as error_:
                    print(error_)
                    print(f'is not possible to open {name_file_dicom}')
            
        df = pd.DataFrame(self.dict_data_frame, columns=self.dict_data_frame.keys())
        df.to_csv('data_dicom_compare_zip.csv', index=False)
        #df_old = pd.read_csv('data_dicom_compare.csv')
        #pd.concat([df_old, df_new]).to_csv('data_dicom_compare2.csv', index=False)
        

            

# import zipfile
#
# path_to_zip_file = 'data_test/CLEONICE_BELMIRA_DE_SOUZA_10Apr2010-154433_VBM_6min.zip'
# directory_to_extract_to = ''
# with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
#     zip_ref.extractall(directory_to_extract_to)
