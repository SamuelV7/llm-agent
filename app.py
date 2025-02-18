import io
import streamlit as st
import req_check

def main():
    # App title
    st.title("Transcript Uploader")
    st.write("Welcome! Use this app to upload a transcript file (TXT or PDF).")

    # File uploader for transcripts
    uploaded_file = st.file_uploader("Upload your transcript file", 
                                     type=["txt"])
    
    if uploaded_file is not None:
        # Display the filename
        st.write("**Uploaded file:**", uploaded_file.name)
        # st.write("uploaded file", uploaded_file)
        if uploaded_file.type == "text/plain":
            # For .txt, .csv, or other text-based transcripts
            # (Here we assume it's plain text)
            content = uploaded_file.read().decode("utf-8")
            baseline_json = req_check.verify_transcript(content)
            show_results(baseline_json)
                # Here you can add code to process or analyze the transcript content.
        elif uploaded_file.type == "audio/mpeg":
            st.write("Transcription")
            audio_data = uploaded_file.read()
            audio_file = io.BytesIO(audio_data)
            audio_file.name = uploaded_file.name


        # For example, call some NLP model or store it in a database:
        # process_transcript(content)

    st.write("---")
    st.write("Thank you for using the Transcript Uploader!")

def show_results(baseline_json):
    st.write("**Transcript Check:**")
            # st.write(baseline_json)
    st.subheader("Detailed Results")

            # 1) Missing Items
    st.header("Missing Items")
    if baseline_json.missing_items:
        for item in baseline_json.missing_items:
            st.write(f"- {item}")
    else:
        st.write("No missing items.")

            # 2) Violations
    st.header("Violations")
    if baseline_json.violations:
        for violation in baseline_json.violations:
            st.write(f"- {violation}")
    else:
        st.write("No violations found.")

            # 3) Met Requirements
    st.header("Met Requirements")
    if baseline_json.met_requirements:
        for requirement in baseline_json.met_requirements:
            st.write(f"- {requirement}")
    else:
        st.write("No requirements met.")

            # 4) Ideas to Improve
    st.header("Ideas to Improve")
    if baseline_json.ideas_to_improve:
        for idea in baseline_json.ideas_to_improve:
            st.write(f"- {idea}")
    else:
        st.write("No improvement ideas.")

            # (Optional) Show the underlying JSON
    st.subheader("Raw JSON Output")
    st.json(baseline_json.dict())

if __name__ == "__main__":
    main()
