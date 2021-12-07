crab_positions = [int(pos) for pos in open("input").read().split(",")]


def _fuel_costs_to_move_all_crabs(target_pos: int, constant_fuel: bool = True):
    fuel_costs = 0
    for crab_pos in crab_positions:
        if constant_fuel:
            fuel_costs += abs(crab_pos - target_pos)
        else:
            moves = abs(crab_pos - target_pos)
            fuel_costs += (moves * (moves + 1)) // 2  # Cheers, Carl Friedrich
    return fuel_costs


def part_one() -> int:
    return min(
        [_fuel_costs_to_move_all_crabs(target_pos) for target_pos in crab_positions]
    )


def part_two() -> int:
    return min(
        [
            _fuel_costs_to_move_all_crabs(target_pos, False)
            for target_pos in range(min(crab_positions), max(crab_positions) + 1)
        ]
    )


if __name__ == "__main__":
    print(f"{part_one()=}  335330 (sample: 37)")
    print(f"{part_two()=}  92439766 (sample: 168)")
