import os
from pathlib import Path
from typing import Optional, Union

from wandb import env
from wandb.errors import term
from wandb.sdk.lib import filesystem

_staging_dir: Optional[Path] = None


def get_staging_dir() -> Path:
    """Return the staging directory for the current run."""
    global _staging_dir
    if _staging_dir is None:
        path = Path(env.get_data_dir()) / "artifacts" / "staging"
        filesystem.mkdir_exists_ok(path)
        _staging_dir = path.expanduser().resolve()
    return _staging_dir


def is_staged_copy(local_path: Union[str, os.PathLike]) -> bool:
    """Returns True if the given path is a staging copy of a local file."""
    try:
        # Raises if the path is not a child of the staging directory.
        Path(local_path).relative_to(get_staging_dir())
        return True
    except ValueError:
        return False


def remove_from_staging(local_path: Union[str, os.PathLike]) -> None:
    """Remove the given file from staging."""
    local_path = Path(local_path)
    if not is_staged_copy(local_path):
        term.termerror(f"Staging file '{local_path}' is not in staging directory")
        return
    try:
        local_path.chmod(0o600)
        local_path.unlink()
    except PermissionError:
        term.termerror(f"Unable to remove staging file {local_path}")
    except FileNotFoundError:
        pass
