import sys
import pandas as pd
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


def main():
    if len(sys.argv) < 2:
        sys.exit("Incorrect input")
    file = sys.argv[1]
    signal = load_file(file)
    peaks, peaks_count = peaks_detection(signal)
    bpm = calculate_bpm(peaks_count, len(signal))
    intervals = rr_intervals(peaks)

    print(f"Value BPM: {bpm:.2f}| Diagnose: {diagnose_bpm(bpm)}")
    print(f"Avg time RR interval: {(sum(intervals)/len(intervals))*1000:.2f} ms")
    print(f"Number of detected peaks: {peaks_count}")

    graph(signal, peaks)


def peaks_detection(signal):
    """
    Here we look for ECG R peaks, which we then use to calculate BPM (beats per minute).
    """
    peaks, _ = find_peaks(signal, height=max(signal) * 0.7, distance=150)
    peaks_count = len(peaks)
    return peaks, peaks_count


def load_file(file):
    """
        Loading file
    """
    try:
        df = pd.read_csv(file)
        signal = df.head(15000)["MLII"]
        return signal
    except FileNotFoundError:
        sys.exit("File not found.")


def calculate_bpm(peak_count, signal_length):
    """
    Here we calculate BPM
    """
    time = signal_length / 360
    return (peak_count / time) * 60

def diagnose_bpm(bpm):
    """
        BPM diagnose
    """
    if bpm < 60:
        return "Bradycardia"
    elif bpm > 100:
        return "Tachycardia"
    else:
        return "Normal"

def graph(signal, peaks):
    """
        Graph
    """
    fs = 360
    time = signal.index / fs
    peaks_time = peaks / fs
    plt.figure(figsize=(12, 5))
    plt.plot(time * 1000, signal)
    plt.plot(peaks_time * 1000, signal[peaks], "x", color="red")
    plt.title("EKG curve")
    plt.xlabel("Time[ms]")
    plt.ylabel("Volt [mV]")
    plt.savefig("ekg.png")
    plt.show()


def rr_intervals(peaks, fs=360):
    return np.diff(peaks) / fs


if __name__ == "__main__":
    main()
