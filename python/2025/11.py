from functools import cache


def solver(inp: str):
    p1(inp)
    p2(inp)


def inptopaths(inp: str):
    lines = inp.strip().splitlines()
    paths = {}
    for line in lines:
        key, rest = line.split(": ")
        options = rest.split(" ")
        paths[key] = options
    return paths


def p1(inp: str):
    paths = inptopaths(inp)
    unique_paths = set()

    @cache
    def dfs(node, path):
        if node == "out":
            unique_paths.add("->".join(path))
            return
        for neighbor in paths.get(node, []):
            dfs(neighbor, path + (neighbor,))

    # Find paths from 'you' to 'out'
    dfs("you", ("you",))
    print("p1: ", len(unique_paths))


def p2(inp: str):
    paths = inptopaths(inp)

    @cache
    def dfs(node, has_dac, has_fft):
        # Count paths from current node to 'out' with required visits
        if node == "out":
            # Only count if we've visited both dac and fft
            return 1 if (has_dac and has_fft) else 0

        total = 0
        for neighbor in paths.get(node, []):
            new_has_dac = has_dac or (neighbor == "dac")
            new_has_fft = has_fft or (neighbor == "fft")
            total += dfs(neighbor, new_has_dac, new_has_fft)

        return total

    # Find paths from 'svr' to 'out' that pass through both 'dac' and 'fft'
    result = dfs("svr", False, False)
    print("p2: ", result)
