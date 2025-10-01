from pathlib import Path
import csv
import logging
from typing import Iterable, Sequence

def load_signal_csv(path: Path) -> list[float]:
    """
    Load a single-column CSV of floats into a list.
    """

    data = []

    try:
      with open(path,"r",newline='') as datafile:
          reader = csv.reader(datafile)
          for row in reader:
              try:
                data.append(float(row[0]))
              except ValueError :
                 print(f"Non-numeric data found in row {len(data)+1}")
    except FileNotFoundError :
        print("File doesn't exist")

    return data


def save_features_csv(path: Path, rows: Iterable[Sequence[float]]) -> None:
    """
    Save a CSV with header: rms,zero_crossings,peak_to_peak,mad
    """
    
    path.mkdir(parents=True,exist_ok=True)

    with open(path,'w',newline='') as writefile:
        writer = csv.writer(writefile)
        writer.writerow(['rms','zero_crossings','peak_to_peak','mad'])
        writer.writerows(rows)
