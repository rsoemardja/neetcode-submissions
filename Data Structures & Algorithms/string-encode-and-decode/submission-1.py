class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = []
        for s in strs:
            # Append length + delimiter + string
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string back to a list of strings."""
        decoded = []
        i = 0
        while i < len(s):
            # Find the position of the next delimiter
            j = s.find('#', i)
            # The length is the number before '#'
            length = int(s[i:j])
            # The string starts right after '#'
            start = j + 1
            end = start + length
            decoded.append(s[start:end])
            # Move the pointer to the next encoded segment
            i = end
        return decoded