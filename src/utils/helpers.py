
from pathlib import Path

from utils.constants import HASH_BUFFER_LEN, TEMP_FOLDER_PATH  # MESSAGE_MAX_LEN,
from utils.types import CompressionMethod, DirData


def path_to_dict(path: Path, share_folder_path: str) -> DirData:
    """Converts a given folder path to a dictionary representation of the entire directory structure

    Recursively constructs the output dictionary.
    Works relative to the user's share folder.

    Parameters
    ----------
    path : Path
        Path to an item to be added to dictionary
    share_folder_path : str
        string path to user's share directory which contains the item at [path]

    Returns
    -------
    DirData
        Returns dictionary representation as defined by the DirData custom type
    """
    d: DirData = {
        "path": str(path).removeprefix(share_folder_path + "/"),
        "name": path.name,
        "hash": None,
        "compression": CompressionMethod.NONE.value,
        "type": "",
        "size": None,
        "children": [],
    }
    if path.is_dir():
        d["type"] = "directory"
        d["children"] = [path_to_dict(item, share_folder_path) for item in path.iterdir()]
    else:
        d["type"] = "file"
        d["size"] = Path(path).stat().st_size

    return d

