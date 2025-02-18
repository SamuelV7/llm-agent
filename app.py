import streamlit as st
import PyPDF2  # Only needed if you want to handle PDF files
import io

def main():
    # App title
    st.title("Transcript Uploader")
    st.write("Welcome! Use this app to upload a transcript file (TXT or PDF).")

    # File uploader for transcripts
    uploaded_file = st.file_uploader("Upload your transcript file", 
                                     type=["txt", "pdf"])
    
    if uploaded_file is not None:
        # Display the filename
        st.write("**Uploaded file:**", uploaded_file.name)
        
        # Check the file type:
        if uploaded_file.type == "application/pdf":
            # Optionally, handle PDF content
            pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
            all_text = ""
            for page_num in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page_num)
                all_text += page.extractText()
            
            st.write("**Extracted text from PDF:**")
            st.write(all_text)
            
        else:
            # For .txt, .csv, or other text-based transcripts
            # (Here we assume it's plain text)
            content = uploaded_file.read().decode("utf-8")
            st.write("**Transcript Content:**")
            st.write(content)

        # Here you can add code to process or analyze the transcript content.
        # For example, call some NLP model or store it in a database:
        # process_transcript(content)

    st.write("---")
    st.write("Thank you for using the Transcript Uploader!")

if __name__ == "__main__":
    main()
