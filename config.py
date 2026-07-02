from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    CHUNK_SIZE: int = 1024
    TOP_K: int = 100
    DEBUG_LOGGING: bool = False
    LOG_FILE: str = "recruiter.log"
    DATASET_PATH: str = "[PUB] India_runs_data_and_ai_challenge/India_runs_data_and_ai_challenge/candidates.jsonl"
    OUTPUT_CSV_PATH: str = "outputs/submission.csv"

config = Config()
