#!/usr/bin/env python3
"""Decode the 16 base32 tones from Frequency and Consequence."""

import argparse
import wave

import numpy as np


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
SLOT_SECONDS = 0.5


def read_samples(path):
    with wave.open(str(path), "rb") as wav:
        if wav.getnchannels() != 1 or wav.getsampwidth() != 2:
            raise ValueError("expected mono 16-bit PCM")
        return np.frombuffer(wav.readframes(wav.getnframes()), dtype=np.int16).astype(float), wav.getframerate()


def tone_score(samples, rate, frequencies):
    centered = samples - samples.mean()
    windowed = centered * np.hanning(len(centered))
    spectrum = np.abs(np.fft.rfft(windowed))
    bins = np.fft.rfftfreq(len(windowed), 1 / rate)
    values = []
    for frequency in frequencies:
        nearby = (bins >= frequency - 3) & (bins <= frequency + 3)
        values.append(float(spectrum[nearby].max()))
    return max(values), values.index(max(values))


def decode(samples, rate):
    slot = round(rate * SLOT_SECONDS)
    frequencies = [500 + 50 * index for index in range(32)]
    best = None
    for offset in range(0, slot, 100):
        windows = [samples[offset + i * slot : offset + (i + 1) * slot] for i in range(16)]
        if any(len(window) != slot for window in windows):
            continue
        scores = [tone_score(window, rate, frequencies) for window in windows]
        total = sum(np.log1p(score) for score, _ in scores)
        if best is None or total > best[0]:
            best = (total, scores)
    if best is None:
        raise ValueError("the WAV is shorter than 16 slots")
    return "".join(ALPHABET[index] for _, index in best[1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("wav", help="mono 16-bit signal.wav")
    args = parser.parse_args()
    samples, rate = read_samples(args.wav)
    print(decode(samples, rate))


if __name__ == "__main__":
    main()
