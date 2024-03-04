def team_efficiency(skill):
    total_sum = sum(skill)
    print(total_sum)
    total_sum = total_sum // ((len(skill))/2)
    print(total_sum)
    # if total_sum % 2 != 0:
    #     return -1  # Not possible to form teams with equal sums of skills

    target_sum = total_sum // 2
    skill_count = {}

    # Count occurrences of each skill
    for s in skill:
        if s in skill_count:
            skill_count[s] += 1
        else:
            skill_count[s] = 1

    efficiency_sum = 0

    # Pair up skills to form teams
    for s in skill_count:
        complement = target_sum - s
        if complement in skill_count:
            pairs = min(skill_count[s], skill_count[complement])
            skill_count[s] -= pairs
            skill_count[complement] -= pairs
            efficiency_sum += s * complement * pairs

    # If all pairs are not formed
    if sum(skill_count.values()) != 0:
        return -1

    return efficiency_sum

# Example usage
skill = [2,1,1,4,3,4]
print(team_efficiency(skill))  # Output should be 7 (3 + 4)
