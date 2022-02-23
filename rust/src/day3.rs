#[aoc_generator(day3)]
fn input_generator(input: &str) -> Vec<String> {
    input
        .lines()
        .map(|e| e.parse::<String>().unwrap())
        .collect()
}

#[aoc(day3, part1)]
fn part1(input: &[String]) -> isize {
    let nlines = input.len();
    let mut gamma: String = "".to_owned();
    let mut epsilon: String = "".to_owned();
    let linelen = input[0].len();
    for j in 0..linelen {
        let count = 0u32;
        for i in [0..nlines] {
            let num: u32 = input[j][i].try_into().unwrap();
            count += num;
        }
        let limit: f32 = count as f32 / nlines as f32;
        if limit > 0.5 {
            gamma.push('1');
            epsilon.push('0');
        }
        if limit < 0.5 {
            gamma.push('0');
            epsilon.push('1');
        }
    }
    println!("{}", gamma);
    let gamma_int = isize::from_str_radix(&gamma, 2).unwrap();
    let epsilon_int = isize::from_str_radix(&epsilon, 2).unwrap();

    return gamma_int * epsilon_int;
}
