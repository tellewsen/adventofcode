enum Move {
    Forward(i32),
    Down(i32),
    Up(i32),
}

#[aoc_generator(day2)]
fn input_generator(input: &str) -> Vec<Move> {
    input
        .lines()
        .map(|e| {
            let parts: Vec<&str> = e.split(' ').collect();
            match parts[0] {
                "forward" => Move::Forward(parts[1].parse().unwrap()),
                "down" => Move::Down(parts[1].parse().unwrap()),
                "up" => Move::Up(parts[1].parse().unwrap()),
                _ => {
                    panic!("invalid move")
                }
            }
        })
        .collect()
}

#[aoc(day2, part1)]
fn part1(input: &[Move]) -> i32 {
    let mut pos = (0, 0);
    for cmd in input {
        match cmd {
            Move::Forward(num) => pos.0 += num,
            Move::Down(num) => pos.1 += num,
            Move::Up(num) => pos.1 -= num,
        }
    }
    pos.0 * pos.1
}

#[aoc(day2, part2)]
fn part2(input: &[Move]) -> i32 {
    let mut pos = (0, 0);
    let mut aim = 0;
    for cmd in input {
        match cmd {
            Move::Forward(num) => {
                pos.0 += num;
                pos.1 += aim * num;
            }
            Move::Down(num) => aim += num,
            Move::Up(num) => aim -= num,
        }
    }
    pos.0 * pos.1
}
