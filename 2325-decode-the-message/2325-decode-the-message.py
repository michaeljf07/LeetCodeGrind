class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_map = {' ': ' '}
        current_letter = ord('a')
        
        for char in key:
            if char not in key_map:
                key_map[char] = chr(current_letter)
                current_letter += 1
        
        return "".join(key_map[char] for char in message)