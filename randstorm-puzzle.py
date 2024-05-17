import random
import sys
import secp256k1 as ice  # Ensure you have a module or implementation that provides these functions.

class SecureRandom3:
    def __init__(self, seed_time_value):
        self.SEED_TIME_VALUE = seed_time_value
        self.poolSize = 256
        self.pool = [0] * self.poolSize
        self.pptr = 0
        self.state = None
        
        # Initialize the pool
        while self.pptr < self.poolSize:
            t = random.randint(0, 65535)
            self.pool[self.pptr] = t >> 8
            self.pptr += 1
            self.pool[self.pptr] = t & 255
            self.pptr += 1
        
        self.pptr = 0
        self.seed_time()

    def seed_time(self):
        self.seed_int(self.SEED_TIME_VALUE)

    def seed_int(self, x):
        for shift in (0, 8, 16, 24):
            self.pool[self.pptr] ^= (x >> shift) & 255
            self.pptr += 1
            if self.pptr >= self.poolSize:
                self.pptr -= self.poolSize

    def get_byte(self):
        if self.state is None:
            self.seed_time()
            self.state = self.ArcFour()
            self.state.init(self.pool)
            for i in range(len(self.pool)):
                self.pool[i] = 0
            self.pptr = 0
        return self.state.next()

    class ArcFour:
        def __init__(self):
            self.i = 0
            self.j = 0
            self.S = list(range(256))

        def init(self, key):
            j = 0
            for i in range(256):
                j = (j + self.S[i] + key[i % len(key)]) & 255
                self.S[i], self.S[j] = self.S[j], self.S[i]

        def next(self):
            self.i = (self.i + 1) & 255
            self.j = (self.j + self.S[self.i]) & 255
            self.S[self.i], self.S[self.j] = self.S[self.j], self.S[self.i]
            return self.S[(self.S[self.i] + self.S[self.j]) & 255]

def generate_keys(seed_time_value, target_address,key_length):
    random3 = SecureRandom3(seed_time_value)

    num_bytes = (key_length + 7) // 8  # This rounds up to ensure all bits are covered

    # Generate the required number of private key bytes
    privateKeyBytes3 = [random3.get_byte() for _ in range(num_bytes)]

    # Convert private key bytes to hex string
    hex_string = ''.join(f'{byte:02x}' for byte in privateKeyBytes3)

    # Calculate the number of hex characters to represent the bit length
    hex_length = key_length // 4  # Each hex digit represents 4 bits

    # Truncate to keep only the last 'hex_length' characters of the hex string
    if hex_length > len(hex_string):
        privateKeyHex3 = hex_string  # Use the full key if 'hex_length' exceeds the actual length
    else:
        privateKeyHex3 = hex_string[-hex_length:]  # Slice to get the last 'hex_length' characters


    # Generate the public key using secp256k1
    P = ice.scalar_multiplication(int(privateKeyHex3, 16))
    p2pkh_address = ice.pubkey_to_address(0, True, P)

    # Check if the generated address matches the target address
    if p2pkh_address == target_address:
        print(f"Match found!\nPrivate Key: {privateKeyHex3}")
    


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python script.py <seed_time_value> <target_address> <key_length_in_bytes> <loop_count>")
        sys.exit(1)

    seed_time_value = int(sys.argv[1])
    target_address = sys.argv[2]
    key_length = int(sys.argv[3])
    loop_count = int(sys.argv[4])
    
    for i in range(1,loop_count):
        generate_keys(seed_time_value, target_address,key_length)

