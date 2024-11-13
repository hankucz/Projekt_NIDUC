import komm

def bsc_channel(data, error_prob):
    """Symuluje kanał BSC z prawdopodobieństwem błędu error_prob."""
    channel = komm.BinarySymmetricChannel(error_probability=error_prob)
    return channel(data)
