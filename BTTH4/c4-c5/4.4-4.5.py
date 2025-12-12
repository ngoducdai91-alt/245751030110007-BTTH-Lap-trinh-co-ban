print("NGÔ ĐỨC ĐAI")
print("msv:245751030110007")
print("################################")
print("4)")
class py_solution:
    def roman_to_int(self, s: str) -> int:
        if not s or not isinstance(s, str):
            raise ValueError("Input must be a non-empty string")
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s.upper()
        total = 0
        for i in range(len(s)):
            if s[i] not in rom:
                raise ValueError(f"Invalid Roman numeral character: {s[i]}")
            val = rom[s[i]]
            if i + 1 < len(s) and rom.get(s[i + 1], 0) > val:
                total -= val
            else:
                total += val
        return total
    def reverse_words(self, s: str) -> str:
        if s is None:
            raise ValueError("Input must be a string")
        words = s.split()
        return " ".join(reversed(words))
if __name__ == "__main__":
    solver = py_solution()
    examples = ["III", "IV", "IX", "LVIII", "MCMXCIV", "MMXXV"]
    for rom in examples:
        print(f"{rom} -> {solver.roman_to_int(rom)}")
print("5)")
class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))
print(py_solution().reverse_words("hello.py"))
