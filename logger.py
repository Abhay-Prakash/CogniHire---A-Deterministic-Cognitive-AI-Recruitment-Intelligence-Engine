import json
import logging
from core.config import config

class RecruiterLogger:
    def __init__(self):
        self.logger = logging.getLogger("AIRecruiter")
        self.logger.setLevel(logging.DEBUG if config.DEBUG_LOGGING else logging.INFO)
        
        handler = logging.FileHandler(config.LOG_FILE)
        handler.setFormatter(logging.Formatter('%(message)s'))
        self.logger.addHandler(handler)

    def log(self, candidate_id: str, line_number: int, stage: str, module: str, severity: str, message: str, reason_code: str, runtime_ms: float = 0.0):
        log_entry = {
            "candidate_id": candidate_id,
            "line_number": line_number,
            "stage": stage,
            "module": module,
            "severity": severity,
            "message": message,
            "reason_code": reason_code,
            "runtime_ms": runtime_ms
        }
        
        if severity == "ERROR":
            self.logger.error(json.dumps(log_entry))
        elif severity == "WARN":
            self.logger.warning(json.dumps(log_entry))
        elif severity == "INFO":
            self.logger.info(json.dumps(log_entry))
        elif severity == "DEBUG":
            self.logger.debug(json.dumps(log_entry))

logger = RecruiterLogger()
