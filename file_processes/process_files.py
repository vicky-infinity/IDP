from fastapi import FastAPI, HTTPException, APIRouter



fprouter = APIRouter(
    prefix="/File",
    tags=["File Data Extraction"],
)

@fprouter.post("/File_processing")
def file_processing():

    # Calculates how many files are uploaded

    # Identify the extention of all the files count them and return the accepted filenems that we process and extract data from

    # Extract data form the identified fils

    # Understand the files what file it is Ex: It is invoice or bill or polici document or any thing might use the regex or llm over here

    # calculate the processing time from the extracting the data to understanding the file type and marking it
    
    #uploaded the information of the fiels exc time process pass or failed file name timing and all to the database

    # dump file in s3 if required this fucntion will be their but it will be empty

    # finally return the inpute file names, processed files list, execution time of each files,
    #  rejected files list,


    ...