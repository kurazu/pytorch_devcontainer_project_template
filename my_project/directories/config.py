from pathlib import Path

from pydantic import BaseSettings


class DirectoryConfig(BaseSettings):
    input_dir: Path
    output_dir: Path
