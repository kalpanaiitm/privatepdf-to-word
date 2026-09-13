# PrivatePDF to Word

A free, open-source, privacy-conscious converter for turning **text-based PDFs** into editable Word (`.docx`) documents.

## Privacy by design

- conversion runs in memory; the app creates no upload directory or database
- uploaded PDF bytes and generated DOCX bytes are used only in the active app session
- filenames and document contents are not intentionally logged
- a **Clear this session** control removes application-held conversion results
- maximum 10 MB and 50 pages
- encrypted, corrupt, non-PDF, and scan-only files are rejected
- users must confirm ownership/permission and accept the privacy limitations

No hosted service can responsibly promise that infrastructure creates no operational metadata. Do not upload medical, banking, identity, legal, classified, export-controlled, unpublished, or otherwise highly sensitive documents.

## Conversion scope

Version 1 extracts selectable text and creates an editable Word document with page breaks and basic heading detection. It does not perform OCR. Complex layouts, columns, equations, tables, footnotes, and images may not be preserved accurately.

## Run

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Test

```bash
pytest -q
```

## Responsible use

Convert only documents you own or have permission to process. The software makes no warranty about formatting fidelity, accessibility, legal validity, confidentiality, or suitability for a particular purpose.

## Licence

MIT. See `LICENSE`.
