from dataclasses import dataclass

@dataclass
class OperationalMetrics:
    rows_processed: int = 0
    rows_valid: int = 0
    rows_invalid: int = 0
    malformed_rows: int = 0
    honeypots: int = 0
    validation_time_ms: float = 0.0
    stream_time_ms: float = 0.0
    
    @property
    def average_latency_ms(self) -> float:
        if self.rows_processed == 0:
            return 0.0
        return self.validation_time_ms / self.rows_processed

metrics = OperationalMetrics()
