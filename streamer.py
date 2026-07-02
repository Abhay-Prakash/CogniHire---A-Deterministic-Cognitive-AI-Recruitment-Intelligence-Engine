import json
import time
from typing import Iterator, Tuple
from core.schemas import RawRecord
from common.logger import logger
from common.metrics import metrics

def stream_candidates(file_path: str) -> Iterator[Tuple[int, RawRecord]]:
    """
    Deterministically yields raw records from a JSONL file.
    """
    start_stream = time.time()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, start=1):
            metrics.rows_processed += 1
            line = line.strip()
            if not line:
                continue
            
            try:
                raw_dict = json.loads(line)
                yield line_num, raw_dict
            except json.JSONDecodeError as e:
                metrics.malformed_rows += 1
                logger.log(
                    candidate_id=f"UNKNOWN_{line_num}",
                    line_number=line_num,
                    stage="streaming",
                    module="stream_io.streamer",
                    severity="WARN",
                    message=f"Malformed JSON: {str(e)}",
                    reason_code="INVALID_JSON",
                    runtime_ms=0.0
                )
    metrics.stream_time_ms += (time.time() - start_stream) * 1000
