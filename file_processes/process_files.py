from fastapi import FastAPI, HTTPException, APIRouter



fprouter = APIRouter(
    prefix="/File",
    tags=["File Data Extraction"],
)

@fprouter.post("/File_processing")
@fprouter.post("/File_processing")
def file_processing():
    """
    Process multiple uploaded documents (Invoice, Bill, Policy, etc.).
    """

    # ============================
    # 1. PRE-PROCESSING (Global)
    # ============================
    
    # 1a. Calculate how many files were uploaded.
    #     If zero, return a 400 error immediately.
    
    # 1b. Initialize empty lists for results:
    #     - processed_files  (stores filename, extracted data, time)
    #     - rejected_files   (stores filename, error reason)
    #     - total_time_ms    (sum of per-file processing times)
    

    # ============================
    # 2. LOOP: Process EACH file individually
    # ============================
    
    # for each file in uploaded_files:
    
        # ---------- START TIMER ----------
        # 2a. Start the per-file execution timer IMMEDIATELY.
        #     This captures the time for classification + extraction + saving.
        
        
        # ---------- VALIDATE & IDENTIFY ----------
        # 2b. Validate the file:
        #     - Check file size (e.g., reject if > 100MB).
        #     - Read the first few bytes (Magic Number / MIME type) 
        #       to confirm it's ACTUALLY a PDF/PNG/CSV.
        #     - DO NOT TRUST the filename extension.
        
        # 2c. Understand the document type (Classification):
        #     - If it's a PDF, use Regex or LLM to determine if 
        #       it's an "Invoice", "Policy Document", "Bill", or "Unknown".
        #     - If it doesn't match any pattern, mark it as "unclassified".
        #       (We will extract generic text but reject specific extraction).
        
        
        # ---------- EXTRACT DATA (Run this SECOND) ----------
        # 2d. Based on the identified type (Step 2c), extract the specific data:
        #     - If "Invoice": extract Invoice Number, Total Amount, Date.
        #     - If "Policy": extract Policy Number, Holder Name, Premium.
        #     - If "Unknown": extract generic text (or skip).
        #     - If extraction fails, catch the error and mark file as "rejected".
        
        
        # ---------- STOP TIMER & RECORD ----------
        # 2e. Calculate processing time for THIS file:
        #     elapsed_ms = (end_time - start_time) * 1000
        #     Add this value to the global total_time_ms accumulator.
        
        
        # ---------- PERSIST TO DATABASE ----------
        # 2f. Save the metadata to the database:
        #     Columns: filename, file_type, status (processed/rejected),
        #              extracted_data (JSON string), processing_time_ms, error_message.
        #     Even failed files are logged here for auditing.
        
        
        # ---------- DUMP TO S3 (Optional) ----------
        # 2g. Upload the raw file to S3 (Placeholder / Empty function).
        #     Do this BEFORE deleting the local file so we don't lose it 
        #     if the upload fails.
        #     (You mentioned this function will be empty, so we just call it).
        
        
        # ---------- CLEANUP & AGGREGATE ----------
        # 2h. Delete the temporary file from local disk.
        
        # 2i. Append the result to either the "processed" or "rejected" list:
        #     - Include filename, extracted_data, processing_time_ms.
        #     - Include the specific error if rejected.
    

    # ============================
    # 3. FINAL RESPONSE
    # ============================
    
    # 3a. Return the final JSON payload:
    #     {
    #       "total_files": X,
    #       "processed_files": [ {filename, extracted_data, time}, ... ],
    #       "rejected_files": [ {filename, error}, ... ],
    #       "total_processing_time_ms": X
    #     }
    
    ...