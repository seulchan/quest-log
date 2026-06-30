// Rewrite the factorial function using a `for` loop.
pub fn factorial(n: u32) -> u32 {
    let mut result = 1;
    for num in 1..=n {
        result = result * num;
    }
    result
}
