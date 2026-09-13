from io import BytesIO

from pypdf import PdfReader
from pypdf.errors import PdfReadError

MAX_BYTES = 10 * 1024 * 1024
MAX_PAGES = 50


class ValidationError(ValueError):
    """Raised when an upload is outside the public app's safe scope."""


def validate_pdf(data: bytes) -> PdfReader:
    if not data:
        raise ValidationError("The uploaded file is empty.")
    if len(data) > MAX_BYTES:
        raise ValidationError("The PDF exceeds the 10 MB public-demo limit.")
    if not data.startswith(b"%PDF-"):
        raise ValidationError("The file does not have a valid PDF signature.")
    try:
        reader = PdfReader(BytesIO(data), strict=True)
    except (PdfReadError, ValueError, TypeError) as exc:
        raise ValidationError("The PDF is corrupt or unsupported.") from exc
    if reader.is_encrypted:
        raise ValidationError("Password-protected or encrypted PDFs are not processed.")
    page_count = len(reader.pages)
    if page_count == 0:
        raise ValidationError("The PDF contains no pages.")
    if page_count > MAX_PAGES:
        raise ValidationError(f"The PDF has {page_count} pages; the public limit is {MAX_PAGES}.")
    return reader
