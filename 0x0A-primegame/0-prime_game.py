#!/usr/bin/python3
def isWinner(x, nums):
    def get_primes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]

    def play(player, nums):
        primes = get_primes(max(nums))
        moves = []
        for p in primes:
            if p in nums:
                moves += [p *
                          i for i in
                          range(1, (max(nums) // p) + 1) if p * i in nums]
        if not moves:
            return 'Maria' if player == 'Ben' else 'Ben'
        next_player = 'Maria' if player == 'Ben' else 'Ben'
        for move in moves:
            new_nums = [num for num in nums if num not in range(
                move, move + p * (max(nums) // p) + 1, p)]
            if play(next_player, new_nums) == player:
                return player
        return next_player

    maria_wins = 0
    ben_wins = 0
    for i in range(x):
        winner = play('Maria', list(range(1, nums[i] + 1)))
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
