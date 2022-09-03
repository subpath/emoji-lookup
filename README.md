# emoji-lookup 🕵‍♂
search emoji characters in the terminal, pure python stdlib with no dependencies 🙌


## Usage:
1. clone this repo
2. run main.py with your search_query
```bash
python main.py skate 
>>:ice_skate: ⛸️
>>:skateboard: 🛹
```
To use only prefix match start your query with `:`
```bash
python main.py :skate 
>>:skateboard: 🛹
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
>>:heavy_check_mark: ✔️
>>:white_check_mark: ✅
>>:ballot_box_with_check: ☑️
>>:checkered_flag: 🏁
>>:check_box_with_check: ☑
>>:check_mark: ✔
```
