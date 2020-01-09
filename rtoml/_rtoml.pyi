from datetime import date, time
from typing import Any, Callable, Union

VERSION: str

def deserialize(toml: str, parse_datetime: Callable[[str], Union[date, time]]) -> Any: ...
def serialize(obj: Any) -> str: ...

class TomlParsingError(ValueError): ...
class TomlSerializationError(ValueError): ...
