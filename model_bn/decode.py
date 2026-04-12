#!/usr/bin/env python3
import wave
from pathlib import Path
from typing import Tuple
import sys
import numpy as np
import sherpa_onnx
from timeit import default_timer as timer

def read_wave(wave_filename: str) -> Tuple[np.ndarray, int]:
    with wave.open(wave_filename) as f:
        assert f.getnchannels() == 1, f.getnchannels()
        assert f.getsampwidth() == 2, f.getsampwidth()  # it is in bytes
        num_samples = f.getnframes()
        samples = f.readframes(num_samples)
        samples_int16 = np.frombuffer(samples, dtype=np.int16)
        samples_float32 = samples_int16.astype(np.float32)
        samples_float32 = samples_float32 / 32768
        return samples_float32, f.getframerate()

def main():

    start = timer()
    recognizer = sherpa_onnx.OnlineRecognizer.from_transducer(
            encoder="am-onnx/encoder.onnx",
            decoder="am-onnx/decoder.onnx",
            joiner="am-onnx/joiner.onnx",
            tokens="lang/tokens.txt",
            num_threads=2,
            sample_rate=16000,
            dither=3e-5,
            decoding_method="modified_beam_search",
            max_active_paths=10,
            provider="cpu",
            model_type="zipformer2")
    end = timer()
    print (f"Initialized in {end - start:.4f} seconds")

    samples, sample_rate = read_wave("test.wav")

    start = timer()
    s = recognizer.create_stream()
    s.accept_waveform(sample_rate, waveform=samples)
    tail_padding = np.zeros(int(sample_rate * 1.0)).astype(np.float32)
    s.accept_waveform(sample_rate, waveform=tail_padding)
    s.input_finished()

    while recognizer.is_ready(s):
        recognizer.decode_stream(s)
        print (recognizer.get_result(s))
    end = timer()
    print (f"Recognized in {end - start:.4f} seconds")

if __name__ == "__main__":
    main()

