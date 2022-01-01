use itertools::Itertools;

#[aoc_generator(day1)]
pub fn input_generator(input: &str) -> Vec<i32> {
    input.lines().map(|e| e.parse::<i32>().unwrap()).collect()
}

#[aoc(day1, part1)]
pub fn part1(input: &[i32]) -> usize {
    input
        .iter()
        .tuple_windows()
        .filter(|(first, second)| first < second)
        .count()
}

#[aoc(day1, part2)]
pub fn part2(input: &[i32]) -> usize {
    input
        .iter()
        .tuple_windows()
        .filter(|(first, _, _, fourth)| first < fourth)
        .count()
}
