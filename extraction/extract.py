from nanonets import NANONETSOCR
import os
import pandas as pd



def get_text(id,uploaded_file):
    '''
    using an external api that can identify images from pdf or csv 
    and display the table in csv
    '''

    # preparing file paths(input and output)
    file_path = f'./media/uploads/{id}_{uploaded_file}'
    out_path = f'./media/outputs/{id}_{uploaded_file}'

    # absolute paths - will run on any system, avoiding relative paths
    abs_path = os.path.abspath(file_path)
    abs_path2 = os.path.abspath(out_path) 

    # convert img/pdf to csv
    model = NANONETSOCR()
    model.set_token(os.environ.get('API_KEY'))

    if os.path.exists(abs_path):
        model.convert_to_csv(abs_path, output_file_name = abs_path2)

        # delete the file once we read it(optional)
        # os.remove(abs_path)
        
        # convert the csv to a pandas dataframe to remove NaN values
        data = pd.read_csv(abs_path2)
        data = data.dropna(how='all').reset_index(drop=True)

        # convert back to csv
        data.to_csv(abs_path2)
        data_html = data.to_html
        return data_html
    
    return None


# optional: was made to handle non-grayscale images, however not required
# def mark_region(image_path):
    
#     im = cv2.imread(image_path)

#     gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
#     kernel = np.ones((5,5),np.uint8)

#     erode = cv2.erode(gray, kernel,iterations=2)
#     dilate = cv2.dilate(erode,kernel)

#     cv2.imwrite("../Sample Files/uggggg.jpg",dilate)
