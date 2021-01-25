import src  # My utility functions
import numpy as np

SIGNAL = np.array([int(n) for n in src.read()[0]])


def fft(signal, iterations=100):
    n = len(signal)
    pattern = np.array([0, 1, 0, -1])
    transforms = np.array([np.tile(pattern.repeat(i), n // (4*i) + 1)[1:n+1] for i in range(1, n+1)])
    new_signal = src.repeat(lambda sig: abs(transforms @ sig) % 10, signal, iterations)
    return ''.join(str(n) for n in new_signal[:8])


def find_message(signal, iterations=100):
    offset = int(''.join(str(n) for n in signal[:7]))
    n = len(signal)
    size = 10_000 * n - offset
    assert size < 5000 * n, "This algorithm is unfit for smaller offsets."
    sig = np.array(list(SIGNAL) * (size // n + 1))[-size:]
    new_sig = src.repeat(lambda s: np.cumsum(s) % 10, sig[::-1], iterations)
    return ''.join(str(n) for n in new_sig[-8:][::-1])


def main(signal=None):
    signal = signal or SIGNAL

    print("Part One:")
    ans1 = fft(signal)  # 74369033
    print(f"After 100 phases of FFT, the signal starts with {ans1}.")

    print("\nPart Two:")
    ans2 = find_message(signal)  # 19903864
    print(f"The embedded 8-digit message is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
