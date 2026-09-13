import re

import streamlit as st

from privatepdf import ConversionError, convert_pdf_bytes
from privatepdf.sample import make_sample_pdf

st.set_page_config(page_title="PrivatePDF to Word", page_icon="🔐", layout="centered")
st.title("🔐 PrivatePDF to Word")
st.subheader("Free, privacy-conscious conversion for text-based PDFs")
st.info(
    "No account, database, or intentional document storage. Files are processed in application memory "
    "for the active session. Do not upload highly sensitive documents."
)

with st.expander("Read privacy and conversion limitations", expanded=True):
    st.markdown(
        "- Version 1 supports PDFs containing selectable text; it does not perform OCR.\n"
        "- Complex layouts, tables, images, equations and footnotes may change or be omitted.\n"
        "- Hosting infrastructure may create operational metadata outside this app's control.\n"
        "- Never upload medical, banking, identity, classified, legally privileged, unpublished or export-controlled files.\n"
        "- Download and inspect the Word file before relying on it."
    )

sample = make_sample_pdf()
st.download_button(
    "Download fictional test PDF",
    sample,
    file_name="privatepdf_fictional_test.pdf",
    mime="application/pdf",
)

if "upload_key" not in st.session_state:
    st.session_state.upload_key = 0

uploaded = st.file_uploader(
    "Upload one PDF (maximum 10 MB and 50 pages)",
    type=["pdf"],
    accept_multiple_files=False,
    key=f"pdf_upload_{st.session_state.upload_key}",
)

permission = st.checkbox("I own this document or have permission to convert it")
privacy = st.checkbox("I understand the privacy and conversion limitations")

if st.button("Convert to Word", type="primary", disabled=not (uploaded and permission and privacy)):
    try:
        result = convert_pdf_bytes(uploaded.getvalue())
        st.session_state["docx_result"] = result.docx_bytes
        safe_stem = re.sub(r"[^A-Za-z0-9_-]+", "_", uploaded.name.rsplit(".", 1)[0]).strip("_")
        st.session_state["output_name"] = f"{safe_stem or 'converted'}.docx"
        st.success(f"Converted {result.page_count} page(s) and {result.character_count:,} characters.")
        for warning in result.warnings:
            st.warning(warning)
    except ConversionError as exc:
        st.error(str(exc))

if "docx_result" in st.session_state:
    st.download_button(
        "Download Word document",
        st.session_state["docx_result"],
        file_name=st.session_state["output_name"],
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )

if st.button("Clear this session"):
    st.session_state.pop("docx_result", None)
    st.session_state.pop("output_name", None)
    st.session_state.upload_key += 1
    st.rerun()

st.caption(
    "Convert only authorised material. This service provides no guarantee of confidentiality, formatting fidelity, "
    "accessibility, legal validity, or fitness for a particular purpose."
)
