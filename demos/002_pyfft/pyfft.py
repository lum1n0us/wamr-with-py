import cmath
from time import perf_counter_ns as clock

def fft(sequence):
    N = len(sequence)
    if N <= 1:
        return sequence
    even = fft(sequence[0::2])
    odd = fft(sequence[1::2])
    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k % len(odd)] for k in range(N // 2)]
    return [even[k % len(even)] + T[k] for k in range(N // 2)] + [
        even[k % len(even)] - T[k] for k in range(N // 2)
    ]

def fft_iterative(sequence):
    N = len(sequence)
    levels = N.bit_length() - 1

    # If the input size is not a power of 2, raise an error
    if not (N & (N - 1)) == 0:
        raise ValueError(f"The length of the input sequence {N} must be a power of 2.")

    # Reorder the input array by bit-reversed indices
    bit_reversed_indices = [int('{:0{}b}'.format(i, levels)[::-1], 2) for i in range(N)]
    reordered_sequence = [sequence[i] for i in bit_reversed_indices]

    # Perform the butterfly operations
    for i in range(levels):
        m = 1 << i
        n = m * 2
        w_m = cmath.exp(-2j * cmath.pi / n)
        for k in range(0, N, n):
            w = 1
            for j in range(m):
                t = w * reordered_sequence[k + j + m]
                u = reordered_sequence[k + j]
                reordered_sequence[k + j] = u + t
                reordered_sequence[k + j + m] = u - t
                w *= w_m
    return reordered_sequence


# Generate a sine wave sequence
def generate_sine_wave(freq, sample_rate, duration):
    x = [
        cmath.sin(2 * cmath.pi * freq * (i / sample_rate))
        for i in range(int(sample_rate * duration))
    ]
    return x


def main():
    """
    run 3 times
    """
    # Sine wave parameters
    frequency = 5  # Frequency in Hz
    sample_rate = 1024 # Sample rate in samples per second
    duration = 64  # Duration in seconds

    # Generate a sine wave
    sine_wave = generate_sine_wave(frequency, sample_rate, duration)

    execution_times = []
    for i in range(3):
        starttime  = clock()
        # Apply FFT to the sine wave
        sine_wave_fft = fft_iterative(sine_wave)
        endtime = clock()

        execution_times.append(endtime - starttime)
    
    print(f"This machine benchmarks in {sum(execution_times) / 3 / 1000 / 1000} ms")


# Example usage:
if __name__ == "__main__":
    main()
