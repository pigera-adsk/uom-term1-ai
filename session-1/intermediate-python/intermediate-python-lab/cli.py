# Optional CLI using typer
import typer, logging
from pathlib import Path
import numpy as np
import time

from src.ipylab.io import load_signal_csv, save_features_csv
from src.ipylab.features import feature_vector

app = typer.Typer(help="Intermediate Python Lab CLI")

@app.command()
def generate_data(out: Path = typer.Option(Path("data/signal.csv"), help="Output CSV path"),
                  n: int = 4000,
                  noise: float = 0.15):
    """
    Generate synthetic signal data (sine + square mixture) and save to CSV.
    TODO:
      - Implement signal synthesis similar to dataset seeded in data/signal.csv
    """
    # Generate time vector
    t = np.linspace(0, 1, n)
    # Sine + square mixture
    signal = np.sin(2 * np.pi * 5 * t) + np.sign(np.sin(2 * np.pi * 2 * t))
    # Add Gaussian noise
    signal += np.random.normal(0, noise, size=n)

    # Save to CSV
    out.parent.mkdir(parents=True, exist_ok=True)
    np.savetxt(out, np.column_stack((t, signal)), delimiter=",", header="time,signal", comments="")
    typer.echo(f"Generated {n} samples and saved to {out}")

@app.command()
def run_pipeline(inp: Path = Path("data/signal.csv"),
                 out: Path = Path("data/features.csv"),
                 chunk: int = 256):
    """
    Stream the input CSV in chunks, compute features per chunk, and save to CSV.
    TODO:
      - Use load_signal_csv, slice into chunks, compute feature_vector on each chunk (np.array)
      - Save with save_features_csv
    """
    typer.echo(f"Loading data from {inp} ...")
    data = load_signal_csv(inp)
    features = []
    for i in range(0, len(data), chunk):
        chunk_data = data[i:i+chunk]
        vec = feature_vector(np.array(chunk_data))
        features.append(vec)

    save_features_csv(out, np.array(features))
    typer.echo(f"Processed {len(features)} chunks and saved features to {out}")


@app.command()
def profile():
    """
    Profile Python vs NumPy RMS on a large array and print timings.
    TODO:
      - Create 1e6 random floats (np.random.randn)
      - Time pure-python and numpy versions; print ms
    """
    data = np.random.randn(int(1e6))

    start = time.perf_counter()
    rms_py = (sum(x*x for x in data) / len(data)) ** 0.5
    py_time = (time.perf_counter() - start) * 1000 

    start = time.perf_counter()
    rms_np = np.sqrt(np.mean(np.square(data)))
    np_time = (time.perf_counter() - start) * 1000

    typer.echo(f"Pure Python : {rms_py:.f} ({py_time:.2f} ms)")
    typer.echo(f"NumPy : {rms_np:.f} ({np_time:.2f} ms)")
   


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app()
