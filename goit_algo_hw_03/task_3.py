def display_towers(towers):
    print(f"Current state: {towers}")

def move_disk(towers, source, destination):
    disk = towers[source].pop()
    towers[destination].append(disk)
    print(f"Moving disk from {source} to {destination}: {disk}")
    display_towers(towers)

def solve_towers_of_hanoi(towers, num_disks, source, destination, auxiliary):
    if num_disks == 1:
        move_disk(towers, source, destination)
    else:
        solve_towers_of_hanoi(towers, num_disks - 1, source, auxiliary, destination)
        move_disk(towers, source, destination)
        solve_towers_of_hanoi(towers, num_disks - 1, auxiliary, destination, source)

def initialize_and_solve_hanoi(num_disks):
    towers = {'A': list(range(num_disks, 0, -1)), 'B': [], 'C': []}
    print("Initial state:", towers)
    solve_towers_of_hanoi(towers, num_disks, 'A', 'C', 'B')
    print("Final state:", towers)

# Solve the Towers of Hanoi puzzle with 10 disks
initialize_and_solve_hanoi(10)