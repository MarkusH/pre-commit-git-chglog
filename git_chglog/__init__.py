import dataclasses
import re
import sys
from pathlib import Path
from typing import Dict, List

import yaml


@dataclasses.dataclass
class Config:
    allowed_filters: Dict[str, List[str]]
    pattern: re.Pattern
    pattern_maps: List[str]


def get_config(path: Path) -> Config:
    with path.open("r") as fp:
        config = yaml.safe_load(fp)

    return Config(
        allowed_filters=config["options"]["commits"]["filters"]["Type"],
        pattern=re.compile(config["options"]["header"]["pattern"]),
        pattern_maps=config["options"]["header"]["pattern_maps"],
    )


def check(commit_msg_file: Path):
    cwd = Path.cwd()

    chglog_config_file = cwd / ".chglog" / "config.yml"
    config = get_config(chglog_config_file)

    with open(commit_msg_file) as fp:
        subject = fp.readline()

    match = config.pattern.match(subject)
    if not match:
        print(f"Subject line doesn't match pattern '{config.pattern.pattern}'")
        return False

    try:
        type_index = config.pattern_maps.index("Type")
    except ValueError:
        print("'Type' is not listed in `pattern_maps`.")
        return False

    num_groups = len(match.groups())
    if type_index >= num_groups:
        print(
            f"'Type' not found in subject. Subject has {num_groups} groups, "
            f"'Type' is expected in group {type_index + 1}."
        )
        return False

    type_in_subject = match.group(type_index + 1)
    if type_in_subject not in config.allowed_filters:
        allowed = ", ".join(config.allowed_filters)
        print(f"Type '{type_in_subject}' is not one of the allowed: {allowed}")
        return False

    return True


def main():
    if len(sys.argv) != 2:
        print("Missing or too many arguments. Expected 1.")
        sys.exit(2)

    status = check(Path(sys.argv[1]))
    if status:
        sys.exit(0)
    else:
        sys.exit(1)
