import logging
from pathlib import Path


LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "app.log"

LOG_DIR.mkdir(exist_ok=True)


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger("HelpDeskSystem")