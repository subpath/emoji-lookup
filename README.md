# emoji-lookup π΅ββ
search emoji characters in the terminal, pure python stdlib with no dependencies π


## Usage:
1. clone this repo
2. run main.py with your search_query
```bash
python main.py skate 
>>:ice_skate: βΈοΈ
>>:skateboard: πΉ
```
To use only prefix match start your query with `:`
```bash
python main.py :skate 
>>:skateboard: πΉ
```

## Which shortnames are used here?
I'm using [GitHub's](https://emojipedia.org/github/) short names

## Setup alias:
to use it everywhere in your terminal you can setup an alias in you bashrc or zshrc in the following format:
```bash
alias emoji='{path-to-your-python} {path-to-the-main.py}'
```
example:
```bash
emoji check
>>:heavy_check_mark: βοΈ
>>:white_check_mark: β
>>:ballot_box_with_check: βοΈ
>>:checkered_flag: π
>>:check_box_with_check: β
>>:check_mark: β
```
