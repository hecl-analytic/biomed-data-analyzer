from main import calculate_bpm, diagnose_bpm, peaks_detection
import pandas as pd


def test_calculate_bmp():
    assert calculate_bpm(10, 3600) == 60
    assert calculate_bpm(30, 3600) == 180


def test_diagnose_bpm():
    assert diagnose_bpm(80) == "Normal"
    assert diagnose_bpm(22) == "Bradycardia"
    assert diagnose_bpm(200) == "Tachycardia"


def test_peaks_detection():
    signal = pd.Series([0, 0, 10, 0, 0])
    _, peak_count = peaks_detection(signal)
    assert peak_count == 1
