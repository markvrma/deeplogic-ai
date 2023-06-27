# Image/PDF to CSV convertor

### CSV Outputs
refer: `media/outputs`

### Data extraction script
`extraction/extract.py`

- I have used nanonets python library here, which requires an API key(you need to sign-up for it, but its free)
- Initially I planned on using [this](https://towardsdatascience.com/extracting-text-from-scanned-pdf-using-pytesseract-open-cv-cd670ee38052) article, but on further inspection I realized
  - a. The code was too big and messy
  - b. I was able to get most of the required data using only pytesseract, it was just a question of how i could get it into a csv file
  - c. I could try segmentation but coding that from scratch seemed impractical and time consuming

**Challenges**
- Getting the script to identify the tables and not just paste everything into a csv file
- I considered using [Tabula](https://tabula.technology), but its meant to handle neat software generated tables in pdfs not the image type tables taken with phones

While trying to see if there was software that could mimic what I was trying to do was when I stumbled on [NanoNets](https://github.com/NanoNets/ocr-python).
Using the freely available api-key I was able to easily generate tables from pdfs as well as images.

### Web App
I created the web app using Django for backend and bootstrap for frontend

**How it works**
- When the user uploads a file, the `forms.py` file checks if the file extention is allowed
- in the `views.py` file, a `UploadedFile` model is initialized, with a unique name for the file.
  - It is stored in the `/media/uploads/` folder
- Once uploaded we use `get_text()` in `extract.py` 
  - to get the csv output
  - convert the csv output to a dataframe, so that we can remove the rows that are completely filled with NaN values
  - convert it back to the csv file and render the output

### How to run
- Clone the repo
- `cd main`
- run `pip install -r requirements.txt`
- create `.env` file and configure `API_KEY`
- `python manage.py runserver`

### Output
![result](./Sample%20Files/result.png)