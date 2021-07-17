from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in. │ ─ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘
    """
    def get_cols_max_len(data: List[List[Any]], head: Optional[List[Any]]):
        cols_num = len(data[0])
        cols_lens = [0] * cols_num
        if head:
            for col in range(cols_num):
                cols_lens[col] += len(str(head[col])) + 2
        for row in range(len(data)):
            for col in range(cols_num):
                len_difference = len(str(data[row][col])) + 2 - cols_lens[col]
                if len_difference > 0:
                    cols_lens[col] += len_difference
        return cols_lens

    def fill_line(chars: str, cols_lens: List[int]):
        line = []
        for col in cols_lens:
            line.append('─' * col)
        return chars[0] + chars[1].join(line) + chars[2]

    def fill_row(words: List[Any], cols_lens: List[int], to_center: bool):
        line = []
        for col in range(len(cols_lens)):
            if to_center:
                word = str(words[col]).center(cols_lens[col])
            else:
                word = ' ' + str(words[col]).ljust(cols_lens[col] - 1)
            line.append(word)
        return '│' + '│'.join(line) + '│'

    cols_max_len = get_cols_max_len(rows, labels)
    table = [fill_line('┌┬┐', cols_max_len)]
    if labels:
        table.append(fill_row(labels, cols_max_len, centered))
        table.append(fill_line('├┼┤', cols_max_len))
    for item in rows:
        table.append(fill_row(item, cols_max_len, centered))
    table.append(fill_line('└┴┘', cols_max_len))
    return '\n'.join(table)

table = make_table(
   rows=[
       ["Ducky Yellow", 3],
       ["Ducky Dave", 12],
       ["Ducky Tube", 7],
       ["Ducky Lemon", 1]
   ],
   labels=["Name", "Duckiness"],
   centered=True
)
print(table)
