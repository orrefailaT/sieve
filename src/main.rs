use std::mem::replace;

fn sieve_of_eratosthenes(upper_limit: usize) -> Vec<usize> {
    let mut primes = Vec::new();
    let mut sieve: Vec<bool> = vec![true; upper_limit];

    let stopping_point = (upper_limit as f64).sqrt() as usize + 1;

    for i in 2..stopping_point {
        if sieve[i] {
            primes.push(i);
            for j in (i.pow(2)..upper_limit).step_by(i) {
                _ = replace(&mut sieve[j], false);
            }
        }
    }

    for i in stopping_point..upper_limit {
        if sieve[i] {
            primes.push(i);
        }
    }

    primes
}

fn main() {
    let upper_limit = 100_000_000;
    println!("{}", sieve_of_eratosthenes(upper_limit).len())
}
