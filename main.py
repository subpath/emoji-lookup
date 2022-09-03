import json
import argparse

with open("shortnames.json", "r") as f:
    shortnames = json.load(f)


def lookup(query: str) -> str:
    """Find shortnames that are matching query."""
    suggestions = []
    for shortname in shortnames:
        if query in shortname:
            suggestions.append(shortname)
    return suggestions


def format_for_output(query: str, suggestion: str) -> str:
    """"Highlight part of the shortname that matching the query."""
    return suggestion.replace(query, f"\033[1m{query}\033[0m")


def main():

    query = args.shortname.strip()
    suggestions = lookup(query)
    for suggestion in suggestions:
        print(format_for_output(query, suggestion), shortnames[suggestion])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('shortname')
    args = parser.parse_args()
    main()
