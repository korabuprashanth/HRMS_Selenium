import logging
import os

# ─────────────────────────────────────────────
#  Logger  –  writes to console + test.log
#  Usage:  log = get_logger()
#          log.info("Login successful")
# ─────────────────────────────────────────────

def get_logger(name="OrangeHRM"):
    logger = logging.getLogger(name)

    if not logger.handlers:                          # avoid duplicate handlers
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s  [%(levelname)-7s]  %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Console handler
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

        # File handler  (logs/test.log)
        log_dir = os.path.join(os.path.dirname(__file__), "..", "reports")
        os.makedirs(log_dir, exist_ok=True)
        file_handler = logging.FileHandler(os.path.join(log_dir, "test.log"))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
