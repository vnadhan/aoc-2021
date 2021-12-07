def main():
    # pull text from an txt file
    with open('day2.input.txt', 'r') as f:
        file_text = f.readlines()
        commands = [line.rstrip() for line in file_text]

        horizontal_position = 0
        depth = 0
        aim = 0

        for command in commands:
            cmd_split = command.split(' ')
            instruction = cmd_split[0]
            value = int(cmd_split[1])

            if instruction == 'forward':
                horizontal_position += value
                depth += (aim*value)
            elif instruction == 'down':
                aim += value
            elif instruction == 'up':
                aim -= value

        print(f"Horizontal position {horizontal_position}, Depth {depth}")
        print(f"Total {horizontal_position * depth}")


if __name__ == '__main__':
    main()
