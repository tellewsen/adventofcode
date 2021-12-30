use itertools::Itertools;
use std::fs;

fn parse_data(data: String) -> Vec<i32> {
    data.lines()
        .map(|e| e.parse::<i32>().expect("cannot parse line"))
        .collect()
}

fn main() {
    let puzzle_input = fs::read_to_string("input.txt").expect("cannot read file");
    let parsed = parse_data(puzzle_input);
    println!("{}", part1(&parsed));
    println!("{}", part2(&parsed));
}

fn part1(depths: &Vec<i32>) -> usize {
    depths
        .iter()
        .tuple_windows()
        .filter(|(first, second)| first < second)
        .count()
}

fn part2(deep_scan: &Vec<i32>) -> usize {
    deep_scan
        .iter()
        .tuple_windows()
        .filter(|(first, _, _, fourth)| first < fourth)
        .count()
}
